# ThesisBibliography

Temporary staging repository for collecting, identifying, deduplicating and curating sources for the thesis **“Comparison and Evaluation of Resilient AI Agents in Uncertain Environments.”**

This repository is not the final thesis bibliography and is not the source of truth for the research design. Its role is to turn mixed NotebookLM exports and future source batches into a traceable corpus that can later be copied selectively into `MariosGiannakaras/resilient-ai-agents-thesis`.

## Working model

1. New, unprocessed files enter through `incoming/`.
2. Original Markdown is preserved unchanged in `sources/raw-md/` under a stable source ID.
3. NotebookLM audit reports and source tables remain separate in `sources/group-reports/`; they are leads, not verified evidence.
4. `catalog/source-catalog.csv` and `.json` are the working archive of titles, authors, links, types, tags, quality, relevance, duplicates and verification state.
5. `catalog/malformed-or-missing.md` records files with missing metadata, bad extraction, empty content or unresolved identity.
6. `excerpts/by-source/` contains short machine-extracted candidate passages. They must be checked before citation.
7. `excerpts/by-topic/` indexes sources without duplicating them.
8. `queues/next-sources.md` and `queues/references-to-screen.csv` hold future candidates found in NotebookLM reports and source bibliographies.
9. `archive/original-path-map.csv` preserves the original group/path and SHA-256 for every imported file.

## Directory map

```text
sources/
  raw-md/             Complete archived Markdown sources
  group-reports/      NotebookLM audit reports and generated tables
catalog/
  source-catalog.*    Working source archive
  malformed-or-missing.md
  duplicate-groups.md
  peripheral-or-exclusion-candidates.md
  metadata-verification-log.json
excerpts/
  by-source/          Candidate passages with source IDs
  by-topic/           Topic indexes
queues/
  next-sources.md
  references-to-screen.csv
  manual-verification.md
archive/
  original-path-map.csv
incoming/             Drop folder for future batches
scripts/              Repeatable inventory, curation, enrichment and validation
workspace/            Generated diagnostics for curation runs
tests/                Repository integrity checks
```

## Source states

- **Archived:** the original Markdown is present and checksum-tracked.
- **Parsed:** metadata was extracted locally but not independently verified.
- **Verified metadata API:** title/authors/year were returned by an official scholarly metadata service.
- **Probable OpenAlex match:** a high-similarity match that still needs human/ChatGPT review.
- **Unresolved:** identity or required metadata is missing.
- **Duplicate candidate:** retained until the preferred scholarly version is chosen.
- **Exclusion candidate:** retained in the archive but unlikely to enter the final thesis corpus.

## Rules

- Do not delete or overwrite an original source because it appears duplicated or irrelevant.
- Do not treat NotebookLM summaries, classifications or proposed sources as verified facts.
- Do not cite a candidate excerpt without checking the archived source and, when necessary, the original PDF.
- Prefer peer-reviewed, official, institutional or author-provided sources.
- Do not add pirated books or papers.
- References mined from a source are candidates, not automatically approved additions.
- Final selection depends on the bounded research question, chosen GridWorld, models, uncertainty types and experimental protocol.

## Adding another batch

Place the new files in `incoming/` and keep their original names. The curation pass will:

1. identify source type and real origin,
2. detect exact and semantic duplicates,
3. assign stable source IDs and normalized names,
4. update the catalog and path map,
5. flag missing or malformed data,
6. extract candidate passages and cited references,
7. update the next-source and verification queues.

No file should be copied directly into the final thesis repository before this review is complete.
