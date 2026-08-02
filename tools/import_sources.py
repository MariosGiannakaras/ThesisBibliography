#!/usr/bin/env python3
"""Εισάγει πηγές από οποιαδήποτε δομή φακέλων κάτω από `new-sources/`."""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import secrets
import shutil
import unicodedata
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
INCOMING = ROOT / "new-sources"
SOURCES = ROOT / "sources"
ORIGINALS = ROOT / "originals"
CATALOG = ROOT / "catalog"
CATALOG_CSV = CATALOG / "sources.csv"

FIELDS = [
    "Κωδικός", "Τίτλος", "Συγγραφείς", "Έτος", "Σύνδεσμος",
    "Τύπος", "Θέματα", "Κατάσταση", "Επιβεβαίωση", "Προτεραιότητα", "Σημειώσεις",
]

TRACKING_PARAMS = {
    "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
    "fbclid", "gclid", "mc_cid", "mc_eid",
}

HELPER_NAME = re.compile(
    r"(?:audit|report|summary|source[-_ ]?list|reference[-_ ]?list|duplicates?|"
    r"έλεγχ|αναφορ|σύνοψη|λίστα[-_ ]?πηγ|βιβλιογραφ)",
    re.IGNORECASE,
)
HELPER_CONTENT = re.compile(
    r"(?:NotebookLM|διπλότυπ|προτεινόμεν(?:ες|η) πηγ|Source Name|Author\(s\)|"
    r"Πηγές προς προσθήκη|προτάσεις αφαίρεσης)",
    re.IGNORECASE,
)
SOURCE_MARKER = re.compile(r"^>\s*Source:\s*(\S+)", re.MULTILINE | re.IGNORECASE)
YEAR_RE = re.compile(r"\b(19\d{2}|20[0-3]\d)\b")
URL_RE = re.compile(r"https?://[^\s)>\]]+")

TOPIC_RULES = {
    "εύρωστη ενισχυτική μάθηση": ["robust reinforcement", "robust mdp", "distributionally robust", "ambiguity set"],
    "ανθεκτικότητα και ανάκαμψη": ["resilien", "recovery time", "adaptation speed", "performance degradation"],
    "μη στασιμότητα": ["non-station", "nonstation", "concept drift", "change-point", "sudden change"],
    "GridWorld": ["gridworld", "grid world", "frozenlake", "cliffwalking", "minigrid", "novgrid"],
    "ασφαλής ενισχυτική μάθηση": ["safe reinforcement", "safety grid", "constrained mdp", "safe exploration"],
    "αβεβαιότητα μεταβάσεων": ["transition uncertainty", "transition perturb", "uncertain transition"],
    "αβεβαιότητα ενεργειών": ["action robust", "action perturb", "action failure"],
    "αβεβαιότητα παρατηρήσεων": ["observation perturb", "state perturb", "adversarial state"],
    "αβεβαιότητα ανταμοιβής": ["reward uncertainty", "reward robust", "reward hacking"],
    "μερική παρατηρησιμότητα": ["pomdp", "partially observable", "belief state"],
    "πινακοποιημένη ενισχυτική μάθηση": ["q-learning", "q learning", "sarsa", "value iteration", "policy iteration"],
    "βαθιά ενισχυτική μάθηση": ["deep reinforcement", " dqn ", " ppo ", "actor-critic", "actor critic"],
    "ενισχυτική μάθηση με μοντέλο": ["model-based reinforcement", "model based reinforcement", "dyna-q", "dyna q"],
    "συνεχής προσαρμογή": ["continual reinforcement", "lifelong reinforcement", "catastrophic forgetting", "meta-reinforcement"],
    "στατιστική αξιολόγηση": ["confidence interval", "effect size", "statistical", "rliable", "multiple seeds"],
    "περιβάλλοντα και benchmarks": ["benchmark", "gymnasium", "minigrid", "robust gymnasium", "mdp playground"],
    "πράκτορες τεχνητής νοημοσύνης": ["ai agent", "agentic ai", "intelligent agent", "multi-agent"],
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def new_source_id(existing: set[str]) -> str:
    while True:
        candidate = f"SRC-{secrets.token_hex(5).upper()}"
        if candidate not in existing:
            return candidate


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def slug_key(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).casefold()
    return "".join(ch for ch in normalized if ch.isalnum())


def association_key(path: Path) -> tuple[str, str]:
    relative = path.relative_to(INCOMING)
    return relative.parent.as_posix().casefold(), slug_key(path.stem)


def canonical_url(url: str) -> str:
    url = url.strip().rstrip(".,;:)")
    if not url:
        return ""
    try:
        parts = urlsplit(url)
    except ValueError:
        return url
    query = [
        (key, value) for key, value in parse_qsl(parts.query, keep_blank_values=True)
        if key.lower() not in TRACKING_PARAMS
    ]
    host = parts.netloc.lower().removeprefix("www.")
    path = re.sub(r"/+", "/", parts.path)
    if host == "arxiv.org":
        match = re.search(r"/(?:abs|pdf|html)/(\d{4}\.\d+)(?:v\d+)?", path)
        if match:
            return f"https://arxiv.org/abs/{match.group(1)}"
    return urlunsplit((parts.scheme.lower() or "https", host, path, urlencode(query), ""))


def is_helper_markdown(path: Path, text: str) -> bool:
    return bool(HELPER_NAME.search(path.stem) and HELPER_CONTENT.search(text[:12000]))


def extract_title(path: Path, text: str) -> str:
    for line in text.splitlines()[:120]:
        if line.startswith("# "):
            candidate = clean(line[2:])
            if len(candidate) >= 5:
                return candidate
    value = re.sub(r"^\d+[-_ ]+", "", path.stem).replace("_", " ")
    return clean(value) or "Χωρίς τίτλο"


def extract_url(text: str) -> str:
    marker = SOURCE_MARKER.search(text)
    if marker:
        return canonical_url(marker.group(1))
    head = "\n".join(text.splitlines()[:80])
    arxiv = re.search(r"https?://(?:www\.)?arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d+)(?:v\d+)?", head)
    if arxiv:
        return f"https://arxiv.org/abs/{arxiv.group(1)}"
    doi = re.search(r"https?://(?:dx\.)?doi\.org/10\.\d{4,9}/[^\s)>\]]+", head, re.IGNORECASE)
    if doi:
        return canonical_url(doi.group(0))
    first = URL_RE.search(head)
    return canonical_url(first.group(0)) if first else ""


def extract_authors(text: str) -> str:
    for line in text.splitlines()[:80]:
        match = re.match(r"(?:Authors?|Συγγραφείς?)\s*:\s*(.+)", line.strip(), re.IGNORECASE)
        if match:
            return clean(match.group(1))
    return ""


def extract_year(title: str, text: str) -> str:
    for sample in (title, "\n".join(text.splitlines()[:60])):
        match = YEAR_RE.search(sample)
        if match:
            return match.group(1)
    return ""


def source_type(title: str, url: str, text: str) -> str:
    lower = f"{title} {url}".lower()
    domain = urlsplit(url).netloc.lower() if url else ""
    if "youtube.com" in domain or "youtu.be" in domain or "youtube" in lower:
        return "βίντεο ή διάλεξη"
    if "github.com" in domain:
        return "αποθετήριο κώδικα"
    if any(term in lower for term in ("phd thesis", "doctoral thesis", "dissertation", "master thesis", "διπλωματικ")):
        return "διπλωματική ή διατριβή"
    if any(term in lower for term in ("book", "handbook", "textbook", "chapter")):
        return "βιβλίο ή κεφάλαιο"
    if any(term in lower for term in ("standard", "white paper", "whitepaper", "technical report")):
        return "θεσμική ή τεχνική αναφορά"
    if any(host in domain for host in (
        "arxiv.org", "openreview.net", "proceedings.mlr.press", "ieeexplore.ieee.org",
        "acm.org", "springer.com", "sciencedirect.com", "mdpi.com", "aaai.org",
    )):
        return "ακαδημαϊκή εργασία"
    opening = text[:5000].lower()
    if len(text) > 10000 and "abstract" in opening and "references" in text.lower():
        return "ακαδημαϊκή εργασία"
    if any(term in lower for term in ("documentation", "tutorial", "course", "lecture", "seminar")):
        return "τεκμηρίωση ή εκπαιδευτικό υλικό"
    if url:
        return "ιστοσελίδα"
    return "άγνωστος τύπος"


def topics(title: str, text: str) -> str:
    haystack = f" {title} {' '.join(text.splitlines()[:100])} ".lower()
    result = []
    for label, terms in TOPIC_RULES.items():
        if any(term in haystack for term in terms):
            result.append(label)
    return "; ".join(result or ["χωρίς κατηγορία"])


def content_status(text: str) -> str:
    stripped = text.strip()
    if "Failed to load source content" in stripped or stripped.startswith("> Error:"):
        return "αποτυχημένη εισαγωγή"
    words = len(re.findall(r"\b\w+\b", stripped, flags=re.UNICODE))
    if len(stripped) < 200 or words < 40:
        return "μόνο μεταδεδομένα"
    if len(stripped) < 2000 or words < 300:
        return "ελλιπές κείμενο"
    return "διαθέσιμο πλήρες κείμενο"


def priority(status: str, kind: str, topic_text: str) -> str:
    if status in {"αποτυχημένη εισαγωγή", "μόνο μεταδεδομένα", "ελλιπές κείμενο"}:
        return "χρειάζεται διόρθωση"
    core = {"εύρωστη ενισχυτική μάθηση", "ανθεκτικότητα και ανάκαμψη", "μη στασιμότητα", "GridWorld", "στατιστική αξιολόγηση"}
    selected = set(topic_text.split("; "))
    if kind in {"ακαδημαϊκή εργασία", "διπλωματική ή διατριβή"} and selected & core:
        return "υψηλή"
    if selected & core:
        return "μεσαία"
    return "χαμηλή"


def load_catalog() -> list[dict[str, str]]:
    if not CATALOG_CSV.exists():
        return []
    with CATALOG_CSV.open(encoding="utf-8", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def markdown_escape(value: str) -> str:
    return (value or "").replace("|", "\\|").replace("\n", " ")


def write_catalog(rows: list[dict[str, str]]) -> None:
    CATALOG.mkdir(parents=True, exist_ok=True)
    rows = sorted(rows, key=lambda row: row["Τίτλος"].casefold())
    with CATALOG_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    counts = Counter(row["Προτεραιότητα"] for row in rows)
    lines = [
        "# Κατάλογος πηγών", "",
        f"Συνολικές πηγές: **{len(rows)}** — υψηλή προτεραιότητα: **{counts['υψηλή']}**, "
        f"μεσαία: **{counts['μεσαία']}**, χρειάζονται διόρθωση: **{counts['χρειάζεται διόρθωση']}**.",
        "",
        "> Η καταχώριση δεν σημαίνει ότι η πηγή έχει εγκριθεί για χρήση στη διπλωματική.",
        "",
        "| Κωδικός | Τίτλος | Συγγραφείς | Έτος | Τύπος | Θέματα | Κατάσταση | Επιβεβαίωση | Προτεραιότητα |",
        "|---|---|---|---:|---|---|---|---|---|",
    ]
    rank = {"υψηλή": 0, "μεσαία": 1, "χρειάζεται διόρθωση": 2, "χαμηλή": 3}
    for row in sorted(rows, key=lambda item: (rank.get(item["Προτεραιότητα"], 9), item["Τίτλος"].casefold())):
        title = markdown_escape(row["Τίτλος"])
        if row["Σύνδεσμος"]:
            title = f"[{title}]({row['Σύνδεσμος']})"
        lines.append(
            f"| `{row['Κωδικός']}` | {title} | {markdown_escape(row['Συγγραφείς'] or '—')} | "
            f"{row['Έτος'] or '—'} | {markdown_escape(row['Τύπος'])} | {markdown_escape(row['Θέματα'])} | "
            f"{markdown_escape(row['Κατάσταση'])} | {markdown_escape(row['Επιβεβαίωση'])} | "
            f"{markdown_escape(row['Προτεραιότητα'])} |"
        )
    (CATALOG / "sources.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    bad = [
        row for row in rows
        if row["Κατάσταση"] != "διαθέσιμο πλήρες κείμενο"
        or not row["Σύνδεσμος"]
        or row["Τύπος"] == "άγνωστος τύπος"
        or (row["Τύπος"] in {"ακαδημαϊκή εργασία", "διπλωματική ή διατριβή"} and row["Επιβεβαίωση"] in {"εκκρεμεί", "δεν βρέθηκε αυτόματη αντιστοίχιση"})
    ]
    problem_lines = [
        "# Πηγές που χρειάζονται διόρθωση", "",
        "| Κωδικός | Τίτλος | Τι λείπει |", "|---|---|---|",
    ]
    for row in bad:
        problems = []
        if row["Κατάσταση"] != "διαθέσιμο πλήρες κείμενο":
            problems.append(row["Κατάσταση"])
        if not row["Σύνδεσμος"]:
            problems.append("σύνδεσμος")
        if row["Τύπος"] == "άγνωστος τύπος":
            problems.append("τύπος πηγής")
        if row["Τύπος"] in {"ακαδημαϊκή εργασία", "διπλωματική ή διατριβή"} and row["Επιβεβαίωση"] in {"εκκρεμεί", "δεν βρέθηκε αυτόματη αντιστοίχιση"}:
            problems.append("επιβεβαίωση μεταδεδομένων")
        problem_lines.append(
            f"| `{row['Κωδικός']}` | {markdown_escape(row['Τίτλος'])} | {', '.join(dict.fromkeys(problems))} |"
        )
    if not bad:
        problem_lines.append("| — | Δεν υπάρχουν προβληματικές πηγές | — |")
    (CATALOG / "problematic-sources.md").write_text("\n".join(problem_lines) + "\n", encoding="utf-8")


def clear_incoming() -> None:
    for path in sorted(INCOMING.iterdir(), reverse=True):
        if path.name == "README.md":
            continue
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--μόνο-κατάλογος", "--catalog-only", action="store_true")
    args = parser.parse_args()

    SOURCES.mkdir(parents=True, exist_ok=True)
    ORIGINALS.mkdir(parents=True, exist_ok=True)
    INCOMING.mkdir(parents=True, exist_ok=True)

    rows = load_catalog()
    if args.μόνο_κατάλογος:
        write_catalog(rows)
        print("Ο κατάλογος ανανεώθηκε χωρίς εισαγωγή αρχείων.")
        return 0

    files = [path for path in INCOMING.rglob("*") if path.is_file() and path.name != "README.md"]
    if not files:
        write_catalog(rows)
        print("Δεν βρέθηκαν νέες πηγές. Ο κατάλογος ανανεώθηκε.")
        return 0

    unsupported = [path for path in files if path.suffix.lower() not in {".md", ".pdf", ".csv", ".txt", ".json"}]
    if unsupported:
        names = ", ".join(str(path.relative_to(INCOMING)) for path in unsupported[:10])
        raise RuntimeError(f"Μη υποστηριζόμενα αρχεία: {names}")

    existing_ids = {row["Κωδικός"] for row in rows}
    existing_hashes = {sha256(path) for path in SOURCES.glob("*.md")}
    markdown_to_id: dict[tuple[str, str], str] = {}
    imported = 0
    skipped_duplicates = 0
    ignored_helpers = 0

    for path in sorted(path for path in files if path.suffix.lower() == ".md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        if is_helper_markdown(path, text):
            ignored_helpers += 1
            continue
        content_hash = sha256(path)
        if content_hash in existing_hashes:
            skipped_duplicates += 1
            continue
        sid = new_source_id(existing_ids)
        title = extract_title(path, text)
        link = extract_url(text)
        kind = source_type(title, link, text)
        topic_text = topics(title, text)
        status = content_status(text)
        target = SOURCES / f"{sid}.md"
        shutil.copy2(path, target)
        rows.append({
            "Κωδικός": sid,
            "Τίτλος": title,
            "Συγγραφείς": extract_authors(text),
            "Έτος": extract_year(title, text),
            "Σύνδεσμος": link,
            "Τύπος": kind,
            "Θέματα": topic_text,
            "Κατάσταση": status,
            "Επιβεβαίωση": "μόνο καταγεγραμμένος σύνδεσμος" if link else "εκκρεμεί",
            "Προτεραιότητα": priority(status, kind, topic_text),
            "Σημειώσεις": "",
        })
        existing_hashes.add(content_hash)
        existing_ids.add(sid)
        markdown_to_id[association_key(path)] = sid
        imported += 1

    for path in sorted(path for path in files if path.suffix.lower() == ".pdf"):
        content_hash = sha256(path)
        matched = markdown_to_id.get(association_key(path))
        name = f"{matched}.pdf" if matched else f"PDF-{content_hash[:10].upper()}.pdf"
        target = ORIGINALS / name
        if target.exists() and sha256(target) != content_hash:
            target = ORIGINALS / f"{target.stem}-{content_hash[:8].upper()}.pdf"
        if not target.exists():
            shutil.copy2(path, target)

    ignored_helpers += sum(1 for path in files if path.suffix.lower() in {".csv", ".txt", ".json"})
    write_catalog(rows)
    clear_incoming()

    print(f"Νέες πηγές: {imported}")
    print(f"Ακριβή διπλότυπα που αγνοήθηκαν: {skipped_duplicates}")
    print(f"Προσωρινά αρχεία ελέγχου που αγνοήθηκαν: {ignored_helpers}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
