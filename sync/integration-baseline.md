# Bibliography integration baseline v1

The first consumer-side integration into `MariosGiannakaras/resilient-ai-agents-thesis` must use the immutable Git tag:

```text
bibliography-integration-v1
```

This tag is published only after the committed `thesis-package/` passes:

```bash
python tools/package_integrity.py validate thesis-package
python tools/validate_thesis_package.py
python tools/fix_verified_catalog_flags.py
```

The consumer repository should checkout this tag with full Git history and read-only credentials, validate the package again, and copy `thesis-package/` byte-for-byte into `research/bibliography/`.

The tag commit identifies the repository snapshot that contains the generated package. `thesis-package/SOURCE_COMMIT` and `catalog/package-metadata.json.source_commit` identify the earlier canonical bibliography state from which that package was generated. These values are expected to differ when the generated package was committed in a later descendant commit.

The baseline contains 112 selected, verified sources with matching analyses and evidence. It intentionally excludes all original PDFs, raw source Markdown, unidentified archival files, pending intake, rejected sources, and non-exported material.
