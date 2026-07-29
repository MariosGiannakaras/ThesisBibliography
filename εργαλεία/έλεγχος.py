#!/usr/bin/env python3
"""Ελέγχει ότι η απλή ελληνική δομή παραμένει συνεπής."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "πηγές"
CATALOG = ROOT / "κατάλογος" / "πηγές.csv"
INCOMING = ROOT / "νέες-πηγές"

REQUIRED_COLUMNS = {
    "Κωδικός", "Τίτλος", "Συγγραφείς", "Έτος", "Σύνδεσμος", "Τύπος",
    "Θέματα", "Κατάσταση", "Επιβεβαίωση", "Προτεραιότητα", "Σημειώσεις",
}
ALLOWED_STATUS = {
    "διαθέσιμο πλήρες κείμενο", "ελεγμένη", "ελλιπές κείμενο",
    "μόνο μεταδεδομένα", "αποτυχημένη εισαγωγή",
}
ALLOWED_VERIFICATION = {
    "επιβεβαιωμένη μέσω arXiv", "επιβεβαιωμένη μέσω Crossref",
    "πιθανή αντιστοίχιση OpenAlex", "μόνο καταγεγραμμένος σύνδεσμος", "εκκρεμεί",
}
ALLOWED_PRIORITY = {"υψηλή", "μεσαία", "χαμηλή", "χρειάζεται διόρθωση"}
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


def main() -> int:
    errors: list[str] = []
    if not CATALOG.exists():
        errors.append("Λείπει το κατάλογος/πηγές.csv")
        rows = []
    else:
        with CATALOG.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            rows = list(reader)
            columns = set(reader.fieldnames or [])
        if columns != REQUIRED_COLUMNS:
            errors.append(f"Λανθασμένες στήλες καταλόγου: {sorted(columns)}")

    ids = [row.get("Κωδικός", "") for row in rows]
    if len(ids) != len(set(ids)):
        errors.append("Υπάρχουν διπλοί κωδικοί πηγών")

    source_files = sorted(SOURCES.glob("ΠΗΓΗ-*.md")) if SOURCES.exists() else []
    file_ids = {path.stem for path in source_files}
    if set(ids) != file_ids:
        missing = sorted(set(ids) - file_ids)
        extra = sorted(file_ids - set(ids))
        if missing:
            errors.append(f"Λείπουν αρχεία για κωδικούς: {', '.join(missing[:10])}")
        if extra:
            errors.append(f"Υπάρχουν αρχεία χωρίς καταχώριση: {', '.join(extra[:10])}")

    hashes = [sha256(path) for path in source_files]
    if len(hashes) != len(set(hashes)):
        errors.append("Υπάρχουν ακριβή διπλότυπα αρχεία Markdown")

    for row in rows:
        sid = row.get("Κωδικός", "")
        if not sid.startswith("ΠΗΓΗ-"):
            errors.append(f"Μη έγκυρος κωδικός: {sid}")
        if not row.get("Τίτλος"):
            errors.append(f"{sid}: λείπει τίτλος")
        if row.get("Κατάσταση") not in ALLOWED_STATUS:
            errors.append(f"{sid}: μη έγκυρη κατάσταση")
        if row.get("Επιβεβαίωση") not in ALLOWED_VERIFICATION:
            errors.append(f"{sid}: μη έγκυρη επιβεβαίωση")
        if row.get("Προτεραιότητα") not in ALLOWED_PRIORITY:
            errors.append(f"{sid}: μη έγκυρη προτεραιότητα")

    for relative in OBSOLETE_PATHS:
        if (ROOT / relative).exists():
            errors.append(f"Παρέμεινε παλιά διαδρομή: {relative}")

    if INCOMING.exists():
        leftovers = [
            path for path in INCOMING.rglob("*")
            if path.is_file() and path.name != "README.md"
        ]
        if leftovers:
            errors.append("Ο φάκελος νέες-πηγές περιέχει μη επεξεργασμένα αρχεία")

    required = [
        ROOT / "README.md",
        ROOT / "κατάλογος" / "πηγές.md",
        ROOT / "κατάλογος" / "προβληματικές-πηγές.md",
        ROOT / "κατάλογος" / "προς-προσθήκη.md",
        ROOT / "νέες-πηγές" / "README.md",
    ]
    for path in required:
        if not path.exists():
            errors.append(f"Λείπει: {path.relative_to(ROOT)}")

    if errors:
        print("Ο έλεγχος απέτυχε:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Ο έλεγχος ολοκληρώθηκε για {len(rows)} πηγές.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
