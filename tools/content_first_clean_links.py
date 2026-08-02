#!/usr/bin/env python3
"""Run link cleanup without deleting distinct source content.

Filenames and bibliographic metadata are useful for matching, but destructive
record deduplication requires source-content identity. DOI, arXiv, OpenReview,
and concrete canonical URLs may link records to the same publication; they do
not prove that two Markdown payloads are the same file/version/chapter/export.
"""
from __future__ import annotations

from collections import defaultdict

import clean_links


def exact_markdown_content(left: str, right: str) -> bool:
    """Return True only for the same non-empty decoded Markdown content."""
    return bool(left) and left == right


def _content_only_corroboration(
    primary: dict[str, str],
    duplicate: dict[str, str],
    texts: dict[str, str],
) -> bool:
    return exact_markdown_content(
        texts.get(primary["Κωδικός"], ""),
        texts.get(duplicate["Κωδικός"], ""),
    )


def _merge_strong_identities_content_first(
    rows: list[dict[str, str]],
    texts: dict[str, str],
    changes: list[str],
    merged: list[tuple[str, str, str]],
) -> list[dict[str, str]]:
    """Merge shared-identifier records only when their Markdown is identical.

    A shared DOI/arXiv/OpenReview/concrete URL remains evidence that records
    refer to the same publication, but distinct Markdown payloads are retained
    as distinct records so chapters, versions, exports, and bad wrappers cannot
    erase each other. The loop merges at most one proven-identical pair per
    pass, then rebuilds the identity index.
    """
    while True:
        index: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in rows:
            source_id = row["Κωδικός"]
            for key in clean_links.identities(
                row.get("Σύνδεσμος", ""),
                row.get("Τίτλος", ""),
                texts.get(source_id, ""),
            ):
                index[key].append(row)

        candidate: tuple[str, dict[str, str], dict[str, str]] | None = None
        for key, values in index.items():
            unique = {item["Κωδικός"]: item for item in values}
            ordered = sorted(
                unique.values(),
                key=lambda item: clean_links.source_score(
                    item, texts.get(item["Κωδικός"], "")
                ),
                reverse=True,
            )
            for position, primary in enumerate(ordered):
                for duplicate in ordered[position + 1 :]:
                    if _content_only_corroboration(primary, duplicate, texts):
                        candidate = (key, primary, duplicate)
                        break
                if candidate:
                    break
            if candidate:
                break

        if candidate is None:
            return rows

        key, primary, duplicate = candidate
        rows = clean_links.merge_one(
            rows,
            texts,
            primary,
            duplicate,
            f"content-identical+{key}",
            changes,
            merged,
        )


def main() -> int:
    clean_links.orphan_corroborated = _content_only_corroboration
    clean_links.merge_strong_identities = _merge_strong_identities_content_first
    return clean_links.main()


if __name__ == "__main__":
    raise SystemExit(main())
