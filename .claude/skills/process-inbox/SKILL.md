---
name: process-inbox
description: Convert files in any `*/background/new/` inbox to date-prefixed `.md` files and move them to the correct `background/` folder. Trigger when the user asks to "process the inbox", "convert the files in new/", or "handle the new background files" — or when a session starts and `generic/background/new/` or any `*/background/new/` folder contains files. Follows the standard conversion pipeline (pdftotext for PDFs, pandoc for DOCX/PPTX/ODT/RTF/HTML, images stay as-is).
---

# process-inbox

## When to use

- User says: "process the inbox", "convert the new background files", "handle `generic/background/new/`", or similar.
- Session start inbox check reveals unprocessed files in `generic/background/new/` or any `*/background/new/` folder (ask the user before processing — do not act unilaterally).
- A specific inbox subfolder is passed as the scope.

## Procedure

1. **List inbox contents.** Enumerate every file under the target `*/background/new/` folder. Report the list to the user and confirm scope before converting.

2. **Classify each file:**
   - `.pdf` → `pdftotext -layout "<path>" "<path>.txt"` then hand-tidy to `.md`. If the PDF has embedded figures that matter, use the extract-pdf-with-images skill instead.
   - `.docx`, `.pptx`, `.odt`, `.rtf`, `.html` → `pandoc "<path>" -o "<path>.md" --wrap=none`.
   - `.md`, `.txt` → already text; tidy and move.
   - `.png`, `.jpg`, `.jpeg`, other true binary evidence → keep as-is; timestamp-prefix and move; do not convert.
   - `.xlsx`, `.csv` → data files; keep raw. Do not convert to Markdown unless explicitly asked (prior precedent: T108 kept D7.4 cost `.xlsx` raw next to its `.md`).

3. **For each converted `.md`:**
   - Review the output and add a short preamble noting the document's original date (if known) in the body. Do not add a YAML `source:` field pointing at the original binary — the converted `.md` must be self-contained (see `docs/rules/` and CLAUDE.md "Converted `.md` files must be self-contained").
   - Rename to `YYYY-MM-DD_short_description.md` where `YYYY-MM-DD` is the document's *own* date — issued / written / sent for external material; created for internal (see `docs/rules/date-prefix.md`).
   - Move to `generic/background/` for cross-cutting material, or to the activity-specific `*/background/` folder (`sure/background/`, `funding/background/`, etc.).

4. **Clean up intermediates.** Remove the intermediate `.txt` output from `pdftotext` after the `.md` is finalised (if generated locally). Keep the original binary in `background/` **only** if it is the authoritative source (signed PDFs, signed contracts, presentations we might redistribute). Otherwise drop it after conversion.

5. **Report what you did:** per-file what source became which `.md` under which folder, which originals were kept vs. dropped and why.

## Applicable rules

- CLAUDE.md "**`background/new/` inbox check**" — never process on your own initiative; always confirm with the user first.
- CLAUDE.md "**Converted `.md` files must be self-contained**" — no `source:` YAML, no "converted from X" body text.
- CLAUDE.md "**Date-prefix naming convention**" + `docs/rules/date-prefix.md` — the date is the document's own date.
- CLAUDE.md "**Batch in-place edits require dry-run + backups**" + `docs/rules/batch-edits.md` — if the conversion step uses regex cleanup across many files, dry-run first.
- CLAUDE.md "**`rm` and other destructive operations**" + `docs/rules/destructive-ops.md` — ask before deleting the original binary if there is any doubt.
- `docs/background_convention.md` — full conversion pipeline and inbox routing.

## Historical references

- T73 — adoption of the `generic/background/new/` convention; the investor-update truncation incident that produced the dry-run + backup rule.
- T95 — conversion of `generic/background/new/` DOCX files tied to the EIC Transition application.
- T100 — Vollsfjorden PDF set conversion; established the combined PDF-with-images recipe (see extract-pdf-with-images skill).
- T108 — SUREWAVE consortium material converted from a `new/` inbox; `.docx` sources deleted after conversion per the "non-authoritative originals can be dropped" rule.
- T119 — SUREWAVE images housekeeping, EMF rasterisation; date-prefix rule extended to per-source folders.

## Known pitfalls

- **Over-broad regex cleanup**: T73 incident where two files lost ~90 % of content to a signature-stripping regex that matched Markdown horizontal rules. Always dry-run and inspect per-file word-count deltas; flag anything that shrinks below 70 %.
- **JP2 images**: pdfimages / pypdf sometimes hand back JPEG 2000 (`.jp2`), which no Markdown viewer renders. Convert to PNG before linking. Use the extract-pdf-with-images skill for PDFs with figures.
- **Stem mismatch**: for the combined PDF + images recipe, the `.md` stem must equal the `.pdf` stem — stage copies under their final slug names before converting.
- **Un-dated external material**: when the document's own date is unknown, use the best approximation and note the uncertainty in the file body. Do not fall back to the filing date silently.
- **Not asking first**: the CLAUDE.md rule is explicit — never process without the user's go-ahead, even when the inbox is obviously full.
