#!/usr/bin/env python3
"""Ελέγχει και δημιουργεί το ελεγχόμενο πακέτο προς το κύριο repository."""
from __future__ import annotations

import argparse
import csv
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "κατάλογος" / "πηγές.csv"
SELECTION = ROOT / "κατάλογος" / "επιλογή-διπλωματικής.csv"
ANALYSES = ROOT / "αναλύσεις"
EXCERPTS = ROOT / "αποσπάσματα"
DEFAULT_OUTPUT = ROOT / "πακέτο-διπλωματικής"

SELECTION_FIELDS = [
    "Κωδικός",
    "Ρόλος",
    "Κατάσταση",
    "Κεφάλαια",
    "Θέματα",
    "Εξαγωγή",
    "Σημείωση",
]
ALLOWED_ROLES = {"κύρια", "υποστηρικτική", "υπόβαθρο", "απόρριψη"}
ALLOWED_STATUSES = {"προς ανάλυση", "πρόχειρη", "επαληθευμένη", "απορρίφθηκε"}
YES_VALUES = {"ναι", "yes", "true", "1"}
MIN_ANALYSIS_WORDS = 150
MIN_EXCERPT_WORDS = 120
REQUIRED_ANALYSIS_HEADINGS = (
    "## Βιβλιογραφική ταυτότητα",
    "## Σύνοψη",
    "## Μεθοδολογία",
    "## Κύρια ευρήματα",
    "## Περιορισμοί και απειλές εγκυρότητας",
    "## Χρήση στη διπλωματική",
    "## Κατάσταση επαλήθευσης",
)


def normalize(value: str | None) -> str:
    return (value or "").strip().casefold()


def meaningful_word_count(text: str) -> int:
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"[`#>*_\-|:\[\]()]+", " ", text)
    words = re.findall(r"[A-Za-zΑ-Ωα-ωΆ-ώ0-9]{2,}", text)
    boilerplate = {
        "source", "πηγή", "τίτλος", "συγγραφείς", "έτος", "σύνδεσμος",
        "πρωτότυπο", "χρειάζεται", "έλεγχο", "μεταδεδομένα",
    }
    return sum(word.casefold() not in boilerplate for word in words)


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), [dict(row) for row in reader]


def repository_commit() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True, stderr=subprocess.DEVNULL
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "άγνωστο"


def is_exported(row: dict[str, str]) -> bool:
    return normalize(row.get("Εξαγωγή")) in YES_VALUES


def validate() -> tuple[list[str], list[dict[str, str]], dict[str, dict[str, str]], list[str]]:
    errors: list[str] = []
    if not CATALOG.exists():
        return [f"Λείπει ο κατάλογος: {CATALOG.relative_to(ROOT)}"], [], {}, []
    if not SELECTION.exists():
        return [f"Λείπει το μητρώο επιλογής: {SELECTION.relative_to(ROOT)}"], [], {}, []

    catalog_fields, catalog_rows = read_csv(CATALOG)
    selection_fields, selection_rows = read_csv(SELECTION)
    missing_fields = [field for field in SELECTION_FIELDS if field not in selection_fields]
    if missing_fields:
        errors.append("Λείπουν πεδία από το μητρώο επιλογής: " + ", ".join(missing_fields))

    catalog = {row.get("Κωδικός", "").strip(): row for row in catalog_rows if row.get("Κωδικός")}
    seen: set[str] = set()
    exported: list[dict[str, str]] = []

    for line_number, row in enumerate(selection_rows, start=2):
        source_id = row.get("Κωδικός", "").strip()
        role = normalize(row.get("Ρόλος"))
        status = normalize(row.get("Κατάσταση"))

        if not source_id:
            errors.append(f"Γραμμή {line_number}: λείπει κωδικός πηγής")
            continue
        if source_id in seen:
            errors.append(f"Διπλή εγγραφή στο μητρώο επιλογής: {source_id}")
        seen.add(source_id)
        if source_id not in catalog:
            errors.append(f"Άγνωστος κωδικός στο μητρώο επιλογής: {source_id}")
        if role and role not in ALLOWED_ROLES:
            errors.append(f"{source_id}: μη αποδεκτός ρόλος «{row.get('Ρόλος', '')}»")
        if status and status not in ALLOWED_STATUSES:
            errors.append(f"{source_id}: μη αποδεκτή κατάσταση «{row.get('Κατάσταση', '')}»")

        if not is_exported(row):
            continue
        exported.append(row)
        if role not in ALLOWED_ROLES:
            errors.append(f"{source_id}: απαιτείται έγκυρος ρόλος πριν από την εξαγωγή")
        elif role == "απόρριψη":
            errors.append(f"{source_id}: πηγή με ρόλο απόρριψης δεν μπορεί να εξαχθεί")
        if status != "επαληθευμένη":
            errors.append(f"{source_id}: εξαγωγή επιτρέπεται μόνο με κατάσταση «επαληθευμένη»")

        analysis_path = ANALYSES / f"{source_id}.md"
        excerpt_path = EXCERPTS / f"{source_id}.md"
        if not analysis_path.exists():
            errors.append(f"{source_id}: λείπει η δομημένη ανάλυση")
        else:
            analysis_text = analysis_path.read_text(encoding="utf-8", errors="replace")
            for heading in REQUIRED_ANALYSIS_HEADINGS:
                if heading not in analysis_text:
                    errors.append(f"{source_id}: λείπει από την ανάλυση η ενότητα «{heading}»")
            if "κατάσταση: επαληθευμένη" not in normalize(analysis_text):
                errors.append(f"{source_id}: η ανάλυση δεν δηλώνει επαληθευμένη κατάσταση")
            if meaningful_word_count(analysis_text) < MIN_ANALYSIS_WORDS:
                errors.append(
                    f"{source_id}: η ανάλυση δεν έχει αρκετό ουσιαστικό περιεχόμενο "
                    f"({meaningful_word_count(analysis_text)}/{MIN_ANALYSIS_WORDS} λέξεις)"
                )

        if not excerpt_path.exists():
            errors.append(f"{source_id}: λείπει το αρχείο επαληθευμένων αποσπασμάτων")
        else:
            excerpt_text = excerpt_path.read_text(encoding="utf-8", errors="replace")
            excerpt_lower = excerpt_text.lower()
            if "κατάσταση: επαληθευμένο" not in normalize(excerpt_text):
                errors.append(f"{source_id}: τα αποσπάσματα δεν δηλώνουν επαληθευμένη κατάσταση")
            if "**θέση:**" not in excerpt_lower:
                errors.append(f"{source_id}: λείπει ακριβής θέση στα αποσπάσματα")
            if "**ισχυρισμός:**" not in excerpt_lower:
                errors.append(f"{source_id}: λείπει ο ισχυρισμός που υποστηρίζεται")
            if meaningful_word_count(excerpt_text) < MIN_EXCERPT_WORDS:
                errors.append(
                    f"{source_id}: τα αποσπάσματα δεν έχουν αρκετό ουσιαστικό περιεχόμενο "
                    f"({meaningful_word_count(excerpt_text)}/{MIN_EXCERPT_WORDS} λέξεις)"
                )

    return errors, exported, catalog, catalog_fields


def write_package(
    output: Path,
    exported: list[dict[str, str]],
    catalog: dict[str, dict[str, str]],
    catalog_fields: list[str],
) -> None:
    if output.exists():
        shutil.rmtree(output)
    (output / "αναλύσεις").mkdir(parents=True)
    (output / "αποσπάσματα").mkdir(parents=True)
    (output / "κατάλογος").mkdir(parents=True)

    commit = repository_commit()
    manifest_fields = SELECTION_FIELDS + ["Τίτλος", "Σύνδεσμος", "Commit βιβλιογραφίας"]
    manifest_rows: list[dict[str, str]] = []
    selected_catalog_rows: list[dict[str, str]] = []

    for row in sorted(exported, key=lambda item: item["Κωδικός"]):
        source_id = row["Κωδικός"].strip()
        source = catalog[source_id]
        shutil.copy2(ANALYSES / f"{source_id}.md", output / "αναλύσεις" / f"{source_id}.md")
        shutil.copy2(EXCERPTS / f"{source_id}.md", output / "αποσπάσματα" / f"{source_id}.md")
        selected_catalog_rows.append(source)
        manifest_rows.append(
            {
                **{field: row.get(field, "") for field in SELECTION_FIELDS},
                "Τίτλος": source.get("Τίτλος", ""),
                "Σύνδεσμος": source.get("Σύνδεσμος", ""),
                "Commit βιβλιογραφίας": commit,
            }
        )

    with (output / "manifest.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=manifest_fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(manifest_rows)

    with (output / "κατάλογος" / "πηγές.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=catalog_fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(selected_catalog_rows)

    (output / "SOURCE_COMMIT").write_text(commit + "\n", encoding="utf-8")
    (output / "README.md").write_text(
        "# Επαληθευμένο πακέτο διπλωματικής\n\n"
        f"- Επιλεγμένες πηγές: **{len(exported)}**\n"
        f"- Commit `ThesisBibliography`: `{commit}`\n\n"
        "Το πακέτο δημιουργείται αποκλειστικά από το μητρώο "
        "`κατάλογος/επιλογή-διπλωματικής.csv`. Περιλαμβάνει μόνο επαληθευμένες "
        "αναλύσεις και αποσπάσματα. Δεν περιλαμβάνει PDF, ακατέργαστες μεταγραφές "
        "ή μη ελεγμένες σημειώσεις.\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--validate-only", action="store_true")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    errors, exported, catalog, catalog_fields = validate()
    if errors:
        print("Η εξαγωγή απέτυχε:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    if not args.validate_only:
        output = args.output if args.output.is_absolute() else ROOT / args.output
        write_package(output, exported, catalog, catalog_fields)
        print(f"Δημιουργήθηκε πακέτο με {len(exported)} επαληθευμένες πηγές στο {output}.")
    else:
        print(f"Το μητρώο εξαγωγής είναι έγκυρο: {len(exported)} επαληθευμένες πηγές.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
