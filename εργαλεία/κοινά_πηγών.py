#!/usr/bin/env python3
"""Κοινές, αυστηρές βοηθητικές συναρτήσεις για τα εργαλεία πηγών."""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit

SOURCE_ID_RE = re.compile(r"SRC-[A-F0-9]{10}")
URL_RE = re.compile(r"https?://[^\s)>\]}'\"]+")
DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.IGNORECASE)
ARXIV_RE = re.compile(r"(?:arxiv\.org/(?:abs|pdf|html)/|arXiv:\s*)(\d{4}\.\d{4,5})(?:v\d+)?", re.IGNORECASE)
OPENREVIEW_RE = re.compile(r"openreview\.net/(?:forum|pdf)\?(?:id=)?([A-Za-z0-9_-]+)", re.IGNORECASE)
SOURCE_MARKER_RE = re.compile(r"^>\s*Source:\s*(\S+)", re.IGNORECASE | re.MULTILINE)
STANDALONE_ID_URL_RE = re.compile(
    r"^https?://(?:www\.)?(?:doi\.org/10\.|arxiv\.org/(?:abs|pdf|html)/|openreview\.net/(?:forum|pdf)\?)\S+$",
    re.IGNORECASE,
)
HEADER_MARKERS = ("> source:", "source:", "doi:", "arxiv:", "citation:")


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def normalized(value: str) -> str:
    value = unicodedata.normalize("NFKD", value or "").casefold()
    return "".join(ch for ch in value if ch.isalnum())


def normalized_words(value: str) -> str:
    value = unicodedata.normalize("NFKC", value or "").casefold()
    return " ".join("".join(ch if ch.isalnum() else " " for ch in value).split())


def canonical_url(url: str) -> str:
    url = clean(url).rstrip(".,;:)")
    if not url:
        return ""
    arxiv = ARXIV_RE.search(url)
    if arxiv:
        return f"https://arxiv.org/abs/{arxiv.group(1)}"
    doi = DOI_RE.search(unquote(url))
    if doi:
        return f"https://doi.org/{doi.group(0).rstrip('.').casefold()}"
    parts = urlsplit(url)
    if not parts.scheme:
        return url
    host = parts.netloc.lower().removeprefix("www.")
    return parts._replace(netloc=host, fragment="").geturl().rstrip("/")


def meaningful_resource_url(url: str) -> bool:
    """Αποκλείει homepages και κανάλια που μπορεί να φιλοξενούν πολλές πηγές."""
    if not url:
        return False
    parts = urlsplit(url)
    host = parts.netloc.casefold().removeprefix("www.")
    path = parts.path.rstrip("/")
    if not path and not parts.query:
        return False
    if host in {"youtube.com", "m.youtube.com"} and (
        path.startswith("/@") or path.startswith("/channel/") or path.startswith("/c/")
    ):
        return False
    if host == "openreview.net" and path in {"", "/"}:
        return False
    return True


def _joined_header_lines(text: str) -> list[str]:
    """Συλλέγει ρητές γραμμές κεφαλίδας και σύντομες συνέχειές τους.

    Πολλά PDF exports σπάνε DOI και τίτλους citation σε διαδοχικές γραμμές,
    π.χ. ``https://`` σε μία γραμμή και ``doi.org/...`` στην επόμενη.
    Κρατάμε μόνο μικρά παράθυρα μετά από ρητό marker ώστε να μη θεωρούνται
    οι βιβλιογραφικές αναφορές του σώματος ταυτότητα της πηγής.
    """
    raw_lines = text.splitlines()[:120]
    selected: list[str] = []
    continuation = 0
    for raw in raw_lines:
        stripped = raw.strip()
        low = stripped.casefold()
        if low.startswith(HEADER_MARKERS):
            selected.append(stripped)
            continuation = 8 if low.startswith("citation:") else 3
            continue
        if STANDALONE_ID_URL_RE.fullmatch(stripped):
            selected.append(stripped)
            continuation = 0
            continue
        if continuation > 0:
            if not stripped:
                continuation = 0
                continue
            selected.append(stripped)
            continuation -= 1
    return selected


def explicit_source_sample(link: str, title: str, text: str) -> str:
    """Κρατά μόνο ρητά στοιχεία κεφαλίδας και όχι citations του σώματος."""
    lines = _joined_header_lines(text)
    # Η ενοποίηση whitespace επιτρέπει την αναγνώριση line-broken DOI.
    joined = clean(" ".join(lines))
    return "\n".join([link or "", title or "", joined])


def identities(link: str, title: str, text: str) -> set[str]:
    sample = explicit_source_sample(link, title, text)
    result: set[str] = set()
    for match in ARXIV_RE.finditer(sample):
        result.add(f"arxiv:{match.group(1)}")
    for match in DOI_RE.finditer(sample):
        result.add(f"doi:{match.group(0).rstrip('.,;').casefold()}")
    for match in OPENREVIEW_RE.finditer(sample):
        result.add(f"openreview:{match.group(1)}")
    url = canonical_url(link)
    if meaningful_resource_url(url):
        result.add(f"url:{url.casefold()}")
    return result


def source_text(sources: Path, source_id: str) -> str:
    path = sources / f"{source_id}.md"
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""
