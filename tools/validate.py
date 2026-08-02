#!/usr/bin/env python3
"""Validate repository structure and source links after the English path migration."""
from __future__ import annotations

import csv
import hashlib
import re
import subprocess
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "sources"
ORIGINALS = ROOT / "originals"
UNMATCHED = ORIGINALS / "unidentified"
ANALYSES = ROOT / "analyses"
EXCERPTS = ROOT / "evidence"
CATALOG = ROOT / "catalog" / "sources.csv"
SELECTION = ROOT / "catalog" / "thesis-selection.csv"
ORIGINALS_REPORT = ROOT / "catalog" / "originals.csv"
INCOMING = ROOT / "new-sources"
INCOMING_ORIGINALS = ROOT / "new-originals"
GIT_ATTRIBUTES = ROOT / ".gitattributes"

REQUIRED_COLUMNS = {
    "Κωδικός", "Τίτλος", "Συγγραφείς", "Έτος", "Σύνδεσμος", "Τύπος",
    "Θέματα", "Κατάσταση", "Επιβεβαίωση", "Προτεραιότητα", "Σημειώσεις",
}
SELECTION_COLUMNS = {
    "Κωδικός", "Ρόλος", "Κατάσταση", "Κεφάλαια", "Θέματα", "Εξαγωγή", "Σημείωση",
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
LINKED_ORIGINAL_RE = re.compile(
    r"(SRC-[A-F0-9]{10})(?:__(?:alternative|conflict)-(?:SRC-[A-F0-9]{10}|[A-F0-9]{10,16}))?\.(?:pdf|url)",
    re.IGNORECASE,
)
LFS_OID_RE = re.compile(rb"oid sha256:([a-f0-9]{64})", re.IGNORECASE)
OBSOLETE_PATHS = [
    "curation", "imports", "notes", "queues", "incoming",
    "archive", "workspace", "AGENTS.md",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def pdf_identity(path: Path) -> str:
    with path.open("rb") as handle:
        prefix = handle.read(512)
    lfs = LFS_OID_RE.search(prefix)
    if lfs:
        return lfs.group(1).decode("ascii").lower()
    return sha256(path)


def validate_repository_paths(errors: list[str]) -> None:
    """Keep canonical tracked/worktree paths ASCII-safe after each intake run."""
    try:
        tracked = subprocess.check_output(
            ["git", "ls-files"], cwd=ROOT, text=True, stderr=subprocess.DEVNULL
        ).splitlines()
    except (OSError, subprocess.CalledProcessError):
        tracked = [
            path.relative_to(ROOT).as_posix()
            for path in ROOT.rglob("*")
            if path.is_file() and ".git" not in path.parts
        ]

    # During an intake run, an uploaded non-ASCII file can already be deleted from
    # the worktree but still be present in the Git index until the generated PR is
    # staged. Ignore those deleted intake paths; validate the resulting worktree.
    residual = sorted(
        relative for relative in tracked
        if (ROOT / relative).exists() and any(ord(char) > 127 for char in relative)
    )
    if residual:
        errors.append(
            "Υπάρχουν μη ASCII tracked paths μετά την επεξεργασία intake: "
            + ", ".join(residual[:10])
        )


def read_catalog(errors: list[str]) -> list[dict[str, str]]:
    if not CATALOG.exists():
        errors.append("Λείπει το catalog/sources.csv")
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
    pdfs: list[Path] = []
    if ORIGINALS.exists():
        for path in sorted(item for item in ORIGINALS.rglob("*") if item.is_file()):
            relative = path.relative_to(ORIGINALS)
            if path.name == "README.md":
                continue
            if path.suffix.casefold() == ".pdf":
                pdfs.append(path)
            if path.parent == ORIGINALS:
                match = LINKED_ORIGINAL_RE.fullmatch(path.name)
                if match:
                    if match.group(1).upper() not in catalog_ids:
                        errors.append(f"Πρωτότυπο για ανύπαρκτη πηγή: {path.name}")
                    continue
                if path.suffix.casefold() == ".pdf":
                    errors.append(
                        f"Μη συνδεδεμένο PDF στη ρίζα των πρωτοτύπων: {path.name}· "
                        "πρέπει να αρχειοθετηθεί στο unidentified/"
                    )
                    continue
                errors.append(f"Μη αναγνωρισμένο αρχείο στον φάκελο πρωτοτύπων: {path.name}")
                continue
            if UNMATCHED not in path.parents:
                errors.append(f"Μη αναγνωρισμένη υποδιαδρομή πρωτοτύπων: {relative}")
            elif path.suffix.casefold() != ".pdf":
                errors.append(f"Μη υποστηριζόμενο αρχείο στα μη ταυτοποιημένα πρωτότυπα: {relative}")

    by_identity: dict[str, list[Path]] = defaultdict(list)
    for path in pdfs:
        try:
            by_identity[pdf_identity(path)].append(path)
        except OSError as exc:
            errors.append(f"Δεν διαβάστηκε το πρωτότυπο {path.relative_to(ROOT)}: {type(exc).__name__}")
    exact_duplicates = [paths for paths in by_identity.values() if len(paths) > 1]
    for paths in exact_duplicates[:10]:
        names = ", ".join(path.relative_to(ROOT).as_posix() for path in paths)
        errors.append(f"Υπάρχουν ακριβή διπλότυπα PDF: {names}")

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


def validate_analysis_assets(catalog_ids: set[str], errors: list[str]) -> None:
    for directory, label in ((ANALYSES, "ανάλυση"), (EXCERPTS, "απόσπασμα")):
        if not directory.exists():
            errors.append(f"Λείπει ο φάκελος: {directory.relative_to(ROOT)}")
            continue
        for path in sorted(directory.glob("*.md")):
            if path.name == "README.md":
                continue
            if not SOURCE_ID_RE.fullmatch(path.stem):
                errors.append(f"Μη έγκυρο όνομα αρχείου {label}: {path.name}")
            elif path.stem not in catalog_ids:
                errors.append(f"{label.capitalize()} για ανύπαρκτη πηγή: {path.name}")

    if not SELECTION.exists():
        errors.append("Λείπει το catalog/thesis-selection.csv")
    else:
        with SELECTION.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            rows = list(reader)
            columns = set(reader.fieldnames or [])
        if columns != SELECTION_COLUMNS:
            errors.append(f"Λανθασμένες στήλες μητρώου επιλογής: {sorted(columns)}")
        ids = [row.get("Κωδικός", "").strip() for row in rows if row.get("Κωδικός", "").strip()]
        if len(ids) != len(set(ids)):
            errors.append("Υπάρχουν διπλοί κωδικοί στο μητρώο επιλογής")
        unknown = sorted(set(ids) - catalog_ids)
        if unknown:
            errors.append(f"Το μητρώο επιλογής περιέχει ανύπαρκτους κωδικούς: {', '.join(unknown[:10])}")


def main() -> int:
    errors: list[str] = []
    validate_repository_paths(errors)
    rows = read_catalog(errors)
    catalog_ids = validate_sources(rows, errors)
    validate_originals(catalog_ids, errors)
    validate_analysis_assets(catalog_ids, errors)

    for relative in OBSOLETE_PATHS:
        if (ROOT / relative).exists():
            errors.append(f"Παρέμεινε παλιά διαδρομή: {relative}")

    if INCOMING.exists():
        leftovers = [path for path in INCOMING.rglob("*") if path.is_file() and path.name != "README.md"]
        if leftovers:
            errors.append("Ο φάκελος new-sources περιέχει μη επεξεργασμένα αρχεία")

    if INCOMING_ORIGINALS.exists():
        pending_pdfs = [
            path for path in INCOMING_ORIGINALS.rglob("*.pdf")
            if path.is_file()
        ]
        if pending_pdfs:
            errors.append(
                "Ο φάκελος new-originals περιέχει PDF που δεν αρχειοθετήθηκαν: "
                + ", ".join(path.name for path in pending_pdfs[:10])
            )
        unsupported = [
            path for path in INCOMING_ORIGINALS.rglob("*")
            if path.is_file() and path.name != "README.md" and path.suffix.casefold() != ".pdf"
        ]
        if unsupported:
            errors.append(
                "Ο φάκελος new-originals περιέχει μη υποστηριζόμενα αρχεία: "
                + ", ".join(path.name for path in unsupported[:10])
            )

    required = [
        ROOT / "README.md",
        ROOT / "analyses" / "README.md",
        ROOT / "evidence" / "README.md",
        ROOT / "templates" / "source-analysis.md",
        ROOT / "templates" / "source-evidence.md",
        ROOT / "catalog" / "sources.md",
        ROOT / "catalog" / "problematic-sources.md",
        ROOT / "catalog" / "next-sources.md",
        ROOT / "catalog" / "thesis-selection.csv",
        ROOT / "catalog" / "thesis-selection.md",
        ROOT / "sync" / "README.md",
        ROOT / "sync" / "main-repo-prompt.md",
        ROOT / "new-sources" / "README.md",
        ROOT / "new-originals" / "README.md",
        ROOT / "originals" / "unidentified" / "README.md",
    ]
    for path in required:
        if not path.exists():
            errors.append(f"Λείπει: {path.relative_to(ROOT)}")

    if errors:
        print("Ο έλεγχος απέτυχε:")
        for error in errors:
            print(f"- {error}")
        return 1

    original_count = len(list(ORIGINALS.rglob("*.pdf"))) if ORIGINALS.exists() else 0
    unmatched_count = len(list(UNMATCHED.rglob("*.pdf"))) if UNMATCHED.exists() else 0
    print(
        f"Ο έλεγχος ολοκληρώθηκε για {len(rows)} πηγές, {original_count} PDF "
        f"και {unmatched_count} μη ταυτοποιημένα πρωτότυπα."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
