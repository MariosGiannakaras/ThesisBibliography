# Structured original files

This directory archives original non-PDF textual/structured payloads that were uploaded for bibliography or research intake.

Examples include JATS XML, TXT, CSV, and JSON. Files are stored byte-for-byte with content-derived ASCII-safe names. `index.csv` records the original intake path, SHA-256 identity, media type, and any derived canonical Markdown or research-note path.

Archival originals are not citation-ready by themselves and are not copied into the thesis repository. Their useful textual content is exposed through canonical `sources/` Markdown or `research-notes/`, which is included in the complete `research-corpus/`.

An archival original may be de-duplicated only when its complete byte content is identical (same SHA-256). Filename similarity or metadata similarity is never sufficient for destructive de-duplication.
