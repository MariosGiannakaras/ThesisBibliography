# Ready-to-paste prompt for `resilient-ai-agents-thesis`

Use the following prompt in the chat/Codex session that manages `MariosGiannakaras/resilient-ai-agents-thesis`.

---

Integrate the verified bibliography produced by the private repository `MariosGiannakaras/ThesisBibliography` into `MariosGiannakaras/resilient-ai-agents-thesis`.

## Current architecture

`ThesisBibliography` is the sole source of truth for bibliography intake, originals, metadata, deduplication, full source Markdown, scientific analysis, verified evidence, selection, and export. The thesis repository must not reimplement source ingestion, OCR, deduplication, scientific source review, or evidence extraction.

The active bibliography baseline is scientifically complete. Lossless archival originals that cannot yet be identified safely may remain under `originals/unidentified/`; they are not citation-ready, are never exported, and do not block integration.

The thesis repository consumes only the generated and validated `thesis-package/`.

## First inspect the thesis repository

Before changing anything, inspect the repository, current Git state, applicable `AGENTS.md` files, project documentation, existing bibliography/citation implementation, tests, TODO/status tracking, relevant branches, issues, pull requests, and direct dependencies. Do not guess repository facts. Limit inspection to paths relevant to bibliography integration and their direct dependencies.

Preserve unrelated user changes. Do not use destructive Git operations. Reuse and update existing artifacts instead of duplicating them.

## Bibliography package contract

The imported generated directory should contain exactly the bibliography package content:

```text
research/bibliography/
├── README.md
├── SOURCE_COMMIT
├── manifest.csv
├── catalog/
│   ├── sources.csv
│   ├── package-metadata.json
│   └── SHA256SUMS
├── analyses/
└── evidence/
```

The package contains only selected, verified bibliography material. It must not contain `originals/`, PDFs, Git LFS objects, raw `sources/`, pending intake, draft analyses, or unverified evidence.

`catalog/package-metadata.json` is the machine-readable package contract. Schema version `1` uses SHA-256 and `catalog/SHA256SUMS`. `SOURCE_COMMIT` identifies the canonical bibliography source state used to build the package. The commit that contains the already-generated package may be a later descendant; do not incorrectly require the checkout commit itself to equal `SOURCE_COMMIT`.

## Implement the integration directly

1. Remove or adapt obsolete thesis-repository workflows that treat the thesis repo as the place where raw bibliography sources are ingested, OCRed, deduplicated, analyzed, or converted into evidence. Do not remove unrelated thesis functionality.
2. Use `research/bibliography/` as the single generated bibliography import directory. Do not hand-edit files inside it.
3. Implement a pull-based sync tool in the thesis repository. It must accept an explicit full commit SHA or tag for `ThesisBibliography`, authenticate read-only, and checkout with full Git history (`fetch-depth: 0`).
4. In the checked-out bibliography repository, before copying anything, run:

```bash
python tools/export_thesis.py --validate-only
python tools/package_integrity.py validate thesis-package
python tools/validate_thesis_package.py
```

If any command fails, abort without modifying `research/bibliography/`.

5. Copy the validated `thesis-package/` byte-for-byte into `research/bibliography/`, replacing only that generated directory.
6. From inside `research/bibliography/`, verify the imported bytes with:

```bash
sha256sum -c catalog/SHA256SUMS
```

7. Validate that:
   - `catalog/package-metadata.json` has supported `schema_version` (`1` initially),
   - its `source_commit` equals the imported `SOURCE_COMMIT`,
   - its selected-source count matches `manifest.csv`,
   - all checksum entries pass,
   - no prohibited artifacts exist,
   - every imported analysis/evidence source ID exists in the manifest.
8. Add CI validation so every `SRC-*` identifier used by thesis text or citation tooling exists in the imported manifest and so any manual modification of the generated bibliography directory is detected by the checksum validation.
9. Add a `workflow_dispatch` sync workflow that accepts the bibliography ref/commit, performs all validation, updates only `research/bibliography/`, and opens a pull request in the thesis repository. Do not push from `ThesisBibliography` into the thesis repository and do not auto-merge the sync.
10. Use a fine-grained read-only `BIBLIOGRAPHY_SYNC_TOKEN` scoped only to `ThesisBibliography`, or an equivalently restricted GitHub App installation token. Do not grant write access when read access is sufficient.
11. Update thesis-side writing/citation instructions so scientific claims cite `SRC-*` records and their verified evidence. Preserve source/evidence language; translation for final thesis prose is a separate authoring step and must not mutate imported evidence.
12. Add or update tests for the sync tool, integrity/schema validation, prohibited-artifact rejection, source-ID validation, and failure-before-replacement behavior.

If the workflow deliberately regenerates the package instead of copying the committed package, use this exact sequence in the checked-out bibliography repository:

```bash
python tools/export_thesis.py
python tools/package_integrity.py write thesis-package
python tools/package_integrity.py validate thesis-package
python tools/validate_thesis_package.py
```

## Acceptance criteria

- The thesis repository no longer treats itself as the source-ingestion/scientific-review system.
- `research/bibliography/` contains only the validated package contract above.
- SHA-256 integrity validation succeeds after import and fails after any package-file tampering.
- Package metadata, `SOURCE_COMMIT`, manifest, analyses, and evidence are internally consistent.
- No raw PDFs, originals, LFS objects, raw source Markdown, pending items, or non-selected evidence are imported.
- Thesis references to `SRC-*` are validated against the imported manifest.
- Sync is reproducible from an explicit bibliography ref and uses read-only credentials.
- Sync changes arrive through a thesis-repository pull request and pass CI before merge.
- Existing unrelated thesis code and user changes are preserved.

Implement the integration, tests, CI, and documentation directly. Use the narrowest relevant tests first and broader validation only where repository rules or the affected surface require it. For work large enough to risk session exhaustion, create coherent verified checkpoints with clear commits. Stop when the acceptance criteria pass.

Final report: outcome, changed files, validation performed, blockers if any, and commit/push/PR status only.

---
