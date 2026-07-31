#!/usr/bin/env python3
"""Εφαρμόζει λίγες τεκμηριωμένες, επαναλήψιμες διορθώσεις πηγών.

Το εργαλείο δεν κάνει ασαφή αντιστοίχιση. Περιέχει μόνο περιπτώσεις που
επιβεβαιώθηκαν από το ίδιο το PDF, επίσημη σελίδα ή ακριβές αρχείο.
"""
from __future__ import annotations

import csv
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "κατάλογος" / "πηγές.csv"
SOURCES = ROOT / "πηγές"
ORIGINALS = ROOT / "πρωτότυπα"
PENDING = ROOT / "νέα-πρωτότυπα" / "εκκρεμή"
FIELDS = [
    "Κωδικός", "Τίτλος", "Συγγραφείς", "Έτος", "Σύνδεσμος",
    "Τύπος", "Θέματα", "Κατάσταση", "Επιβεβαίωση", "Προτεραιότητα", "Σημειώσεις",
]


def combine_topics(*values: str) -> str:
    topics: list[str] = []
    for raw in values:
        for topic in (raw or "").split("; "):
            topic = topic.strip()
            if topic and topic != "χωρίς κατηγορία" and topic not in topics:
                topics.append(topic)
    return "; ".join(topics or ["χωρίς κατηγορία"])


def combine_notes(*values: str) -> str:
    notes: list[str] = []
    for raw in values:
        for value in (raw or "").split(" | "):
            value = value.strip()
            if value and value not in notes:
                notes.append(value)
    return " | ".join(notes)


def load_rows() -> list[dict[str, str]]:
    with CATALOG.open(encoding="utf-8", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def save_rows(rows: list[dict[str, str]]) -> None:
    with CATALOG.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda row: row.get("Τίτλος", "").casefold()))


def write_cisco_source() -> None:
    source_id = "SRC-C7E22C59DE"
    content = """# AI Agents 101: An Introduction to Agents and Examples of How to Build Them

> Source: https://www.ciscolive.com/c/dam/r/ciscolive/global-event/docs/2025/pdf/BRKETI-1008.pdf

- **Παρουσιαστής:** Timothy Miller
- **Διοργάνωση:** Cisco Live 2025
- **Κωδικός συνεδρίας:** BRKETI-1008
- **Τύπος:** διαφάνειες τεχνικής παρουσίασης
- **Πρωτότυπο:** `πρωτότυπα/SRC-C7E22C59DE.pdf`

Η παλαιότερη αυτόματη ονομασία προερχόταν από εσωτερική διαφάνεια άλλης συνεδρίας και διορθώθηκε από το επίσημο όνομα του αρχείου και την επίσημη σελίδα του Cisco Live.
"""
    (SOURCES / f"{source_id}.md").write_text(content, encoding="utf-8")


def write_manning_source() -> None:
    source_id = "SRC-13CFB90F59"
    content = """# AI Agents in Action

> Source: https://www.manning.com/books/ai-agents-in-action

- **Συγγραφέας:** Micheal Lanham
- **Εκδότης:** Manning
- **ISBN αγγλικής έκδοσης:** 9781633436343
- **Ιταλική έκδοση:** *AI Agent in pratica*, ISBN 9788850337767
- **Πρωτότυπο αγγλικής έκδοσης:** `πρωτότυπα/SRC-13CFB90F59.pdf`
- **Εναλλακτική ιταλική έκδοση:** `πρωτότυπα/SRC-13CFB90F59__εναλλακτικό-6799C781D0.pdf`

Τα δύο PDF διατηρούνται ως διαφορετικές γλωσσικές εκδόσεις της ίδιας βιβλιογραφικής πηγής. Η προέλευση και τα δικαιώματα των τοπικών αντιγράφων πρέπει να ελεγχθούν πριν από οποιαδήποτε διανομή.
"""
    (SOURCES / f"{source_id}.md").write_text(content, encoding="utf-8")


def move_bad_fulltext_to_pending() -> bool:
    source = ORIGINALS / "SRC-9D8496BE2C.pdf"
    if not source.exists():
        return False
    PENDING.mkdir(parents=True, exist_ok=True)
    target = PENDING / "FULLTEXT02.pdf"
    if target.exists():
        target = PENDING / "FULLTEXT02__9D8496BE2C.pdf"
    shutil.move(str(source), target)
    return True


def remove_related(source_id: str, *, keep_pdf: bool = False) -> None:
    source = SOURCES / f"{source_id}.md"
    if source.exists():
        source.unlink()
    for suffix in (".url",):
        related = ORIGINALS / f"{source_id}{suffix}"
        if related.exists():
            related.unlink()
    if not keep_pdf:
        pdf = ORIGINALS / f"{source_id}.pdf"
        if pdf.exists():
            pdf.unlink()


def apply(rows: list[dict[str, str]]) -> tuple[list[dict[str, str]], list[str]]:
    by_id = {row["Κωδικός"]: row for row in rows}
    changes: list[str] = []

    cisco = by_id.get("SRC-C7E22C59DE")
    if cisco:
        cisco.update({
            "Τίτλος": "AI Agents 101: An Introduction to Agents and Examples of How to Build Them",
            "Συγγραφείς": "Timothy Miller",
            "Έτος": "2025",
            "Σύνδεσμος": "https://www.ciscolive.com/c/dam/r/ciscolive/global-event/docs/2025/pdf/BRKETI-1008.pdf",
            "Τύπος": "θεσμική ή τεχνική αναφορά",
            "Θέματα": combine_topics(cisco.get("Θέματα", ""), "πράκτορες τεχνητής νοημοσύνης"),
            "Κατάσταση": "διαθέσιμο πλήρες κείμενο",
            "Επιβεβαίωση": "μόνο καταγεγραμμένος σύνδεσμος",
            "Προτεραιότητα": "μεσαία",
            "Σημειώσεις": combine_notes(
                cisco.get("Σημειώσεις", ""),
                "Διορθώθηκε από το επίσημο Cisco Live PDF BRKETI-1008· η προηγούμενη ονομασία ήταν εσωτερική διαφάνεια.",
            ),
        })
        write_cisco_source()
        changes.append("Διορθώθηκε η πηγή SRC-C7E22C59DE από την επίσημη συνεδρία Cisco Live.")

    manning = by_id.get("SRC-13CFB90F59")
    if manning:
        manning.update({
            "Τίτλος": "AI Agents in Action",
            "Συγγραφείς": "Micheal Lanham",
            "Έτος": "2025",
            "Σύνδεσμος": "https://www.manning.com/books/ai-agents-in-action",
            "Τύπος": "βιβλίο ή κεφάλαιο",
            "Θέματα": combine_topics(manning.get("Θέματα", ""), "πράκτορες τεχνητής νοημοσύνης"),
            "Κατάσταση": "διαθέσιμο πλήρες κείμενο",
            "Επιβεβαίωση": "μόνο καταγεγραμμένος σύνδεσμος",
            "Προτεραιότητα": "χαμηλή",
            "Σημειώσεις": combine_notes(
                manning.get("Σημειώσεις", ""),
                "Η ιταλική έκδοση AI Agent in pratica διατηρείται ως εναλλακτικό PDF της ίδιας πηγής· απαιτείται έλεγχος δικαιωμάτων τοπικών αντιγράφων.",
            ),
        })
        write_manning_source()
        changes.append("Συνδέθηκαν οι αγγλική και ιταλική εκδόσεις του AI Agents in Action.")

    canonical = by_id.get("SRC-95C9DAEE68")
    aliases = [
        row for source_id in ("SRC-698EC08DEE", "SRC-B2713DB7BE")
        if (row := by_id.get(source_id)) is not None
    ]
    if canonical:
        canonical.update({
            "Τίτλος": "Deep reinforcement learning in non-stationary environments",
            "Συγγραφείς": "Zihe Liu",
            "Έτος": "2024",
            "Σύνδεσμος": "https://opus.lib.uts.edu.au/handle/10453/186408",
            "Τύπος": "διπλωματική ή διατριβή",
            "Θέματα": combine_topics(
                canonical.get("Θέματα", ""),
                *(row.get("Θέματα", "") for row in aliases),
                "μη στασιμότητα; βαθιά ενισχυτική μάθηση; συνεχής προσαρμογή",
            ),
            "Κατάσταση": "διαθέσιμο πλήρες κείμενο",
            "Επιβεβαίωση": "μόνο καταγεγραμμένος σύνδεσμος",
            "Προτεραιότητα": "υψηλή",
            "Σημειώσεις": combine_notes(
                canonical.get("Σημειώσεις", ""),
                *(row.get("Σημειώσεις", "") for row in aliases),
                "Κύρια εγγραφή για τη διατριβή Zihe Liu· αφαιρέθηκαν ορφανή landing-page εγγραφή και ακριβές διπλότυπο PDF.",
            ),
        })
        if aliases:
            changes.append("Ενοποιήθηκαν οι εγγραφές της διατριβής Zihe Liu στο SRC-95C9DAEE68.")

    remove_ids = {"SRC-9D8496BE2C", "SRC-B2713DB7BE"}
    rows = [row for row in rows if row["Κωδικός"] not in remove_ids]
    if "SRC-9D8496BE2C" in by_id:
        moved = move_bad_fulltext_to_pending()
        remove_related("SRC-9D8496BE2C", keep_pdf=True)
        changes.append(
            "Η λανθασμένη εγγραφή SRC-9D8496BE2C αφαιρέθηκε και το FULLTEXT02 επέστρεψε στα εκκρεμή."
            if moved else
            "Η λανθασμένη εγγραφή SRC-9D8496BE2C αφαιρέθηκε."
        )
    if "SRC-B2713DB7BE" in by_id:
        remove_related("SRC-B2713DB7BE")

    return rows, changes


def main() -> int:
    rows, changes = apply(load_rows())
    save_rows(rows)
    subprocess.run(
        [sys.executable, str(ROOT / "εργαλεία" / "εισαγωγή.py"), "--catalog-only"],
        cwd=ROOT,
        check=True,
    )
    for change in changes:
        print(change)
    print(f"Εφαρμόστηκαν {len(changes)} γνωστές διορθώσεις.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())