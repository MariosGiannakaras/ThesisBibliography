#!/usr/bin/env python3
"""Εκτυπώνει τα linked PDF που χρειάζονται τεχνική μετατροπή σε Markdown.

Χρησιμοποιείται πριν από `git lfs pull`, ώστε το workflow να κατεβάζει μόνο
τα LFS αντικείμενα των πηγών που λείπουν ή έχουν placeholder/ελάχιστο Markdown.
Δεν τροποποιεί αρχεία.
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "κατάλογος" / "πηγές.csv"
SOURCES = ROOT / "πηγές"
ORIGINALS = ROOT / "πρωτότυπα"
AUTO_MARKER = "<!-- AUTO_PDF_CONVERSION: v1 -->"
PLACEHOLDER_MARKERS = (
    "Η εγγραφή δημιουργήθηκε από πρωτότυπο PDF που δεν υπήρχε ακόμη στον κατάλογο.",
    "Χρειάζεται πλήρης μετατροπή σε Markdown",
)
REPLACEABLE_STATUSES = {"μόνο μεταδεδομένα", "αποτυχημένη εισαγωγή", "ελλιπές κείμενο"}


def useful_word_count(text: str) -> int:
    text = re.sub(r"https?://\S+", " ", text)
    return len(re.findall(r"[A-Za-zΑ-Ωα-ωΆ-ώ0-9]{2,}", text))


def source_is_replaceable(path: Path, row: dict[str, str]) -> bool:
    if not path.exists():
        return True
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.strip():
        return True
    if AUTO_MARKER in text or any(marker in text for marker in PLACEHOLDER_MARKERS):
        return True
    return row.get("Κατάσταση", "") in REPLACEABLE_STATUSES and useful_word_count(text) < 120


def main() -> int:
    with CATALOG.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    needed: list[str] = []
    for row in rows:
        source_id = (row.get("Κωδικός", "") or "").strip()
        if not source_id:
            continue
        pdf = ORIGINALS / f"{source_id}.pdf"
        source = SOURCES / f"{source_id}.md"
        if pdf.exists() and source_is_replaceable(source, row):
            needed.append(pdf.relative_to(ROOT).as_posix())

    for path in sorted(needed):
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
