#!/usr/bin/env python3
"""Run canonical Markdown intake with deterministic source IDs.

`import_sources.py` historically generated new SRC IDs randomly. That is harmless
for a single successful run but makes retries of the same pending intake diverge.
The canonical workflow uses this wrapper so the source content SHA-256 determines
the candidate ID. Existing exact-content duplicates are still skipped before an
ID is allocated. If a 40-bit prefix is already occupied by an unrelated source,
subsequent digest windows are tried deterministically.
"""
from __future__ import annotations

from pathlib import Path

import import_sources

_CURRENT_INCOMING_HASH: str | None = None
_ORIGINAL_SHA256 = import_sources.sha256


def deterministic_source_id(existing: set[str], content_hash: str) -> str:
    digest = content_hash.upper()
    if len(digest) < 10 or any(ch not in "0123456789ABCDEF" for ch in digest):
        raise ValueError("content_hash must be a hexadecimal SHA-256 digest")
    for offset in range(0, len(digest) - 9):
        candidate = f"SRC-{digest[offset:offset + 10]}"
        if candidate not in existing:
            return candidate
    raise RuntimeError("no deterministic SRC identifier available from content hash")


def tracking_sha256(path: Path) -> str:
    global _CURRENT_INCOMING_HASH
    digest = _ORIGINAL_SHA256(path)
    try:
        is_incoming_markdown = (
            path.suffix.casefold() == ".md"
            and path.resolve().is_relative_to(import_sources.INCOMING.resolve())
        )
    except (OSError, ValueError):
        is_incoming_markdown = False
    if is_incoming_markdown:
        _CURRENT_INCOMING_HASH = digest
    return digest


def deterministic_new_source_id(existing: set[str]) -> str:
    if not _CURRENT_INCOMING_HASH:
        raise RuntimeError("incoming Markdown hash was not captured before ID allocation")
    return deterministic_source_id(existing, _CURRENT_INCOMING_HASH)


def main() -> int:
    import_sources.sha256 = tracking_sha256
    import_sources.new_source_id = deterministic_new_source_id
    return import_sources.main()


if __name__ == "__main__":
    raise SystemExit(main())
