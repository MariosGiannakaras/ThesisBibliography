#!/usr/bin/env python3
"""Διορθώνει τίτλους και εμφανώς λανθασμένα έτη από DOI ή arXiv."""
from __future__ import annotations

import csv
import json
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

from sources_common import ARXIV_RE, DOI_RE, explicit_source_sample, source_text

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "sources.csv"
SOURCES = ROOT / "sources"
FIELDS = [
    "Κωδικός", "Τίτλος", "Συγγραφείς", "Έτος", "Σύνδεσμος",
    "Τύπος", "Θέματα", "Κατάσταση", "Επιβεβαίωση", "Προτεραιότητα", "Σημειώσεις",
]
GENERIC_TITLE = re.compile(
    r"^(?:https?[-_:]|thesis(?:\.pdf)?$|applsci-\d|academic editors?:|"
    r"verifying your browser|pdf[-_]|ebook[-_]|final-web-version-report|agents\s*-\s*kaggle|"
    r"arxiv[-_:]|\[?\d{4}\.\d{4,5}\]?)",
    re.IGNORECASE,
)
CONFIRMED = {"επιβεβαιωμένη μέσω arXiv", "επιβεβαιωμένη μέσω Crossref"}
CURRENT_YEAR = datetime.now(timezone.utc).year


def request(url: str, accept: str) -> bytes:
    error: Exception | None = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "ThesisBibliography/1.0", "Accept": accept},
            )
            with urllib.request.urlopen(req, timeout=30) as response:
                return response.read()
        except Exception as exc:
            error = exc
            if attempt < 2:
                time.sleep(2 ** attempt)
    raise RuntimeError(f"Αποτυχία ανάκτησης μεταδεδομένων: {url}") from error


def arxiv_metadata(arxiv_id: str) -> dict[str, str] | None:
    root = ET.fromstring(
        request(
            "https://export.arxiv.org/api/query?id_list=" + urllib.parse.quote(arxiv_id),
            "application/atom+xml",
        )
    )
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    entry = root.find("atom:entry", ns)
    if entry is None:
        return None
    title = re.sub(r"\s+", " ", entry.findtext("atom:title", default="", namespaces=ns)).strip()
    authors = [
        author.findtext("atom:name", default="", namespaces=ns).strip()
        for author in entry.findall("atom:author", ns)
    ]
    published = entry.findtext("atom:published", default="", namespaces=ns)
    if not title:
        return None
    return {
        "Τίτλος": title,
        "Συγγραφείς": "; ".join(name for name in authors if name),
        "Έτος": published[:4],
        "Σύνδεσμος": f"https://arxiv.org/abs/{arxiv_id}",
        "Τύπος": "ακαδημαϊκή εργασία",
        "Επιβεβαίωση": "επιβεβαιωμένη μέσω arXiv",
    }


def crossref_metadata(doi: str) -> dict[str, str] | None:
    payload = json.loads(
        request(
            "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe=""),
            "application/json",
        ).decode("utf-8")
    )["message"]
    titles = payload.get("title") or []
    title = re.sub(r"\s+", " ", str(titles[0] if titles else "")).strip()
    if not title:
        return None
    authors = []
    for item in payload.get("author") or []:
        name = " ".join(part for part in (item.get("given", ""), item.get("family", "")) if part).strip()
        if name:
            authors.append(name)
    date_parts = (payload.get("published") or payload.get("issued") or {}).get("date-parts") or []
    year = str(date_parts[0][0]) if date_parts and date_parts[0] else ""
    return {
        "Τίτλος": title,
        "Συγγραφείς": "; ".join(authors),
        "Έτος": year,
        "Σύνδεσμος": f"https://doi.org/{doi}",
        "Τύπος": "ακαδημαϊκή εργασία",
        "Επιβεβαίωση": "επιβεβαιωμένη μέσω Crossref",
    }


def arxiv_expected_year(arxiv_id: str) -> int | None:
    try:
        prefix = int(arxiv_id[:2])
    except (TypeError, ValueError):
        return None
    # Το σύγχρονο YYMM.nnnnn format ξεκινά το 2007.
    return 2000 + prefix if 7 <= prefix <= 99 else None


def year_is_suspicious(row: dict[str, str], arxiv_id: str | None) -> bool:
    raw = row.get("Έτος", "").strip()
    if not raw.isdigit():
        return True
    year = int(raw)
    if year < 1950 or year > CURRENT_YEAR + 1:
        return True
    if arxiv_id:
        expected = arxiv_expected_year(arxiv_id)
        if expected and abs(year - expected) > 1:
            return True
    return False


def needs_refresh(row: dict[str, str], arxiv_id: str | None, doi: str | None) -> bool:
    if GENERIC_TITLE.search(row.get("Τίτλος", "")):
        return True
    if year_is_suspicious(row, arxiv_id):
        return True
    if row.get("Επιβεβαίωση", "") not in CONFIRMED and (arxiv_id or doi):
        return True
    return False


def add_note(row: dict[str, str], note: str) -> None:
    notes = [value.strip() for value in row.get("Σημειώσεις", "").split(" | ") if value.strip()]
    if note not in notes:
        notes.append(note)
    row["Σημειώσεις"] = " | ".join(notes)


def main() -> int:
    with CATALOG.open(encoding="utf-8", newline="") as handle:
        rows = [dict(row) for row in csv.DictReader(handle)]

    updated = 0
    attempted = 0
    for row in rows:
        text = source_text(SOURCES, row["Κωδικός"])
        sample = explicit_source_sample(row.get("Σύνδεσμος", ""), row.get("Τίτλος", ""), text)
        arxiv_match = ARXIV_RE.search(sample)
        doi_match = DOI_RE.search(sample)
        arxiv_id = arxiv_match.group(1) if arxiv_match else None
        doi = doi_match.group(0).rstrip(".") if doi_match else None
        if not needs_refresh(row, arxiv_id, doi):
            continue
        attempted += 1
        metadata = None
        try:
            if arxiv_id:
                metadata = arxiv_metadata(arxiv_id)
            elif doi:
                metadata = crossref_metadata(doi)
        except (RuntimeError, ET.ParseError, KeyError, json.JSONDecodeError):
            continue
        if metadata:
            old_title = row.get("Τίτλος", "")
            old_year = row.get("Έτος", "")
            row.update({key: value for key, value in metadata.items() if value})
            if old_title != row.get("Τίτλος"):
                add_note(row, f"Αυτόματη διόρθωση παλιού τίτλου: {old_title}")
            if old_year and old_year != row.get("Έτος"):
                add_note(row, f"Αυτόματη διόρθωση παλιού έτους: {old_year}")
            updated += 1
            time.sleep(0.15)

    with CATALOG.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    subprocess.run([sys.executable, str(ROOT / "tools" / "import_sources.py"), "--catalog-only"], cwd=ROOT, check=True)
    print(f"Ελέγχθηκαν {attempted} εγγραφές και διορθώθηκαν {updated} τίτλοι ή έτη.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
