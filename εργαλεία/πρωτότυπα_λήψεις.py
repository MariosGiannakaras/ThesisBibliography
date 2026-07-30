#!/usr/bin/env python3
"""Νόμιμη αναζήτηση και λήψη δημόσιων πρωτοτύπων PDF."""
from __future__ import annotations

import html
import json
import re
from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urljoin, urlsplit
from urllib.request import Request, urlopen

from κοινά_πηγών import ARXIV_RE, OPENREVIEW_RE, URL_RE, explicit_source_sample, identities
from πρωτότυπα_κοινά import DownloadResult, MAX_BYTES if False else None
from πρωτότυπα_κοινά import ORIGINALS, url_is_direct_pdf

USER_AGENT = "ThesisBibliography/1.1 (+https://github.com/MariosGiannakaras/ThesisBibliography)"
MAX_DOWNLOAD_BYTES = 180 * 1024 * 1024
ANTI_BOT = (
    b"verifying your browser", b"complete the check below", b"captcha",
    b"making sure you're not a bot", b"cloudflare",
)


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


def request_bytes(
    url: str,
    *,
    timeout: int = 35,
    limit: int = MAX_DOWNLOAD_BYTES,
) -> tuple[bytes, str, str]:
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
            if not isinstance(location, dict):
                continue
            for key in ("pdf_url", "landing_page_url"):
                if location.get(key):
                    result.append(location[key])
    return list(dict.fromkeys(result))


def candidate_urls(row: dict[str, str], text: str) -> list[str]:
    seeds: list[str] = []
    if row.get("Σύνδεσμος"):
        seeds.append(row["Σύνδεσμος"])
    seeds.extend(
        URL_RE.findall(
            explicit_source_sample(
                row.get("Σύνδεσμος", ""),
                row.get("Τίτλος", ""),
                text,
            )
        )
    )

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
