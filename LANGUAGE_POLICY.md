# Source-language preservation policy

## Core rule

Scientific source material must remain in the language in which the source was published or otherwise supplied.

This applies to:

- retained originals (PDF or other original files),
- converted source text,
- citation-ready evidence/excerpts,
- source-derived scientific paraphrases used as canonical evidence,
- thesis drafting that is directly grounded in a source, until the user explicitly chooses to translate it.

Automatic translation is **not** part of the canonical bibliography pipeline.

## What may use another language

Operational repository prose may use Greek or English as convenient. Examples include README explanations, workflow messages, internal documentation, and project-management notes. These must not be mistaken for source evidence.

Metadata keys and structural labels do not by themselves count as translation of scientific content.

## Existing cross-language evidence

If an older citation-ready file paraphrases an English source in Greek (or a Greek source in English), it must not be silently machine-translated back. It is marked for remediation and re-authored against the retained original source in the source language.

The older note may be retained as a non-canonical working note if useful, but it must not pass the export gate as citation-ready evidence until the source-language version is verified.

## Bilingual or genuinely multilingual sources

If the original publication itself contains equivalent content in more than one language, the evidence may use the language of the specific original passage that was checked. The provenance/location field should make that clear.

## File and directory names

Repository paths are an infrastructure concern, not scientific content. Final directory names, workflow filenames, tool filenames, generated artifact filenames, and operational file names should use English names. README prose and other explanatory text do not need to be translated merely because the path is renamed.

## Export rule

A selected source is export-ready only when:

1. its original is retained or otherwise verifiably linked,
2. the scientific decision is final,
3. citation-ready evidence is verified against the original,
4. the evidence preserves the source language,
5. no automated translation has been used to manufacture the canonical evidence.
