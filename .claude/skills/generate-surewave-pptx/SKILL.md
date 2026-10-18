---
name: generate-surewave-pptx
description: Produce a SUREWAVE-branded `.pptx` from a Markdown source by passing the SUREWAVE consortium pptx template to pandoc as `--reference-doc`. Trigger when the user asks to "generate the SUREWAVE pptx", "apply the SUREWAVE pptx template", "convert this to a SUREWAVE presentation", or when a `.md` presentation under `surewave/deliverables/` is ready for consortium-branded `.pptx` output (WP8 presentations, final-event talks, interview decks, consortium status presentations). Different brand from Sunlit Sea slides.
---

# generate-surewave-pptx

## When to use

- User asks for a SUREWAVE presentation as `.pptx` in the consortium brand.
- WP8 presentations (talking points, interviews, HRB kickoff), consortium status snapshots, final-event talks, DoA-aligned decks.

**Do not use** for:

- Sunlit Sea branded decks — use `generate-slides` instead (different brand, different pipeline, beamer + xelatex vs. pandoc → pptx).
- Sunlit Sea letters or docx deliverables — use `generate-letter` or the plain pandoc path.
- SUREWAVE `.docx` deliverables — use `generate-surewave-docx` instead.
- SuRE / D6.1 / D6.2 presentations to CINEA — those are typically plain pandoc or produced in Google Slides / PowerPoint directly.

## Procedure

1. **Confirm the source `.md` is a presentation.** The deck convention for pandoc → pptx is one slide per `## Heading` (pandoc default `--slide-level=2`). If the content is a report or a document, the pptx output will look wrong — surface that before converting.

2. **Verify the template path.** Current template: `surewave/background/2026-10-16_surewave_pptx_template.pptx`. The pptx template defines slide masters, colour palette, title/body fonts, consortium chrome and footer. If a newer template arrives (another date-prefixed file in `surewave/background/`), reference the newer one and note the change in the output report.

3. **Verify content conventions** before converting:
   - One slide per `## Heading`.
   - Pandoc → pptx has limited support for raw LaTeX/beamer features — do not use TikZ, `\bignum`, `columns` beamer environments, or `\begin{tabular}` for custom tables. Those features are specific to the Sunlit beamer path.
   - Markdown pipe-tables and bullet lists work. Images with `![caption](path)` work. Fenced code blocks render as monospace text blocks.
   - Mermaid diagrams in fenced code blocks need `mermaid-filter` on PATH; they are rendered to PNG and embedded.
   - Speaker notes: pandoc supports `::: notes ... :::` fenced-div blocks that become PowerPoint speaker notes.
   - External-deliverable stand-alone rule applies when the deck is going outside Sunlit Sea: no repo paths, no task numbers, no "see the earlier draft".
   - Global rules: no bold in body text (`**...**` is reserved for titles), no emphasis-by-assertion phrasing, lead with the positive claim.

4. **Run the conversion:**

   ```bash
   pandoc path/to/deck.md \
     -o path/to/deck.pptx \
     --reference-doc=surewave/background/2026-10-16_surewave_pptx_template.pptx \
     -F mermaid-filter.cmd \
     --slide-level=2 \
     --wrap=none
   ```

   Platform note — on Linux/macOS the filter is `mermaid-filter` (no `.cmd`); on Git Bash / Windows it is `mermaid-filter.cmd`.

5. **Check the rendered output.** Open the `.pptx` in PowerPoint (or Google Slides / LibreOffice Impress if that's the chosen renderer) and verify:
   - SUREWAVE title slide and section layouts come through from the template's slide masters.
   - Slide titles use the template's title font and colour.
   - Body text uses the template's body font and size.
   - Footer, page numbers and consortium strap are consistent with the template.
   - Images and mermaid-rendered PNGs appear in the correct frames and are not clipped.
   - Any speaker notes from `::: notes :::` blocks are present in the Notes pane.
   - Pandoc's pptx output does not try to shape slides against the slide masters perfectly — some manual touch-up in PowerPoint is expected on slide 1 (title) and on image-heavy slides.

6. **Flag what will not survive.** Report back on content that pandoc cannot represent cleanly in pptx and should be handled manually in PowerPoint afterwards:
   - Complex multi-column layouts.
   - Vector diagrams / charts other than mermaid.
   - Animations, transitions, and build-up effects (pandoc has no support).
   - Custom table styling (borders, colour, column widths) beyond simple pipe-table rendering.
   - Any raw-LaTeX blocks (pandoc silently drops them to pptx).

7. **Report back:** source `.md` → output `.pptx` path, template version used, number of mermaid diagrams rendered, number of slides, and a list of items that need manual PowerPoint follow-up.

## Applicable rules

- CLAUDE.md "**Pandoc is the chosen conversion tool**" — pandoc's pptx path is the right first attempt; propose alternative pipelines only if pandoc has been tried and rejected.
- CLAUDE.md "**Do not convert to docx automatically**" — same spirit for pptx: only convert on explicit user order.
- CLAUDE.md "**External deliverables stand alone**" — SUREWAVE presentations are consortium- or public-facing; the stand-alone rule applies in full.
- CLAUDE.md "**No bold in body text**", "**Markdown lists render correctly**", "**Avoid emphasis-by-assertion phrasing**", "**Lead with the positive claim**" — all apply.
- CLAUDE.md "**Mermaid deliverables**" — fenced code blocks + `.mmd` sidecars in the activity's `figures/` folder when the diagram is substantial.
- `docs/pandoc_conversion.md` — Pandoc + mermaid-filter installation.

## Historical references

- T115 — SUREWAVE WP8 presentation talking points (all-project walkthrough).
- T117 — SUREWAVE WP8 final-meeting interview scripts (4 partners, 5 min each).
- T122 — SUREWAVE Horizon Results Booster kickoff (prep for 2026-10-02 call).
- `surewave/deliverables/2026-09-29_surewave_wp8_presentation.md` — WP8 presentation source.
- `surewave/deliverables/2026-10-01_hrb_kickoff_ker_presentation.md` + `.pdf` — HRB kickoff presentation (currently in PDF; pptx version would use this skill).
- `surewave/background/2026-10-16_surewave_pptx_template.pptx` — current consortium pptx template.

## Known pitfalls

- **Pandoc layout-name warnings are expected, not errors.** Pandoc expects the reference `.pptx` to contain slide layouts with exact names like "Title Slide", "Section Header", "Content with Caption", "Blank". The SUREWAVE 2026-10-16 template does not contain all of these names, so pandoc falls back to its *default* (unbranded) layouts for the slides that would have used them. Verified behaviour on `2026-09-29_surewave_wp8_presentation.md`:

  ```
  [WARNING] Powerpoint template warning: Couldn't find layout named "Section Header" in provided reference doc. Falling back to the default included with pandoc.
  [WARNING] Powerpoint template warning: Couldn't find layout named "Content with Caption" in provided reference doc. Falling back to the default included with pandoc.
  ```

  Flag these warnings in the report-back. Content slides using "Title and Content" (the common case) are branded correctly; the warnings only affect section-divider slides and image-with-caption slides. Fix either by (a) accepting the fallback and touching up those specific slides in PowerPoint after conversion, or (b) renaming layouts inside the `.pptx` template to pandoc's expected names using PowerPoint's Slide Master view (template-side fix, not script-side).

- **Wrong template file**: using a Sunlit Sea template or the SUREWAVE `.docx` template for a pptx conversion produces output with mismatched slide masters. Confirm template path before the pandoc call.
- **Expecting the Sunlit beamer features**: raw-LaTeX blocks, TikZ section dividers, `\bignum{}` and `columns` do not survive the pandoc → pptx path — they are silently dropped or rendered as literal code. If the deck needs any of those, it belongs in `generate-slides` (and therefore in the Sunlit beamer pipeline, not the SUREWAVE one). If the deck needs them *and* must be SUREWAVE-branded, the right path is to produce a plain pandoc pptx first and then do the layout work manually in PowerPoint.
- **Slide masters not applied**: pandoc applies the template's slide masters imperfectly. The title slide and the first content slide often need a manual touch-up in PowerPoint afterwards.
- **Mermaid-filter missing or wrong suffix**: as for docx — see `docs/pandoc_conversion.md`.
- **YAML title block**: `title`, `author`, `date` in YAML frontmatter become the title-slide content in pandoc pptx. If the metadata is internal, rename to `internal_title` etc. before converting.
- **Image sizing**: pandoc places images at their native pixel dimensions; `{width=…}` attributes on image references help control sizing. Images that are too big for a slide get clipped silently — verify in PowerPoint after conversion.
- **Not asking before converting**: wait for the explicit "produce the SUREWAVE pptx".
