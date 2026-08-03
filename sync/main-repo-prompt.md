# Ready-to-paste prompt for `resilient-ai-agents-thesis`

Integrate the complete bibliography writing corpus produced by private repository `MariosGiannakaras/ThesisBibliography` into `MariosGiannakaras/resilient-ai-agents-thesis`.

## Inspect first

Inspect the thesis repository, Git state, applicable `AGENTS.md`, documentation, existing bibliography/citation code, workflows, tests, status files, open PRs/issues, and direct dependencies. Preserve unrelated changes and avoid destructive Git operations.

## Architecture

`ThesisBibliography` is the sole source of truth for intake, originals, OCR/conversion, deduplication, canonical source text, analyses, evidence, research materials, author notes, identification review, and export. The thesis repository must not reimplement those processes.

The consumer imports the generated `research-corpus/`, not only the strict citation package.

```text
research/bibliography/
├── README.md
├── SOURCE_COMMIT
├── citation-ready/
├── sources/
├── analyses/
├── evidence/
├── materials/
├── notes/
├── aggregates/
└── catalog/
    ├── sources.csv
    ├── thesis-selection.csv
    ├── research-materials.csv
    ├── research-material-review.csv
    ├── originals-index.csv
    ├── package-metadata.json
    └── SHA256SUMS
```

Trust semantics:

- `citation-ready/` is the strict verified package. A thesis citation using `SRC-*` must resolve in `citation-ready/manifest.csv` and use verified evidence.
- `sources/`, `analyses/`, `evidence/`, `materials/`, `notes/`, and `aggregates/` are the complete writing and discovery corpus.
- `MAT-*`, rejected sources, theory-only items, partial records, and user-authored notes remain searchable and usable for drafting/synthesis, but are not automatically verified citations.
- Missing title, author, URL, or formal citation metadata must never make useful content inaccessible.
- Do not copy PDF binaries or Git LFS objects; use extracted Markdown and `catalog/originals-index.csv` for immutable original URLs and hashes.

## Implement directly

1. Use `research/bibliography/` as a generated, read-only import directory.
2. Implement a pull-based sync accepting an explicit full SHA or immutable tag from `ThesisBibliography`, with `fetch-depth: 0` and read-only secret `BIBLIOGRAPHY_SYNC_TOKEN`.
3. Before copying, run in the checked-out bibliography repo:

```bash
python tools/package_integrity.py validate thesis-package
python tools/validate_thesis_package.py
python tools/research_materials.py validate
python tools/validate_research_material_review.py
python tools/export_research_corpus.py validate
```

Abort before modifying the existing import if any validator fails.

4. Copy committed `research-corpus/` byte-for-byte into `research/bibliography/`.
5. Verify after copying:

```bash
sha256sum -c catalog/SHA256SUMS
sha256sum -c citation-ready/catalog/SHA256SUMS
```

6. Validate schema version, `SOURCE_COMMIT`, package counts, exact checksum path sets, material/review ID coverage, and absence of PDFs/LFS objects.
7. Add citation validation:
   - formal `SRC-*` citations must exist in `citation-ready/manifest.csv`;
   - `MAT-*` references may be used in drafting notes or provenance links but must not be treated as verified bibliography citations unless explicitly promoted through `ThesisBibliography`;
   - notes require no bibliographic identity.
8. Add search/index support across the entire imported corpus so thesis writing can retrieve useful text from selected, rejected, theory-only, unidentified-origin, chapter-level, and author-note material.
9. Remove or adapt obsolete thesis-side bibliography ingestion/OCR/review workflows without touching unrelated thesis functionality.
10. Add a `workflow_dispatch` sync workflow that opens a PR, never auto-merges, and never pushes from the bibliography repo into the thesis repo.
11. Add tests for failure-before-replacement, SHA tampering, schema/count mismatch, prohibited binaries, exact `SRC-*` citation validation, `MAT-*` trust handling, note accessibility, and complete corpus searchability.
12. Preserve original source language. Translation into final thesis prose is an authoring step and must not mutate imported evidence or extracted material.

## Acceptance criteria

- The complete `research-corpus/` is imported and integrity-verified.
- All writing material is accessible even when not citation-ready.
- The strict verified citation layer remains enforceable and separate.
- No PDF or LFS binary is imported.
- Sync is reproducible from an explicit ref, uses read-only credentials, and arrives through a PR.
- Imported files are never edited manually.
- Existing unrelated code and user changes are preserved.

Implement the integration, tests, CI, and documentation directly. Final report only: outcome, changed files, validation, blockers, commit/push/PR status.
