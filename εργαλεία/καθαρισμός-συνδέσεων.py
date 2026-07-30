#!/usr/bin/env python3
"""Διορθώνει ασφαλείς συνδέσεις πηγών και συγχωνεύει βέβαια διπλότυπα.

Δεν συγχωνεύει πηγές μόνο επειδή έχουν παρόμοιο τίτλο. Αυτόματη συγχώνευση
γίνεται μόνο όταν υπάρχει κοινό ισχυρό αναγνωριστικό (DOI, arXiv, OpenReview)
ή ακριβώς ο ίδιος κανονικοποιημένος σύνδεσμος.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
import sys
import time
import unicodedata
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote, urlsplit
from urllib.request import Request, urlopen

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
DOI_RE = re.compile(r"(?:doi\.org/|doi\s*:\s*)(10\.\d{4,9}/[^\s)>\],;]+)", re.IGNORECASE)
ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})(?:v\d+)?", re.IGNORECASE)
OPENREVIEW_RE = re.compile(r"openreview\.net/(?:forum|pdf)\?(?:id=)?([A-Za-z0-9_-]+)", re.IGNORECASE)
SOURCE_RE = re.compile(r"^>\s*Source:\s*(\S+)", re.IGNORECASE | re.MULTILINE)
ANTI_BOT = re.compile(r"verifying your browser|complete the check below|making sure you're not a bot", re.IGNORECASE)
HELPER_TITLES = {"audit", "audit2", "source audit", "notebooklm audit"}
GENERIC_TITLE_RE = re.compile(
    r"^(?:https?[-_:]|thesis(?:\.pdf)?$|applsci-\d|academic editors?:|verifying your browser|"
    r"pdf[-_]|ebook[-_]|final-web-version-report|agents\s*-\s*kaggle)",
    re.IGNORECASE,
)


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKC", value or "").casefold()
    return " ".join("".join(ch if ch.isalnum() else " " for ch in value).split())


def read_text(source_id: str) -> str:
    path = SOURCES / f"{source_id}.md"
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def canonical_url(url: str) -> str:
    url = clean(url).rstrip(".,;:)")
    if not url:
        return ""
    arxiv = ARXIV_RE.search(url)
    if arxiv:
        return f"https://arxiv.org/abs/{arxiv.group(1)}"
    doi = DOI_RE.search(url)
    if doi:
        return f"https://doi.org/{doi.group(1).rstrip('.').casefold()}"
    parts = urlsplit(url)
    if not parts.scheme:
        return url
    return parts._replace(netloc=parts.netloc.lower().removeprefix("www."), fragment="").geturl().rstrip("/")


def keys(row: dict[str, str], text: str) -> set[str]:
    sample = "\n".join([row.get("Σύνδεσμος", ""), text[:25000]])
    result: set[str] = set()
    for match in DOI_RE.finditer(sample):
        result.add("doi:" + match.group(1).rstrip(".").casefold())
    for match in ARXIV_RE.finditer(sample):
        result.add("arxiv:" + match.group(1))
    for match in OPENREVIEW_RE.finditer(sample):
        result.add("openreview:" + match.group(1))
    url = canonical_url(row.get("Σύνδεσμος", ""))
    if url:
        result.add("url:" + url.casefold())
    return result


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


def primary_score(row: dict[str, str], text: str) -> tuple[int, int, int, str]:
    sid = row["Κωδικός"]
    has_excerpt = 1 if (EXCERPTS / f"{sid}.md").exists() else 0
    generic = 0 if GENERIC_TITLE_RE.search(row.get("Τίτλος", "")) else 1
    return (
        has_excerpt * 100 + status_score(row.get("Κατάσταση", "")) + verification_score(row.get("Επιβεβαίωση", "")) + generic * 10,
        len(text),
        -len(row.get("Τίτλος", "")),
        sid,
    )


def combine_topics(left: str, right: str) -> str:
    values = []
    for source in (left, right):
        for value in source.split("; "):
            value = clean(value)
            if value and value != "χωρίς κατηγορία" and value not in values:
                values.append(value)
    return "; ".join(values or ["χωρίς κατηγορία"])


def merge_rows(primary: dict[str, str], duplicate: dict[str, str]) -> None:
    generic_primary = bool(GENERIC_TITLE_RE.search(primary.get("Τίτλος", "")))
    generic_duplicate = bool(GENERIC_TITLE_RE.search(duplicate.get("Τίτλος", "")))
    if (generic_primary and not generic_duplicate) or (not primary.get("Τίτλος") and duplicate.get("Τίτλος")):
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
    priority_order = {"υψηλή": 4, "μεσαία": 3, "χαμηλή": 2, "χρειάζεται διόρθωση": 1}
    if priority_order.get(duplicate.get("Προτεραιότητα", ""), 0) > priority_order.get(primary.get("Προτεραιότητα", ""), 0):
        primary["Προτεραιότητα"] = duplicate["Προτεραιότητα"]
    notes = [clean(primary.get("Σημειώσεις", "")), clean(duplicate.get("Σημειώσεις", ""))]
    primary["Σημειώσεις"] = " | ".join(dict.fromkeys(value for value in notes if value))


def move_associated_files(primary_id: str, duplicate_id: str, changes: list[str]) -> None:
    for folder, suffix in ((EXCERPTS, ".md"), (ORIGINALS, ".pdf"), (ORIGINALS, ".url")):
        old = folder / f"{duplicate_id}{suffix}"
        new = folder / f"{primary_id}{suffix}"
        if not old.exists():
            continue
        if not new.exists():
            old.rename(new)
            changes.append(f"Μεταφέρθηκε `{old.name}` στο `{new.name}`.")
        else:
            try:
                same = hashlib.sha256(old.read_bytes()).digest() == hashlib.sha256(new.read_bytes()).digest()
            except OSError:
                same = False
            if same:
                old.unlink()
            else:
                conflict = folder / f"{primary_id}__εναλλακτικό-{duplicate_id}{suffix}"
                old.rename(conflict)
                changes.append(f"Διατηρήθηκε διαφορετικό συσχετισμένο αρχείο ως `{conflict.name}`.")


def request_json(url: str) -> dict | None:
    try:
        req = Request(url, headers={"User-Agent": "ThesisBibliography/1.0", "Accept": "application/json"})
        with urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception:
        return None


def content_value(value):
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
        title = clean(str(content_value(content.get("title")) or ""))
        authors_raw = content_value(content.get("authors")) or []
        if isinstance(authors_raw, str):
            authors = authors_raw
        else:
            authors = "; ".join(clean(str(item)) for item in authors_raw if clean(str(item)))
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


def enrich_safe_titles(rows: list[dict[str, str]], changes: list[str]) -> None:
    for row in rows:
        sid = row["Κωδικός"]
        text = read_text(sid)
        if not row.get("Σύνδεσμος"):
            marker = SOURCE_RE.search(text)
            if marker:
                row["Σύνδεσμος"] = canonical_url(marker.group(1))
                row["Επιβεβαίωση"] = "μόνο καταγεγραμμένος σύνδεσμος"
                changes.append(f"Συνδέθηκε το `{sid}` με τον σύνδεσμο του Markdown.")
        openreview = OPENREVIEW_RE.search("\n".join([row.get("Σύνδεσμος", ""), text[:5000]]))
        if openreview and (GENERIC_TITLE_RE.search(row.get("Τίτλος", "")) or ANTI_BOT.search(text[:3000])):
            metadata = openreview_metadata(openreview.group(1))
            if metadata:
                old_title = row.get("Τίτλος", "")
                row.update({key: value for key, value in metadata.items() if value})
                changes.append(f"Διορθώθηκε το `{sid}`: «{old_title}» → «{row['Τίτλος']}».")
                time.sleep(0.2)


def main() -> int:
    with CATALOG.open(encoding="utf-8", newline="") as handle:
        rows = [dict(row) for row in csv.DictReader(handle)]

    changes: list[str] = []
    removed_non_sources: list[str] = []
    retained: list[dict[str, str]] = []
    for row in rows:
        sid = row["Κωδικός"]
        text = read_text(sid)
        title_key = norm(row.get("Τίτλος", ""))
        is_helper = title_key in HELPER_TITLES or ("notebooklm" in text[:5000].casefold() and "audit" in title_key)
        is_empty = not text.strip() and not row.get("Σύνδεσμος")
        if is_helper or is_empty:
            path = SOURCES / f"{sid}.md"
            if path.exists():
                path.unlink()
            for related in (EXCERPTS / f"{sid}.md", ORIGINALS / f"{sid}.pdf", ORIGINALS / f"{sid}.url"):
                if related.exists():
                    related.unlink()
            removed_non_sources.append(f"`{sid}` — {row.get('Τίτλος', '')}")
        else:
            retained.append(row)
    rows = retained

    enrich_safe_titles(rows, changes)
    texts = {row["Κωδικός"]: read_text(row["Κωδικός"]) for row in rows}
    merged_aliases: list[tuple[str, str, str]] = []

    while True:
        index: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in rows:
            for key in keys(row, texts.get(row["Κωδικός"], "")):
                index[key].append(row)
        group = next(((key, items) for key, items in index.items() if len({item["Κωδικός"] for item in items}) > 1), None)
        if group is None:
            break
        key, items = group
        unique = {item["Κωδικός"]: item for item in items}
        ordered = sorted(unique.values(), key=lambda row: primary_score(row, texts.get(row["Κωδικός"], "")), reverse=True)
        primary = ordered[0]
        for duplicate in ordered[1:]:
            pid, did = primary["Κωδικός"], duplicate["Κωδικός"]
            ptext, dtext = texts.get(pid, ""), texts.get(did, "")
            if len(dtext) > len(ptext):
                (SOURCES / f"{pid}.md").write_text(dtext, encoding="utf-8")
                texts[pid] = dtext
            merge_rows(primary, duplicate)
            move_associated_files(pid, did, changes)
            duplicate_path = SOURCES / f"{did}.md"
            if duplicate_path.exists():
                duplicate_path.unlink()
            rows = [row for row in rows if row["Κωδικός"] != did]
            texts.pop(did, None)
            merged_aliases.append((did, pid, key))

    with CATALOG.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda row: row["Τίτλος"].casefold()))

    subprocess.run([sys.executable, str(ROOT / "εργαλεία" / "εισαγωγή.py"), "--catalog-only"], cwd=ROOT, check=True)

    lines = [
        "# Έλεγχος συνδέσεων πηγών", "",
        "Ο έλεγχος συγχωνεύει μόνο βέβαια διπλότυπα με κοινό DOI, arXiv ID, OpenReview ID ή ακριβώς ίδιο σύνδεσμο.",
        "Δεν συγχωνεύει πηγές απλώς επειδή οι τίτλοι μοιάζουν.", "",
        f"- Συγχωνεύθηκαν ασφαλώς: **{len(merged_aliases)}** εγγραφές",
        f"- Αφαιρέθηκαν καθαρά προσωρινά/κενά αρχεία: **{len(removed_non_sources)}**",
        f"- Άλλες ασφαλείς διορθώσεις: **{len(changes)}**", "",
    ]
    if merged_aliases:
        lines.extend(["## Συγχωνεύσεις", "", "| Παλαιός κωδικός | Κύριος κωδικός | Κοινή ταυτότητα |", "|---|---|---|"])
        lines.extend(f"| `{old}` | `{new}` | `{key}` |" for old, new, key in merged_aliases)
        lines.append("")
    if removed_non_sources:
        lines.extend(["## Αρχεία που δεν ήταν πηγές", ""])
        lines.extend(f"- {item}" for item in removed_non_sources)
        lines.append("")
    if changes:
        lines.extend(["## Διορθώσεις", ""])
        lines.extend(f"- {item}" for item in changes)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Συγχωνεύθηκαν {len(merged_aliases)} εγγραφές και αφαιρέθηκαν {len(removed_non_sources)} μη πηγές.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
