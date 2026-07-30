#!/usr/bin/env python3
"""Διορθώνει συνδέσεις και συγχωνεύει μόνο τεκμηριωμένα διπλότυπα."""
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
from πρωτότυπα_κοινά import GENERIC_TITLE

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


def source_score(row: dict[str, str], text: str) -> tuple[int, int, int, str]:
    source_id = row["Κωδικός"]
    excerpt_bonus = 100 if (EXCERPTS / f"{source_id}.md").exists() else 0
    title_bonus = 10 if not GENERIC_TITLE.search(row.get("Τίτλος", "")) else 0
    link_bonus = 30 if row.get("Σύνδεσμος") else 0
    return (
        excerpt_bonus
        + status_score(row.get("Κατάσταση", ""))
        + verification_score(row.get("Επιβεβαίωση", ""))
        + title_bonus
        + link_bonus,
        len(text),
        len(row.get("Τίτλος", "")),
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


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def move_one_related(old: Path, new: Path, changes: list[str]) -> None:
    if not old.exists():
        return
    if not new.exists():
        old.rename(new)
        changes.append(f"Μεταφέρθηκε `{old.name}` στο `{new.name}`.")
        return
    try:
        same = file_sha256(old) == file_sha256(new)
    except OSError:
        same = False
    if same:
        old.unlink()
        return
    suffix = old.suffix
    conflict = new.with_name(f"{new.stem}__σύγκρουση-{file_sha256(old)[:10].upper()}{suffix}")
    old.rename(conflict)
    changes.append(f"Διατηρήθηκε διαφορετικό αρχείο ως `{conflict.name}`.")


def move_related(primary_id: str, duplicate_id: str, changes: list[str]) -> None:
    move_one_related(
        EXCERPTS / f"{duplicate_id}.md",
        EXCERPTS / f"{primary_id}.md",
        changes,
    )
    for old in sorted(ORIGINALS.glob(f"{duplicate_id}*.pdf")):
        tail = old.stem[len(duplicate_id):]
        move_one_related(old, ORIGINALS / f"{primary_id}{tail}.pdf", changes)
    move_one_related(
        ORIGINALS / f"{duplicate_id}.url",
        ORIGINALS / f"{primary_id}.url",
        changes,
    )


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
        authors = (
            authors_raw
            if isinstance(authors_raw, str)
            else "; ".join(str(item).strip() for item in authors_raw if str(item).strip())
        )
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


def authors_compatible(left: str, right: str) -> bool:
    if not left.strip() or not right.strip():
        return False
    a = normalized_words(left)
    b = normalized_words(right)
    return a == b or a in b or b in a


def years_compatible(left: str, right: str) -> bool:
    if not left.strip() or not right.strip():
        return True
    if not left.isdigit() or not right.isdigit():
        return False
    return abs(int(left) - int(right)) <= 1


def texts_are_exact_duplicates(left: str, right: str) -> bool:
    a = normalized_words(left)
    b = normalized_words(right)
    return len(a) >= 300 and a == b


def orphan_corroborated(
    primary: dict[str, str],
    duplicate: dict[str, str],
    texts: dict[str, str],
) -> bool:
    if authors_compatible(primary.get("Συγγραφείς", ""), duplicate.get("Συγγραφείς", "")):
        return years_compatible(primary.get("Έτος", ""), duplicate.get("Έτος", ""))
    return texts_are_exact_duplicates(
        texts.get(primary["Κωδικός"], ""),
        texts.get(duplicate["Κωδικός"], ""),
    )


def merge_one(
    rows: list[dict[str, str]],
    texts: dict[str, str],
    primary: dict[str, str],
    duplicate: dict[str, str],
    key: str,
    changes: list[str],
    merged: list[tuple[str, str, str]],
) -> list[dict[str, str]]:
    primary_id, duplicate_id = primary["Κωδικός"], duplicate["Κωδικός"]
    if len(texts.get(duplicate_id, "")) > len(texts.get(primary_id, "")):
        (SOURCES / f"{primary_id}.md").write_text(texts[duplicate_id], encoding="utf-8")
        texts[primary_id] = texts[duplicate_id]
    merge_rows(primary, duplicate)
    move_related(primary_id, duplicate_id, changes)
    duplicate_path = SOURCES / f"{duplicate_id}.md"
    if duplicate_path.exists():
        duplicate_path.unlink()
    texts.pop(duplicate_id, None)
    merged.append((duplicate_id, primary_id, key))
    return [row for row in rows if row["Κωδικός"] != duplicate_id]


def merge_strong_identities(
    rows: list[dict[str, str]],
    texts: dict[str, str],
    changes: list[str],
    merged: list[tuple[str, str, str]],
) -> list[dict[str, str]]:
    while True:
        index: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in rows:
            for key in identities(row.get("Σύνδεσμος", ""), row.get("Τίτλος", ""), texts[row["Κωδικός"]]):
                index[key].append(row)
        group = next(
            (
                (key, values)
                for key, values in index.items()
                if len({item["Κωδικός"] for item in values}) > 1
            ),
            None,
        )
        if group is None:
            return rows
        key, values = group
        unique = {item["Κωδικός"]: item for item in values}
        ordered = sorted(
            unique.values(),
            key=lambda item: source_score(item, texts[item["Κωδικός"]]),
            reverse=True,
        )
        primary = ordered[0]
        for duplicate in ordered[1:]:
            rows = merge_one(rows, texts, primary, duplicate, key, changes, merged)


def merge_exact_title_orphans(
    rows: list[dict[str, str]],
    texts: dict[str, str],
    changes: list[str],
    merged: list[tuple[str, str, str]],
) -> list[dict[str, str]]:
    """Συγχωνεύει exact-title orphan μόνο με δεύτερο ισχυρό τεκμήριο.

    Απαιτεί είτε συμβατούς, μη κενούς δημιουργούς είτε ακριβώς ίδιο πλήρες
    Markdown. Το ίδιο έτος μόνο του και η απουσία μεταδεδομένων δεν αρκούν.
    """
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        title_key = normalized_words(row.get("Τίτλος", ""))
        if len(title_key) >= 20 and not GENERIC_TITLE.search(row.get("Τίτλος", "")):
            groups[title_key].append(row)

    for title_key, values in list(groups.items()):
        current = [
            row for row in values
            if any(item["Κωδικός"] == row["Κωδικός"] for item in rows)
        ]
        if len(current) < 2 or all(row.get("Σύνδεσμος") for row in current):
            continue
        ordered = sorted(
            current,
            key=lambda item: source_score(item, texts[item["Κωδικός"]]),
            reverse=True,
        )
        primary = ordered[0]
        for duplicate in ordered[1:]:
            if primary.get("Σύνδεσμος") and duplicate.get("Σύνδεσμος"):
                continue
            primary_ids = identities(
                primary.get("Σύνδεσμος", ""),
                primary.get("Τίτλος", ""),
                texts[primary["Κωδικός"]],
            )
            duplicate_ids = identities(
                duplicate.get("Σύνδεσμος", ""),
                duplicate.get("Τίτλος", ""),
                texts[duplicate["Κωδικός"]],
            )
            if primary_ids and duplicate_ids and not (primary_ids & duplicate_ids):
                continue
            if not orphan_corroborated(primary, duplicate, texts):
                continue
            rows = merge_one(
                rows,
                texts,
                primary,
                duplicate,
                f"exact-title-corroborated:{title_key}",
                changes,
                merged,
            )
    return rows


def append_report(
    merged: list[tuple[str, str, str]],
    removed: list[str],
    changes: list[str],
) -> None:
    if not merged and not removed and not changes:
        return
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    if REPORT.exists() and REPORT.read_text(encoding="utf-8", errors="replace").strip():
        lines = [REPORT.read_text(encoding="utf-8", errors="replace").rstrip(), "", "---", ""]
    else:
        lines = [
            "# Έλεγχος συνδέσεων πηγών", "",
            "Συγχώνευση γίνεται με κοινό DOI, arXiv ID, OpenReview ID, ακριβώς ίδιο συγκεκριμένο σύνδεσμο ή ακριβώς ίδιο τίτλο μαζί με συμβατούς δημιουργούς/ακριβώς ίδιο κείμενο.",
            "Παρόμοιος τίτλος ή κενά μεταδεδομένα από μόνα τους δεν αρκούν.", "",
        ]
    lines.extend([
        f"## Έλεγχος {timestamp}", "",
        f"- Ασφαλείς συγχωνεύσεις: **{len(merged)}**",
        f"- Προσωρινά ή κενά αρχεία που αφαιρέθηκαν: **{len(removed)}**",
        f"- Άλλες ασφαλείς διορθώσεις: **{len(changes)}**", "",
    ])
    if merged:
        lines.extend([
            "### Συγχωνεύσεις", "",
            "| Παλαιός κωδικός | Κύριος κωδικός | Τεκμήριο |",
            "|---|---|---|",
        ])
        lines.extend(f"| `{old}` | `{new}` | `{key}` |" for old, new, key in merged)
        lines.append("")
    if removed:
        lines.extend(["### Αρχεία που δεν ήταν πηγές", ""])
        lines.extend(f"- {item}" for item in removed)
        lines.append("")
    if changes:
        lines.extend(["### Διορθώσεις", ""])
        lines.extend(f"- {item}" for item in changes)
    REPORT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


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
        is_helper = title_key in HELPERS or (
            "notebooklm" in text[:5000].casefold() and "audit" in title_key
        )
        is_empty = not normalized_words(text) and not row.get("Σύνδεσμος")
        original = ORIGINALS / f"{source_id}.pdf"
        if is_helper:
            path = SOURCES / f"{source_id}.md"
            if path.exists():
                path.unlink()
            for related in (
                EXCERPTS / f"{source_id}.md",
                original,
                ORIGINALS / f"{source_id}.url",
            ):
                if related.exists():
                    related.unlink()
            removed.append(f"`{source_id}` — {row.get('Τίτλος', '')}")
        elif is_empty and original.exists():
            (SOURCES / f"{source_id}.md").write_text(
                f"# {row.get('Τίτλος', source_id)}\n\n"
                "> Υπάρχει το πρωτότυπο PDF, αλλά το πλήρες Markdown δεν έχει ακόμη δημιουργηθεί ή ελεγχθεί.\n",
                encoding="utf-8",
            )
            row["Κατάσταση"] = "μόνο μεταδεδομένα"
            changes.append(f"Διατηρήθηκε το `{source_id}` επειδή υπάρχει συνδεδεμένο πρωτότυπο PDF.")
            kept.append(row)
        elif is_empty:
            path = SOURCES / f"{source_id}.md"
            if path.exists():
                path.unlink()
            removed.append(f"`{source_id}` — {row.get('Τίτλος', '')}")
        else:
            kept.append(row)
    rows = kept

    enrich_rows(rows, changes)
    texts = {row["Κωδικός"]: source_text(SOURCES, row["Κωδικός"]) for row in rows}
    merged: list[tuple[str, str, str]] = []
    rows = merge_strong_identities(rows, texts, changes, merged)
    rows = merge_exact_title_orphans(rows, texts, changes, merged)

    with CATALOG.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda row: row["Τίτλος"].casefold()))

    subprocess.run(
        [sys.executable, str(ROOT / "εργαλεία" / "εισαγωγή.py"), "--catalog-only"],
        cwd=ROOT,
        check=True,
    )
    append_report(merged, removed, changes)
    print(f"Συγχωνεύθηκαν {len(merged)} βέβαια διπλότυπα και αφαιρέθηκαν {len(removed)} μη πηγές.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
