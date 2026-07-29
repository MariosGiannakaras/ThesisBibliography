# Catalog Schema

`SOURCE_CATALOG.csv` and `source_catalog.json` contain one record for every file in `sources/markdown/`. They are inventories and triage aids, not a final approved bibliography.

## Identity and provenance

- `source_id` — stable repository identifier in the form `SRC-XXXXXXXXXX`.
- `original_group` — NotebookLM group from which the file was imported.
- `original_path` — path before normalization.
- `normalized_path` — current flat archive path.
- `content_sha256` — checksum of the preserved Markdown bytes.

## Bibliographic metadata

- `title`, `authors`, `year`, `url`, `domain` — extracted or matched metadata.
- `metadata_confidence` — confidence in the automated match, not source quality.
- `source_type` — paper, thesis, repository, video, web article, institutional report, educational material, unknown, or non-citable NotebookLM synthesis.
- `language` — detected source language.

Metadata must be verified before formal citation. The NotebookLM reference CSVs include references cited inside documents and therefore cannot be treated as authoritative source lists.

## Content state

- `full-text` — substantial content is present; completeness still requires verification.
- `partial` — some content is present but may be incomplete.
- `metadata-only` — little more than title/link/transcript metadata is available.
- `failed-load` — NotebookLM did not retrieve usable content.

## Research triage

- `relevance` — automated relation to the current thesis direction.
- `quality` — rough source-quality signal based on type and provenance.
- `priority` — initial queue from `P1-core` to `P5-archive-only`.
- `topics` — overlapping content tags; they are not folder locations.
- `curation_status` — proposed next action, such as candidate core, background only, recover, duplicate candidate, archive only, or non-citable context.
- `review_status` — manual full-text review state. Initial value is `not-reviewed`.

These fields may change after the research question, models, uncertainty taxonomy and experimental protocol are finalized.

## Duplicate handling

- `duplicate_type` describes the detected relation.
- `duplicate_of` points to the preferred record for review.

No duplicate is deleted automatically. Same-title and same-URL matches remain review candidates until the actual versions and content are checked.

## Citation rule

A record is safe to cite only after:

1. bibliographic metadata is verified against the official source;
2. the relevant claim is checked in the full text;
3. page, section, figure or table location is recorded where applicable;
4. `review_status` is updated;
5. the source is not a NotebookLM synthesis, failed load, or unresolved metadata-only record.
