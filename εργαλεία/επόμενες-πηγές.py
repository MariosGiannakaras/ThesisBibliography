#!/usr/bin/env python3
"""Ανανεώνει τη λίστα προτεινόμενων πηγών χωρίς δικτυακό enrichment."""

from __future__ import annotations

import csv
import importlib.util
import re
from pathlib import Path
from types import ModuleType
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parents[1]
CATALOG_CSV = ROOT / "κατάλογος" / "πηγές.csv"
SOURCES = ROOT / "πηγές"
METADATA_SCRIPT = ROOT / "εργαλεία" / "μεταδεδομένα.py"

ARXIV_ID_RE = re.compile(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d+)", re.IGNORECASE)
DOI_ID_RE = re.compile(r"(?:doi\.org/|doi\s*:\s*)(10\.\d{4,9}/[^\s)>\],;]+)", re.IGNORECASE)
PMLR_ID_RE = re.compile(r"proceedings\.mlr\.press/(v\d+)/([^/?#.]+)", re.IGNORECASE)

NON_BIBLIOGRAPHIC_MARKERS = (
    "github.com/arxiv/html_feedback",
    "github.com/brucemiller/latexml",
    "math.nist.gov/~bmiller/latexml",
)


def load_metadata_module() -> ModuleType:
    """Φορτώνει τις κοινές συναρτήσεις χωρίς να εκτελεί το πλήρες enrichment."""
    spec = importlib.util.spec_from_file_location(
        "thesis_bibliography_metadata",
        METADATA_SCRIPT,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Δεν ήταν δυνατή η φόρτωση του {METADATA_SCRIPT}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def canonical_identifier(value: str) -> str:
    """Επιστρέφει σταθερό identifier για γνωστά scholarly URL formats."""
    value = (value or "").strip()
    if not value:
        return ""

    if match := ARXIV_ID_RE.search(value):
        return f"arxiv:{match.group(1).lower()}"
    if match := DOI_ID_RE.search(value):
        return f"doi:{match.group(1).rstrip('.').lower()}"
    if match := PMLR_ID_RE.search(value):
        return f"pmlr:{match.group(1).lower()}:{match.group(2).lower()}"

    parsed = urlsplit(value)
    host = parsed.netloc.casefold().removeprefix("www.")
    if host == "openreview.net":
        forum_id = (parse_qs(parsed.query).get("id") or [""])[0]
        if forum_id:
            return f"openreview:{forum_id.casefold()}"

    path = parsed.path.rstrip("/")
    path = re.sub(r"\.(?:html?|pdf)$", "", path, flags=re.IGNORECASE)
    return f"url:{host}{path.casefold()}" if host else ""


def collect_source_identifiers(rows: list[dict[str, str]], metadata: ModuleType) -> set[str]:
    """Συλλέγει identifiers από τον κατάλογο και τις κεφαλίδες των Markdown."""
    identifiers: set[str] = set()
    for row in rows:
        if identifier := canonical_identifier(row.get("Σύνδεσμος", "")):
            identifiers.add(identifier)

        source_id = row.get("Κωδικός", "")
        path = SOURCES / f"{source_id}.md"
        if not source_id or not path.exists():
            continue
        head = "\n".join(
            path.read_text(encoding="utf-8", errors="replace").splitlines()[:40]
        )
        for url in metadata.URL_RE.findall(head):
            if identifier := canonical_identifier(url.rstrip(".,;:)")):
                identifiers.add(identifier)
    return identifiers


def augment_rows_with_identifier_matches(
    rows: list[dict[str, str]],
    metadata: ModuleType,
) -> list[dict[str, str]]:
    """Προσθέτει εικονικό title match όταν μία γνωστή πηγή υπάρχει με άλλο label."""
    augmented = [dict(row) for row in rows]
    identifiers = collect_source_identifiers(rows, metadata)
    titles = [row.get("Τίτλος", "") for row in rows]

    for target_title, target_link, _ in metadata.KNOWN_TARGETS:
        already_matched = any(
            metadata.title_similarity(target_title, existing) >= 0.9
            for existing in titles
        )
        target_identifier = canonical_identifier(target_link)
        if not already_matched and target_identifier in identifiers:
            augmented.append({"Κωδικός": "", "Τίτλος": target_title})
    return augmented


def is_bibliographic_candidate(url: str) -> bool:
    """Απορρίπτει τεχνικά boilerplate links που δεν είναι πηγές."""
    normalized = (url or "").casefold()
    return not any(marker in normalized for marker in NON_BIBLIOGRAPHIC_MARKERS)


def filtered_reference_candidates(
    rows: list[dict[str, str]],
    metadata: ModuleType,
) -> list[tuple[str, int, list[str]]]:
    """Διατηρεί μόνο επαναλαμβανόμενα links με βιβλιογραφική χρησιμότητα."""
    candidates = metadata.mine_references(rows)
    return [item for item in candidates if is_bibliographic_candidate(item[0])]


def main() -> int:
    with CATALOG_CSV.open(encoding="utf-8", newline="") as handle:
        rows = [dict(row) for row in csv.DictReader(handle)]

    metadata = load_metadata_module()
    augmented_rows = augment_rows_with_identifier_matches(rows, metadata)
    original_mine_references = metadata.mine_references
    metadata.mine_references = lambda items: [
        item
        for item in original_mine_references(items)
        if is_bibliographic_candidate(item[0])
    ]
    metadata.write_next_sources(augmented_rows)
    print(f"Ανανεώθηκε η λίστα επόμενων πηγών από {len(rows)} εγγραφές.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
