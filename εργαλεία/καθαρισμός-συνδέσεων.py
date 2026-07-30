#!/usr/bin/env python3
"""Διορθώνει ασφαλείς συνδέσεις και συγχωνεύει μόνο βέβαια διπλότυπα."""
from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

from κοινά_πηγών import (
    OPENREVIEW_RE,
    SOURCE_MARKER_RE,
    canonical_url,
    identities,
    normalized_words,
    source_text,
)

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "κατάλογος" / "πηγές.csv"
REPORT = ROOT / "κατάλογος" / "έλεγχος-συνδέσεων.md"
SOURCES = ROOT / "πηγές"
EXCERPTS = ROOT / "αποσπάσματα"
ORIGINALS = ROOT / "πρωτότυπα"
FIELDS = [
    "Κωδικός", "Τίτλος", "Συγγραφείς", "Έτος", "Σύνδεσμος",
    "Τύπος", "Θέματα", "Κατάσταση", "Επιβεβαίωση", "Προτεραιότητα", "Σημειώσεις",
]
ANTI_BOT = re.compile(
    r"verifying your browser|complete the check below|making sure you're not a bot",
    re.IGNORECASE,
)
HELPERS = {"audit", "audit2", "source audit", "notebooklm audit"}
GENERIC_TITLE = re.compile(
    r"^(?:https?[-_:]|thesis(?:\.pdf)?$|applsci-\d|academic editors?:|"
    r"verifying your browser|pdf[-_]|ebook[-_]|final-web-version-report|agents\s*-\s*kaggle)",
    re.IGNORECASE,
)


def status_score(value: str) -> int:
    return {
        "ελεγμένη": 50,
        "διαθέσιμο πλήρες κείμενο": 40,
        "ελλιπές κείμενο": 20,
        "μόνο μεταδεδομένα": 10,
        "αποτυχημένη εισαγωγή": 0,
    }.get(value, 0)


def verification_score(value: str) -> int:
    return {
        "επιβεβαιωμένη μέσω Crossref": 40,
        "επιβεβαιωμένη μέσω arXiv": 40,
        "πιθανή αντιστοίχιση OpenAlex": 20,
        "μόνο καταγεγραμμένος σύνδεσμος": 10,
        "εκκρεμεί": 0,
        "δεν βρέθηκε αυτόματη αντιστοίχιση": 0,
    }.get(value, 0)


def source_score(row: dict[str, str], text: str) -> tuple[int, int, str]:
    source_id = row["Κωδικός"]
    excerpt_bonus = 100 if (EXCERPTS / f"{source_id}.md").exists() else 0
    title_bonus = 10 if not GENERIC_TITLE.search(row.get("Τίτλος", "")) else 0
    return (
        excerpt_bonus
        + status_score(row.get("Κατάσταση", ""))
        + verification_score(row.get("Επιβεβαίωση", ""))
        + title_bonus,
        len(text),
        source_id,
    )


def combine_topics(left: str, right: str) -> str:
    result: list[str] = []
    for value in [*left.split("; "), *right.split("; ")]:
        value = value.strip()
        if value and value != "χωρίς κατηγορία" and value not in result:
            result.append(value)
    return "; ".join(result or ["χωρίς κατηγορία"])


def merge_rows(primary: dict[str, str], duplicate: dict[str, str]) -> None:
    if GENERIC_TITLE.search(primary.get("Τίτλος", "")) and not GENERIC_TITLE.search(duplicate.get("Τίτλος", "")):
        primary["Τίτλος"] = duplicate["Τίτλος"]
    for field in ("Συγγραφείς", "Έτος", "Σύνδεσμος", "Τύπος"):
        if not primary.get(field) or primary.get(field) == "άγνωστος τύπος":
            if duplicate.get(field):
                primary[field] = duplicate[field]
    primary["Θέματα"] = combine_topics(primary.get("Θέματα", ""), duplicate.get("Θέματα", ""))
    if status_score(duplicate.get("Κατάσταση", "")) > status_score(primary.get("Κατάσταση", "")):
        primary["Κατάσταση"] = duplicate["Κατάσταση"]
    if verification_score(duplicate.get("Επιβεβαίωση", "")) > verification_score(primary.get("Επιβεβαίωση", "")):
        primary["Επιβεβαίωση"] = duplicate["Επιβεβαίωση"]
    priority = {"υψηλή": 4, "μεσαία": 3, "χαμηλή": 2, "χρειάζεται διόρθωση": 1}
    if priority.get(duplicate.get("Προτεραιότητα", ""), 0) > priority.get(primary.get("Προτεραιότητα", ""), 0):
        primary["Προτεραιότητα"] = duplicate["Προτεραιότητα"]
    notes = [primary.get("Σημειώσεις", "").strip(), duplicate.get("Σημειώσεις", "").strip()]
    primary["Σημειώσεις"] = " | ".join(dict.fromkeys(value for value in notes if value))


def move_related(primary_id: str, duplicate_id: str, changes: list[str]) -> None:
    for folder, suffix in ((EXCERPTS, ".md"), (ORIGINALS, ".pdf"), (ORIGINALS, ".url")):
        old = folder / f"{duplicate_id}{suffix}"
        new = folder / f"{primary_id}{suffix}"
        if not old.exists():
            continue
        if not new.exists():
            old.rename(new)
            changes.append(f"Μεταφέρθηκε `{old.name}` στο `{new.name}`.")
            continue
        try:
            same = hashlib.sha256(old.read_bytes()).digest() == hashlib.sha256(new.read_bytes()).digest()
        except OSError:
            same = False
        if same:
            old.unlink()
        else:
            conflict = folder / f"{primary_id}__εναλλακτικό-{duplicate_id}{suffix}"
            old.rename(conflict)
            changes.append(f"Διατηρήθηκε διαφορετικό αρχείο ως `{conflict.name}`.")


def request_json(url: str) -> dict | None:
    try:
        request = Request(url, headers={"User-Agent": "ThesisBibliography/1.0", "Accept": "application/json"})
        with urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception:
        return None


def field_value(value):
    if isinstance(value, dict) and "value" in value:
        return value["value"]
    return value


def openreview_metadata(openreview_id: str) -> dict[str, str] | None:
    for base in ("https://api2.openreview.net/notes?forum=", "https://api.openreview.net/notes?forum="):
        payload = request_json(base + quote(openreview_id))
        notes = (payload or {}).get("notes") or []
        if not notes:
            continue
        note = notes[0]
        content = note.get("content") or {}
        title = str(field_value(content.get("title")) or "").strip()
        authors_raw = field_value(content.get("authors")) or []
        authors = authors_raw if isinstance(authors_raw, str) else "; ".join(str(item).strip() for item in authors_raw if str(item).strip())
        timestamp = note.get("pdate") or note.get("cdate") or note.get("tcdate")
        year = ""
        if isinstance(timestamp, (int, float)):
            year = datetime.fromtimestamp(timestamp / 1000, tz=timezone.utc).strftime("%Y")
        if title:
            return {
                "Τίτλος": title,
                "Συγγραφείς": authors,
                "Έτος": year,
                "Σύνδεσμος": f"https://openreview.net/forum?id={openreview_id}",
                "Τύπος": "ακαδημαϊκή εργασία",
                "Επιβεβαίωση": "μόνο καταγεγραμμένος σύνδεσμος",
            }
    return None


def enrich_rows(rows: list[dict[str, str]], changes: list[str]) -> None:
    for row in rows:
        source_id = row["Κωδικός"]
        text = source_text(SOURCES, source_id)
        if not row.get("Σύνδεσμος"):
            marker = SOURCE_MARKER_RE.search(text)
            if marker:
                row["Σύνδεσμος"] = canonical_url(marker.group(1))
                row["Επιβεβαίωση"] = "μόνο καταγεγραμμένος σύνδεσμος"
                changes.append(f"Συνδέθηκε το `{source_id}` με τον πραγματικό σύνδεσμο του Markdown.")
        openreview = OPENREVIEW_RE.search("\n".join([row.get("Σύνδεσμος", ""), text[:5000]]))
        if openreview and (GENERIC_TITLE.search(row.get("Τίτλος", "")) or ANTI_BOT.search(text[:3000])):
            metadata = openreview_metadata(openreview.group(1))
            if metadata:
                old = row.get("Τίτλος", "")
                row.update({key: value for key, value in metadata.items() if value})
                changes.append(f"Διορθώθηκε το `{source_id}`: «{old}» → «{row['Τίτλος']}».")
                time.sleep(0.2)


def main() -> int:
    with CATALOG.open(encoding="utf-8", newline="") as handle:
        rows = [dict(row) for row in csv.DictReader(handle)]

    changes: list[str] = []
    removed: list[str] = []
    kept: list[dict[str, str]] = []
    for row in rows:
        source_id = row["Κωδικός"]
        text = source_text(SOURCES, source_id)
        title_key = normalized_words(row.get("Τίτλος", ""))
        is_helper = title_key in HELPERS or ("notebooklm" in text[:5000].casefold() and "audit" in title_key)
        is_empty = not text.strip() and not row.get("Σύνδεσμος")
        if is_helper or is_empty:
            path = SOURCES / f"{source_id}.md"
            if path.exists():
                path.unlink()
            for related in (EXCERPTS / f"{source_id}.md", ORIGINALS / f"{source_id}.pdf", ORIGINALS / f"{source_id}.url"):
                if related.exists():
                    related.unlink()
            removed.append(f"`{source_id}` — {row.get('Τίτλος', '')}")
        else:
            kept.append(row)
    rows = kept

    enrich_rows(rows, changes)
    texts = {row["Κωδικός"]: source_text(SOURCES, row["Κωδικός"]) for row in rows}
    merged: list[tuple[str, str, str]] = []

    while True:
        index: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in rows:
            for key in identities(row.get("Σύνδεσμος", ""), row.get("Τίτλος", ""), texts[row["Κωδικός"]]):
                index[key].append(row)
        group = next(((key, values) for key, values in index.items() if len({item["Κωδικός"] for item in values}) > 1), None)
        if group is None:
            break
        key, values = group
        unique = {item["Κωδικός"]: item for item in values}
        ordered = sorted(unique.values(), key=lambda item: source_score(item, texts[item["Κωδικός"]]), reverse=True)
        primary = ordered[0]
        for duplicate in ordered[1:]:
            primary_id, duplicate_id = primary["Κωδικός"], duplicate["Κωδικός"]
            if len(texts[duplicate_id]) > len(texts[primary_id]):
                (SOURCES / f"{primary_id}.md").write_text(texts[duplicate_id], encoding="utf-8")
                texts[primary_id] = texts[duplicate_id]
            merge_rows(primary, duplicate)
            move_related(primary_id, duplicate_id, changes)
            duplicate_path = SOURCES / f"{duplicate_id}.md"
            if duplicate_path.exists():
                duplicate_path.unlink()
            rows = [row for row in rows if row["Κωδικός"] != duplicate_id]
            texts.pop(duplicate_id, None)
            merged.append((duplicate_id, primary_id, key))

    with CATALOG.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda row: row["Τίτλος"].casefold()))

    subprocess.run([sys.executable, str(ROOT / "εργαλεία" / "εισαγωγή.py"), "--catalog-only"], cwd=ROOT, check=True)

    lines = [
        "# Έλεγχος συνδέσεων πηγών", "",
        "Συγχώνευση γίνεται μόνο με κοινό DOI, arXiv ID, OpenReview ID ή ακριβώς ίδιο σύνδεσμο.",
        "Παρόμοιοι τίτλοι μόνοι τους δεν αρκούν.", "",
        f"- Ασφαλείς συγχωνεύσεις: **{len(merged)}**",
        f"- Προσωρινά ή κενά αρχεία που αφαιρέθηκαν: **{len(removed)}**",
        f"- Άλλες ασφαλείς διορθώσεις: **{len(changes)}**", "",
    ]
    if merged:
        lines.extend(["## Συγχωνεύσεις", "", "| Παλαιός κωδικός | Κύριος κωδικός | Κοινή ταυτότητα |", "|---|---|---|"])
        lines.extend(f"| `{old}` | `{new}` | `{key}` |" for old, new, key in merged)
        lines.append("")
    if removed:
        lines.extend(["## Αρχεία που δεν ήταν πηγές", ""])
        lines.extend(f"- {item}" for item in removed)
        lines.append("")
    if changes:
        lines.extend(["## Διορθώσεις", ""])
        lines.extend(f"- {item}" for item in changes)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Συγχωνεύθηκαν {len(merged)} βέβαια διπλότυπα και αφαιρέθηκαν {len(removed)} μη πηγές.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
