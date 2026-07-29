# Bibliography Enrichment Method

The intake catalog records every uploaded Markdown file and its provenance. It may contain incomplete or incorrect metadata inherited from filenames or NotebookLM helper tables.

The enrichment overlay adds separate evidence levels without editing archived source text:

- `verified-arxiv-api` — an explicit arXiv identifier resolved through the arXiv API;
- `verified-crossref-api` — an explicit DOI resolved through Crossref;
- `probable-openalex-match` — a strict title-similarity candidate that still requires review;
- `recorded-source-url` — the export contained a URL, but bibliographic identity is not independently verified;
- `unresolved` — no adequate identity was found automatically.

None of these states means that methods, experiments, results or limitations were checked. A source becomes citation-ready only after full-text review, version confirmation and recording of the exact page, section, figure or table needed for the thesis claim.
