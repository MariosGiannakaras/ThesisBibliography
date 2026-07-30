#!/usr/bin/env python3
"""Αντιστοιχίζει, αρχειοθετεί και κατεβάζει νόμιμα πρωτότυπα πηγών."""
from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import re
import shutil
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from difflib import SequenceMatcher
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urljoin, urlsplit
from urllib.request import Request, urlopen

from κοινά_πηγών import (
    ARXIV_RE,
    DOI_RE,
    OPENREVIEW_RE,
    SOURCE_ID_RE,
    URL_RE,
    canonical_url,
    explicit_source_sample,
    identities,
    normalized,
    source_text,
)

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "πηγές"
ORIGINALS = ROOT / "πρωτότυπα"
INCOMING = ROOT / "νέα-πρωτότυπα"
CATALOG = ROOT / "κατάλογος" / "πηγές.csv"
REPORT_CSV = ROOT / "κατάλογος" / "πρωτότυπα.csv"
REPORT_MD = ROOT / "κατάλογος" / "πρωτότυπα.md"
REPORT_FIELDS = [
    "Κωδικός", "Τίτλος", "Κατάσταση", "Αρχείο", "Σύνδεσμος",
    "Προσπάθειες", "Τελευταίος έλεγχος", "Σημείωση",
]
USER_AGENT = "ThesisBibliography/1.0 (+https://github.com/MariosGiannakaras/ThesisBibliography)"
MAX_BYTES = 180 * 1024 * 1024
ANTI_BOT = (
    b"verifying your browser", b"complete the check below", b"captcha",
    b"making sure you're not a bot", b"cloudflare",
)


@dataclass
class DownloadResult:
    status: str
    url: str = ""
    note: str = ""


class LinkCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "a":
            return
        for key, value in attrs:
            if key.lower() == "href" and value:
                self.links.append(html.unescape(value))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_catalog() -> list[dict[str, str]]:
    with CATALOG.open(encoding="utf-8", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def read_previous() -> dict[str, dict[str, str]]:
    if not REPORT_CSV.exists():
        return {}
    with REPORT_CSV.open(encoding="utf-8", newline="") as handle:
        return {row["Κωδικός"]: dict(row) for row in csv.DictReader(handle)}


def is_link_only(row: dict[str, str]) -> bool:
    kind = row.get("Τύπος", "").casefold()
    url = row.get("Σύνδεσμος", "").casefold()
    return (
        "βίντεο" in kind
        or "youtube.com" in url
        or "youtu.be" in url
        or row.get("Τύπος") in {
            "ιστοσελίδα", "αποθετήριο κώδικα", "τεκμηρίωση ή εκπαιδευτικό υλικό"
        }
    )


def write_shortcut(source_id: str, url: str) -> Path:
    path = ORIGINALS / f"{source_id}.url"
    content = f"[InternetShortcut]\nURL={url}\n"
    if not path.exists() or path.read_text(encoding="utf-8", errors="replace") != content:
        path.write_text(content, encoding="utf-8", newline="\n")
    return path


def request_bytes(url: str, *, timeout: int = 45, limit: int = MAX_BYTES) -> tuple[bytes, str, str]:
    request = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/pdf,text/html;q=0.9,*/*;q=0.5",
        },
    )
    with urlopen(request, timeout=timeout) as response:
        total = 0
        chunks: list[bytes] = []
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            total += len(chunk)
            if total > limit:
                raise ValueError("το αρχείο ξεπερνά το επιτρεπόμενο μέγεθος")
            chunks.append(chunk)
        return b"".join(chunks), response.headers.get("Content-Type", "").lower(), response.geturl()


def looks_like_pdf(data: bytes) -> bool:
    return data.lstrip().startswith(b"%PDF-") and len(data) > 1024


def page_pdf_links(data: bytes, base_url: str) -> list[str]:
    if any(marker in data[:200000].lower() for marker in ANTI_BOT):
        return []
    parser = LinkCollector()
    try:
        parser.feed(data.decode("utf-8", errors="replace"))
    except Exception:
        return []
    result: list[str] = []
    for href in parser.links:
        url = urljoin(base_url, href)
        low = url.casefold()
        if low.endswith(".pdf") or "/pdf" in low or "bitstream" in low or "download" in low:
            result.append(url)
    return list(dict.fromkeys(result))[:12]


def openalex_candidates(row: dict[str, str], text: str) -> list[str]:
    result: list[str] = []
    for identity in identities(row.get("Σύνδεσμος", ""), row.get("Τίτλος", ""), text):
        if not identity.startswith("doi:"):
            continue
        doi = identity[4:]
        endpoint = f"https://api.openalex.org/works/https://doi.org/{quote(doi, safe='/:')}"
        try:
            data, _, _ = request_bytes(endpoint, timeout=30, limit=5 * 1024 * 1024)
            payload = json.loads(data.decode("utf-8"))
        except Exception:
            continue
        locations = [payload.get("best_oa_location"), payload.get("primary_location")]
        locations.extend(payload.get("locations") or [])
        for location in locations:
            if isinstance(location, dict):
                for key in ("pdf_url", "landing_page_url"):
                    if location.get(key):
                        result.append(location[key])
    return list(dict.fromkeys(result))


def candidate_urls(row: dict[str, str], text: str) -> list[str]:
    seeds: list[str] = []
    if row.get("Σύνδεσμος"):
        seeds.append(row["Σύνδεσμος"])
    seeds.extend(URL_RE.findall(explicit_source_sample(row.get("Σύνδεσμος", ""), row.get("Τίτλος", ""), text)))

    result: list[str] = []
    for raw in seeds:
        url = raw.rstrip(".,;:)")
        arxiv = ARXIV_RE.search(url)
        if arxiv:
            result.append(f"https://arxiv.org/pdf/{arxiv.group(1)}")
            continue
        openreview = OPENREVIEW_RE.search(url)
        if openreview:
            result.append(f"https://openreview.net/pdf?id={openreview.group(1)}")
            continue
        parts = urlsplit(url)
        host = parts.netloc.lower().removeprefix("www.")
        if host == "proceedings.mlr.press":
            match = re.search(r"/(v\d+)/([^/]+?)(?:\.html|/)?$", parts.path)
            if match:
                result.append(
                    f"https://proceedings.mlr.press/{match.group(1)}/{match.group(2)}/{match.group(2)}.pdf"
                )
        if host == "mdpi.com" and "/pdf" not in url.casefold():
            result.append(url.rstrip("/") + "/pdf")
        result.append(url)
    result.extend(openalex_candidates(row, text))
    return list(dict.fromkeys(url for url in result if url))


def download_pdf(source_id: str, row: dict[str, str], text: str) -> DownloadResult:
    target = ORIGINALS / f"{source_id}.pdf"
    if target.exists():
        return DownloadResult("διαθέσιμο PDF", note="υπήρχε ήδη")

    attempted: set[str] = set()
    for url in candidate_urls(row, text):
        if url in attempted:
            continue
        attempted.add(url)
        try:
            data, content_type, final_url = request_bytes(url)
        except (HTTPError, URLError, TimeoutError, ValueError, OSError):
            continue
        if looks_like_pdf(data):
            target.write_bytes(data)
            return DownloadResult("διαθέσιμο PDF", final_url, "λήψη από δημόσια διαθέσιμη πηγή")
        if "html" in content_type or data.lstrip().startswith(b"<"):
            for pdf_url in page_pdf_links(data, final_url):
                if pdf_url in attempted:
                    continue
                attempted.add(pdf_url)
                try:
                    candidate, _, pdf_final = request_bytes(pdf_url)
                except (HTTPError, URLError, TimeoutError, ValueError, OSError):
                    continue
                if looks_like_pdf(candidate):
                    target.write_bytes(candidate)
                    return DownloadResult("διαθέσιμο PDF", pdf_final, "λήψη από επίσημη σελίδα")
    return DownloadResult(
        "χρειάζεται χειροκίνητη λήψη",
        row.get("Σύνδεσμος", ""),
        f"δεν βρέθηκε δημόσιο PDF μετά από {len(attempted)} ασφαλείς δοκιμές",
    )


def extract_pdf_text(path: Path) -> str:
    try:
        from pypdf import PdfReader  # type: ignore
    except ImportError:
        return ""
    try:
        reader = PdfReader(str(path))
        return "\n".join((page.extract_text() or "") for page in reader.pages[:4])[:40000]
    except Exception:
        return ""


def match_uploaded(path: Path, rows: list[dict[str, str]], texts: dict[str, str]) -> tuple[str | None, str]:
    id_in_name = SOURCE_ID_RE.search(path.name.upper())
    if id_in_name and any(row["Κωδικός"] == id_in_name.group(0) for row in rows):
        return id_in_name.group(0), "κωδικός στο όνομα"

    pdf_text = extract_pdf_text(path)
    pdf_ids: set[str] = set()
    for match in ARXIV_RE.finditer(pdf_text[:12000]):
        pdf_ids.add(f"arxiv:{match.group(1)}")
    for match in DOI_RE.finditer(pdf_text[:12000]):
        pdf_ids.add(f"doi:{match.group(0).rstrip('.,;').casefold()}")

    matches: list[str] = []
    for row in rows:
        row_ids = identities(row.get("Σύνδεσμος", ""), row.get("Τίτλος", ""), texts[row["Κωδικός"]])
        if pdf_ids & row_ids:
            matches.append(row["Κωδικός"])
    if len(matches) == 1:
        return matches[0], "DOI ή arXiv ID"
    if len(matches) > 1:
        return None, "πολλαπλές εγγραφές με το ίδιο ισχυρό αναγνωριστικό"

    filename_key = normalized(re.sub(r"^\d+[-_ ]+", "", path.stem))
    first_pages = normalized(pdf_text[:7000])
    scores: list[tuple[float, str]] = []
    for row in rows:
        title_key = normalized(row.get("Τίτλος", ""))
        if len(title_key) < 12:
            continue
        score = SequenceMatcher(None, filename_key, title_key).ratio()
        if title_key in first_pages:
            score = max(score, 0.98)
        scores.append((score, row["Κωδικός"]))
    scores.sort(reverse=True)
    if scores and scores[0][0] >= 0.86 and (len(scores) == 1 or scores[0][0] - scores[1][0] >= 0.08):
        return scores[0][1], f"μοναδική ομοιότητα τίτλου {scores[0][0]:.2f}"
    return None, "δεν βρέθηκε ασφαλής μοναδική αντιστοίχιση"


def import_uploaded(rows: list[dict[str, str]]) -> list[str]:
    ORIGINALS.mkdir(parents=True, exist_ok=True)
    INCOMING.mkdir(parents=True, exist_ok=True)
    texts = {row["Κωδικός"]: source_text(SOURCES, row["Κωδικός"]) for row in rows}
    notes: list[str] = []
    candidates = list(INCOMING.rglob("*.pdf"))
    candidates.extend(path for path in ORIGINALS.glob("*.pdf") if not SOURCE_ID_RE.fullmatch(path.stem))
    for path in sorted(set(candidates)):
        source_id, reason = match_uploaded(path, rows, texts)
        if not source_id:
            notes.append(f"{path.name}: {reason}")
            continue
        target = ORIGINALS / f"{source_id}.pdf"
        if target.exists():
            if sha256(path) == sha256(target):
                path.unlink()
                notes.append(f"{path.name}: αφαιρέθηκε ακριβές διπλότυπο του {source_id}")
            else:
                notes.append(f"{path.name}: αντιστοιχεί στο {source_id}, αλλά υπάρχει ήδη διαφορετικό PDF")
            continue
        shutil.move(str(path), target)
        notes.append(f"{path.name} → {target.name} ({reason})")
    return notes


def requested_ids(path: Path | None) -> set[str] | None:
    if not path or not path.exists():
        return None
    result = set(SOURCE_ID_RE.findall(path.read_text(encoding="utf-8", errors="replace")))
    return result or None


def write_report(
    rows: list[dict[str, str]],
    previous: dict[str, dict[str, str]],
    results: dict[str, DownloadResult],
    import_notes: list[str],
) -> None:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    output: list[dict[str, str]] = []
    for row in sorted(rows, key=lambda item: item["Τίτλος"].casefold()):
        source_id = row["Κωδικός"]
        pdf = ORIGINALS / f"{source_id}.pdf"
        shortcut = ORIGINALS / f"{source_id}.url"
        old = previous.get(source_id, {})
        result = results.get(source_id)
        if pdf.exists():
            status, file_name = "διαθέσιμο PDF", pdf.name
        elif shortcut.exists():
            status, file_name = "μόνο σύνδεσμος", shortcut.name
        elif not row.get("Σύνδεσμος"):
            status, file_name = "χωρίς σύνδεσμο", ""
        elif result:
            status, file_name = result.status, ""
        else:
            status, file_name = old.get("Κατάσταση", "εκκρεμεί"), old.get("Αρχείο", "")
        output.append({
            "Κωδικός": source_id,
            "Τίτλος": row.get("Τίτλος", ""),
            "Κατάσταση": status,
            "Αρχείο": file_name,
            "Σύνδεσμος": result.url if result else old.get("Σύνδεσμος", row.get("Σύνδεσμος", "")),
            "Προσπάθειες": str(int(old.get("Προσπάθειες", "0") or 0) + (1 if result else 0)),
            "Τελευταίος έλεγχος": today if result else old.get("Τελευταίος έλεγχος", ""),
            "Σημείωση": result.note if result else old.get("Σημείωση", ""),
        })

    REPORT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with REPORT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=REPORT_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(output)

    counts: dict[str, int] = {}
    for item in output:
        counts[item["Κατάσταση"]] = counts.get(item["Κατάσταση"], 0) + 1
    lines = [
        "# Πρωτότυπα πηγών", "",
        f"- PDF: **{counts.get('διαθέσιμο PDF', 0)}**",
        f"- Σύνδεσμοι (YouTube, ιστοσελίδες κ.λπ.): **{counts.get('μόνο σύνδεσμος', 0)}**",
        f"- Χειροκίνητη λήψη: **{counts.get('χρειάζεται χειροκίνητη λήψη', 0)}**",
        f"- Χωρίς σύνδεσμο: **{counts.get('χωρίς σύνδεσμο', 0)}**",
        f"- Εκκρεμούν: **{counts.get('εκκρεμεί', 0)}**", "",
        "> Τα PDF είναι αρχειακά αντίγραφα. Η καθημερινή εργασία γίνεται στα Markdown.", "",
        "| Κωδικός | Τίτλος | Κατάσταση | Αρχείο ή σύνδεσμος |",
        "|---|---|---|---|",
    ]
    rank = {"χρειάζεται χειροκίνητη λήψη": 0, "χωρίς σύνδεσμο": 1, "εκκρεμεί": 2, "διαθέσιμο PDF": 3, "μόνο σύνδεσμος": 4}
    for item in sorted(output, key=lambda x: (rank.get(x["Κατάσταση"], 9), x["Τίτλος"].casefold())):
        target = item["Αρχείο"] or "—"
        if not item["Αρχείο"] and item["Σύνδεσμος"]:
            target = f"[άνοιγμα]({item['Σύνδεσμος']})"
        title = item["Τίτλος"].replace("|", "\\|")
        lines.append(f"| `{item['Κωδικός']}` | {title} | {item['Κατάσταση']} | {target} |")
    if import_notes:
        lines.extend(["", "## Αρχεία που αντιστοιχίστηκαν ή χρειάζονται έλεγχο", ""])
        lines.extend(f"- {note}" for note in import_notes)
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--λήψη", "--download", action="store_true")
    parser.add_argument("--όριο", "--limit", type=int, default=25)
    parser.add_argument("--κωδικοί-αρχείο", "--ids-file", type=Path)
    parser.add_argument("--επανάληψη", "--retry", action="store_true")
    args = parser.parse_args()

    rows = read_catalog()
    previous = read_previous()
    notes = import_uploaded(rows)
    wanted = requested_ids(args.κωδικοί_αρχείο)
    results: dict[str, DownloadResult] = {}

    for row in rows:
        if is_link_only(row) and row.get("Σύνδεσμος"):
            write_shortcut(row["Κωδικός"], row["Σύνδεσμος"])

    if args.λήψη:
        priorities = {"υψηλή": 0, "μεσαία": 1, "χρειάζεται διόρθωση": 2, "χαμηλή": 3}
        candidates = []
        for row in rows:
            source_id = row["Κωδικός"]
            if wanted is not None and source_id not in wanted:
                continue
            if (ORIGINALS / f"{source_id}.pdf").exists() or is_link_only(row) or not row.get("Σύνδεσμος"):
                continue
            attempts = int(previous.get(source_id, {}).get("Προσπάθειες", "0") or 0)
            if attempts >= 3 and not args.επανάληψη:
                continue
            candidates.append((priorities.get(row.get("Προτεραιότητα", ""), 9), attempts, row["Τίτλος"].casefold(), row))
        candidates.sort(key=lambda item: item[:3])
        for _, _, _, row in candidates[: max(0, args.όριο)]:
            source_id = row["Κωδικός"]
            results[source_id] = download_pdf(source_id, row, source_text(SOURCES, source_id))
            print(f"{source_id}: {results[source_id].status}")
            time.sleep(0.2)

    write_report(rows, previous, results, notes)
    print(f"Ελέγχθηκαν {len(rows)} πηγές και έγιναν {len(results)} προσπάθειες λήψης.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
