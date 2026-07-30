#!/usr/bin/env python3
"""Κοινά δεδομένα και βοηθητικές συναρτήσεις για τα πρωτότυπα."""
from __future__ import annotations

import csv
import hashlib
import re
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from pathlib import Path
from urllib.parse import urlsplit

from κοινά_πηγών import ARXIV_RE, DOI_RE, OPENREVIEW_RE, normalized, normalized_words

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
        or ("download" in low and "youtube" not in low)
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
    return row.get("Τύπος") in {
        "ιστοσελίδα", "τεκμηρίωση ή εκπαιδευτικό υλικό", "άγνωστος τύπος"
    }


def write_shortcut(source_id: str, url: str) -> Path:
    path = ORIGINALS / f"{source_id}.url"
    content = f"[InternetShortcut]\nURL={url}\n"
    if not path.exists() or path.read_text(encoding="utf-8", errors="replace") != content:
        path.write_text(content, encoding="utf-8", newline="\n")
    return path


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
        score = 20 if 4 <= len(words) <= 24 else 0
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
        info.text = "\n".join((page.extract_text() or "") for page in reader.pages[:5])[:50000]
    except Exception as exc:
        info.metadata_error = type(exc).__name__
        return info
    if not info.title or GENERIC_TITLE.search(info.title.strip()):
        info.title = likely_title_from_text(info.text) or info.title
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
    if title_key and (title_key in filename_key or (filename_key in title_key and len(filename_key) >= 15)):
        score = max(score, 0.97)
    if metadata_key:
        score = max(score, SequenceMatcher(None, metadata_key, title_key).ratio())
        if title_key in metadata_key or (metadata_key in title_key and len(metadata_key) >= 15):
            score = max(score, 0.99)
    if title_key in text_key:
        score = max(score, 0.98)
    return score


def strong_new_title(info: PdfInfo, path: Path) -> str:
    title = re.sub(r"\s+", " ", info.title).strip(" -_:.")
    if not title or GENERIC_TITLE.search(title) or len(normalized_words(title)) < 15:
        filename = re.sub(r"[_-]+", " ", path.stem)
        filename = re.sub(r"\s+", " ", filename).strip()
        if not GENERIC_TITLE.search(filename) and len(normalized_words(filename)) >= 20:
            title = filename
    if not title or GENERIC_TITLE.search(title) or len(normalized_words(title)) < 15:
        return ""
    return title[:300]
