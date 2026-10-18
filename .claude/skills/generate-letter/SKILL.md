---
name: generate-letter
description: Produce a `.docx` or `.pdf` of a Sunlit Sea official letter on the letterhead template, using `scripts/md_to_letter.py`. Trigger when the user asks to "generate the letter", "produce a brev", "lag et formelt brev som .docx/pdf", "svar på henvendelse som brev", or when turning an existing draft `.md` into a sendable letter on the Sunlit Sea letterhead. Enforces use of the wrapper (not plain pandoc) so the wordmark, cream "A" watermark, Letter page size, margins and styles land correctly.
---

# generate-letter

## When to use

- User explicitly asks for a letter output as `.docx` or `.pdf` for an official outbound letter (henvendelse til myndighet, kunde, partner; formelle svarbrev; styreprotokoller som sendes eksternt).
- A Markdown source for a letter exists (or is being written now) and the user wants the physical deliverable.

**Do not use** for non-letter deliverables (slide decks → `scripts/md_to_slides.py`; reports → plain `pandoc`; auditor packs → plain `pandoc`). The letterhead wrapper is only correct for genuine letters.

## Procedure

1. **Confirm the source `.md` is in letter shape.** Address block, date, salutation, body, signature. If the content is a report, auditor pack, or technical brochure, surface that to the user rather than forcing it into letterhead chrome.

2. **Verify content conventions** before converting:
   - No H1 heading at the top (competes visually with the SUNLIT SEA wordmark). Use a short bold subject line as the opening, or H2 if a heading is needed.
   - Stacked address and signature blocks use two trailing spaces at line end (or a trailing `\`) — otherwise lines fold into one paragraph.
   - YAML `title`, `author`, `date` render as a visible title block in docx/PDF. If the metadata is for us (internal title) rather than for the recipient, rename to `internal_title` etc.
   - External deliverable stand-alone rule: no repo file paths, no `background/…` references, no task numbers, no internal framing ("draft" / "offered to X" / "as described in the løypemelding"). Cite laws and standards by their canonical citation.
   - No bold in body text (`**...**` only for titles and subtitles).
   - No emphasis-by-assertion phrasing (*which is precisely*, *crucially*, *it is worth noting*, etc.).

3. **Run the wrapper:**

   ```bash
   # DOCX next to the .md
   python scripts/md_to_letter.py path/to/brev.md

   # PDF next to the .md (xelatex + eso-pic; no LibreOffice/Word needed)
   python scripts/md_to_letter.py --pdf path/to/brev.md

   # Custom output path (either format)
   python scripts/md_to_letter.py path/to/brev.md -o generic/deliverable/path.docx
   python scripts/md_to_letter.py --pdf path/to/brev.md -o generic/deliverable/path.pdf

   # Different letterhead (if a new version arrives)
   python scripts/md_to_letter.py path/to/brev.md --letterhead other_letterhead.docx
   ```

   Default letterhead: `generic/background/2026-10-10_sunlit_sea_letterhead.docx`. The `.docx` path uses pandoc `--reference-doc` on the letterhead template. The `.pdf` path extracts the wordmark + watermark PNGs from the same `.docx` on the fly and places them via an `eso-pic` LaTeX header-include at the Word positions.

4. **Check the rendered output.** Open the resulting `.docx` or `.pdf` and verify:
   - Wordmark present at the correct position on page 1.
   - Watermark present on every page.
   - Signature block renders as separate lines (not folded into one paragraph).
   - YAML title block (if present) is intentional and recipient-facing.
   - Page size, margins, fonts match the template.

5. **Signature block cases.** See `docs/pandoc_conversion.md` → "Letter / letterhead output" for:
   - Single signer — escaped-underscore signature line + two-space line breaks for name/title stacking.
   - Two signers side by side — raw-LaTeX `minipage` blocks (PDF only; `.docx` needs manual signature add in Word).

## Applicable rules

- CLAUDE.md "**Letters on the Sunlit Sea letterhead**" — always use `scripts/md_to_letter.py`, never plain `pandoc`.
- CLAUDE.md "**Do not convert to docx automatically**" — only convert on explicit user order; letter generation is one of the explicit-order cases.
- CLAUDE.md "**External deliverables stand alone**" — no repo paths, no task numbers, no companion-doc references.
- CLAUDE.md "**No bold in body text**", "**Markdown lists render correctly**", "**Avoid emphasis-by-assertion phrasing**", "**Lead with the positive claim**" — all apply.
- `docs/pandoc_conversion.md` → "Letter / letterhead output" — full prerequisites and signature-block templates.

## Historical references

- T123 — styrefullmakt sakspapir for ordinær generalforsamling 2026 (early use of the letterhead output in a board paper).
- T124 — Produksjons-pipeline for brev på Sunlit Sea-brevmal (open; the wrapper itself was built here).
- `generic/background/2026-10-10_sunlit_sea_letterhead.docx` — the current single source of truth for letterhead.

## Known pitfalls

- **Using plain `pandoc` instead of the wrapper** — the wordmark and watermark will not land correctly; the output looks almost right but is not on brand.
- **Signature block folding** — forgetting the two trailing spaces on each name/title line causes pandoc to join them into a single paragraph. Especially visible in PDF output.
- **Underscore signature line being centred** — plain `________` is parsed as a Markdown horizontal rule, which LaTeX centres. Use `\_\_\_\_...` to keep it inline and left-aligned.
- **Raw-LaTeX minipage in docx** — pandoc silently drops raw-LaTeX blocks when producing `.docx`. If you need side-by-side signatures in docx, add them in Word after the base `.docx` is produced.
- **YAML title block for internal metadata** — `title: ...` renders as a visible title in docx/PDF. If the title field is really for us, rename to `internal_title`.
- **Not asking before converting** — the "do not convert to docx automatically" rule still applies: do not generate the letter output speculatively, even when the `.md` is complete. Wait for the explicit "produce the docx" or "produce the pdf".
