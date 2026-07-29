# AGENTS.md

## Purpose

Maintain an auditable temporary bibliography staging repository for the thesis **“Comparison and Evaluation of Resilient AI Agents in Uncertain Environments.”**

This repository collects, identifies, deduplicates, verifies and curates source material before a selected subset is transferred to `MariosGiannakaras/resilient-ai-agents-thesis`.

## Authority order

1. Original source content and official source pages.
2. DOI/Crossref, arXiv, OpenAlex and institutional repository metadata, with provider/status recorded.
3. Repository catalog and reviewed by-source notes.
4. NotebookLM group reports and extracted tables only as discovery aids.

Never invent titles, authors, dates, venues, DOI values, methods, results or source relationships.

## Required intake workflow

For every new batch:

1. Place the untouched export under `incoming/GroupN/`.
2. Inspect the group audit and extracted-reference table before processing sources.
3. Inventory every file and preserve its original path and SHA-256.
4. Move source Markdown into the flat `sources/markdown/` archive through the organizer.
5. Preserve NotebookLM helper files under `imports/notebooklm/group-NN/`.
6. Detect exact, URL and title/version duplicate candidates without deleting them.
7. Run official metadata enrichment and record the provider and confidence/status.
8. Record failed, sparse, metadata-only, noisy or unresolved files.
9. Extract reference candidates into a screening queue; do not add them automatically.
10. Generate candidate excerpts as traceable review aids, never as citation-ready evidence.
11. Run repository validation and review the Pull Request before merge.

## Naming and identity

- Source IDs are permanent after import.
- Archived Markdown uses `<source-id>__<readable-slug>.md`.
- Original paths and checksums remain in the catalog.
- Different versions remain separate until the preferred scholarly version is chosen explicitly.
- Avoid names such as `final`, `new`, `best`, `fixed2` or unexplained abbreviations.

## Metadata verification

- `verified-arxiv-api` and `verified-crossref-api` mean bibliographic metadata was returned for an explicit identifier.
- `probable-openalex-match` is a high-similarity candidate and still needs review.
- `recorded-source-url` means only that the export contained a URL.
- A verified citation record does not imply that the full text or its claims were reviewed.
- Formal citation requires checking the actual source and recording the relevant page, section, figure or table where applicable.

## Excerpts and notes

- Machine-selected excerpts are candidates only.
- Keep direct quotations short and label them explicitly.
- Separate quotation, paraphrase and interpretation.
- Verified notes belong under `notes/by-source/` and include method, setup, findings, limitations and thesis use.
- Open the original PDF only for conversion errors, figures, equations, page numbers or exact citation checks.

## Reference mining

- References found inside a source become entries in `queues/REFERENCES_TO_SCREEN.csv`.
- Citation frequency is a prioritization signal, not proof of relevance or quality.
- Check whether a candidate already exists under another version before adding it.
- Prefer peer-reviewed, official, institutional or author-provided copies.
- Do not bypass paywalls or add pirated material.

## Git and review

- Use descriptive branches and Pull Requests for corpus changes.
- Commit bodies explain what changed, why, validation and exclusions.
- Generated files must be reproducible from version-controlled scripts.
- CI validates source count, paths, IDs, hashes, imports and generated indexes.
- The user does not manage routine GitHub approval; Codex executes bounded work, GitHub runs checks and ChatGPT reviews technical readiness.
