#!/usr/bin/env python3
"""Μετατρέπει την παλιά δομή του αποθετηρίου στη νέα, απλή ελληνική μορφή."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OLD_CATALOG = ROOT / "catalog" / "source_catalog.json"
OLD_OVERLAY = ROOT / "catalog" / "verified_source_metadata.json"
OLD_EXCERPTS = ROOT / "curation" / "excerpts" / "by-source"

SOURCES = ROOT / "πηγές"
CATALOG = ROOT / "κατάλογος"
EXCERPTS = ROOT / "αποσπάσματα"
INCOMING = ROOT / "νέες-πηγές"
ORIGINALS = ROOT / "πρωτότυπα"

TYPE_MAP = {
    "academic-paper": "ακαδημαϊκή εργασία",
    "thesis-or-dissertation": "διπλωματική ή διατριβή",
    "book-or-chapter": "βιβλίο ή κεφάλαιο",
    "standard-or-institutional-report": "θεσμική ή τεχνική αναφορά",
    "code-repository": "αποθετήριο κώδικα",
    "documentation-or-educational": "τεκμηρίωση ή εκπαιδευτικό υλικό",
    "video-or-lecture": "βίντεο ή διάλεξη",
    "web-article": "ιστοσελίδα",
    "unknown": "άγνωστος τύπος",
}

TOPIC_MAP = {
    "robust-rl": "εύρωστη ενισχυτική μάθηση",
    "resilience-recovery": "ανθεκτικότητα και ανάκαμψη",
    "nonstationarity": "μη στασιμότητα",
    "gridworld": "GridWorld",
    "safe-rl": "ασφαλής ενισχυτική μάθηση",
    "transition-uncertainty": "αβεβαιότητα μεταβάσεων",
    "action-uncertainty": "αβεβαιότητα ενεργειών",
    "observation-uncertainty": "αβεβαιότητα παρατηρήσεων",
    "reward-uncertainty": "αβεβαιότητα ανταμοιβής",
    "partial-observability": "μερική παρατηρησιμότητα",
    "tabular-rl": "πινακοποιημένη ενισχυτική μάθηση",
    "deep-rl": "βαθιά ενισχυτική μάθηση",
    "model-based-rl": "ενισχυτική μάθηση με μοντέλο",
    "continual-adaptation": "συνεχής προσαρμογή",
    "evaluation-statistics": "στατιστική αξιολόγηση",
    "benchmark-tooling": "περιβάλλοντα και benchmarks",
    "ai-agents-background": "πράκτορες τεχνητής νοημοσύνης",
    "governance-ethics": "διακυβέρνηση και ηθική",
    "unclassified": "χωρίς κατηγορία",
}

STATUS_MAP = {
    "full-text": "διαθέσιμο πλήρες κείμενο",
    "partial": "ελλιπές κείμενο",
    "metadata-only": "μόνο μεταδεδομένα",
    "failed-load": "αποτυχημένη εισαγωγή",
}

PRIORITY_MAP = {
    "P1-core": "υψηλή",
    "P2-supporting": "υψηλή",
    "P3-review": "μεσαία",
    "P4-recover-or-replace": "χρειάζεται διόρθωση",
    "P5-archive-only": "χαμηλή",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def greek_id(content_hash: str) -> str:
    return f"ΠΗΓΗ-{content_hash[:10].upper()}"


def clean_text(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def normalize_topics(value: Any) -> str:
    if isinstance(value, list):
        raw = value
    else:
        raw = re.split(r"[;,]", str(value or ""))
    translated = []
    for item in raw:
        key = clean_text(item)
        if not key:
            continue
        label = TOPIC_MAP.get(key, key)
        if label not in translated:
            translated.append(label)
    return "; ".join(translated or ["χωρίς κατηγορία"])


def source_status(record: dict[str, Any]) -> str:
    status = STATUS_MAP.get(str(record.get("content_status") or ""), "χρειάζεται έλεγχο")
    if status == "διαθέσιμο πλήρες κείμενο" and str(record.get("review_status") or "") == "reviewed":
        return "ελεγμένη"
    return status


def priority(record: dict[str, Any]) -> str:
    return PRIORITY_MAP.get(str(record.get("priority") or ""), "μεσαία")


def preferred_metadata(record: dict[str, Any], overlay: dict[str, Any]) -> dict[str, str]:
    verified = str(overlay.get("verification_status") or "")
    use_overlay = verified in {
        "verified-arxiv-api", "verified-crossref-api", "probable-openalex-match"
    }
    title = clean_text(overlay.get("verified_title")) if use_overlay else ""
    authors = clean_text(overlay.get("authors")) if use_overlay else ""
    year = clean_text(overlay.get("year")) if use_overlay else ""
    link = clean_text(overlay.get("official_url")) or clean_text(record.get("url"))
    return {
        "Τίτλος": title or clean_text(record.get("title")) or "Χωρίς τίτλο",
        "Συγγραφείς": authors or clean_text(record.get("authors")),
        "Έτος": year or clean_text(record.get("year")),
        "Σύνδεσμος": link,
    }


def translate_excerpt(text: str, old_id: str, new_id: str) -> str:
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
    for source, target in replacements.items():
        text = text.replace(source, target)
    text = text.replace(old_id, new_id)
    return text


def markdown_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def write_catalog(rows: list[dict[str, str]]) -> None:
    CATALOG.mkdir(parents=True, exist_ok=True)
    fields = [
        "Κωδικός", "Τίτλος", "Συγγραφείς", "Έτος", "Σύνδεσμος",
        "Τύπος", "Θέματα", "Κατάσταση", "Επιβεβαίωση", "Προτεραιότητα", "Σημειώσεις",
    ]
    with (CATALOG / "πηγές.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    lines = [
        "# Κατάλογος πηγών",
        "",
        f"Συνολικές ενεργές πηγές: **{len(rows)}**.",
        "",
        "> Ο κατάλογος είναι εργαλείο διαλογής. Μια πηγή θεωρείται έτοιμη για τη διπλωματική μόνο μετά από έλεγχο του πλήρους κειμένου.",
        "",
        "| Κωδικός | Τίτλος | Συγγραφείς | Έτος | Τύπος | Θέματα | Κατάσταση | Επιβεβαίωση | Προτεραιότητα |",
        "|---|---|---|---:|---|---|---|---|---|",
    ]
    for row in sorted(rows, key=lambda item: (
        {"υψηλή": 0, "μεσαία": 1, "χρειάζεται διόρθωση": 2, "χαμηλή": 3}.get(item["Προτεραιότητα"], 9),
        item["Τίτλος"].casefold(),
    )):
        title = markdown_escape(row["Τίτλος"])
        if row["Σύνδεσμος"]:
            title = f"[{title}]({row['Σύνδεσμος']})"
        lines.append(
            f"| `{row['Κωδικός']}` | {title} | {markdown_escape(row['Συγγραφείς'] or '—')} | "
            f"{row['Έτος'] or '—'} | {markdown_escape(row['Τύπος'])} | {markdown_escape(row['Θέματα'])} | "
            f"{markdown_escape(row['Κατάσταση'])} | {markdown_escape(row['Επιβεβαίωση'])} | {markdown_escape(row['Προτεραιότητα'])} |"
        )
    (CATALOG / "πηγές.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    problematic = [
        row for row in rows
        if row["Κατάσταση"] in {"ελλιπές κείμενο", "μόνο μεταδεδομένα", "αποτυχημένη εισαγωγή"}
        or not row["Σύνδεσμος"]
        or row["Τύπος"] == "άγνωστος τύπος"
    ]
    problem_lines = [
        "# Πηγές που χρειάζονται διόρθωση",
        "",
        "Οι παρακάτω πηγές δεν είναι ακόμη ασφαλείς για χρήση στη διπλωματική.",
        "",
        "| Κωδικός | Τίτλος | Πρόβλημα |",
        "|---|---|---|",
    ]
    for row in problematic:
        problems = []
        if row["Κατάσταση"] not in {"διαθέσιμο πλήρες κείμενο", "ελεγμένη"}:
            problems.append(row["Κατάσταση"])
        if not row["Σύνδεσμος"]:
            problems.append("λείπει σύνδεσμος")
        if row["Τύπος"] == "άγνωστος τύπος":
            problems.append("άγνωστος τύπος")
        problem_lines.append(
            f"| `{row['Κωδικός']}` | {markdown_escape(row['Τίτλος'])} | {', '.join(dict.fromkeys(problems))} |"
        )
    if not problematic:
        problem_lines.append("| — | Δεν υπάρχουν προβληματικές πηγές | — |")
    (CATALOG / "προβληματικές-πηγές.md").write_text(
        "\n".join(problem_lines) + "\n", encoding="utf-8"
    )


def remove_obsolete_paths() -> None:
    obsolete = [
        "catalog", "curation", "imports", "notes", "queues", "sources", "incoming",
        "scripts", "tests", "archive", "workspace",
    ]
    for name in obsolete:
        path = ROOT / name
        if path.exists():
            shutil.rmtree(path)
    path = ROOT / "AGENTS.md"
    if path.exists():
        path.unlink()

    workflows = ROOT / ".github" / "workflows"
    if workflows.exists():
        keep = {
            "αυτόματη-εισαγωγή.yml",
            "έλεγχος.yml",
            "ενημέρωση-μεταδεδομένων.yml",
            "μετάβαση.yml",
        }
        for workflow in workflows.iterdir():
            if workflow.is_file() and workflow.name not in keep:
                workflow.unlink()


def main() -> int:
    if not OLD_CATALOG.exists():
        raise SystemExit("Δεν βρέθηκε ο παλιός κατάλογος πηγών.")

    records = json.loads(OLD_CATALOG.read_text(encoding="utf-8"))
    overlays = {}
    if OLD_OVERLAY.exists():
        overlays = {
            str(item.get("source_id")): item
            for item in json.loads(OLD_OVERLAY.read_text(encoding="utf-8"))
            if isinstance(item, dict) and item.get("source_id")
        }

    SOURCES.mkdir(parents=True, exist_ok=True)
    EXCERPTS.mkdir(parents=True, exist_ok=True)
    INCOMING.mkdir(parents=True, exist_ok=True)
    ORIGINALS.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, str]] = []
    old_to_new: dict[str, str] = {}
    seen_hashes: set[str] = set()
    removed_out_of_scope = 0
    removed_syntheses = 0
    removed_exact_duplicates = 0

    for record in records:
        source_type = str(record.get("source_type") or "")
        relevance = str(record.get("relevance") or "")
        if source_type == "notebooklm-synthesis":
            removed_syntheses += 1
            continue
        if relevance == "out-of-scope":
            removed_out_of_scope += 1
            continue

        old_path = ROOT / str(record.get("normalized_path") or "")
        if not old_path.exists() or not old_path.is_file():
            continue
        content_hash = sha256(old_path)
        if content_hash in seen_hashes:
            removed_exact_duplicates += 1
            continue
        seen_hashes.add(content_hash)

        new_id = greek_id(content_hash)
        old_id = str(record.get("source_id") or "")
        old_to_new[old_id] = new_id
        target = SOURCES / f"{new_id}.md"
        shutil.copy2(old_path, target)

        metadata = preferred_metadata(record, overlays.get(old_id, {}))
        rows.append({
            "Κωδικός": new_id,
            **metadata,
            "Τύπος": TYPE_MAP.get(source_type, "άγνωστος τύπος"),
            "Θέματα": normalize_topics(record.get("topics")),
            "Κατάσταση": source_status(record),
            "Επιβεβαίωση": {
                "verified-arxiv-api": "επιβεβαιωμένη μέσω arXiv",
                "verified-crossref-api": "επιβεβαιωμένη μέσω Crossref",
                "probable-openalex-match": "πιθανή αντιστοίχιση OpenAlex",
                "recorded-source-url": "μόνο καταγεγραμμένος σύνδεσμος",
            }.get(str(overlays.get(old_id, {}).get("verification_status") or ""), "εκκρεμεί"),
            "Προτεραιότητα": priority(record),
            "Σημειώσεις": "",
        })

    if OLD_EXCERPTS.exists():
        for old_excerpt in sorted(OLD_EXCERPTS.glob("*.md")):
            old_id = old_excerpt.name.split("__", 1)[0].upper()
            new_id = old_to_new.get(old_id)
            if not new_id:
                continue
            text = translate_excerpt(
                old_excerpt.read_text(encoding="utf-8", errors="replace"), old_id, new_id
            )
            (EXCERPTS / f"{new_id}.md").write_text(text, encoding="utf-8")

    write_catalog(rows)

    (CATALOG / "προς-προσθήκη.md").write_text(
        "# Επόμενες πηγές\n\n"
        "Η λίστα ενημερώνεται αυτόματα από το GitHub. Περιλαμβάνει βασικές ελλείψεις και επαναλαμβανόμενες αναφορές από τις υπάρχουσες πηγές.\n\n"
        "- [ ] [AI Safety Gridworlds](https://arxiv.org/abs/1711.09883) — benchmark ασφάλειας σε GridWorld\n"
        "- [ ] [NovGrid](https://arxiv.org/abs/2203.12117) — καινοτομία, πτώση επίδοσης και ανάκαμψη\n"
        "- [ ] [CARL](https://arxiv.org/abs/2110.02102) — μεταβολές περιβάλλοντος και προσαρμογή\n"
        "- [ ] [Deep Reinforcement Learning at the Edge of the Statistical Precipice](https://arxiv.org/abs/2108.13264) — στατιστική αξιολόγηση\n",
        encoding="utf-8",
    )

    (INCOMING / "README.md").write_text(
        "# Νέες πηγές\n\n"
        "Ανέβασε εδώ έναν οποιονδήποτε φάκελο με αρχεία Markdown, προαιρετικά PDF, "
        "και τα προσωρινά αρχεία ελέγχου του NotebookLM. Δεν απαιτείται συγκεκριμένη εσωτερική δομή.\n",
        encoding="utf-8",
    )
    (ORIGINALS / "README.md").write_text(
        "# Πρωτότυπα αρχεία\n\n"
        "Εδώ αποθηκεύονται προαιρετικά τα αρχικά PDF που αντιστοιχούν στις πηγές. "
        "Δεν χρησιμοποιούνται ως έτοιμες παραπομπές χωρίς έλεγχο.\n",
        encoding="utf-8",
    )

    remove_obsolete_paths()

    report = {
        "ενεργές_πηγές": len(rows),
        "αφαιρέθηκαν_εκτός_θέματος": removed_out_of_scope,
        "αφαιρέθηκαν_συνθέσεις_notebooklm": removed_syntheses,
        "αφαιρέθηκαν_ακριβή_διπλότυπα": removed_exact_duplicates,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
