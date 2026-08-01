#!/usr/bin/env python3
"""Audit citation-ready evidence for source-language preservation.

This tool deliberately does not translate or rewrite evidence. It detects the main
Greek-vs-Latin mismatch that can arise when English/Latin-source material was
paraphrased in Greek, or vice versa. Mixed/bilingual sources are reported for
manual review rather than failed automatically.
"""
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def first_existing(*candidates: str) -> Path:
    for candidate in candidates:
        path = ROOT / candidate
        if path.exists():
            return path
    return ROOT / candidates[-1]


CATALOG_DIR = first_existing("catalog", "κατάλογος")
SOURCES_DIR = first_existing("sources", "πηγές")
EVIDENCE_DIR = first_existing("evidence", "αποσπάσματα")
SELECTION = (
    CATALOG_DIR / "thesis-selection.csv"
    if (CATALOG_DIR / "thesis-selection.csv").exists()
    else CATALOG_DIR / "επιλογή-διπλωματικής.csv"
)
REPORT = CATALOG_DIR / "language-audit.md"

YES_VALUES = {"ναι", "yes", "true", "1"}


def normalize(value: str | None) -> str:
    return (value or "").strip().casefold()


def strip_frontmatter(text: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            return text[end + 4 :]
    return text


def scientific_prose(text: str) -> str:
    text = strip_frontmatter(text)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    kept: list[str] = []
    structural_prefixes = (
        "type:", "location:", "claim:", "thesis use:", "topics:", "status:",
        "τύπος:", "θέση:", "ισχυρισμός:", "κεφάλαιο:", "θέματα:", "κατάσταση:",
        "προτεινόμενη χρήση", "περιορισμοί και κίνδυνος", "συμφραζόμενα",
        "safe use", "avoid overclaiming", "context and limitation",
    )
    for raw in text.splitlines():
        line = raw.strip().lstrip("- ").strip("* ").casefold()
        if not line:
            continue
        if any(line.startswith(prefix) for prefix in structural_prefixes):
            continue
        if raw.lstrip().startswith("#"):
            continue
        kept.append(raw)
    return "\n".join(kept)


def script_stats(text: str) -> tuple[int, int, float]:
    prose = scientific_prose(text)
    greek = len(re.findall(r"[Α-Ωα-ωΆΈΉΊΌΎΏάέήίόύώϊΐϋΰ]", prose))
    latin = len(re.findall(r"[A-Za-z]", prose))
    total = greek + latin
    fraction = greek / total if total else 0.0
    return greek, latin, fraction


def classify(text: str) -> tuple[str, float, int]:
    greek, latin, fraction = script_stats(text)
    total = greek + latin
    if total < 120:
        return "unknown", fraction, total
    if fraction >= 0.45:
        return "greek", fraction, total
    if fraction <= 0.05:
        return "latin", fraction, total
    return "mixed", fraction, total


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def field(row: dict[str, str], *keys: str) -> str:
    for key in keys:
        if key in row:
            return (row.get(key) or "").strip()
    return ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--enforce", action="store_true", help="return non-zero on definite language mismatch")
    args = parser.parse_args()

    if not SELECTION.exists():
        raise SystemExit(f"Missing selection registry: {SELECTION.relative_to(ROOT)}")

    rows = read_rows(SELECTION)
    exported = [
        row for row in rows
        if normalize(field(row, "Εξαγωγή", "Export")) in YES_VALUES
    ]

    violations: list[tuple[str, str, float, str, float]] = []
    reviews: list[tuple[str, str, float, str, float]] = []
    missing: list[str] = []
    compliant = 0

    for row in exported:
        source_id = field(row, "Κωδικός", "Source ID", "source_id")
        source_path = SOURCES_DIR / f"{source_id}.md"
        evidence_path = EVIDENCE_DIR / f"{source_id}.md"
        if not source_path.exists() or not evidence_path.exists():
            missing.append(source_id)
            continue
        source_text = source_path.read_text(encoding="utf-8", errors="replace")
        evidence_text = evidence_path.read_text(encoding="utf-8", errors="replace")
        source_lang, source_fraction, _ = classify(source_text)
        evidence_lang, evidence_fraction, _ = classify(evidence_text)

        definite = (
            source_lang == "latin" and evidence_lang == "greek"
        ) or (
            source_lang == "greek" and evidence_lang == "latin"
        )
        if definite:
            violations.append((source_id, source_lang, source_fraction, evidence_lang, evidence_fraction))
        elif source_lang in {"mixed", "unknown"} or evidence_lang in {"mixed", "unknown"}:
            reviews.append((source_id, source_lang, source_fraction, evidence_lang, evidence_fraction))
        else:
            compliant += 1

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Source-language audit",
        "",
        "This report checks selected/exported citation-ready evidence for a clear Greek-vs-Latin script mismatch.",
        "It does **not** translate content. Mixed/bilingual/short sources are sent to manual review.",
        "",
        f"- Exported sources checked: **{len(exported)}**",
        f"- Definite cross-language violations: **{len(violations)}**",
        f"- Manual-review cases: **{len(reviews)}**",
        f"- Script-compatible cases: **{compliant}**",
        f"- Missing source/evidence files: **{len(missing)}**",
        "",
    ]
    if violations:
        lines += [
            "## Definite violations",
            "",
            "These files must be re-authored against the original source; automatic translation is not an accepted fix.",
            "",
            "| Source | Source script | Source Greek ratio | Evidence script | Evidence Greek ratio |",
            "|---|---|---:|---|---:|",
        ]
        for source_id, source_lang, sf, evidence_lang, ef in violations:
            lines.append(f"| `{source_id}` | {source_lang} | {sf:.3f} | {evidence_lang} | {ef:.3f} |")
        lines.append("")
    if reviews:
        lines += [
            "## Manual review",
            "",
            "| Source | Source script | Source Greek ratio | Evidence script | Evidence Greek ratio |",
            "|---|---|---:|---|---:|",
        ]
        for source_id, source_lang, sf, evidence_lang, ef in reviews:
            lines.append(f"| `{source_id}` | {source_lang} | {sf:.3f} | {evidence_lang} | {ef:.3f} |")
        lines.append("")
    if missing:
        lines += ["## Missing files", ""] + [f"- `{source_id}`" for source_id in missing] + [""]

    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Language audit: exported={len(exported)} violations={len(violations)} review={len(reviews)} missing={len(missing)}")

    if args.enforce and (violations or missing):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
