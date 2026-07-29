# AGENTS.md

## Purpose

Maintain a temporary, auditable bibliography staging repository for the resilient-AI-agents thesis. Preserve source provenance, repair NotebookLM exports, screen references and prepare a curated subset for later transfer to the main thesis repository.

## Authority

- Source files and official metadata are evidence.
- NotebookLM reports are unverified analysis aids.
- The current thesis topic and bounded research design determine relevance.
- Never invent titles, authors, venues, DOI values, results or source relationships.

## Required workflow

For each new batch:

1. Inspect all group companion reports/tables before changing source files.
2. Inventory every file, size, hash and original path.
3. Preserve complete source Markdown byte-for-byte in `sources/raw-md/`.
4. Keep NotebookLM reports in `sources/group-reports/`, never among source documents.
5. Assign a stable source ID and collision-safe filename.
6. Verify high-priority metadata through official pages, DOI/Crossref, arXiv, OpenAlex or institutional repositories.
7. Detect exact-content, canonical-URL, title and version duplicates.
8. Record malformed, empty, sparse, noisy or provenance-missing files.
9. Tag and rank sources only as screening aids; do not silently delete low-value material.
10. Extract short candidate excerpts with source IDs and approximate source lines.
11. Mine source references into a screening queue; do not approve them automatically.
12. Run integrity tests and review the diff before merge.

## Naming

- Source IDs are permanent.
- Archived Markdown: `<source-id>__<normalized-title>.md`.
- Do not use names such as `final`, `new`, `best`, `fixed2` or unexplained abbreviations.
- Different source versions remain separate until one is selected explicitly.

## Verification

- `verified-metadata-api` means metadata came from an official scholarly API; it does not mean the paper was read.
- `probable-openalex-match` requires review.
- A recorded URL is not proof that title/authors/year are correct.
- Full-text claims, methods, results and limitations require direct source reading.
- PDF remains the fallback for page numbers, figures, equations and conversion errors.

## Excerpts and notes

- Keep excerpts short and traceable.
- Separate direct text, paraphrase and interpretation.
- Candidate excerpts are not citation-ready.
- Record relevance, methods, setup, findings and limitations in future by-source notes.

## Git and automation

- Use a descriptive branch and Pull Request for corpus migrations.
- Commit messages explain what changed, why, validation and exclusions.
- Generated catalogs must be reproducible from scripts.
- Never commit credentials or bypass lawful access restrictions.
- CI must validate catalog paths, source IDs, SHA-256, required folders and source coverage.
