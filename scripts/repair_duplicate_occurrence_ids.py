#!/usr/bin/env python3
"""Repair duplicate import IDs while preserving content-deduplicated archive paths."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CATALOG_JSON = ROOT / "catalog" / "source-catalog.json"
CATALOG_CSV = ROOT / "catalog" / "source-catalog.csv"
CATALOG_MD = ROOT / "catalog" / "source-catalog.md"
MALFORMED_MD = ROOT / "catalog" / "malformed-or-missing.md"
EXCLUSION_MD = ROOT / "catalog" / "peripheral-or-exclusion-candidates.md"
DUPLICATES_MD = ROOT / "catalog" / "duplicate-groups.md"
PATH_MAP = ROOT / "archive" / "original-path-map.csv"
TOPIC_ROOT = ROOT / "excerpts" / "by-topic"
EXCERPT_ROOT = ROOT / "excerpts" / "by-source"


def occurrence_suffix(original_path: str) -> str:
    return hashlib.sha256(original_path.encode("utf-8")).hexdigest()[:6].upper()


def normalize_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    key: "; ".join(str(item) for item in value)
                    if isinstance(value, list)
                    else value
                    for key, value in row.items()
                }
            )


def report_table(
    title: str,
    intro: str,
    rows: list[dict[str, Any]],
    columns: list[tuple[str, str]],
) -> str:
    lines = [f"# {title}", "", intro, ""]
    if not rows:
        return "\n".join(lines + ["No entries."]) + "\n"
    lines.append("| " + " | ".join(label for _key, label in columns) + " |")
    lines.append("| " + " | ".join("---" for _ in columns) + " |")
    for row in rows:
        cells: list[str] = []
        for key, _label in columns:
            value = row.get(key, "")
            if isinstance(value, list):
                value = ", ".join(str(item) for item in value)
            cells.append(str(value or "").replace("|", "\\|").replace("\n", " ")[:300])
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines) + "\n"


def main() -> int:
    payload = json.loads(CATALOG_JSON.read_text(encoding="utf-8"))
    records: list[dict[str, Any]] = payload["sources"]

    by_base_id: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        by_base_id[str(record["source_id"])].append(record)

    repairs: list[dict[str, str]] = []
    for base_id, members in by_base_id.items():
        if len(members) < 2:
            continue
        members.sort(key=lambda item: str(item.get("original_path") or ""))
        for record in members[1:]:
            new_id = f"{base_id}-{occurrence_suffix(str(record['original_path']))}"
            repairs.append(
                {
                    "old_source_id": base_id,
                    "new_source_id": new_id,
                    "original_path": str(record["original_path"]),
                    "shared_normalized_path": str(record["normalized_path"]),
                }
            )
            record["source_id"] = new_id

    ids = [str(record["source_id"]) for record in records]
    if len(ids) != len(set(ids)):
        raise RuntimeError("Occurrence-specific source IDs are still not unique")

    for record in records:
        record["duplicate_group"] = ""
    groups: dict[tuple[str, str], list[str]] = defaultdict(list)
    for record in records:
        groups[("exact-content", str(record.get("sha256") or ""))].append(str(record["source_id"]))
        if record.get("canonical_url"):
            groups[("canonical-url", str(record["canonical_url"]))].append(str(record["source_id"]))
        title_key = normalize_title(str(record.get("title") or ""))
        if title_key:
            groups[("normalized-title", title_key)].append(str(record["source_id"]))

    by_id = {str(record["source_id"]): record for record in records}
    duplicate_sets: list[tuple[str, str, list[str]]] = []
    seen: set[tuple[str, ...]] = set()
    for (mechanism, _key), members in groups.items():
        unique = sorted(set(members))
        if len(unique) < 2 or tuple(unique) in seen:
            continue
        seen.add(tuple(unique))
        group_id = f"DUP-{len(duplicate_sets) + 1:04d}"
        duplicate_sets.append((group_id, mechanism, unique))
        for source_id in unique:
            current = str(by_id[source_id].get("duplicate_group") or "")
            by_id[source_id]["duplicate_group"] = ";".join(
                item for item in (current, group_id) if item
            )

    records.sort(key=lambda item: str(item["source_id"]))
    fields = [
        "source_id", "group", "title", "authors", "year", "venue", "source_type",
        "relevance", "topics", "source_url", "canonical_url", "doi", "arxiv_id",
        "content_quality", "metadata_status", "verification_status", "duplicate_group",
        "word_count", "line_count", "sha256", "normalized_path", "original_path",
        "issues", "reference_extraction_status",
    ]
    write_csv(CATALOG_CSV, records, fields)
    CATALOG_JSON.write_text(
        json.dumps({**payload, "schema_version": 3, "sources": records}, ensure_ascii=False, indent=2)
        + "\n",
        encoding="utf-8",
    )
    write_csv(
        PATH_MAP,
        [
            {
                "source_id": record["source_id"],
                "original_path": record["original_path"],
                "normalized_path": record["normalized_path"],
                "sha256": record["sha256"],
            }
            for record in records
        ],
        ["source_id", "original_path", "normalized_path", "sha256"],
    )
    (ROOT / "catalog" / "occurrence-id-repairs.json").write_text(
        json.dumps({"repairs": repairs}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    CATALOG_MD.write_text(
        report_table(
            "Source Catalog",
            "The authoritative working index. Multiple import occurrences may point to one archive file only when their bytes are identical.",
            records,
            [
                ("source_id", "ID"), ("title", "Title"), ("authors", "Authors"),
                ("year", "Year"), ("venue", "Venue"), ("source_type", "Type"),
                ("relevance", "Relevance"), ("topics", "Tags"),
                ("canonical_url", "Link"), ("verification_status", "Verification"),
            ],
        ),
        encoding="utf-8",
    )
    malformed = [record for record in records if record.get("issues")]
    MALFORMED_MD.write_text(
        report_table(
            "Malformed or Missing Source Data",
            "Entries remain archived until repaired or explicitly excluded.",
            malformed,
            [
                ("source_id", "ID"), ("title", "Title"), ("issues", "Problems"),
                ("normalized_path", "File"), ("source_url", "Recorded source"),
            ],
        ),
        encoding="utf-8",
    )
    excluded = [
        record for record in records
        if record.get("relevance") in {"peripheral", "exclude-candidate"}
    ]
    EXCLUSION_MD.write_text(
        report_table(
            "Peripheral or Exclusion Candidates",
            "Automated labels are screening aids and do not delete archived material.",
            excluded,
            [
                ("source_id", "ID"), ("title", "Title"),
                ("relevance", "Status"), ("issues", "Reason"),
                ("source_type", "Type"),
            ],
        ),
        encoding="utf-8",
    )

    lines = [
        "# Duplicate Groups", "",
        "Each uploaded occurrence has a unique source ID. Identical bytes may share one archived Markdown path while preserving every original path in the catalog.", "",
    ]
    for group_id, mechanism, members in duplicate_sets:
        lines.extend([f"## {group_id} — {mechanism}", ""])
        for source_id in members:
            record = by_id[source_id]
            lines.append(
                f"- `{source_id}` — {record['title']} — original: `{record['original_path']}` — archive: `{record['normalized_path']}`"
            )
        lines.append("")
    DUPLICATES_MD.write_text("\n".join(lines), encoding="utf-8")

    for path in TOPIC_ROOT.glob("*.md"):
        path.unlink()
    topic_records: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        for topic in record.get("topics") or ["uncategorized"]:
            topic_records[str(topic)].append(record)
    for topic, members in sorted(topic_records.items()):
        lines = [
            f"# Topic Index — {topic}", "",
            "Automatic screening index; verify taxonomy and relevance before thesis use.", "",
        ]
        for record in sorted(members, key=lambda item: str(item["source_id"])):
            excerpt = EXCERPT_ROOT / f"{str(record['source_id']).split('-')[0].lower()}__candidate-excerpts.md"
            extra = f"; excerpts: `../by-source/{excerpt.name}`" if excerpt.exists() else ""
            lines.append(
                f"- `{record['source_id']}` — {record['title']} — raw: `../../{record['normalized_path']}`{extra}"
            )
        (TOPIC_ROOT / f"{topic}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (TOPIC_ROOT / "README.md").write_text(
        "# By-topic Excerpt Indexes\n\nGenerated source and candidate-excerpt links.\n",
        encoding="utf-8",
    )

    print(json.dumps({"repaired_occurrences": len(repairs), "sources": len(records), "duplicate_groups": len(duplicate_sets)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
