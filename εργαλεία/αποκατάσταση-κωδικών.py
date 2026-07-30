#!/usr/bin/env python3
"""Επαναφέρει τους μόνιμους κωδικούς SRC της αρχικής καταχώρισης."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "πηγές"
EXCERPTS = ROOT / "αποσπάσματα"
ORIGINALS = ROOT / "πρωτότυπα"
CATALOG = ROOT / "κατάλογος" / "πηγές.csv"

FIELDS = [
    "Κωδικός", "Τίτλος", "Συγγραφείς", "Έτος", "Σύνδεσμος",
    "Τύπος", "Θέματα", "Κατάσταση", "Επιβεβαίωση", "Προτεραιότητα", "Σημειώσεις",
]


def git_text(path: str) -> str:
    result = subprocess.run(
        ["git", "show", f"origin/main:{path}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return result.stdout.decode("utf-8", errors="replace")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def record_score(record: dict[str, Any]) -> tuple[int, int, int, int, str]:
    canonical = 1 if not record.get("duplicate_of") else 0
    priority = {
        "P1-core": 5, "P2-supporting": 4, "P3-review": 3,
        "P4-recover-or-replace": 2, "P5-archive-only": 1,
    }.get(str(record.get("priority") or ""), 0)
    status = {
        "full-text": 4, "partial": 3, "metadata-only": 2, "failed-load": 1,
    }.get(str(record.get("content_status") or ""), 0)
    confidence = {"high": 3, "medium": 2, "low": 1}.get(
        str(record.get("metadata_confidence") or ""), 0
    )
    return canonical, priority, status, confidence, str(record.get("source_id") or "")


def translate_excerpt(text: str, source_id: str) -> str:
    replacements = {
        "# Candidate excerpt": "# Υποψήφιο απόσπασμα",
        "# Candidate Excerpt": "# Υποψήφιο απόσπασμα",
        "- **Source:**": "- **Πηγή:**",
        "- **Priority:**": "- **Προτεραιότητα:**",
        "- **Topics:**": "- **Θέματα:**",
        "- **Markdown:**": "- **Αρχείο:**",
        "- **Review status:**": "- **Κατάσταση ελέγχου:**",
        "Machine-selected review candidate; verify against the original source before citation.":
            "Αυτόματα επιλεγμένο απόσπασμα. Χρειάζεται έλεγχος στην πραγματική πηγή πριν χρησιμοποιηθεί ως παραπομπή.",
        "machine-selected; full-text verification pending":
            "αυτόματη επιλογή· εκκρεμεί έλεγχος του πλήρους κειμένου",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"`sources/markdown/[^`]+`", f"`πηγές/{source_id}.md`", text)
    return text


def main() -> int:
    old_records = json.loads(git_text("catalog/source_catalog.json"))
    eligible = [
        record for record in old_records
        if record.get("source_type") != "notebooklm-synthesis"
        and record.get("relevance") != "out-of-scope"
        and record.get("content_sha256")
        and record.get("source_id")
    ]

    by_hash: dict[str, list[dict[str, Any]]] = defaultdict(list)
    old_by_id: dict[str, dict[str, Any]] = {}
    for record in eligible:
        by_hash[str(record["content_sha256"])].append(record)
        old_by_id[str(record["source_id"])] = record
    canonical_by_hash = {
        content_hash: max(records, key=record_score)
        for content_hash, records in by_hash.items()
    }

    with CATALOG.open(encoding="utf-8", newline="") as handle:
        rows = [dict(row) for row in csv.DictReader(handle)]

    current_to_stable: dict[str, str] = {}
    retained_hashes: set[str] = set()
    for row in rows:
        current_id = row["Κωδικός"]
        path = SOURCES / f"{current_id}.md"
        if not path.exists():
            raise RuntimeError(f"Λείπει το αρχείο {path}")
        content_hash = sha256(path)
        record = canonical_by_hash.get(content_hash)
        if not record:
            raise RuntimeError(f"Δεν βρέθηκε αρχική ταυτότητα για {current_id}")
        stable_id = str(record["source_id"])
        current_to_stable[current_id] = stable_id
        retained_hashes.add(content_hash)

    if len(set(current_to_stable.values())) != len(current_to_stable):
        raise RuntimeError("Η αντιστοίχιση μόνιμων κωδικών δεν είναι μοναδική")

    for current_id, stable_id in current_to_stable.items():
        old_path = SOURCES / f"{current_id}.md"
        new_path = SOURCES / f"{stable_id}.md"
        if old_path == new_path:
            continue
        if new_path.exists():
            raise RuntimeError(f"Υπάρχει ήδη το {new_path}")
        old_path.rename(new_path)

    for row in rows:
        row["Κωδικός"] = current_to_stable[row["Κωδικός"]]
    with CATALOG.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    EXCERPTS.mkdir(parents=True, exist_ok=True)
    for path in list(EXCERPTS.glob("*.md")):
        if path.name == "README.md":
            continue
        current_id = path.stem
        stable_id = current_to_stable.get(current_id)
        if not stable_id:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        text = text.replace(current_id, stable_id)
        text = translate_excerpt(text, stable_id)
        target = EXCERPTS / f"{stable_id}.md"
        path.unlink()
        if target.exists():
            existing = target.read_text(encoding="utf-8", errors="replace")
            if text.strip() not in existing:
                target.write_text(existing.rstrip() + "\n\n---\n\n" + text.lstrip(), encoding="utf-8")
        else:
            target.write_text(text, encoding="utf-8")

    tree = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", "origin/main", "--", "curation/excerpts/by-source"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    for old_path in tree:
        if not old_path.endswith(".md"):
            continue
        old_id = Path(old_path).name.split("__", 1)[0].upper()
        record = old_by_id.get(old_id)
        if not record:
            continue
        content_hash = str(record.get("content_sha256") or "")
        if content_hash not in retained_hashes:
            continue
        stable_id = str(canonical_by_hash[content_hash]["source_id"])
        text = git_text(old_path).replace(old_id, stable_id)
        text = translate_excerpt(text, stable_id)
        target = EXCERPTS / f"{stable_id}.md"
        if target.exists():
            existing = target.read_text(encoding="utf-8", errors="replace")
            if text.strip() not in existing:
                target.write_text(existing.rstrip() + "\n\n---\n\n" + text.lstrip(), encoding="utf-8")
        else:
            target.write_text(text, encoding="utf-8")

    if ORIGINALS.exists():
        for path in list(ORIGINALS.glob("ΠΗΓΗ-*.pdf")):
            current_id = path.stem
            stable_id = current_to_stable.get(current_id)
            if stable_id:
                path.rename(ORIGINALS / f"{stable_id}.pdf")

    print(f"Αποκαταστάθηκαν {len(rows)} μόνιμοι κωδικοί SRC.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
