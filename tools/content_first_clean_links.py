#!/usr/bin/env python3
"""Run link cleanup with content-first orphan deduplication.

Strong publication identifiers (DOI, arXiv, OpenReview, concrete canonical URL)
remain valid record identity. For records that have no such shared identifier,
matching title/author/year metadata is not enough: their substantive Markdown
must be exactly equivalent after normalization before the records can merge.
"""
from __future__ import annotations

import clean_links


def orphan_content_identity(
    primary: dict[str, str],
    duplicate: dict[str, str],
    texts: dict[str, str],
) -> bool:
    del primary, duplicate
    values = list(texts.values())
    # This helper is invoked through the monkey-patched base function below,
    # where the source IDs are still available. The standalone function is
    # intentionally conservative and is mainly exposed for tests/documentation.
    return len(values) == 2 and clean_links.texts_are_exact_duplicates(values[0], values[1])


def _content_only_corroboration(
    primary: dict[str, str],
    duplicate: dict[str, str],
    texts: dict[str, str],
) -> bool:
    return clean_links.texts_are_exact_duplicates(
        texts.get(primary["Κωδικός"], ""),
        texts.get(duplicate["Κωδικός"], ""),
    )


def main() -> int:
    clean_links.orphan_corroborated = _content_only_corroboration
    return clean_links.main()


if __name__ == "__main__":
    raise SystemExit(main())
