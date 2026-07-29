#!/usr/bin/env python3
"""Create a complete, read-only inventory of the temporary bibliography corpus."""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "workspace"
GROUP_RE = re.compile(r"^Group(?P<group>\d+)$", re.IGNORECASE)
SOURCE_DIR_RE = re.compile(r"^Group(?P<group>\d+)Files$", re.IGNORECASE)
IGNORED_TOP_LEVEL = {".git", ".github", "scripts", "workspace"}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def text_stats(path: Path) -> tuple[int | None, int | None]:
    if path.suffix.lower() not in {".md", ".csv", ".txt", ".json", ".yaml", ".yml"}:
        return None, None
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None, None
    return len(text.splitlines()), len(text.split())


def classify(path: Path) -> tuple[str, str | None]:
    parts = path.relative_to(ROOT).parts
    if not parts:
        return "other", None
    group_match = GROUP_RE.match(parts[0])
    if not group_match:
        return "other", None
    group = f"Group{int(group_match.group('group'))}"
    if len(parts) >= 3 and SOURCE_DIR_RE.match(parts[1]):
        return "source", group
    return "group_companion", group


def main() -> int:
    records: list[dict[str, object]] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        if relative.parts[0] in IGNORED_TOP_LEVEL:
            continue
        kind, group = classify(path)
        lines, words = text_stats(path)
        records.append(
            {
                "path": relative.as_posix(),
                "kind": kind,
                "group": group,
                "extension": path.suffix.lower(),
                "bytes": path.stat().st_size,
                "lines": lines,
                "words": words,
                "sha256": sha256(path),
            }
        )

    groups: dict[str, dict[str, object]] = {}
    for record in records:
        group = record["group"]
        if not group:
            continue
        summary = groups.setdefault(str(group), {"source_count": 0, "companion_files": []})
        if record["kind"] == "source":
            summary["source_count"] = int(summary["source_count"]) + 1
        elif record["kind"] == "group_companion":
            summary["companion_files"].append(record["path"])

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": 1,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "total_files": len(records),
        "total_sources": sum(1 for item in records if item["kind"] == "source"),
        "groups": groups,
        "files": records,
    }
    (OUTPUT_DIR / "repository-inventory.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    lines = [
        "# Group Companion Files",
        "",
        "Generated before normalization. These files are NotebookLM reports or tables, not source documents.",
        "",
    ]
    for group in sorted(groups, key=lambda value: int(value.removeprefix("Group"))):
        summary = groups[group]
        lines.extend([f"## {group}", "", f"Source files: **{summary['source_count']}**", ""])
        companions = list(summary["companion_files"])
        if companions:
            lines.extend(f"- `{path}`" for path in companions)
        else:
            lines.append("- No companion files detected.")
        lines.append("")
    (OUTPUT_DIR / "group-companion-files.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Inventoried {len(records)} files and {payload['total_sources']} source files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
