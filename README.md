# ThesisBibliography

Temporary staging repository for literature collected through Gemini NotebookLM for the thesis **“Comparison and Evaluation of Resilient AI Agents in Uncertain Environments.”**

The repository is a source-processing workspace, not the final thesis bibliography and not the authority for models, metrics or experimental design.

## Current corpus

- **363** uploaded source records are preserved as Markdown;
- **32** records have explicit arXiv/Crossref metadata;
- **15** records have strict but still reviewable OpenAlex matches;
- **25** source-specific candidate excerpt files were generated;
- **1,151** reference candidates were extracted, including URL-free bibliography entries.

These are curation states, not final source approval.

## Repository map

- `sources/markdown/` — all uploaded source Markdown files in one flat archive;
- `catalog/SOURCE_CATALOG.md` — readable master index;
- `catalog/SOURCE_CATALOG.csv` and `catalog/source_catalog.json` — machine-readable intake authorities;
- `catalog/VERIFIED_SOURCE_METADATA.md` and `.csv` — non-destructive metadata overlay;
- `catalog/MALFORMED_OR_MISSING_DATA.md` — missing, incomplete or unresolved source data;
- `catalog/DUPLICATE_REVIEW.md` — suspected duplicates, retained rather than deleted;
- `catalog/COVERAGE_GAPS.md` — current topic and evidence gaps;
- `catalog/ENRICHMENT_METHOD.md` — meaning and limits of metadata states;
- `curation/USEFUL_EXCERPTS.md` — combined initial passage candidates;
- `curation/excerpts/by-source/` — one candidate excerpt file per selected source;
- `notes/by-source/` — verified full-text notes and template;
- `queues/NEXT_SOURCES.md` — known high-priority additions and verification targets;
- `queues/REFERENCES_TO_SCREEN.csv` — references mined from source bibliographies and NotebookLM tables;
- `imports/notebooklm/` — original group audits and extracted reference tables;
- `incoming/` — staging location for future complete source groups;
- `scripts/` — repeatable organization, intake, enrichment and validation tools.

## Evidence rules

- NotebookLM reports, labels and suggestions are advisory.
- Metadata verification does not mean the source was read or its claims checked.
- Candidate excerpts are not citation-ready.
- References mined from a bibliography are screening leads, not automatic additions.
- Original source Markdown is not modified by enrichment.
- Duplicate and peripheral files remain archived until an explicit reviewed decision.

## Future intake

Place a complete new batch under:

```text
incoming/GroupN/
├── GroupNFiles/*.md
├── <NotebookLM audit>.md
└── <NotebookLM source/reference table>.csv
```

Then run:

```bash
python scripts/process_incoming.py
```

The command preflights every group before moving anything, rejects uncataloged non-Markdown source files, runs the organizer and performs online scholarly metadata enrichment by default. `--offline` is available only for an explicitly incomplete local pass.
