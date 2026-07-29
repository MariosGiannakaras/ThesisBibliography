# Incoming Sources

Place new, unprocessed material here. Do not copy it directly into `sources/markdown/` or edit the catalog manually.

## Preferred NotebookLM batch layout

```text
incoming/
└── GroupN/
    ├── GroupNFiles/
    │   └── *.md
    ├── <NotebookLM source audit>.md
    └── <NotebookLM source/reference table>.csv
```

Keep the original filenames. The processing workflow will:

1. inspect the two group helper files;
2. check group-number collisions;
3. preserve original paths and hashes;
4. normalize source names and stable IDs;
5. move helper files to `imports/notebooklm/`;
6. rebuild duplicate, incomplete-source and coverage reports;
7. verify available metadata through official scholarly services;
8. update reference and next-source queues;
9. generate candidate excerpts and review notes where appropriate.

## Other files

Original PDFs may also be staged here for archival linking, but they are not converted or treated as citation-ready automatically. Record lawful acquisition and do not add pirated copies.

An incoming file is not part of the curated corpus until validation passes and the corresponding Pull Request is merged.
