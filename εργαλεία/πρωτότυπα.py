#!/usr/bin/env python3
"""Αντιστοιχίζει και κατεβάζει νόμιμα διαθέσιμα πρωτότυπα πηγών.

Το εργαλείο:
- αντιστοιχίζει χειροκίνητα ανεβασμένα PDF με εγγραφές SRC,
- δημιουργεί συντομεύσεις .url για πηγές χωρίς αρχείο (π.χ. YouTube),
- δοκιμάζει επίσημα/open-access download links,
- απορρίπτει HTML/CAPTCHA που παριστάνει PDF,
- ενημερώνει έναν μικρό κατάλογο κατάστασης.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import re
import shutil
import time
import unicodedata
from dataclasses import dataclass
from datetime import datetime, timezone
from difflib import SequenceMatcher
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote, urljoin, urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "πηγές"
ORIGINALS = ROOT / "πρωτότυπα"
INCOMING_ORIGINALS = ROOT / "νέα-πρωτότυπα"
CATALOG = ROOT / "κατάλογος" / "πηγές.csv"
REPORT_CSV = ROOT / "κατάλογος" / "πρωτότυπα.csv"
REPORT_MD = ROOT / "κατάλογος" / "πρωτότυπα.md"

REPORT_FIELDS = [
    "Κωδικός", "Τίτλος", "Κατάσταση", "Αρχείο", "Σύνδεσμος",
    "Προσπάθειες", "Τελευταίος έλεγχος", "Σημείωση",
]
SOURCE_ID_RE = re.compile(r"SRC-[A-F0-9]{10}")
URL_RE = re.compile(r"https?://[^\s)>\]}'\"]+")
DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.IGNORECASE)
ARXIV_RE = re.compile(r"(?:arxiv\.org/(?:abs|pdf|html)/|arXiv:\s*)(\d{4}\.\d{4,5})(?:v\d+)?", re.IGNORECASE)
OPENREVIEW_RE = re.compile(r"openreview\.net/(?:forum|pdf)\?(?:id=)?([A-Za-z0-9_-]+)", re.IGNORECASE)
ANTI_BOT_MARKERS = (
    b"verifying your browser", b"complete the check below", b"captcha",
    b"making sure you're not a bot", b"cloudflare",
)
USER_AGENT = "ThesisBibliography/1.0 (+https://github.com/MariosGiannakaras/ThesisBibliography)"
MAX_BYTES = 180 * 1024 * 1024


@dataclass
class DownloadResult:
    ok: bool
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


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def normalized(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).casefold()
    return "".join(ch for ch in value if ch.isalnum())


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_catalog() -> list[dict[str, str]]:
    with CATALOG.open(encoding="utf-8", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def read_previous_report() -> dict[str, dict[str, str]]:
    if not REPORT_CSV.exists():
        return {}
    with REPORT_CSV.open(encoding="utf-8", newline="") as handle:
        return {row["Κωδικός"]: dict(row) for row in csv.DictReader(handle)}


def source_text(source_id: str) -> str:
    path = SOURCES / f"{source_id}.md"
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def canonical_url(url: str) -> str:
    url = clean(url).rstrip(".,;:")
    if not url:
        return ""
    arxiv = ARXIV_RE.search(url)
    if arxiv:
        return f"https://arxiv.org/abs/{arxiv.group(1)}"
    doi = DOI_RE.search(unquote(url))
    if doi:
        return f"https://doi.org/{doi.group(0).rstrip('.')}"
    parts = urlsplit(url)
    if not parts.scheme:
        return url
    host = parts.netloc.lower().removeprefix("www.")
    return parts._replace(netloc=host, fragment="").geturl()


def identities(row: dict[str, str], text: str) -> set[str]:
    sample = "\n".join([row.get("Σύνδεσμος", ""), row.get("Τίτλος", ""), text[:30000]])
    result: set[str] = set()
    for match in ARXIV_RE.finditer(sample):
        result.add(f"arxiv:{match.group(1)}")
    for match in DOI_RE.finditer(sample):
        result.add(f"doi:{match.group(0).rstrip('.,;').casefold()}")
    for match in OPENREVIEW_RE.finditer(sample):
        result.add(f"openreview:{match.group(1)}")
    url = canonical_url(row.get("Σύνδεσμος", ""))
    if url:
        result.add(f"url:{url.casefold()}")
    return result


def is_link_only(row: dict[str, str]) -> bool:
    kind = row.get("Τύπος", "").casefold()
    url = row.get("Σύνδεσμος", "").casefold()
    return (
        "βίντεο" in kind
        or "youtube.com" in url
        or "youtu.be" in url
        or row.get("Τύπος") in {"ιστοσελίδα", "αποθετήριο κώδικα", "τεκμηρίωση ή εκπαιδευτικό υλικό"}
    )


def write_url_shortcut(source_id: str, url: str) -> Path:
    path = ORIGINALS / f"{source_id}.url"
    content = f"[InternetShortcut]\nURL={url}\n"
    if not path.exists() or path.read_text(encoding="utf-8", errors="replace") != content:
        path.write_text(content, encoding="utf-8", newline="\n")
    return path


def request_bytes(url: str, *, timeout: int = 45, max_bytes: int = MAX_BYTES) -> tuple[bytes, str, str]:
    req = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/pdf,text/html;q=0.9,*/*;q=0.5"})
    with urlopen(req, timeout=timeout) as response:
        content_type = response.headers.get("Content-Type", "").lower()
        final_url = response.geturl()
        chunks: list[bytes] = []
        total = 0
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            total += len(chunk)
            if total > max_bytes:
                raise ValueError(f"το αρχείο ξεπερνά το όριο των {max_bytes // (1024 * 1024)} MB")
            chunks.append(chunk)
        return b"".join(chunks), content_type, final_url


def looks_like_pdf(data: bytes) -> bool:
    return data.lstrip().startswith(b"%PDF-") and len(data) > 1024


def html_download_links(data: bytes, base_url: str) -> list[str]:
    lower = data[:200000].lower()
    if any(marker in lower for marker in ANTI_BOT_MARKERS):
        return []
    parser = LinkCollector()
    try:
        parser.feed(data.decode("utf-8", errors="replace"))
    except Exception:
        return []
    candidates: list[str] = []
    for href in parser.links:
        absolute = urljoin(base_url, href)
        low = absolute.casefold()
        if (
            low.endswith(".pdf")
            or "/pdf" in low
            or "bitstream" in low
            or "download" in low
            or "fulltext" in low
        ):
            candidates.append(absolute)
    return list(dict.fromkeys(candidates))[:12]


def openalex_pdf(row: dict[str, str], text: str) -> list[str]:
    ids = identities(row, text)
    doi_values = [item[4:] for item in ids if item.startswith("doi:")]
    urls: list[str] = []
    for doi in doi_values[:2]:
        endpoint = f"https://api.openalex.org/works/https://doi.org/{quote(doi, safe='/:')}"
        try:
            data, _, _ = request_bytes(endpoint, timeout=30, max_bytes=5 * 1024 * 1024)
            payload = json.loads(data.decode("utf-8"))
        except Exception:
            continue
        locations = [payload.get("best_oa_location"), payload.get("primary_location")]
        locations.extend(payload.get("locations") or [])
        for location in locations:
            if not isinstance(location, dict):
                continue
            for key in ("pdf_url", "landing_page_url"):
                value = location.get(key)
                if value:
                    urls.append(value)
    return list(dict.fromkeys(urls))


def semantic_scholar_pdf(row: dict[str, str], text: str) -> list[str]:
    ids = identities(row, text)
    doi_values = [item[4:] for item in ids if item.startswith("doi:")]
    result: list[str] = []
    for doi in doi_values[:1]:
        endpoint = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{quote(doi, safe='')}?fields=openAccessPdf,url"
        try:
            data, _, _ = request_bytes(endpoint, timeout=30, max_bytes=2 * 1024 * 1024)
            payload = json.loads(data.decode("utf-8"))
        except Exception:
            continue
        pdf = payload.get("openAccessPdf") or {}
        if isinstance(pdf, dict) and pdf.get("url"):
            result.append(pdf["url"])
    return result


def candidate_urls(row: dict[str, str], text: str) -> list[str]:
    seed_urls: list[str] = []
    if row.get("Σύνδεσμος"):
        seed_urls.append(row["Σύνδεσμος"])
    seed_urls.extend(URL_RE.findall(text[:50000]))

    result: list[str] = []
    for raw in seed_urls:
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
        low = url.casefold()
        if host == "proceedings.mlr.press":
            m = re.search(r"/(v\d+)/([^/]+?)(?:\.html|/)?$", parts.path)
            if m:
                result.append(f"https://proceedings.mlr.press/{m.group(1)}/{m.group(2)}/{m.group(2)}.pdf")
        if host == "mdpi.com" and "/pdf" not in low:
            result.append(url.rstrip("/") + "/pdf")
        result.append(url)

    result.extend(openalex_pdf(row, text))
    result.extend(semantic_scholar_pdf(row, text))
    return list(dict.fromkeys(canonical_url(u) if "doi.org" in u else u for u in result if u))


def download_pdf(source_id: str, row: dict[str, str], text: str) -> DownloadResult:
    target = ORIGINALS / f"{source_id}.pdf"
    if target.exists():
        return DownloadResult(True, "διαθέσιμο PDF", note="υπήρχε ήδη")

    attempted: list[str] = []
    for url in candidate_urls(row, text):
        if url in attempted:
            continue
        attempted.append(url)
        try:
            data, content_type, final_url = request_bytes(url)
        except (HTTPError, URLError, TimeoutError, ValueError, OSError):
            continue
        if looks_like_pdf(data):
            target.write_bytes(data)
            return DownloadResult(True, "διαθέσιμο PDF", final_url, "λήψη από δημόσια διαθέσιμη πηγή")
        if "html" in content_type or data.lstrip().startswith(b"<"):
            for pdf_url in html_download_links(data, final_url):
                if pdf_url in attempted:
                    continue
                attempted.append(pdf_url)
                try:
                    candidate, _, pdf_final = request_bytes(pdf_url)
                except (HTTPError, URLError, TimeoutError, ValueError, OSError):
                    continue
                if looks_like_pdf(candidate):
                    target.write_bytes(candidate)
                    return DownloadResult(True, "διαθέσιμο PDF", pdf_final, "λήψη από επίσημη σελίδα")

    note = "δεν βρέθηκε δημόσιο PDF"
    if attempted:
        note += f" μετά από {len(attempted)} δοκιμές"
    return DownloadResult(False, "χρειάζεται χειροκίνητη λήψη", row.get("Σύνδεσμος", ""), note)


def extract_pdf_text(path: Path) -> str:
    try:
        from pypdf import PdfReader  # type: ignore
    except ImportError:
        return ""
    try:
        reader = PdfReader(str(path))
        parts = []
        for page in reader.pages[:4]:
            parts.append(page.extract_text() or "")
        return "\n".join(parts)[:40000]
    except Exception:
        return ""


def match_uploaded_pdf(path: Path, rows: list[dict[str, str]], source_cache: dict[str, str]) -> tuple[str | None, str]:
    sid_match = SOURCE_ID_RE.search(path.name.upper())
    if sid_match and any(row["Κωδικός"] == sid_match.group(0) for row in rows):
        return sid_match.group(0), "κωδικός στο όνομα"

    pdf_text = extract_pdf_text(path)
    pdf_ids: set[str] = set()
    for match in ARXIV_RE.finditer(pdf_text):
        pdf_ids.add(f"arxiv:{match.group(1)}")
    for match in DOI_RE.finditer(pdf_text):
        pdf_ids.add(f"doi:{match.group(0).rstrip('.,;').casefold()}")

    strong: list[tuple[str, str]] = []
    for row in rows:
        sid = row["Κωδικός"]
        row_ids = identities(row, source_cache.get(sid, ""))
        shared = pdf_ids & row_ids
        if shared:
            strong.append((sid, ", ".join(sorted(shared))))
    if len(strong) == 1:
        return strong[0][0], f"αναγνωριστικό {strong[0][1]}"
    if len(strong) > 1:
        return None, "πολλαπλές εγγραφές με το ίδιο αναγνωριστικό"

    filename_key = normalized(re.sub(r"^\d+[-_ ]+", "", path.stem))
    text_key = normalized(pdf_text[:6000])
    scored: list[tuple[float, str]] = []
    for row in rows:
        title_key = normalized(row.get("Τίτλος", ""))
        if len(title_key) < 12:
            continue
        score = SequenceMatcher(None, filename_key, title_key).ratio()
        if title_key in text_key:
            score = max(score, 0.98)
        scored.append((score, row["Κωδικός"]))
    scored.sort(reverse=True)
    if scored and scored[0][0] >= 0.86 and (len(scored) == 1 or scored[0][0] - scored[1][0] >= 0.08):
        return scored[0][1], f"ομοιότητα τίτλου {scored[0][0]:.2f}"
    return None, "δεν βρέθηκε ασφαλής μοναδική αντιστοίχιση"


def import_uploaded_pdfs(rows: list[dict[str, str]]) -> list[str]:
    ORIGINALS.mkdir(parents=True, exist_ok=True)
    INCOMING_ORIGINALS.mkdir(parents=True, exist_ok=True)
    source_cache = {row["Κωδικός"]: source_text(row["Κωδικός"]) for row in rows}
    notes: list[str] = []

    candidates = list(INCOMING_ORIGINALS.rglob("*.pdf"))
    candidates.extend(path for path in ORIGINALS.glob("*.pdf") if not SOURCE_ID_RE.fullmatch(path.stem))
    for path in sorted(set(candidates)):
        sid, reason = match_uploaded_pdf(path, rows, source_cache)
        if not sid:
            notes.append(f"{path.name}: {reason}")
            continue
        target = ORIGINALS / f"{sid}.pdf"
        if target.exists():
            try:
                same = sha256(path) == sha256(target)
            except OSError:
                same = False
            if same:
                path.unlink()
                notes.append(f"{path.name}: αφαιρέθηκε ακριβές διπλότυπο του {sid}")
            else:
                notes.append(f"{path.name}: αντιστοιχεί στο {sid}, αλλά υπάρχει ήδη διαφορετικό PDF")
            continue
        shutil.move(str(path), target)
        notes.append(f"{path.name} → {target.name} ({reason})")
    return notes


def load_requested_ids(path: Path | None) -> set[str] | None:
    if path is None or not path.exists():
        return None
    ids = {match.group(0) for match in SOURCE_ID_RE.finditer(path.read_text(encoding="utf-8", errors="replace"))}
    return ids or None


def write_report(rows: list[dict[str, str]], previous: dict[str, dict[str, str]], run_results: dict[str, DownloadResult], import_notes: list[str]) -> None:
    ORIGINALS.mkdir(parents=True, exist_ok=True)
    REPORT_CSV.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    output: list[dict[str, str]] = []

    for row in sorted(rows, key=lambda item: item["Τίτλος"].casefold()):
        sid = row["Κωδικός"]
        pdf = ORIGINALS / f"{sid}.pdf"
        shortcut = ORIGINALS / f"{sid}.url"
        old = previous.get(sid, {})
        result = run_results.get(sid)
        if pdf.exists():
            status, file_name, link, note = "διαθέσιμο PDF", pdf.name, result.url if result else old.get("Σύνδεσμος", ""), result.note if result else old.get("Σημείωση", "")
        elif shortcut.exists():
            status, file_name, link, note = "μόνο σύνδεσμος", shortcut.name, row.get("Σύνδεσμος", ""), "δεν αναμένεται ξεχωριστό PDF"
        elif not row.get("Σύνδεσμος"):
            status, file_name, link, note = "χωρίς σύνδεσμο", "", "", "χρειάζεται ταυτοποίηση της πραγματικής πηγής"
        elif result:
            status, file_name, link, note = result.status, "", result.url, result.note
        else:
            status, file_name, link, note = old.get("Κατάσταση", "εκκρεμεί"), old.get("Αρχείο", ""), old.get("Σύνδεσμος", row.get("Σύνδεσμος", "")), old.get("Σημείωση", "")
        attempts = int(old.get("Προσπάθειες", "0") or 0) + (1 if result else 0)
        output.append({
            "Κωδικός": sid,
            "Τίτλος": row.get("Τίτλος", ""),
            "Κατάσταση": status,
            "Αρχείο": file_name,
            "Σύνδεσμος": link,
            "Προσπάθειες": str(attempts),
            "Τελευταίος έλεγχος": now if result else old.get("Τελευταίος έλεγχος", ""),
            "Σημείωση": note,
        })

    with REPORT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=REPORT_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(output)

    counts: dict[str, int] = {}
    for item in output:
        counts[item["Κατάσταση"]] = counts.get(item["Κατάσταση"], 0) + 1
    lines = [
        "# Πρωτότυπα πηγών", "",
        f"- PDF στο αποθετήριο: **{counts.get('διαθέσιμο PDF', 0)}**",
        f"- Πηγές που διατηρούνται ως σύνδεσμοι: **{counts.get('μόνο σύνδεσμος', 0)}**",
        f"- Χειροκίνητη λήψη: **{counts.get('χρειάζεται χειροκίνητη λήψη', 0)}**",
        f"- Χωρίς σύνδεσμο: **{counts.get('χωρίς σύνδεσμο', 0)}**",
        f"- Εκκρεμούν: **{counts.get('εκκρεμεί', 0)}**",
        "",
        "> Τα PDF χρησιμοποιούνται μόνο ως αρχειακά αντίγραφα και για επαλήθευση. Η καθημερινή εργασία βασίζεται στα Markdown.",
        "",
        "| Κωδικός | Τίτλος | Κατάσταση | Αρχείο ή σύνδεσμος |",
        "|---|---|---|---|",
    ]
    rank = {"χρειάζεται χειροκίνητη λήψη": 0, "χωρίς σύνδεσμο": 1, "εκκρεμεί": 2, "διαθέσιμο PDF": 3, "μόνο σύνδεσμος": 4}
    for item in sorted(output, key=lambda x: (rank.get(x["Κατάσταση"], 9), x["Τίτλος"].casefold())):
        target = item["Αρχείο"] or item["Σύνδεσμος"] or "—"
        if item["Σύνδεσμος"] and not item["Αρχείο"]:
            target = f"[άνοιγμα]({item['Σύνδεσμος']})"
        title = item["Τίτλος"].replace("|", "\\|")
        lines.append(f"| `{item['Κωδικός']}` | {title} | {item['Κατάσταση']} | {target} |")
    if import_notes:
        lines.extend(["", "## Αντιστοίχιση αρχείων που ανέβηκαν", ""])
        lines.extend(f"- {note}" for note in import_notes)
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--λήψη", "--download", action="store_true", help="δοκιμάζει λήψη δημόσιων PDF")
    parser.add_argument("--όριο", "--limit", type=int, default=25, help="μέγιστες νέες λήψεις ανά εκτέλεση")
    parser.add_argument("--κωδικοί-αρχείο", "--ids-file", type=Path)
    parser.add_argument("--επανάληψη", "--retry", action="store_true", help="ξαναδοκιμάζει και επανειλημμένες αποτυχίες")
    args = parser.parse_args()

    rows = read_catalog()
    previous = read_previous_report()
    import_notes = import_uploaded_pdfs(rows)
    requested = load_requested_ids(args.κωδικοί_αρχείο)
    run_results: dict[str, DownloadResult] = {}

    for row in rows:
        if is_link_only(row) and row.get("Σύνδεσμος"):
            write_url_shortcut(row["Κωδικός"], row["Σύνδεσμος"])

    if args.λήψη:
        candidates = []
        for row in rows:
            sid = row["Κωδικός"]
            if requested is not None and sid not in requested:
                continue
            if (ORIGINALS / f"{sid}.pdf").exists() or is_link_only(row) or not row.get("Σύνδεσμος"):
                continue
            attempts = int(previous.get(sid, {}).get("Προσπάθειες", "0") or 0)
            if attempts >= 3 and not args.επανάληψη:
                continue
            priority_rank = {"υψηλή": 0, "μεσαία": 1, "χρειάζεται διόρθωση": 2, "χαμηλή": 3}
            candidates.append((priority_rank.get(row.get("Προτεραιότητα", ""), 9), attempts, row["Τίτλος"].casefold(), row))
        candidates.sort(key=lambda item: item[:3])
        for _, _, _, row in candidates[: max(args.όριο, 0)]:
            sid = row["Κωδικός"]
            result = download_pdf(sid, row, source_text(sid))
            run_results[sid] = result
            print(f"{sid}: {result.status} {result.url}")
            time.sleep(0.2)

    write_report(rows, previous, run_results, import_notes)
    print(f"Ελέγχθηκαν {len(rows)} πηγές· νέες προσπάθειες λήψης: {len(run_results)}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
