#!/usr/bin/env python3
"""Αντιστοίχιση εισερχόμενων PDF, ασφαλείς νέες εγγραφές και αναφορές."""
from __future__ import annotations

import csv
import re
import shutil
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

from sources_common import SOURCE_ID_RE, identities, normalized_words, source_text
from originals_common import (
    GENERIC_TITLE,
    INCOMING,
    LINKED_PDF_STEM_RE,
    ORIGINALS,
    PENDING_REPORT,
    REPORT_CSV,
    REPORT_FIELDS,
    REPORT_MD,
    SOURCES,
    UNMATCHED,
    DownloadResult,
    MatchResult,
    PdfInfo,
    can_create_source_from_pdf,
    inspect_pdf,
    pdf_identity,
    sha256,
    strong_new_title,
    strong_pdf_identities,
    title_score,
)


def match_uploaded(path: Path, rows: list[dict[str, str]], texts: dict[str, str]) -> MatchResult:
    id_in_name = SOURCE_ID_RE.search(path.name.upper())
    info = inspect_pdf(path)
    if id_in_name and any(row["Κωδικός"] == id_in_name.group(0) for row in rows):
        return MatchResult(id_in_name.group(0), "κωδικός στο όνομα", info)

    pdf_ids = strong_pdf_identities(info)
    strong_matches: list[str] = []
    for row in rows:
        row_ids = identities(
            row.get("Σύνδεσμος", ""),
            row.get("Τίτλος", ""),
            texts.get(row["Κωδικός"], ""),
        )
        if pdf_ids & row_ids:
            strong_matches.append(row["Κωδικός"])
    if len(strong_matches) == 1:
        return MatchResult(strong_matches[0], "μοναδικό DOI ή arXiv ID", info)
    if len(strong_matches) > 1:
        return MatchResult(None, "πολλαπλές εγγραφές με το ίδιο ισχυρό αναγνωριστικό", info)

    scores = sorted(
        [
            (
                title_score(row.get("Τίτλος", ""), path, info),
                row["Κωδικός"],
                row.get("Τίτλος", ""),
            )
            for row in rows
        ],
        reverse=True,
    )
    useful = [item for item in scores if item[0] >= 0.45][:3]
    if scores and scores[0][0] >= 0.90 and (
        len(scores) == 1 or scores[0][0] - scores[1][0] >= 0.06
    ):
        return MatchResult(
            scores[0][1],
            f"μοναδική ισχυρή ομοιότητα τίτλου {scores[0][0]:.2f}",
            info,
            useful,
        )
    return MatchResult(None, "δεν βρέθηκε ασφαλής μοναδική αντιστοίχιση", info, useful)


def inferred_type(path: Path, info: PdfInfo) -> str:
    sample = " ".join([path.name, info.title, info.text[:2000]]).casefold()
    if any(word in sample for word in ("dissertation", "thesis", "διπλωματική", "doctoral", "master of")):
        return "διπλωματική ή διατριβή"
    if info.doi or info.arxiv or "abstract" in sample:
        return "ακαδημαϊκή εργασία"
    if any(word in sample for word in ("white paper", "whitepaper", "report", "evaluation plan")):
        return "θεσμική ή τεχνική αναφορά"
    return "βιβλίο ή κεφάλαιο"


def new_source_id(path: Path, existing_ids: set[str]) -> str:
    digest = sha256(path).upper()
    for offset in range(0, len(digest) - 9):
        source_id = "SRC-" + digest[offset:offset + 10]
        if source_id not in existing_ids:
            return source_id
    raise RuntimeError("δεν ήταν δυνατό να δημιουργηθεί μοναδικός κωδικός")


def create_source_from_pdf(
    path: Path,
    info: PdfInfo,
    rows: list[dict[str, str]],
) -> tuple[str | None, str]:
    allowed, evidence = can_create_source_from_pdf(path, info)
    if not allowed:
        return None, evidence

    title = strong_new_title(info, path)
    source_id = new_source_id(path, {row["Κωδικός"] for row in rows})
    link = ""
    verification = "εκκρεμεί"
    if len(info.doi) == 1:
        link = f"https://doi.org/{info.doi[0]}"
        verification = "μόνο καταγεγραμμένος σύνδεσμος"
    elif len(info.arxiv) == 1:
        link = f"https://arxiv.org/abs/{info.arxiv[0]}"
        verification = "μόνο καταγεγραμμένος σύνδεσμος"

    markdown = [
        f"# {title}", "",
        "> Η εγγραφή δημιουργήθηκε από πρωτότυπο PDF που δεν υπήρχε ακόμη στον κατάλογο.",
        "> Χρειάζεται πλήρης μετατροπή σε Markdown και έλεγχος πριν χρησιμοποιηθεί ως παραπομπή.", "",
    ]
    if link:
        markdown.insert(2, f"> Source: {link}")
        markdown.insert(3, "")
    if info.authors:
        markdown.append(f"- **Συγγραφείς:** {info.authors}")
    if info.year:
        markdown.append(f"- **Έτος:** {info.year}")
    if link:
        markdown.append(f"- **Σύνδεσμος:** {link}")
    markdown.append(f"- **Πρωτότυπο:** `originals/{source_id}.pdf`")
    (SOURCES / f"{source_id}.md").write_text("\n".join(markdown) + "\n", encoding="utf-8")
    rows.append({
        "Κωδικός": source_id,
        "Τίτλος": title,
        "Συγγραφείς": info.authors,
        "Έτος": info.year,
        "Σύνδεσμος": link,
        "Τύπος": inferred_type(path, info),
        "Θέματα": "χωρίς κατηγορία",
        "Κατάσταση": "μόνο μεταδεδομένα",
        "Επιβεβαίωση": verification,
        "Προτεραιότητα": "χρειάζεται διόρθωση",
        "Σημειώσεις": (
            "Δημιουργήθηκε από πρωτότυπο PDF με " + evidence
            + "· χρειάζεται πλήρης μετατροπή και θεματική αξιολόγηση."
        ),
    })
    shutil.move(str(path), ORIGINALS / f"{source_id}.pdf")
    return source_id, f"δημιουργήθηκε νέα εγγραφή «{title}» ({evidence})"


def repair_row_from_pdf(row: dict[str, str], info: PdfInfo) -> bool:
    changed = False
    title = re.sub(r"\s+", " ", info.title).strip(" -_:. ")
    current = row.get("Τίτλος", "").strip()
    if (
        (not current or GENERIC_TITLE.search(current) or len(normalized_words(current)) < 12)
        and title
        and not GENERIC_TITLE.search(title)
    ):
        row["Τίτλος"] = title[:300]
        changed = True
    if not row.get("Συγγραφείς") and info.authors:
        row["Συγγραφείς"] = info.authors
        changed = True
    if not row.get("Έτος") and info.year:
        row["Έτος"] = info.year
        changed = True
    if not row.get("Σύνδεσμος"):
        if len(info.doi) == 1:
            row["Σύνδεσμος"] = f"https://doi.org/{info.doi[0]}"
            row["Επιβεβαίωση"] = "μόνο καταγεγραμμένος σύνδεσμος"
            changed = True
        elif len(info.arxiv) == 1:
            row["Σύνδεσμος"] = f"https://arxiv.org/abs/{info.arxiv[0]}"
            row["Επιβεβαίωση"] = "μόνο καταγεγραμμένος σύνδεσμος"
            changed = True
    return changed


def _safe_original_name(name: str) -> str:
    """Return an ASCII-safe archival basename without changing the PDF bytes."""
    stem = unicodedata.normalize("NFKD", Path(name).stem)
    stem = stem.encode("ascii", "ignore").decode("ascii")
    stem = re.sub(r"[^0-9A-Za-z._()\- ]+", "_", stem).strip(" ._")
    stem = stem[:150].rstrip(" ._") or "original"
    return stem + ".pdf"


def _find_exact_duplicate(path: Path, originals: Path) -> Path | None:
    identity = pdf_identity(path)
    for existing in sorted(originals.rglob("*.pdf")):
        if existing == path:
            continue
        try:
            if pdf_identity(existing) == identity:
                return existing
        except OSError:
            continue
    return None


def archive_unmatched(
    path: Path,
    *,
    originals: Path = ORIGINALS,
    unmatched: Path = UNMATCHED,
) -> tuple[Path | None, str]:
    """Αρχειοθετεί μη ταυτοποιημένο PDF και αφαιρεί μόνο ακριβές αντίγραφο."""
    originals.mkdir(parents=True, exist_ok=True)
    unmatched.mkdir(parents=True, exist_ok=True)

    duplicate = _find_exact_duplicate(path, originals)
    if duplicate:
        path.unlink()
        return None, f"αφαιρέθηκε ακριβές διπλότυπο του {duplicate.relative_to(originals)}"

    try:
        already_archived = path.is_relative_to(unmatched)
    except ValueError:
        already_archived = False
    if already_archived:
        return path, "παραμένει μόνιμα αρχειοθετημένο ως μη ταυτοποιημένο"

    identity = pdf_identity(path)
    original_name = path.name
    target = unmatched / f"{identity[:16].upper()}__{_safe_original_name(original_name)}"
    if target.exists() and target != path:
        if pdf_identity(target) == identity:
            path.unlink()
            return None, f"αφαιρέθηκε ακριβές διπλότυπο του {target.relative_to(originals)}"
        target = unmatched / f"{identity[:32].upper()}__{_safe_original_name(original_name)}"
    shutil.move(str(path), target)
    return target, f"αρχειοθετήθηκε μόνιμα ως μη ταυτοποιημένο (αρχικό όνομα: {original_name})"


def _store_alternate(path: Path, source_id: str) -> tuple[Path | None, str]:
    identity = pdf_identity(path)
    for existing in sorted(ORIGINALS.glob(f"{source_id}*.pdf")):
        if existing != path and pdf_identity(existing) == identity:
            path.unlink()
            return None, "αφαιρέθηκε ακριβές διπλότυπο υπάρχοντος πρωτοτύπου"

    alternate = ORIGINALS / f"{source_id}__alternative-{identity[:10].upper()}.pdf"
    if alternate.exists():
        if pdf_identity(alternate) == identity:
            path.unlink()
            return None, "αφαιρέθηκε ακριβές διπλότυπο εναλλακτικής έκδοσης"
        alternate = ORIGINALS / f"{source_id}__alternative-{identity[:16].upper()}.pdf"
    shutil.move(str(path), alternate)
    return alternate, "διαφορετική έκδοση της ίδιας πηγής"


def import_uploaded(
    rows: list[dict[str, str]],
    *,
    create_missing: bool,
) -> tuple[list[str], list[tuple[Path, MatchResult]], bool]:
    ORIGINALS.mkdir(parents=True, exist_ok=True)
    UNMATCHED.mkdir(parents=True, exist_ok=True)
    INCOMING.mkdir(parents=True, exist_ok=True)
    texts = {row["Κωδικός"]: source_text(SOURCES, row["Κωδικός"]) for row in rows}
    notes: list[str] = []
    pending: list[tuple[Path, MatchResult]] = []
    catalog_changed = False
    candidates = list(INCOMING.rglob("*.pdf"))
    candidates.extend(
        path for path in ORIGINALS.glob("*.pdf")
        if not LINKED_PDF_STEM_RE.fullmatch(path.stem)
    )
    candidates.extend(UNMATCHED.rglob("*.pdf"))

    for path in sorted(set(candidates)):
        if not path.exists():
            continue
        result = match_uploaded(path, rows, texts)
        if not result.source_id:
            creation_reason = ""
            if create_missing:
                source_id, creation_reason = create_source_from_pdf(path, result.info, rows)
                if source_id:
                    texts[source_id] = source_text(SOURCES, source_id)
                    notes.append(f"{path.name} → {source_id}.pdf ({creation_reason})")
                    catalog_changed = True
                    continue
            reason = result.reason
            if creation_reason:
                reason += f"· {creation_reason}"
            archived, archive_reason = archive_unmatched(path)
            notes.append(f"{path.name}: {reason}· {archive_reason}")
            if archived:
                pending_result = MatchResult(None, reason, result.info, result.candidates)
                pending.append((archived, pending_result))
            continue

        target = ORIGINALS / f"{result.source_id}.pdf"
        row = next(row for row in rows if row["Κωδικός"] == result.source_id)
        catalog_changed = repair_row_from_pdf(row, result.info) or catalog_changed
        if target.exists():
            if pdf_identity(path) == pdf_identity(target):
                path.unlink()
                notes.append(f"{path.name}: αφαιρέθηκε ακριβές διπλότυπο του {result.source_id}")
            else:
                alternate, reason = _store_alternate(path, result.source_id)
                if alternate:
                    notes.append(f"{path.name} → {alternate.name} ({reason})")
                else:
                    notes.append(f"{path.name}: {reason}")
            continue
        shutil.move(str(path), target)
        notes.append(f"{path.name} → {target.name} ({result.reason})")
    return notes, pending, catalog_changed


def write_pending_report(pending: list[tuple[Path, MatchResult]]) -> None:
    lines = [
        "# Εκκρεμή πρωτότυπα", "",
        "Τα παρακάτω PDF διατηρούνται μόνιμα στο `originals/unidentified/` μέχρι να υπάρξει ασφαλής αντιστοίχιση. Διαγράφεται μόνο ακριβές αντίγραφο με ίδιο SHA-256/LFS object ID.", "",
    ]
    if not pending:
        lines.append("Δεν υπάρχουν μη ταυτοποιημένα PDF.")
    for path, result in pending:
        info = result.info
        try:
            relative_path = path.relative_to(ORIGINALS)
        except ValueError:
            relative_path = path
        lines.extend([
            f"## {path.name}", "",
            f"- **Αρχείο:** `{relative_path}`",
            f"- **Αποτέλεσμα:** {result.reason}",
            f"- **Τίτλος PDF:** {info.title or 'δεν αναγνωρίστηκε'}",
            f"- **Συγγραφείς:** {info.authors or 'δεν αναγνωρίστηκαν'}",
            f"- **Έτος:** {info.year or 'δεν αναγνωρίστηκε'}",
            f"- **Σελίδες:** {info.pages or 'άγνωστο'}",
            f"- **DOI κεφαλίδας:** {', '.join(info.doi) or 'δεν βρέθηκε'}",
            f"- **arXiv κεφαλίδας:** {', '.join(info.arxiv) or 'δεν βρέθηκε'}",
        ])
        if result.candidates:
            lines.extend(["", "Καλύτεροι υποψήφιοι:", ""])
            lines.extend(
                f"- `{source_id}` — {title} — βαθμός `{score:.2f}`"
                for score, source_id, title in result.candidates
            )
        if info.metadata_error:
            lines.append(f"- **Σφάλμα ανάγνωσης:** {info.metadata_error}")
        lines.append("")
    PENDING_REPORT.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_report(
    rows: list[dict[str, str]],
    previous: dict[str, dict[str, str]],
    results: dict[str, DownloadResult],
    import_notes: list[str],
) -> None:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    output: list[dict[str, str]] = []
    for row in sorted(rows, key=lambda item: item["Τίτλος"].casefold()):
        source_id = row["Κωδικός"]
        pdf = ORIGINALS / f"{source_id}.pdf"
        shortcut = ORIGINALS / f"{source_id}.url"
        old = previous.get(source_id, {})
        result = results.get(source_id)
        if pdf.exists():
            status, file_name = "διαθέσιμο PDF", pdf.name
        elif shortcut.exists():
            status, file_name = "μόνο σύνδεσμος", shortcut.name
        elif not row.get("Σύνδεσμος"):
            status, file_name = "χωρίς σύνδεσμο", ""
        elif result:
            status, file_name = result.status, ""
        else:
            status, file_name = old.get("Κατάσταση", "εκκρεμεί"), old.get("Αρχείο", "")
        output.append({
            "Κωδικός": source_id,
            "Τίτλος": row.get("Τίτλος", ""),
            "Κατάσταση": status,
            "Αρχείο": file_name,
            "Σύνδεσμος": result.url if result else old.get("Σύνδεσμος", row.get("Σύνδεσμος", "")),
            "Προσπάθειες": str(int(old.get("Προσπάθειες", "0") or 0) + (1 if result else 0)),
            "Τελευταίος έλεγχος": today if result else old.get("Τελευταίος έλεγχος", ""),
            "Σημείωση": result.note if result else old.get("Σημείωση", ""),
        })

    REPORT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with REPORT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=REPORT_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(output)

    counts: dict[str, int] = {}
    for item in output:
        counts[item["Κατάσταση"]] = counts.get(item["Κατάσταση"], 0) + 1
    unmatched_count = sum(1 for path in UNMATCHED.rglob("*.pdf") if path.is_file())
    lines = [
        "# Πρωτότυπα πηγών", "",
        f"- PDF: **{counts.get('διαθέσιμο PDF', 0)}**",
        f"- Μη ταυτοποιημένα PDF που διατηρούνται: **{unmatched_count}**",
        f"- Σύνδεσμοι (YouTube, ιστοσελίδες κ.λπ.): **{counts.get('μόνο σύνδεσμος', 0)}**",
        f"- Χειροκίνητη λήψη: **{counts.get('χρειάζεται χειροκίνητη λήψη', 0)}**",
        f"- Χωρίς σύνδεσμο: **{counts.get('χωρίς σύνδεσμο', 0)}**",
        f"- Εκκρεμούν: **{counts.get('εκκρεμεί', 0)}**", "",
        "> Τα PDF είναι αρχειακά αντίγραφα. Η καθημερινή εργασία γίνεται στα Markdown. Μη ταυτοποιημένα PDF δεν διαγράφονται· διαγράφονται μόνο ακριβή αντίγραφα.", "",
        "| Κωδικός | Τίτλος | Κατάσταση | Αρχείο ή σύνδεσμος |",
        "|---|---|---|---|",
    ]
    rank = {
        "χρειάζεται χειροκίνητη λήψη": 0,
        "χωρίς σύνδεσμο": 1,
        "εκκρεμεί": 2,
        "διαθέσιμο PDF": 3,
        "μόνο σύνδεσμος": 4,
    }
    for item in sorted(output, key=lambda x: (rank.get(x["Κατάσταση"], 9), x["Τίτλος"].casefold())):
        target = item["Αρχείο"] or "—"
        if not item["Αρχείο"] and item["Σύνδεσμος"]:
            target = f"[άνοιγμα]({item['Σύνδεσμος']})"
        title = item["Τίτλος"].replace("|", "\\|")
        lines.append(f"| `{item['Κωδικός']}` | {title} | {item['Κατάσταση']} | {target} |")
    if import_notes:
        lines.extend(["", "## Αρχεία που αντιστοιχίστηκαν, αρχειοθετήθηκαν ή απο-διπλοποιήθηκαν", ""])
        lines.extend(f"- {note}" for note in import_notes)
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
