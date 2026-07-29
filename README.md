# ThesisBibliography

Temporary staging repository for literature collected through Gemini NotebookLM for the thesis **“Comparison and Evaluation of Resilient AI Agents in Uncertain Environments.”**

## Current organization

- `sources/markdown/` — all 363 uploaded source Markdown files in one flat archive;
- `catalog/SOURCE_CATALOG.md` — readable master index;
- `catalog/SOURCE_CATALOG.csv` and `catalog/source_catalog.json` — machine-readable authorities;
- `catalog/DUPLICATE_REVIEW.md` — suspected duplicates, retained rather than deleted;
- `catalog/FAILED_OR_INCOMPLETE_SOURCES.md` — sources requiring re-import or verification;
- `catalog/COVERAGE_GAPS.md` — missing/uncertain literature targets;
- `curation/USEFUL_EXCERPTS.md` — initial useful passages and research leads;
- `curation/REVIEW_QUEUE.md` — high-value sources requiring manual excerpt selection;
- `imports/notebooklm/` — original group audits and extracted reference tables;
- `scripts/organize_sources.py` — repeatable intake normalizer.

## Working rule

Search and writing work from the catalog, curated excerpts and source Markdown. Group reports are advisory. Original PDFs will be archived later in the main thesis repository and linked by source ID.

## Intake rule for future groups

Add each new NotebookLM export as `GroupN/GroupNFiles/*.md` plus its two group-level helper files. Run `python scripts/organize_sources.py` on a branch, review the regenerated catalog and merge only after validation.
