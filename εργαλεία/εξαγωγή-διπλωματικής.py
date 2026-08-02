#!/usr/bin/env python3
"""Validate and build the controlled bibliography package for the thesis repository.

Scientific content is never translated here. Structural metadata may use the legacy
Greek labels or the newer English labels, but citation-ready evidence must preserve
the language of the checked source.
"""
from __future__ import annotations

import argparse
import csv
import re
import shutil
import subprocess
import sys
from pathlib import Path

from κατάσταση_απόφασης import analysis_original_checked, infer_decision
from language_audit import classify

ROOT = Path(__file__).resolve().parents[1]


def first_existing(*candidates: str) -> Path:
    for candidate in candidates:
        path = ROOT / candidate
        if path.exists():
            return path
    return ROOT / candidates[0]


CATALOG_DIR = first_existing("catalog", "κατάλογος")
SOURCES = first_existing("sources", "πηγές")
ANALYSES = first_existing("analyses", "αναλύσεις")
EXCERPTS = first_existing("evidence", "αποσπάσματα")
CATALOG = (
    CATALOG_DIR / "sources.csv"
    if (CATALOG_DIR / "sources.csv").exists()
    else CATALOG_DIR / "πηγές.csv"
)
SELECTION = (
    CATALOG_DIR / "thesis-selection.csv"
    if (CATALOG_DIR / "thesis-selection.csv").exists()
    else CATALOG_DIR / "επιλογή-διπλωματικής.csv"
)
DEFAULT_OUTPUT = (
    ROOT / "thesis-package"
    if (ROOT / "thesis-package").exists()
    else ROOT / "πακέτο-διπλωματικής"
)

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

# A single template is not required. Semantic sections can use legacy Greek or
# source-language-friendly English headings.
ANALYSIS_HEADING_GROUPS = {
    "bibliographic identity": (
        "Βιβλιογραφική ταυτότητα",
        "Ταυτότητα",
        "Βιβλιογραφικά στοιχεία",
        "Bibliographic identity",
        "Bibliographic details",
        "Source identity",
    ),
    "limitations": (
        "Περιορισμοί",
        "Περιορισμοί και απειλές εγκυρότητας",
        "Limitations",
        "Limitations and threats to validity",
        "Threats to validity",
    ),
    "thesis use": (
        "Χρήση στη διπλωματική",
        "Σχέση με τη διπλωματική",
        "Συνάφεια με τη διπλωματική",
        "Συνάφεια",
        "Εφαρμογή στη διπλωματική",
        "Εφαρμογή στη διπλωματική εργασία",
        "Thesis use",
        "Use in thesis",
        "Relevance to thesis",
        "Thesis relevance",
    ),
}
POSITION_PLACEHOLDERS = {
    "σελίδα, ενότητα, πίνακας, σχήμα ή χρονική σήμανση",
    "page, section, table, figure, or timestamp",
}
CLAIM_PLACEHOLDERS = {
    "ποια ακριβώς πρόταση της διπλωματικής υποστηρίζει",
    "the exact thesis claim supported by this evidence",
}


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


def markdown_label_values(text: str, *labels: str) -> list[str]:
    values: list[str] = []
    for label in labels:
        pattern = re.compile(
            rf"^\s*-\s*\*\*{re.escape(label)}:\*\*\s*(.*?)\s*$",
            re.IGNORECASE | re.MULTILINE,
        )
        values.extend(match.group(1).strip() for match in pattern.finditer(text))
    return values


def has_heading(text: str, aliases: tuple[str, ...]) -> bool:
    headings = [normalize(match.group(1)) for match in re.finditer(r"(?m)^##\s+(.+?)\s*$", text)]
    for heading in headings:
        for alias in aliases:
            target = normalize(alias)
            if heading == target or heading.startswith(target + " ") or target in heading:
                return True
    return False


def has_evidence_block(text: str) -> bool:
    return bool(
        re.search(
            r"(?im)^##\s+(?:Τεκμήριο(?:\s+E?\d+)?\b|Evidence(?:\s+E?\d+)?\b|E\d+\b)",
            text,
        )
    )


def evidence_verified(text: str) -> bool:
    normalized = normalize(text)
    return (
        "κατάσταση: επαληθευμένο" in normalized
        or "status: verified" in normalized
    )


def evidence_original_checked(text: str) -> bool:
    normalized = normalize(text)
    return (
        "ελεγχθέν-πρωτότυπο: ναι" in normalized
        or "original-checked: yes" in normalized
    )


def source_language_error(source_text: str, evidence_text: str) -> str | None:
    source_lang, _, _ = classify(source_text)
    evidence_lang, _, _ = classify(evidence_text)

    if source_lang in {"unknown", "mixed"}:
        return f"η γλώσσα της πηγής απαιτεί manual provenance review ({source_lang})"
    if evidence_lang in {"unknown", "mixed"}:
        return f"η γλώσσα του citation-ready evidence απαιτεί manual review ({evidence_lang})"
    if source_lang != evidence_lang:
        return (
            "το citation-ready evidence δεν διατηρεί τη γλώσσα της πηγής "
            f"(source={source_lang}, evidence={evidence_lang})"
        )
    return None


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
        return "unknown"


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

        source_path = SOURCES / f"{source_id}.md"
        analysis_path = ANALYSES / f"{source_id}.md"
        excerpt_path = EXCERPTS / f"{source_id}.md"
        source_text = ""
        analysis_text = ""
        excerpt_text = ""

        if not source_path.exists():
            errors.append(f"{source_id}: λείπει το canonical source Markdown για language verification")
        else:
            source_text = source_path.read_text(encoding="utf-8", errors="replace")

        if not analysis_path.exists():
            errors.append(f"{source_id}: λείπει η δομημένη ανάλυση")
        else:
            analysis_text = analysis_path.read_text(encoding="utf-8", errors="replace")
            decision = infer_decision(analysis_text)
            if decision == "rejected":
                errors.append(f"{source_id}: η canonical ανάλυση δηλώνει απόρριψη αλλά το registry ζητά εξαγωγή")
            for group, aliases in ANALYSIS_HEADING_GROUPS.items():
                if not has_heading(analysis_text, aliases):
                    errors.append(f"{source_id}: λείπει σημασιολογική ενότητα ανάλυσης για «{group}»")
            analysis_words = meaningful_word_count(analysis_text)
            if analysis_words < MIN_ANALYSIS_WORDS:
                errors.append(
                    f"{source_id}: η ανάλυση δεν έχει αρκετό ουσιαστικό περιεχόμενο "
                    f"({analysis_words}/{MIN_ANALYSIS_WORDS} λέξεις)"
                )

        if not excerpt_path.exists():
            errors.append(f"{source_id}: λείπει το αρχείο επαληθευμένων evidence")
        else:
            excerpt_text = excerpt_path.read_text(encoding="utf-8", errors="replace")
            positions = markdown_label_values(excerpt_text, "Θέση", "Location")
            claims = markdown_label_values(excerpt_text, "Ισχυρισμός", "Claim")
            if not evidence_verified(excerpt_text):
                errors.append(f"{source_id}: το evidence δεν δηλώνει verified status")
            if not evidence_original_checked(excerpt_text):
                errors.append(f"{source_id}: το evidence δεν δηλώνει ότι ελέγχθηκε το πρωτότυπο")
            if not has_evidence_block(excerpt_text):
                errors.append(f"{source_id}: λείπει δομημένη ενότητα evidence (Τεκμήριο/Evidence/E#)")
            if not positions or any(
                not value or normalize(value) in POSITION_PLACEHOLDERS for value in positions
            ):
                errors.append(f"{source_id}: λείπει πραγματική ακριβής θέση στο evidence")
            if not claims or any(
                not value or normalize(value) in CLAIM_PLACEHOLDERS for value in claims
            ):
                errors.append(f"{source_id}: λείπει πραγματικός ισχυρισμός που υποστηρίζεται")
            excerpt_words = meaningful_word_count(excerpt_text)
            if excerpt_words < MIN_EXCERPT_WORDS:
                errors.append(
                    f"{source_id}: το evidence δεν έχει αρκετό ουσιαστικό περιεχόμενο "
                    f"({excerpt_words}/{MIN_EXCERPT_WORDS} λέξεις)"
                )

        if source_text and excerpt_text:
            language_error = source_language_error(source_text, excerpt_text)
            if language_error:
                errors.append(f"{source_id}: {language_error}")

        # Primary-source verification may be declared in either the analysis or the
        # citation-ready evidence. A duplicate marker is not required.
        if analysis_text and excerpt_text:
            if not analysis_original_checked(analysis_text) and not evidence_original_checked(excerpt_text):
                errors.append(f"{source_id}: δεν δηλώνεται έλεγχος πρωτοτύπου σε analysis ή evidence")

    return errors, exported, catalog, catalog_fields


def write_package(
    output: Path,
    exported: list[dict[str, str]],
    catalog: dict[str, dict[str, str]],
    catalog_fields: list[str],
) -> None:
    if output.exists():
        shutil.rmtree(output)
    (output / "analyses").mkdir(parents=True)
    (output / "evidence").mkdir(parents=True)
    (output / "catalog").mkdir(parents=True)

    commit = repository_commit()
    manifest_fields = SELECTION_FIELDS + ["Τίτλος", "Σύνδεσμος", "Commit βιβλιογραφίας"]
    manifest_rows: list[dict[str, str]] = []
    selected_catalog_rows: list[dict[str, str]] = []

    for row in sorted(exported, key=lambda item: item["Κωδικός"]):
        source_id = row["Κωδικός"].strip()
        source = catalog[source_id]
        shutil.copy2(ANALYSES / f"{source_id}.md", output / "analyses" / f"{source_id}.md")
        shutil.copy2(EXCERPTS / f"{source_id}.md", output / "evidence" / f"{source_id}.md")
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

    with (output / "catalog" / "sources.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=catalog_fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(selected_catalog_rows)

    (output / "SOURCE_COMMIT").write_text(commit + "\n", encoding="utf-8")
    (output / "README.md").write_text(
        "# Επαληθευμένο πακέτο διπλωματικής\n\n"
        f"- Επιλεγμένες πηγές: **{len(exported)}**\n"
        f"- Commit `ThesisBibliography`: `{commit}`\n\n"
        "Το πακέτο δημιουργείται αποκλειστικά από το canonical thesis-selection registry. "
        "Περιλαμβάνει μόνο επαληθευμένες αναλύσεις και citation-ready evidence στη γλώσσα "
        "της αντίστοιχης πηγής. Δεν περιλαμβάνει PDF, ακατέργαστες μεταγραφές, αυτόματες "
        "μεταφράσεις ή μη ελεγμένες σημειώσεις.\n",
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
