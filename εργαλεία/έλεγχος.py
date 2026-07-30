#!/usr/bin/env python3
"""Ελέγχει ότι η απλή ελληνική δομή και οι συνδέσεις πηγών παραμένουν συνεπείς."""
from __future__ import annotations

import csv
import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "πηγές"
ORIGINALS = ROOT / "πρωτότυπα"
CATALOG = ROOT / "κατάλογος" / "πηγές.csv"
ORIGINALS_REPORT = ROOT / "κατάλογος" / "πρωτότυπα.csv"
INCOMING = ROOT / "νέες-πηγές"
INCOMING_ORIGINALS = ROOT / "νέα-πρωτότυπα"
GIT_ATTRIBUTES = ROOT / ".gitattributes"

REQUIRED_COLUMNS = {
    "Κωδικός", "Τίτλος", "Συγγραφείς", "Έτος", "Σύνδεσμος", "Τύπος",
    "Θέματα", "Κατάσταση", "Επιβεβαίωση", "Προτεραιότητα", "Σημειώσεις",
}
ORIGINAL_REPORT_COLUMNS = {
    "Κωδικός", "Τίτλος", "Κατάσταση", "Αρχείο", "Σύνδεσμος",
    "Προσπάθειες", "Τελευταίος έλεγχος", "Σημείωση",
}
ALLOWED_STATUS = {
    "διαθέσιμο πλήρες κείμενο", "ελεγμένη", "ελλιπές κείμενο",
    "μόνο μεταδεδομένα", "αποτυχημένη εισαγωγή",
}
ALLOWED_VERIFICATION = {
    "επιβεβαιωμένη μέσω arXiv", "επιβεβαιωμένη μέσω Crossref",
    "πιθανή αντιστοίχιση OpenAlex", "μόνο καταγεγραμμένος σύνδεσμος",
    "δεν βρέθηκε αυτόματη αντιστοίχιση", "εκκρεμεί",
}
ALLOWED_PRIORITY = {"υψηλή", "μεσαία", "χαμηλή", "χρειάζεται διόρθωση"}
SOURCE_ID_RE = re.compile(r"SRC-[A-F0-9]{10}")
ORIGINAL_NAME_RE = re.compile(
    r"(SRC-[A-F0-9]{10})(?:__εναλλακτικό-SRC-[A-F0-9]{10})?\.(?:pdf|url)"
)
OBSOLETE_PATHS = [
    "catalog", "curation", "imports", "notes", "queues", "sources", "incoming",
    "archive", "workspace", "AGENTS.md",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_catalog(errors: list[str]) -> list[dict[str, str]]:
    if not CATALOG.exists():
        errors.append("Λείπει το κατάλογος/πηγές.csv")
        return []
    with CATALOG.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        columns = set(reader.fieldnames or [])
    if columns != REQUIRED_COLUMNS:
        errors.append(f"Λανθασμένες στήλες καταλόγου: {sorted(columns)}")
    return rows


def validate_sources(rows: list[dict[str, str]], errors: list[str]) -> set[str]:
    ids = [row.get("Κωδικός", "") for row in rows]
    if len(ids) != len(set(ids)):
        errors.append("Υπάρχουν διπλοί κωδικοί πηγών")

    all_markdown = sorted(SOURCES.glob("*.md")) if SOURCES.exists() else []
    invalid_names = [path.name for path in all_markdown if not SOURCE_ID_RE.fullmatch(path.stem)]
    if invalid_names:
        errors.append(f"Μη έγκυρα ονόματα αρχείων πηγών: {', '.join(invalid_names[:10])}")
    source_files = [path for path in all_markdown if SOURCE_ID_RE.fullmatch(path.stem)]
    file_ids = {path.stem for path in source_files}
    catalog_ids = set(ids)
    if catalog_ids != file_ids:
        missing = sorted(catalog_ids - file_ids)
        extra = sorted(file_ids - catalog_ids)
        if missing:
            errors.append(f"Λείπουν αρχεία για κωδικούς: {', '.join(missing[:10])}")
        if extra:
            errors.append(f"Υπάρχουν αρχεία χωρίς καταχώριση: {', '.join(extra[:10])}")

    hashes = [sha256(path) for path in all_markdown]
    if len(hashes) != len(set(hashes)):
        errors.append("Υπάρχουν ακριβή διπλότυπα αρχεία Markdown")

    for row in rows:
        source_id = row.get("Κωδικός", "")
        if not SOURCE_ID_RE.fullmatch(source_id):
            errors.append(f"Μη έγκυρος κωδικός: {source_id}")
        if not row.get("Τίτλος"):
            errors.append(f"{source_id}: λείπει τίτλος")
        if row.get("Κατάσταση") not in ALLOWED_STATUS:
            errors.append(f"{source_id}: μη έγκυρη κατάσταση")
        if row.get("Επιβεβαίωση") not in ALLOWED_VERIFICATION:
            errors.append(f"{source_id}: μη έγκυρη επιβεβαίωση")
        if row.get("Προτεραιότητα") not in ALLOWED_PRIORITY:
            errors.append(f"{source_id}: μη έγκυρη προτεραιότητα")
    return catalog_ids


def validate_originals(catalog_ids: set[str], errors: list[str]) -> None:
    if ORIGINALS.exists():
        for path in sorted(item for item in ORIGINALS.iterdir() if item.is_file()):
            match = ORIGINAL_NAME_RE.fullmatch(path.name)
            if not match:
                errors.append(f"Πρωτότυπο χωρίς ασφαλή σύνδεση SRC: {path.name}")
                continue
            if match.group(1) not in catalog_ids:
                errors.append(f"Πρωτότυπο για ανύπαρκτη πηγή: {path.name}")

    if ORIGINALS_REPORT.exists():
        with ORIGINALS_REPORT.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            report_rows = list(reader)
            columns = set(reader.fieldnames or [])
        if columns != ORIGINAL_REPORT_COLUMNS:
            errors.append(f"Λανθασμένες στήλες καταλόγου πρωτοτύπων: {sorted(columns)}")
        report_ids = [row.get("Κωδικός", "") for row in report_rows]
        if len(report_ids) != len(set(report_ids)):
            errors.append("Υπάρχουν διπλοί κωδικοί στον κατάλογο πρωτοτύπων")
        unknown = sorted(set(report_ids) - catalog_ids)
        if unknown:
            errors.append(f"Ο κατάλογος πρωτοτύπων περιέχει ανύπαρκτους κωδικούς: {', '.join(unknown[:10])}")

    if not GIT_ATTRIBUTES.exists() or "*.pdf filter=lfs" not in GIT_ATTRIBUTES.read_text(encoding="utf-8", errors="replace"):
        errors.append("Το Git LFS δεν είναι ρυθμισμένο για όλα τα PDF")


def main() -> int:
    errors: list[str] = []
    rows = read_catalog(errors)
    catalog_ids = validate_sources(rows, errors)
    validate_originals(catalog_ids, errors)

    for relative in OBSOLETE_PATHS:
        if (ROOT / relative).exists():
            errors.append(f"Παρέμεινε παλιά διαδρομή: {relative}")

    if INCOMING.exists():
        leftovers = [path for path in INCOMING.rglob("*") if path.is_file() and path.name != "README.md"]
        if leftovers:
            errors.append("Ο φάκελος νέες-πηγές περιέχει μη επεξεργασμένα αρχεία")

    # Τα PDF στο νέα-πρωτότυπα επιτρέπονται: περιμένουν τον ειδικό αυτοματισμό.
    if INCOMING_ORIGINALS.exists():
        unsupported = [
            path for path in INCOMING_ORIGINALS.rglob("*")
            if path.is_file() and path.name != "README.md" and path.suffix.casefold() != ".pdf"
        ]
        if unsupported:
            errors.append(
                "Ο φάκελος νέα-πρωτότυπα περιέχει μη υποστηριζόμενα αρχεία: "
                + ", ".join(path.name for path in unsupported[:10])
            )

    required = [
        ROOT / "README.md",
        ROOT / "κατάλογος" / "πηγές.md",
        ROOT / "κατάλογος" / "προβληματικές-πηγές.md",
        ROOT / "κατάλογος" / "προς-προσθήκη.md",
        ROOT / "νέες-πηγές" / "README.md",
        ROOT / "νέα-πρωτότυπα" / "README.md",
    ]
    for path in required:
        if not path.exists():
            errors.append(f"Λείπει: {path.relative_to(ROOT)}")

    if errors:
        print("Ο έλεγχος απέτυχε:")
        for error in errors:
            print(f"- {error}")
        return 1

    original_count = len(list(ORIGINALS.glob("*.pdf"))) if ORIGINALS.exists() else 0
    print(f"Ο έλεγχος ολοκληρώθηκε για {len(rows)} πηγές και {original_count} PDF.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
