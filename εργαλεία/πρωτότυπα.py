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
import subprocess
import sys
import time
from dataclasses import dataclass, field
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
    normalized_words,
    source_text,
)

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "πηγές"
ORIGINALS = ROOT / "πρωτότυπα"
INCOMING = ROOT / "νέα-πρωτότυπα"
CATALOG = ROOT / "κατάλογος" / "πηγές.csv"
REPORT_CSV = ROOT / "κατάλογος" / "πρωτότυπα.csv"
REPORT_MD = ROOT / "κατάλογος" / "πρωτότυπα.md"
PENDING_REPORT = ROOT / "κατάλογος" / "εκκρεμή-πρωτότυπα.md"
CATALOG_FIELDS = [
    "Κωδικός", "Τίτλος", "Συγγραφείς", "Έτος", "Σύνδεσμος",
    "Τύπος", "Θέματα", "Κατάσταση", "Επιβεβαίωση", "Προτεραιότητα", "Σημειώσεις",
]
REPORT_FIELDS = [
    "Κωδικός", "Τίτλος", "Κατάσταση", "Αρχείο", "Σύνδεσμος",
    "Προσπάθειες", "Τελευταίος έλεγχος", "Σημείωση",
]
USER_AGENT = "ThesisBibliography/1.1 (+https://github.com/MariosGiannakaras/ThesisBibliography)"
MAX_BYTES = 180 * 1024 * 1024
ANTI_BOT = (
    b"verifying your browser", b"complete the check below", b"captcha",
    b"making sure you're not a bot", b"cloudflare",
)
GENERIC_TITLE = re.compile(
    r"^(?:untitled|document|thesis(?:\.pdf)?|fulltext\d*|brketi-?\d+|"
    r"https?[-_:]|pdf[-_]|ebook[-_]|academic editors?:|verifying your browser)$",
    re.IGNORECASE,
)
DOCUMENT_TYPES = {
    "ακαδημαϊκή εργασία",
    "διπλωματική ή διατριβή",
    "βιβλίο ή κεφάλαιο",
    "θεσμική ή τεχνική αναφορά",
}
REPOSITORY_HINTS = (
    "repository", "dspace", "aaltodoc", "pergamos", "opus", "openarchives",
    "/handle/", "/item/", "/record/", "bitstream", "download", "get_pdf",
    "proceedings", "paper_files", "papers.nips", "arxiv.org", "openreview.net",
    "doi.org", "zenodo.org", "ntrs.nasa.gov", "research-collection",
)


@dataclass
class DownloadResult:
    status: str
    url: str = ""
    note: str = ""


@dataclass
class PdfInfo:
    title: str = ""
    authors: str = ""
    year: str = ""
    pages: int = 0
    text: str = ""
    doi: list[str] = field(default_factory=list)
    arxiv: list[str] = field(default_factory=list)
    metadata_error: str = ""


@dataclass
class MatchResult:
    source_id: str | None
    reason: str
    info: PdfInfo
    candidates: list[tuple[float, str, str]] = field(default_factory=list)


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


def write_catalog(rows: list[dict[str, str]]) -> None:
    with CATALOG.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CATALOG_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda row: row.get("Τίτλος", "").casefold()))


def read_previous() -> dict[str, dict[str, str]]:
    if not REPORT_CSV.exists():
        return {}
    with REPORT_CSV.open(encoding="utf-8", newline="") as handle:
        return {row["Κωδικός"]: dict(row) for row in csv.DictReader(handle)}


def url_is_direct_pdf(url: str) -> bool:
    low = url.casefold()
    path = urlsplit(url).path.casefold()
    return (
        path.endswith(".pdf")
        or "/pdf/" in path
        or path.endswith("/pdf")
        or "get_pdf" in low
        or "bitstream" in low
        or "download" in low and "youtube" not in low
    )


def is_document_candidate(row: dict[str, str]) -> bool:
    url = row.get("Σύνδεσμος", "").strip()
    kind = row.get("Τύπος", "").strip()
    low = url.casefold()
    if not url:
        return False
    if url_is_direct_pdf(url):
        return True
    if kind in DOCUMENT_TYPES:
        return True
    if ARXIV_RE.search(url) or DOI_RE.search(url) or OPENREVIEW_RE.search(url):
        return True
    return any(hint in low for hint in REPOSITORY_HINTS)


def is_url_only(row: dict[str, str]) -> bool:
    url = row.get("Σύνδεσμος", "").strip()
    kind = row.get("Τύπος", "").casefold()
    low = url.casefold()
    if not url:
        return False
    if url_is_direct_pdf(url) or is_document_candidate(row):
        return False
    if "βίντεο" in kind or "youtube.com" in low or "youtu.be" in low or "vimeo.com" in low:
        return True
    if row.get("Τύπος") == "αποθετήριο κώδικα":
        return True
    return row.get("Τύπος") in {"ιστοσελίδα", "τεκμηρίωση ή εκπαιδευτικό υλικό", "άγνωστος τύπος"}


def write_shortcut(source_id: str, url: str) -> Path:
    path = ORIGINALS / f"{source_id}.url"
    content = f"[InternetShortcut]\nURL={url}\n"
    if not path.exists() or path.read_text(encoding="utf-8", errors="replace") != content:
        path.write_text(content, encoding="utf-8", newline="\n")
    return path


def request_bytes(url: str, *, timeout: int = 35, limit: int = MAX_BYTES) -> tuple[bytes, str, str]:
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
        if (
            url_is_direct_pdf(url)
            or "fulltext" in low
            or "viewcontent" in low
            or "download?" in low
        ):
            result.append(url)
    return list(dict.fromkeys(result))[:15]


def openalex_candidates(row: dict[str, str], text: str) -> list[str]:
    result: list[str] = []
    for identity in identities(row.get("Σύνδεσμος", ""), row.get("Τίτλος", ""), text):
        if not identity.startswith("doi:"):
            continue
        doi = identity[4:]
        endpoint = f"https://api.openalex.org/works/https://doi.org/{quote(doi, safe='/:')}"
        try:
            data, _, _ = request_bytes(endpoint, timeout=25, limit=5 * 1024 * 1024)
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
            shortcut = ORIGINALS / f"{source_id}.url"
            if shortcut.exists():
                shortcut.unlink()
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
                    shortcut = ORIGINALS / f"{source_id}.url"
                    if shortcut.exists():
                        shortcut.unlink()
                    return DownloadResult("διαθέσιμο PDF", pdf_final, "λήψη από επίσημη σελίδα")
    return DownloadResult(
        "χρειάζεται χειροκίνητη λήψη",
        row.get("Σύνδεσμος", ""),
        f"δεν βρέθηκε δημόσιο PDF μετά από {len(attempted)} ασφαλείς δοκιμές",
    )


def clean_pdf_metadata(value: object) -> str:
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value)).strip()


def likely_title_from_text(text: str) -> str:
    lines = [re.sub(r"\s+", " ", line).strip() for line in text.splitlines()[:80]]
    lines = [line for line in lines if line]
    ignored = re.compile(
        r"^(?:arxiv|doi|abstract|contents|table of contents|copyright|page \d+|"
        r"university|department|faculty|submitted|author(?:s)?\s*:)$",
        re.IGNORECASE,
    )
    candidates: list[tuple[int, str]] = []
    for line in lines:
        words = line.split()
        if ignored.search(line) or len(words) < 3 or len(line) < 15 or len(line) > 260:
            continue
        alpha_ratio = sum(ch.isalpha() for ch in line) / max(len(line), 1)
        if alpha_ratio < 0.55:
            continue
        score = 0
        if 4 <= len(words) <= 24:
            score += 20
        if line == line.title() or sum(word[:1].isupper() for word in words) >= len(words) * 0.5:
            score += 10
        score += max(0, 120 - abs(len(line) - 90)) // 10
        candidates.append((score, line))
    return max(candidates, default=(0, ""))[1]


def inspect_pdf(path: Path) -> PdfInfo:
    info = PdfInfo()
    try:
        from pypdf import PdfReader  # type: ignore
    except ImportError:
        info.metadata_error = "λείπει το pypdf"
        return info
    try:
        reader = PdfReader(str(path))
        info.pages = len(reader.pages)
        metadata = reader.metadata or {}
        info.title = clean_pdf_metadata(getattr(metadata, "title", "") or metadata.get("/Title"))
        info.authors = clean_pdf_metadata(getattr(metadata, "author", "") or metadata.get("/Author"))
        creation = clean_pdf_metadata(metadata.get("/CreationDate"))
        year_match = re.search(r"(?:19|20)\d{2}", creation)
        info.year = year_match.group(0) if year_match else ""
        parts: list[str] = []
        for page in reader.pages[:5]:
            parts.append(page.extract_text() or "")
        info.text = "\n".join(parts)[:50000]
    except Exception as exc:
        info.metadata_error = type(exc).__name__
        return info

    if not info.title or GENERIC_TITLE.search(info.title.strip()):
        guessed = likely_title_from_text(info.text)
        if guessed:
            info.title = guessed
    sample = "\n".join([info.title, info.authors, info.text[:20000]])
    info.doi = list(dict.fromkeys(match.group(0).rstrip(".,;") for match in DOI_RE.finditer(sample)))
    info.arxiv = list(dict.fromkeys(match.group(1) for match in ARXIV_RE.finditer(sample)))
    return info


def title_score(row_title: str, path: Path, info: PdfInfo) -> float:
    title_key = normalized(row_title)
    if len(title_key) < 12 or GENERIC_TITLE.search(row_title.strip()):
        return 0.0
    filename_key = normalized(re.sub(r"^\d+[-_ ]+", "", path.stem))
    metadata_key = normalized(info.title)
    text_key = normalized(info.text[:9000])
    score = SequenceMatcher(None, filename_key, title_key).ratio()
    if title_key and (title_key in filename_key or filename_key in title_key and len(filename_key) >= 15):
        score = max(score, 0.97)
    if metadata_key:
        score = max(score, SequenceMatcher(None, metadata_key, title_key).ratio())
        if title_key in metadata_key or metadata_key in title_key and len(metadata_key) >= 15:
            score = max(score, 0.99)
    if title_key in text_key:
        score = max(score, 0.98)
    return score


def match_uploaded(path: Path, rows: list[dict[str, str]], texts: dict[str, str]) -> MatchResult:
    id_in_name = SOURCE_ID_RE.search(path.name.upper())
    info = inspect_pdf(path)
    if id_in_name and any(row["Κωδικός"] == id_in_name.group(0) for row in rows):
        return MatchResult(id_in_name.group(0), "κωδικός στο όνομα", info)

    pdf_ids = {f"doi:{value.casefold()}" for value in info.doi}
    pdf_ids.update(f"arxiv:{value}" for value in info.arxiv)
    strong_matches: list[str] = []
    for row in rows:
        row_ids = identities(row.get("Σύνδεσμος", ""), row.get("Τίτλος", ""), texts.get(row["Κωδικός"], ""))
        if pdf_ids & row_ids:
            strong_matches.append(row["Κωδικός"])
    if len(strong_matches) == 1:
        return MatchResult(strong_matches[0], "DOI ή arXiv ID", info)
    if len(strong_matches) > 1:
        return MatchResult(None, "πολλαπλές εγγραφές με το ίδιο ισχυρό αναγνωριστικό", info)

    scores = sorted(
        (
            title_score(row.get("Τίτλος", ""), path, info),
            row["Κωδικός"],
            row.get("Τίτλος", ""),
        )
        for row in rows
    , reverse=True)
    useful = [item for item in scores if item[0] >= 0.45][:3]
    if scores and scores[0][0] >= 0.90 and (len(scores) == 1 or scores[0][0] - scores[1][0] >= 0.06):
        return MatchResult(scores[0][1], f"μοναδική ισχυρή ομοιότητα τίτλου {scores[0][0]:.2f}", info, useful)
    return MatchResult(None, "δεν βρέθηκε ασφαλής μοναδική αντιστοίχιση", info, useful)


def inferred_type(path: Path, info: PdfInfo) -> str:
    sample = " ".join([path.name, info.title, info.text[:2000]]).casefold()
    if any(word in sample for word in ("dissertation", "thesis", "διπλωματική", "doctoral", "master of")):
        return "διπλωματική ή διατριβή"
    if info.doi or info.arxiv or "abstract" in sample:
        return "ακαδημαϊκή εργασία"
    if any(word in sample for word in ("white paper", "whitepaper", "report", "evaluation plan")):
        return "θεσμική ή τεχνική αναφορά"
    return "βιβλίο ή κεφάλαιο"


def strong_new_title(info: PdfInfo, path: Path) -> str:
    title = re.sub(r"\s+", " ", info.title).strip(" -_:.")
    if not title or GENERIC_TITLE.search(title) or len(normalized_words(title)) < 15:
        filename = re.sub(r"[_-]+", " ", path.stem)
        filename = re.sub(r"\s+", " ", filename).strip()
        if not GENERIC_TITLE.search(filename) and len(normalized_words(filename)) >= 20:
            title = filename
    if GENERIC_TITLE.search(title) or len(normalized_words(title)) < 15:
        return ""
    return title[:300]


def new_source_id(path: Path, existing_ids: set[str]) -> str:
    base = sha256(path).upper()
    for offset in range(0, len(base) - 10):
        source_id = "SRC-" + base[offset:offset + 10]
        if source_id not in existing_ids:
            return source_id
    raise RuntimeError("δεν ήταν δυνατό να δημιουργηθεί μοναδικός κωδικός")


def create_source_from_pdf(path: Path, info: PdfInfo, rows: list[dict[str, str]]) -> tuple[str | None, str]:
    title = strong_new_title(info, path)
    if not title or len(info.text.strip()) < 120:
        return None, "δεν υπάρχουν αρκετά αξιόπιστα στοιχεία για νέα πηγή"
    existing_ids = {row["Κωδικός"] for row in rows}
    source_id = new_source_id(path, existing_ids)
    link = ""
    verification = "εκκρεμεί"
    if info.doi:
        link = f"https://doi.org/{info.doi[0]}"
        verification = "μόνο καταγεγραμμένος σύνδεσμος"
    elif info.arxiv:
        link = f"https://arxiv.org/abs/{info.arxiv[0]}"
        verification = "μόνο καταγεγραμμένος σύνδεσμος"
    markdown = [
        f"# {title}", "",
        "> Η εγγραφή δημιουργήθηκε από πρωτότυπο PDF που δεν υπήρχε ακόμη στον κατάλογο.",
        "> Χρειάζεται πλήρης μετατροπή σε Markdown και έλεγχος πριν χρησιμοποιηθεί ως παραπομπή.", "",
    ]
    if info.authors:
        markdown.append(f"- **Συγγραφείς:** {info.authors}")
    if info.year:
        markdown.append(f"- **Έτος:** {info.year}")
    if link:
        markdown.append(f"- **Σύνδεσμος:** {link}")
    markdown.append(f"- **Πρωτότυπο:** `πρωτότυπα/{source_id}.pdf`")
    (SOURCES / f"{source_id}.md").write_text("\n".join(markdown) + "\n", encoding="utf-8")
    rows.append({
        "Κωδικός": source_id,
        "Τίτλος": title,
        "Συγγραφείς": info.authors,
        "Έτος": info.year,
        "Σύνδεσμος": link,
        "Τύπος": inferred_type(path, info),
        "Θέματα": "χωρίς κατηγορία",
        "Κατάσταση": "μόνο μεταδεδομένα",
        "Επιβεβαίωση": verification,
        "Προτεραιότητα": "χρειάζεται διόρθωση",
        "Σημειώσεις": "Δημιουργήθηκε από πρωτότυπο PDF· χρειάζεται πλήρης μετατροπή και θεματική αξιολόγηση.",
    })
    target = ORIGINALS / f"{source_id}.pdf"
    shutil.move(str(path), target)
    return source_id, f"δημιουργήθηκε νέα εγγραφή «{title}»"


def repair_row_from_pdf(row: dict[str, str], info: PdfInfo) -> bool:
    changed = False
    title = strong_new_title(info, Path(row.get("Τίτλος", "source.pdf")))
    if (GENERIC_TITLE.search(row.get("Τίτλος", "").strip()) or len(normalized_words(row.get("Τίτλος", ""))) < 12) and title:
        row["Τίτλος"] = title
        changed = True
    if not row.get("Συγγραφείς") and info.authors:
        row["Συγγραφείς"] = info.authors
        changed = True
    if not row.get("Έτος") and info.year:
        row["Έτος"] = info.year
        changed = True
    if not row.get("Σύνδεσμος"):
        if info.doi:
            row["Σύνδεσμος"] = f"https://doi.org/{info.doi[0]}"
            row["Επιβεβαίωση"] = "μόνο καταγεγραμμένος σύνδεσμος"
            changed = True
        elif info.arxiv:
            row["Σύνδεσμος"] = f"https://arxiv.org/abs/{info.arxiv[0]}"
            row["Επιβεβαίωση"] = "μόνο καταγεγραμμένος σύνδεσμος"
            changed = True
    return changed


def import_uploaded(rows: list[dict[str, str]], *, create_missing: bool) -> tuple[list[str], list[tuple[Path, MatchResult]], bool]:
    ORIGINALS.mkdir(parents=True, exist_ok=True)
    INCOMING.mkdir(parents=True, exist_ok=True)
    texts = {row["Κωδικός"]: source_text(SOURCES, row["Κωδικός"]) for row in rows}
    notes: list[str] = []
    pending: list[tuple[Path, MatchResult]] = []
    catalog_changed = False
    candidates = list(INCOMING.rglob("*.pdf"))
    candidates.extend(path for path in ORIGINALS.glob("*.pdf") if not SOURCE_ID_RE.fullmatch(path.stem))
    for path in sorted(set(candidates)):
        result = match_uploaded(path, rows, texts)
        if not result.source_id:
            if create_missing:
                source_id, reason = create_source_from_pdf(path, result.info, rows)
                if source_id:
                    texts[source_id] = source_text(SOURCES, source_id)
                    notes.append(f"{path.name} → {source_id}.pdf ({reason})")
                    catalog_changed = True
                    continue
            notes.append(f"{path.name}: {result.reason}")
            pending.append((path, result))
            continue
        target = ORIGINALS / f"{result.source_id}.pdf"
        row = next(row for row in rows if row["Κωδικός"] == result.source_id)
        catalog_changed = repair_row_from_pdf(row, result.info) or catalog_changed
        if target.exists():
            if sha256(path) == sha256(target):
                path.unlink()
                notes.append(f"{path.name}: αφαιρέθηκε ακριβές διπλότυπο του {result.source_id}")
            else:
                alternate = ORIGINALS / f"{result.source_id}__εναλλακτικό-{sha256(path)[:10].upper()}.pdf"
                shutil.move(str(path), alternate)
                notes.append(f"{path.name} → {alternate.name} (διαφορετική έκδοση της ίδιας πηγής)")
            continue
        shutil.move(str(path), target)
        notes.append(f"{path.name} → {target.name} ({result.reason})")
    return notes, pending, catalog_changed


def requested_ids(path: Path | None) -> set[str] | None:
    if not path or not path.exists():
        return None
    result = set(SOURCE_ID_RE.findall(path.read_text(encoding="utf-8", errors="replace")))
    return result or None


def write_pending_report(pending: list[tuple[Path, MatchResult]]) -> None:
    lines = [
        "# Εκκρεμή πρωτότυπα", "",
        "Τα παρακάτω PDF δεν συνδέθηκαν αυθαίρετα. Εμφανίζονται τα στοιχεία που διαβάστηκαν και οι καλύτεροι υποψήφιοι.", "",
    ]
    if not pending:
        lines.append("Δεν υπάρχουν εκκρεμή PDF.")
    for path, result in pending:
        info = result.info
        lines.extend([
            f"## {path.name}", "",
            f"- **Αποτέλεσμα:** {result.reason}",
            f"- **Τίτλος PDF:** {info.title or 'δεν αναγνωρίστηκε'}",
            f"- **Συγγραφείς:** {info.authors or 'δεν αναγνωρίστηκαν'}",
            f"- **Σελίδες:** {info.pages or 'άγνωστο'}",
            f"- **DOI:** {', '.join(info.doi) or 'δεν βρέθηκε'}",
            f"- **arXiv:** {', '.join(info.arxiv) or 'δεν βρέθηκε'}",
        ])
        if result.candidates:
            lines.extend(["", "Καλύτεροι υποψήφιοι:", ""])
            lines.extend(
                f"- `{source_id}` — {title} — βαθμός `{score:.2f}`"
                for score, source_id, title in result.candidates
            )
        if info.metadata_error:
            lines.append(f"- **Σφάλμα ανάγνωσης:** {info.metadata_error}")
        lines.append("")
    PENDING_REPORT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


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
        lines.extend(["", "## Αρχεία που αντιστοιχίστηκαν ή δημιουργήθηκαν", ""])
        lines.extend(f"- {note}" for note in import_notes)
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--λήψη", "--download", action="store_true")
    parser.add_argument("--όριο", "--limit", type=int, default=100)
    parser.add_argument("--κωδικοί-αρχείο", "--ids-file", type=Path)
    parser.add_argument("--επανάληψη", "--retry", action="store_true")
    parser.add_argument("--χωρίς-νέες-εγγραφές", "--no-create-missing", action="store_true")
    args = parser.parse_args()

    rows = read_catalog()
    previous = read_previous()
    notes, pending, catalog_changed = import_uploaded(rows, create_missing=not args.χωρίς_νέες_εγγραφές)
    if catalog_changed:
        write_catalog(rows)
        subprocess.run([sys.executable, str(ROOT / "εργαλεία" / "εισαγωγή.py"), "--catalog-only"], cwd=ROOT, check=True)
    wanted = requested_ids(args.κωδικοί_αρχείο)
    results: dict[str, DownloadResult] = {}

    for row in rows:
        source_id = row["Κωδικός"]
        shortcut = ORIGINALS / f"{source_id}.url"
        if (ORIGINALS / f"{source_id}.pdf").exists() or is_document_candidate(row):
            if shortcut.exists():
                shortcut.unlink()
        elif is_url_only(row) and row.get("Σύνδεσμος"):
            write_shortcut(source_id, row["Σύνδεσμος"])

    if args.λήψη:
        priorities = {"υψηλή": 0, "μεσαία": 1, "χρειάζεται διόρθωση": 2, "χαμηλή": 3}
        candidates = []
        for row in rows:
            source_id = row["Κωδικός"]
            if wanted is not None and source_id not in wanted:
                continue
            if (ORIGINALS / f"{source_id}.pdf").exists() or is_url_only(row) or not row.get("Σύνδεσμος"):
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
            time.sleep(0.15)

    write_pending_report(pending)
    write_report(rows, previous, results, notes)
    print(
        f"Ελέγχθηκαν {len(rows)} πηγές, έγιναν {len(results)} προσπάθειες λήψης "
        f"και παρέμειναν {len(pending)} μη ασφαλείς αντιστοιχίσεις."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
