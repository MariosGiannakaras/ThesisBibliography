#!/usr/bin/env python3
"""Apply exact, primary-source metadata corrections after automated enrichment.

These corrections are intentionally narrow and fail closed. They exist for
sources whose authoritative local original and official publisher page disagree
with unreliable embedded or DOI-only metadata. They never perform fuzzy source
matching.
"""
from __future__ import annotations

import csv
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog" / "sources.csv"
SOURCES = ROOT / "sources"
FIELDS = [
    "Κωδικός", "Τίτλος", "Συγγραφείς", "Έτος", "Σύνδεσμος",
    "Τύπος", "Θέματα", "Κατάσταση", "Επιβεβαίωση", "Προτεραιότητα", "Σημειώσεις",
]

RANE_SOURCE_ID = "SRC-81C66C1798"
RANE_ORIGINAL_SHA256 = "81c66c179873e77291d54b99e8456a68a2fa86196fd6508221b43ead8900f512"
RANE_TITLE = "Artificial intelligence for enhancing resilience"
RANE_AUTHORS = "Nitin Liladhar Rane; Saurabh P. Choudhary; Jayesh Rane"
RANE_YEAR = "2024"
RANE_PRIMARY_URL = "https://sabapub.com/index.php/jaai/article/view/1053"
RANE_DOI = "10.48185/jaai.v5i2.1053"
RANE_NOTE = (
    "Η βιβλιογραφική ταυτότητα επιβεβαιώθηκε από την πρώτη σελίδα του πρωτότυπου PDF "
    "και την επίσημη article page του publisher. Ο DOI 10.48185/jaai.v5i2.1053 "
    "εμφανίζεται επαναχρησιμοποιημένος σε περισσότερα από ένα αρχεία του ίδιου issue, "
    "οπότε DOI-only ή embedded metadata δεν επιτρέπεται να υπερισχύσει της primary-source ταυτότητας."
)


def combine_topics(*values: str) -> str:
    result: list[str] = []
    for raw in values:
        for value in (raw or "").split("; "):
            value = value.strip()
            if value and value != "χωρίς κατηγορία" and value not in result:
                result.append(value)
    return "; ".join(result or ["χωρίς κατηγορία"])


def combine_notes(*values: str) -> str:
    result: list[str] = []
    for raw in values:
        for value in (raw or "").split(" | "):
            value = value.strip()
            if value and value not in result:
                result.append(value)
    return " | ".join(result)


def load_rows(catalog: Path = CATALOG) -> list[dict[str, str]]:
    if not catalog.exists():
        return []
    with catalog.open(encoding="utf-8", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def save_rows(rows: list[dict[str, str]], catalog: Path = CATALOG) -> None:
    with catalog.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda row: row.get("Τίτλος", "").casefold()))


def source_has_expected_original(path: Path) -> bool:
    if not path.exists():
        return False
    head = "\n".join(path.read_text(encoding="utf-8", errors="replace").splitlines()[:30])
    return f"original_sha256: {RANE_ORIGINAL_SHA256}" in head


def correct_source_document(path: Path) -> bool:
    """Correct only the bibliographic heading/header; preserve extracted body verbatim."""
    if not source_has_expected_original(path):
        return False
    text = path.read_text(encoding="utf-8", errors="strict")
    lines = text.splitlines()
    heading_index = next((index for index, line in enumerate(lines) if line.startswith("# ")), None)
    if heading_index is None:
        raise RuntimeError(f"{RANE_SOURCE_ID}: converted source has no Markdown H1")

    changed = lines[heading_index] != f"# {RANE_TITLE}"
    lines[heading_index] = f"# {RANE_TITLE}"

    source_line = f"> Source: {RANE_PRIMARY_URL}"
    doi_line = f"> DOI as printed by publisher: https://doi.org/{RANE_DOI}"
    header_window = lines[heading_index:heading_index + 12]
    insert_at = heading_index + 1
    if source_line not in header_window:
        lines[insert_at:insert_at] = ["", source_line]
        insert_at += 2
        changed = True
    if doi_line not in lines[heading_index:heading_index + 14]:
        lines[insert_at:insert_at] = [doi_line]
        changed = True

    if changed:
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return changed


def apply(
    rows: list[dict[str, str]],
    sources: Path = SOURCES,
) -> tuple[list[dict[str, str]], list[str]]:
    by_id = {row.get("Κωδικός", ""): row for row in rows}
    row = by_id.get(RANE_SOURCE_ID)
    if row is None:
        return rows, []

    source = sources / f"{RANE_SOURCE_ID}.md"
    if not source_has_expected_original(source):
        raise RuntimeError(
            f"{RANE_SOURCE_ID}: refusing primary metadata override because expected original SHA-256 is absent"
        )

    row.update({
        "Τίτλος": RANE_TITLE,
        "Συγγραφείς": RANE_AUTHORS,
        "Έτος": RANE_YEAR,
        "Σύνδεσμος": RANE_PRIMARY_URL,
        "Τύπος": "ακαδημαϊκή εργασία",
        "Θέματα": combine_topics(row.get("Θέματα", ""), "ανθεκτικότητα και ανάκαμψη"),
        "Κατάσταση": "διαθέσιμο πλήρες κείμενο",
        # The publisher page and primary PDF are authoritative here; the DOI is
        # retained in the source document but is known not to be unique in this issue.
        "Επιβεβαίωση": "μόνο καταγεγραμμένος σύνδεσμος",
        "Προτεραιότητα": "υψηλή",
        "Σημειώσεις": combine_notes(row.get("Σημειώσεις", ""), RANE_NOTE),
    })
    correct_source_document(source)
    return rows, [f"Διορθώθηκε η primary-source βιβλιογραφική ταυτότητα του {RANE_SOURCE_ID}."]


def main() -> int:
    rows, changes = apply(load_rows())
    if not changes:
        print("Δεν απαιτούνται primary-source metadata corrections.")
        return 0
    save_rows(rows)
    subprocess.run(
        [sys.executable, str(ROOT / "tools" / "import_sources.py"), "--catalog-only"],
        cwd=ROOT,
        check=True,
    )
    for change in changes:
        print(change)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
