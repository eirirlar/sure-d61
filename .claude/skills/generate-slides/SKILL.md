---
name: generate-slides
description: Produce a PDF slide deck in Sunlit Sea's visual profile (Everett headlines + Arial body, yellow #FFE775 and blue #2F354F accents) via `scripts/md_to_slides.py`. Trigger when the user asks to "generate the slide deck", "lag presentasjonen som pdf", "produce the deck", "slides in Sunlit Sea style", or when turning a `.md` into a sendable branded presentation (board decks, generalforsamling, pitch decks, grant-presentation talks, WP8 outputs with Sunlit Sea strap). Enforces the wrapper so the colour palette, fonts, footer strap and section-divider chrome land correctly.
---

# generate-slides

## When to use

- User explicitly asks for a slide-deck output as `.pdf` with Sunlit Sea branding (styremøter, generalforsamling, pitches, SPV / investor decks, grant-call presentations where Sunlit Sea is the lead voice).
- A Markdown source exists (or is being drafted) and the user wants the physical deck.

**Do not use** for:

- EU-deliverable reports (D6.1 / D6.2 and similar) — those are plain pandoc with the standard flags from `docs/pandoc_conversion.md`.
- Sunlit Sea letters — use `generate-letter` instead.
- SUREWAVE-branded presentations — use `generate-surewave-pptx` instead (SUREWAVE consortium brand ≠ Sunlit Sea brand).

## Procedure

1. **Confirm the source `.md` is in deck shape.** The deck convention is one frame per `## Heading` (pandoc runs with `--slide-level=2`). If the content reads as prose or a report, surface that to the user before pushing it through the slide pipeline.

2. **Verify content conventions** before converting:
   - `## Heading` begins a new frame.
   - `## {.plain}` begins a chrome-free frame (no title, no footer); use for title slide, section dividers, closing slide. Fill with a raw `\begin{tikzpicture}[remember picture, overlay] ... \end{tikzpicture}` to paint the whole page.
   - Section dividers: `\fill[sunlitYellow] (current page.north west) rectangle (current page.south east);` then nodes for the "Del N" label and section title.
   - Big-number highlight blocks: `\bignum{2{,}2 MNOK}{Beskrivelse}` inside a `columns` layout.
   - Use raw `\begin{tabular}{@{}lrrr@{}}...\end{tabular}` for tables rather than Markdown pipe-tables when you need column emphasis or custom spacing. Keep inline `\color{sunlitBlue900}` *inside* raw tabular — pandoc preserves braces in raw-latex blocks but escapes them in prose, so avoid `{\color{...}...}` in body text (use `\textcolor{sunlitBlue900}{\textbf{...}}` or plain `**bold**` instead).
   - Global rules still apply: no bold in body text (`**...**` is reserved for titles), no emphasis-by-assertion phrasing, lead with the positive claim.
   - External-deliverable rules apply if the deck is going outside Sunlit Sea: no repo paths, no task numbers, no internal framing.

3. **Run the wrapper:**

   ```bash
   # Default: writes <input>.pdf next to <input>.md
   python scripts/md_to_slides.py path/to/deck.md

   # Custom output path
   python scripts/md_to_slides.py path/to/deck.md -o path/to/out.pdf
   ```

   The wrapper does:
   - Loads `scripts/sunlit_sea_slides_header.tex` (colour palette, frame title, footer, `\bignum` helper).
   - Loads Everett `.ttf` files from `visual_profile/fonts/` via an absolute-path prelude generated at build time, so XeLaTeX finds them without the fonts being system-installed.
   - Runs pandoc → beamer → xelatex with the right `--slide-level`, 16:9 aspect ratio, yellow underline below each slide title, footer strap and page counter.

4. **Check the rendered output.** Open the resulting `.pdf` and verify:
   - Title slide and section dividers look right (full-page yellow, Everett headlines).
   - Frame title has the thin yellow underline.
   - Footer strap reads correctly (`SUNLIT SEA | <context>` + page number).
   - Fonts render — Everett for headlines, Arial for body. "Missing character" or substituted-font warnings in the xelatex log mean the font path wasn't found; verify `visual_profile/fonts/` is intact.
   - Big-number blocks (`\bignum{}`) render with the brand colours.
   - Tables (if any) have the right column widths and emphasis.

## Applicable rules

- CLAUDE.md "**Pandoc is the chosen conversion tool**" — this wrapper is the chosen pipeline for Sunlit Sea slides specifically.
- CLAUDE.md "**Do not convert to docx automatically**" — same spirit: don't produce the deck without an explicit order.
- CLAUDE.md "**External deliverables stand alone**" — applies when the deck goes outside Sunlit Sea.
- CLAUDE.md "**No bold in body text**", "**Markdown lists render correctly**", "**Avoid emphasis-by-assertion phrasing**", "**Lead with the positive claim**" — all apply.
- CLAUDE.md "**Norwegian-language deliverables**" vocabulary table — applies for Norwegian decks (GF, styre, investor).
- `docs/scripts.md` → `md_to_slides.py` — full documentation of the wrapper, markdown conventions, reference deck pointer.

## Historical references

- `generic/deliverable/2026-10-13_generalforsamling_arsregnskap_2025_slides.md` — the reference deck (annual general assembly presentation for Årsregnskap 2025). First production use of the pipeline.
- `scripts/sunlit_sea_slides_header.tex` — theme definition (colour palette, frame title, footer, `\bignum{}` helper).
- `visual_profile/fonts/` — Everett `.ttf` files loaded by the wrapper at build time.
- `scripts/md_to_slides.py` — the wrapper itself.

## Known pitfalls

- **Using plain `pandoc -t beamer`** — the Sunlit brand palette, fonts and footer come from the wrapper's header-include and font prelude. Plain pandoc produces a generic beamer deck without any of this.
- **Brace-escape in prose**: `{\color{sunlitBlue900}bold text}` in body text gets escaped by pandoc because `{...}` is reserved. Use `\textcolor{sunlitBlue900}{\textbf{...}}` or plain `**bold**` instead. Inside raw tabular blocks pandoc leaves braces alone, so `{\color{...}...}` works there.
- **Everett fonts missing**: if `visual_profile/fonts/` has been moved or renamed, the xelatex run falls back to substitute fonts and the deck looks off-brand. Check the log for `Font ... not loadable` or `substituted ...` warnings.
- **Two-space line breaks in stacked blocks**: without the trailing two spaces, pandoc folds the lines into one paragraph — especially visible on title slides and signature-style attributions.
- **TikZ section dividers with wrong anchor**: `remember picture, overlay` is required for `current page` to resolve correctly. Dropping either option breaks the full-page fill.
- **Not asking before converting**: the "do not convert to docx automatically" rule generalises here — don't produce the PDF speculatively, wait for the explicit "produce the deck".
- **Markdown pipe-tables for key data tables**: pandoc converts pipe-tables faithfully but with less control over column widths and emphasis. If a table is load-bearing (budget, timeline, headline numbers), switch to raw `\begin{tabular}` for proper formatting.
