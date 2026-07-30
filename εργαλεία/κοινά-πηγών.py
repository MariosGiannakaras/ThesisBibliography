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


def explicit_source_sample(link: str, title: str, text: str) -> str:
    """Επιστρέφει μόνο στοιχεία ταυτότητας από την κεφαλή, όχι citations του σώματος."""
    lines: list[str] = []
    for line in text.splitlines()[:100]:
        low = line.casefold().strip()
        if (
            low.startswith(("> source:", "source:", "doi:", "arxiv:"))
            or "doi.org/" in low
            or "arxiv.org/abs/" in low
            or "openreview.net/forum?" in low
            or "openreview.net/pdf?" in low
        ):
            lines.append(line)
    return "\n".join([link or "", title or "", *lines])


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
    if url:
        result.add(f"url:{url.casefold()}")
    return result


def source_text(sources: Path, source_id: str) -> str:
    path = sources / f"{source_id}.md"
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""
