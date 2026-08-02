#!/usr/bin/env python3
"""Πλήρης μετατροπή συνδεδεμένων PDF σε Markdown με OCR και αναφορά ποιότητας.

Το πρωτότυπο PDF δεν τροποποιείται. Το OCRmyPDF παράγει προσωρινό αντίγραφο
με text layer, ενώ το τελικό Markdown διατηρεί ρητά όρια σελίδων. Υπάρχον
ουσιαστικό Markdown δεν αντικαθίσταται.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

try:
    from pypdf import PdfReader  # type: ignore
except ImportError:  # pragma: no cover - ελέγχεται στο runtime
    PdfReader = None  # type: ignore[assignment]

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
ORIGINALS = ROOT / "originals"
SOURCES = ROOT / "sources"
CATALOG = ROOT / "catalog" / "sources.csv"
REPORT_CSV = ROOT / "catalog" / "conversion-status.csv"
REPORT_MD = ROOT / "catalog" / "conversion-status.md"
AUTO_MARKER = "<!-- AUTO_PDF_CONVERSION: v1 -->"
PLACEHOLDER_MARKERS = (
    "Η εγγραφή δημιουργήθηκε από πρωτότυπο PDF που δεν υπήρχε ακόμη στον κατάλογο.",
    "Χρειάζεται πλήρης μετατροπή σε Markdown",
)
CATALOG_FIELDS = [
    "Κωδικός", "Τίτλος", "Συγγραφείς", "Έτος", "Σύνδεσμος",
    "Τύπος", "Θέματα", "Κατάσταση", "Επιβεβαίωση", "Προτεραιότητα", "Σημειώσεις",
]
REPORT_FIELDS = [
    "Κωδικός", "Τίτλος", "Πρωτότυπο", "Κατάσταση μετατροπής", "OCR",
    "Σελίδες", "Σελίδες χωρίς αναγνώσιμο κείμενο", "Χαρακτήρες",
    "Χρειάζεται περαιτέρω μετατροπή", "Αιτίες", "Ταυτότητα PDF",
]
LFS_POINTER_PREFIX = b"version https://git-lfs.github.com/spec/v1"
LFS_OID_RE = re.compile(rb"oid sha256:([a-f0-9]{64})", re.IGNORECASE)


@dataclass
class PageExtraction:
    number: int
    text: str
    error: str = ""


@dataclass
class QualityAssessment:
    page_count: int
    readable_pages: int
    low_text_pages: int
    empty_pages: int
    text_characters: int
    replacement_characters: int
    extraction_errors: int
    further_conversion_required: bool
    reasons: list[str] = field(default_factory=list)


@dataclass
class OcrResult:
    status: str
    pdf_path: Path
    detail: str = ""


def is_lfs_pointer(path: Path) -> bool:
    try:
        return path.read_bytes()[:200].startswith(LFS_POINTER_PREFIX)
    except OSError:
        return False


def pdf_identity(path: Path) -> str:
    import hashlib

    with path.open("rb") as handle:
        prefix = handle.read(512)
    lfs = LFS_OID_RE.search(prefix)
    if lfs:
        return lfs.group(1).decode("ascii").lower()
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_extracted_text(text: str) -> str:
    text = unicodedata.normalize("NFKC", text or "")
    text = text.replace("\x00", "").replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in text.splitlines()]
    result: list[str] = []
    blank = False
    for line in lines:
        if line.strip():
            result.append(line)
            blank = False
        elif not blank:
            result.append("")
            blank = True
    return "\n".join(result).strip()


def extract_pages(path: Path) -> list[PageExtraction]:
    if PdfReader is None:
        raise RuntimeError("λείπει το pypdf")
    reader = PdfReader(str(path))
    pages: list[PageExtraction] = []
    for number, page in enumerate(reader.pages, start=1):
        try:
            text = normalize_extracted_text(page.extract_text() or "")
            pages.append(PageExtraction(number, text))
        except Exception as exc:  # pragma: no cover - εξαρτάται από προβληματικό PDF
            pages.append(PageExtraction(number, "", type(exc).__name__))
    return pages


def assess_quality(pages: list[PageExtraction]) -> QualityAssessment:
    page_count = len(pages)
    lengths = [len(re.sub(r"\s+", "", page.text)) for page in pages]
    readable_pages = sum(length >= 80 for length in lengths)
    low_text_pages = sum(0 < length < 80 for length in lengths)
    empty_pages = sum(length == 0 for length in lengths)
    text_characters = sum(lengths)
    replacement_characters = sum(page.text.count("�") for page in pages)
    extraction_errors = sum(bool(page.error) for page in pages)
    reasons: list[str] = []

    if page_count == 0:
        reasons.append("δεν αναγνωρίστηκαν σελίδες")
    else:
        unreadable = empty_pages + low_text_pages
        if text_characters < max(500, page_count * 100):
            reasons.append("εξήχθη πολύ λίγο κείμενο για το πλήθος των σελίδων")
        if unreadable >= 2 and unreadable / page_count > 0.20:
            reasons.append("πάνω από 20% των σελίδων έχουν ελάχιστο ή καθόλου κείμενο")
        if extraction_errors:
            reasons.append(f"απέτυχε η εξαγωγή σε {extraction_errors} σελίδες")
        if replacement_characters and replacement_characters / max(text_characters, 1) > 0.005:
            reasons.append("υπάρχουν πολλοί μη αναγνωρίσιμοι χαρακτήρες")

    return QualityAssessment(
        page_count=page_count,
        readable_pages=readable_pages,
        low_text_pages=low_text_pages,
        empty_pages=empty_pages,
        text_characters=text_characters,
        replacement_characters=replacement_characters,
        extraction_errors=extraction_errors,
        further_conversion_required=bool(reasons),
        reasons=reasons,
    )


def run_ocr(path: Path, workdir: Path, language: str) -> OcrResult:
    executable = shutil.which("ocrmypdf")
    if not executable:
        return OcrResult("μη-διαθέσιμο", path, "δεν βρέθηκε το ocrmypdf")

    output = workdir / "ocr.pdf"
    command = [
        executable,
        "--skip-text",
        "--rotate-pages",
        "--deskew",
        "--output-type", "pdf",
        "--optimize", "0",
        "--tesseract-timeout", "180",
        "--language", language,
        str(path),
        str(output),
    ]
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    if completed.returncode == 0 and output.exists():
        return OcrResult("ολοκληρώθηκε", output)
    if completed.returncode == 6:
        return OcrResult("ήδη-υπήρχε-text-layer", path)
    detail = (completed.stderr or completed.stdout or "άγνωστο σφάλμα").strip()
    detail = re.sub(r"\s+", " ", detail)[:500]
    return OcrResult(f"απέτυχε-{completed.returncode}", path, detail)


def useful_word_count(text: str) -> int:
    without_urls = re.sub(r"https?://\S+", " ", text)
    return len(re.findall(r"[A-Za-zΑ-Ωα-ωΆ-ώ0-9]{2,}", without_urls))


def source_is_replaceable(path: Path, row: dict[str, str]) -> bool:
    if not path.exists():
        return True
    text = path.read_text(encoding="utf-8", errors="replace")
    if AUTO_MARKER in text or any(marker in text for marker in PLACEHOLDER_MARKERS):
        return True
    return (
        row.get("Κατάσταση", "") in {"μόνο μεταδεδομένα", "αποτυχημένη εισαγωγή", "ελλιπές κείμενο"}
        and useful_word_count(text) < 120
    )


def parse_front_matter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        key, separator, value = line.partition(":")
        if not separator:
            continue
        value = value.strip()
        try:
            decoded = json.loads(value)
            result[key.strip()] = str(decoded)
        except json.JSONDecodeError:
            result[key.strip()] = value
    return result


def generated_for_identity(path: Path, identity: str) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8", errors="replace")
    if AUTO_MARKER not in text:
        return False
    return parse_front_matter(text).get("original_sha256") == identity


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def render_markdown(
    row: dict[str, str],
    original: Path,
    identity: str,
    pages: list[PageExtraction],
    quality: QualityAssessment,
    ocr: OcrResult,
    language: str,
    legacy_text: str = "",
) -> str:
    title = row.get("Τίτλος", "").strip() or original.stem
    further = quality.further_conversion_required
    reasons = quality.reasons[:]
    if ocr.status.startswith("απέτυχε") and further:
        reasons.append("το OCR απέτυχε και η εξαγωγή παραμένει ανεπαρκής")
    elif ocr.status == "μη-διαθέσιμο" and further:
        reasons.append("το OCR δεν ήταν διαθέσιμο και η εξαγωγή παραμένει ανεπαρκής")
    reasons = list(dict.fromkeys(reasons))
    further = bool(reasons)
    conversion_status = (
        "χρειάζεται-περαιτέρω-μετατροπή"
        if further
        else "πλήρης-αυτόματη-προς-έλεγχο"
    )

    header = [
        "---",
        f"source_id: {yaml_string(row['Κωδικός'])}",
        f"original_pdf: {yaml_string(original.relative_to(ROOT).as_posix())}",
        f"original_sha256: {yaml_string(identity)}",
        f"conversion_status: {yaml_string(conversion_status)}",
        f"ocr_status: {yaml_string(ocr.status)}",
        f"ocr_language: {yaml_string(language)}",
        f"page_count: {quality.page_count}",
        f"pages_without_readable_text: {quality.empty_pages + quality.low_text_pages}",
        f"text_characters: {quality.text_characters}",
        f"further_conversion_required: {yaml_string('ναι' if further else 'όχι')}",
        f"further_conversion_reasons: {yaml_string('; '.join(reasons) if reasons else 'καμία')}",
        f"manual_review_required: {yaml_string('ναι')}",
        "---",
        AUTO_MARKER,
        "",
        f"# {title}",
        "",
        "> Αυτόματη πιστή εξαγωγή από το αρχειακό PDF. Το πρωτότυπο παραμένει η αυθεντική πηγή.",
        "> Η ένδειξη «πλήρης» αφορά την τεχνική εξαγωγή όλων των σελίδων, όχι επιστημονική επαλήθευση.",
        "",
        "## Κατάσταση μετατροπής",
        "",
        f"- **OCR:** {ocr.status}",
        f"- **Σελίδες:** {quality.page_count}",
        f"- **Χρειάζεται περαιτέρω μετατροπή:** {'ναι' if further else 'όχι'}",
        f"- **Αιτίες:** {'; '.join(reasons) if reasons else 'καμία'}",
        "- **Απαιτείται ανθρώπινος έλεγχος:** ναι",
        "",
        "## Πλήρες κείμενο ανά σελίδα",
        "",
    ]
    body: list[str] = []
    for page in pages:
        body.extend([
            f"<!-- PDF_PAGE: {page.number} -->",
            f"### Σελίδα {page.number}",
            "",
            page.text or "[Δεν εξήχθη αναγνώσιμο κείμενο από αυτή τη σελίδα.]",
            "",
        ])
    if legacy_text.strip() and AUTO_MARKER not in legacy_text and not any(
        marker in legacy_text for marker in PLACEHOLDER_MARKERS
    ):
        body.extend([
            "## Προϋπάρχον συνοδευτικό υλικό",
            "",
            "> Διατηρείται αυτούσιο από το προηγούμενο αρχείο χαμηλού περιεχομένου.",
            "",
            legacy_text.strip(),
            "",
        ])
    return "\n".join(header + body).rstrip() + "\n"


def read_catalog() -> list[dict[str, str]]:
    with CATALOG.open(encoding="utf-8", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def write_catalog(rows: list[dict[str, str]]) -> None:
    with CATALOG.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CATALOG_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda row: row.get("Τίτλος", "").casefold()))


def append_note(row: dict[str, str], note: str) -> None:
    current = row.get("Σημειώσεις", "").strip()
    if note in current:
        return
    row["Σημειώσεις"] = f"{current} · {note}".strip(" ·")


def report_entry_from_generated(row: dict[str, str], pdf: Path, identity: str) -> dict[str, str]:
    source = SOURCES / f"{row['Κωδικός']}.md"
    meta = parse_front_matter(source.read_text(encoding="utf-8", errors="replace"))
    return {
        "Κωδικός": row["Κωδικός"],
        "Τίτλος": row.get("Τίτλος", ""),
        "Πρωτότυπο": pdf.relative_to(ROOT).as_posix(),
        "Κατάσταση μετατροπής": meta.get("conversion_status", "άγνωστη"),
        "OCR": meta.get("ocr_status", "άγνωστο"),
        "Σελίδες": meta.get("page_count", ""),
        "Σελίδες χωρίς αναγνώσιμο κείμενο": meta.get("pages_without_readable_text", ""),
        "Χαρακτήρες": meta.get("text_characters", ""),
        "Χρειάζεται περαιτέρω μετατροπή": meta.get("further_conversion_required", "άγνωστο"),
        "Αιτίες": meta.get("further_conversion_reasons", ""),
        "Ταυτότητα PDF": identity,
    }


def write_reports(entries: list[dict[str, str]]) -> None:
    REPORT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with REPORT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=REPORT_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(entries)

    converted = sum(item["Κατάσταση μετατροπής"] in {
        "πλήρης-αυτόματη-προς-έλεγχο", "χρειάζεται-περαιτέρω-μετατροπή"
    } for item in entries)
    further = sum(item["Χρειάζεται περαιτέρω μετατροπή"] == "ναι" for item in entries)
    pending = sum(item["Κατάσταση μετατροπής"].startswith("εκκρεμεί") for item in entries)
    existing = sum(item["Κατάσταση μετατροπής"] == "υπάρχον-markdown-δεν-αντικαταστάθηκε" for item in entries)
    lines = [
        "# Κατάσταση μετατροπών PDF", "",
        f"- Αυτόματες μετατροπές: **{converted}**",
        f"- Χρειάζονται περαιτέρω μετατροπή: **{further}**",
        f"- Εκκρεμούν λόγω μη διαθέσιμου PDF/LFS: **{pending}**",
        f"- Υπάρχον Markdown που δεν αντικαταστάθηκε: **{existing}**", "",
        "> Το OCR εκτελείται με λειτουργία skip-text: οι σελίδες με text layer διατηρούνται και οι σαρωμένες σελίδες OCR-άρονται.",
        "> Κάθε αυτόματη μετατροπή απαιτεί ανθρώπινο έλεγχο πριν χρησιμοποιηθεί ως παραπομπή.", "",
        "| Κωδικός | Τίτλος | Κατάσταση | OCR | Περαιτέρω μετατροπή | Αιτίες |",
        "|---|---|---|---|---|---|",
    ]
    for item in entries:
        title = item["Τίτλος"].replace("|", "\\|")
        reasons = item["Αιτίες"].replace("|", "\\|") or "—"
        lines.append(
            f"| `{item['Κωδικός']}` | {title} | {item['Κατάσταση μετατροπής']} | "
            f"{item['OCR']} | {item['Χρειάζεται περαιτέρω μετατροπή']} | {reasons} |"
        )
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def pending_entry(row: dict[str, str], pdf: Path, status: str, identity: str = "") -> dict[str, str]:
    return {
        "Κωδικός": row["Κωδικός"],
        "Τίτλος": row.get("Τίτλος", ""),
        "Πρωτότυπο": pdf.relative_to(ROOT).as_posix(),
        "Κατάσταση μετατροπής": status,
        "OCR": "δεν εκτελέστηκε",
        "Σελίδες": "",
        "Σελίδες χωρίς αναγνώσιμο κείμενο": "",
        "Χαρακτήρες": "",
        "Χρειάζεται περαιτέρω μετατροπή": "εκκρεμεί",
        "Αιτίες": "",
        "Ταυτότητα PDF": identity,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--όριο", "--limit", type=int, default=0)
    parser.add_argument("--μόνο-αναφορά", "--report-only", action="store_true")
    parser.add_argument("--εξαναγκασμός", "--force", action="store_true")
    parser.add_argument("--γλώσσες-ocr", "--ocr-language", default="eng+ell")
    args = parser.parse_args()

    rows = read_catalog()
    entries: list[dict[str, str]] = []
    changed_catalog = False
    converted_count = 0

    for row in sorted(rows, key=lambda item: item.get("Τίτλος", "").casefold()):
        source_id = row["Κωδικός"]
        pdf = ORIGINALS / f"{source_id}.pdf"
        if not pdf.exists():
            continue
        source = SOURCES / f"{source_id}.md"

        replaceable = source_is_replaceable(source, row)
        try:
            identity = pdf_identity(pdf)
        except OSError as exc:
            entries.append(pending_entry(row, pdf, f"εκκρεμεί-σφάλμα-{type(exc).__name__}"))
            continue

        if not replaceable:
            entries.append({
                **pending_entry(row, pdf, "υπάρχον-markdown-δεν-αντικαταστάθηκε", identity),
                "Χρειάζεται περαιτέρω μετατροπή": "δεν αξιολογήθηκε",
            })
            continue
        if is_lfs_pointer(pdf):
            if source.exists() and AUTO_MARKER in source.read_text(encoding="utf-8", errors="replace") and not args.force:
                stored = parse_front_matter(source.read_text(encoding="utf-8", errors="replace")).get("original_sha256", identity)
                entries.append(report_entry_from_generated(row, pdf, stored))
            else:
                entries.append(pending_entry(row, pdf, "εκκρεμεί-λήψη-lfs", identity))
            continue
        if generated_for_identity(source, identity) and not args.force:
            entries.append(report_entry_from_generated(row, pdf, identity))
            continue
        if args.report_only:
            entries.append(pending_entry(row, pdf, "εκκρεμεί-μετατροπή", identity))
            continue
        if args.limit > 0 and converted_count >= args.limit:
            entries.append(pending_entry(row, pdf, "εκκρεμεί-όριο-εκτέλεσης", identity))
            continue

        legacy_text = source.read_text(encoding="utf-8", errors="replace") if source.exists() else ""
        try:
            original_pages = extract_pages(pdf)
        except Exception as exc:
            entries.append(pending_entry(row, pdf, f"απέτυχε-ανάγνωση-{type(exc).__name__}", identity))
            continue

        with tempfile.TemporaryDirectory(prefix="thesis-ocr-") as temporary:
            ocr = run_ocr(pdf, Path(temporary), args.ocr_language)
            selected_pages = original_pages
            if ocr.pdf_path != pdf:
                try:
                    ocr_pages = extract_pages(ocr.pdf_path)
                    if sum(len(page.text) for page in ocr_pages) >= sum(len(page.text) for page in original_pages):
                        selected_pages = ocr_pages
                except Exception as exc:  # pragma: no cover - εξαρτάται από OCR output
                    ocr = OcrResult(f"απέτυχε-ανάγνωση-output-{type(exc).__name__}", pdf)
            quality = assess_quality(selected_pages)
            markdown = render_markdown(
                row, pdf, identity, selected_pages, quality, ocr, args.ocr_language, legacy_text
            )

        source.write_text(markdown, encoding="utf-8", newline="\n")
        meta = parse_front_matter(markdown)
        needs_more = meta.get("further_conversion_required") == "ναι"
        row["Κατάσταση"] = "ελλιπές κείμενο" if needs_more else "διαθέσιμο πλήρες κείμενο"
        append_note(
            row,
            "Αυτόματη πλήρης μετατροπή PDF με OCR· "
            + ("χρειάζεται περαιτέρω τεχνική μετατροπή" if needs_more else "τεχνικά πλήρης, προς ανθρώπινο έλεγχο"),
        )
        changed_catalog = True
        converted_count += 1
        entries.append(report_entry_from_generated(row, pdf, identity))
        print(f"{source_id}: {meta.get('conversion_status')} ({ocr.status})")

    if changed_catalog:
        write_catalog(rows)
        subprocess.run(
            [sys.executable, str(TOOLS / "import_sources.py"), "--catalog-only"],
            cwd=ROOT,
            check=True,
        )
    write_reports(entries)
    print(f"Μετατράπηκαν {converted_count} PDF και καταγράφηκαν {len(entries)} συνδεδεμένα πρωτότυπα.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
