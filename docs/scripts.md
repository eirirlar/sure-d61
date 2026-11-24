# Scripts

Persistent helper scripts live in `scripts/` at the repo root — never scattered inside data folders like `generic/`, `sure/`, `funding/`, `gen2/`. Follows the same pattern as the neighbouring `../fjordgata30` project.

## Contents

- [`md_to_pdf.py`](#md_to_pdfpy) — dispatcher: Markdown → PDF via the right Sunlit Sea wrapper (slides / report / letter)
- [`md_to_letter.py`](#md_to_letterpy) — Markdown → DOCX/PDF on the Sunlit Sea letterhead
- [`md_to_slides.py`](#md_to_slidespy) — Markdown → PDF slide deck in the Sunlit Sea visual profile
- [`md_to_sunlit_report.py`](#md_to_sunlit_reportpy) — Markdown → PDF long-form report in the Sunlit Sea visual profile
- [`md_to_surewave_docx.py`](#md_to_surewave_docxpy) — Markdown → SUREWAVE consortium branded DOCX (cover + body)
- [`md_to_surewave_docx_from_delivered.py`](#md_to_surewave_docx_from_deliveredpy) — Markdown → SUREWAVE DOCX built on a copy of an accepted deliverable (default D7.4 v2.0)
- [`md_to_template_pptx.py`](#md_to_template_pptxpy) — Markdown slides → pptx filled into a copy of a reference deck (keeps its layouts and footer)
- [`md_image_to_html.py`](#md_image_to_htmlpy) — rewrite Markdown image refs into HTML `<figure>` blocks
- [`format_docx.py`](#format_docxpy) — post-process Pandoc docx (table borders + column widths)
- [`extract_pdf_images.py`](#extract_pdf_imagespy) — extract embedded images from PDFs
- [`insert_pdf_page_images.py`](#insert_pdf_page_imagespy) — inline image refs into pdftotext `.md`
- [`nbsp_numbers.py`](#nbsp_numberspy) — NBSP between thousand-separator digit groups
- [`clean_investor_updates.py`](#clean_investor_updatespy) — strip mail-headers / signatures from investor updates
- [`eu_proposal_template_format.lua`](#eu_proposal_template_formatlua) — Pandoc Lua filter for EU proposal templates
- [`xlsx_to_md.py`](#xlsx_to_mdpy) — xlsx workbook → one Markdown table per sheet
- [`emf_to_png.ps1`](#emf_to_pngps1) — rasterise `.emf` to `.png` (Windows GDI+)
- [`render_docx_pdf.sh`](#render_docx_pdfsh) — sandboxed LibreOffice docx → PDF (does not trip Windows Controlled Folder Access)
- [`pdf_contact_sheets.py`](#pdf_contact_sheetspy) — PDF pages to contact-sheet images for a page-by-page visual check
- [`check_deprecated_wording.py`](#check_deprecated_wordingpy) — report outdated phrasing listed in `docs/deprecated_wording.md`
- [`rebuild_task_indexes.py`](#rebuild_task_indexespy) — regenerate `TASKS_INDEX.md` and `ARCHIVE_INDEX.md` from the master task files
- [`estimate_yield.py`](#estimate_yieldpy) — preliminary annual AC yield estimator for an FPV site (PVGIS 5.2 + FPV cooling bonus)
- [`build_d74_workbook.py`](#build_d74_workbookpy) — build the SUREWAVE D7.4 cost workbook v3 (Excel) from the v2 workbook
- [`d74_cost_model.py`](#d74_cost_modelpy) — Python reference model for the D7.4 cost workbook (test oracle, v2 replica + corrected v3)
- [`test_d74_cost_model.py`](#test_d74_cost_modelpy) — pytest suite: v2 replica, v3 workbook vs Python, portability, input propagation
- [`d74_changelog.py`](#d74_changelogpy) — v2 → v3 result tables for the D7.4 changelog
- [`hrb_financial_model.py`](#hrb_financial_modelpy) — Sunlit Sea KER1 financial plan: assumptions and Python three-statement model 2027–2031
- [`build_hrb_financial_workbook.py`](#build_hrb_financial_workbookpy) — the same model as an Excel workbook with formulas
- [`test_hrb_financial_model.py`](#test_hrb_financial_modelpy) — pytest suite: statements tie, workbook vs Python in all scenarios
- [`breakwater_classes.py`](#breakwater_classespy) — floating breakwater classes for nearshore sites, indicative cost per metre, coverage formula and standard sites
- [`test_breakwater_classes.py`](#test_breakwater_classespy) — tests: Macagno against D3.2, class criterion, ring calibration against D7.4, coverage geometry

## `md_to_pdf.py`

Dispatcher that produces a Sunlit Sea-styled PDF from any Markdown deliverable, routing to the correct underlying wrapper based on the file's declared template type.

The template is picked in this order:

1. CLI `--template slides|report|letter` (override, mainly for debugging).
2. The `sunlit_template:` field in the file's YAML frontmatter.
3. Inference from the markdown shape — slide-chrome `## {.plain}` + TikZ overlay → `slides`; three or more `## N.`-style numbered sections → `report`; Norwegian signoff (`Vennlig hilsen`, `Mvh`) → `letter`.
4. If still ambiguous: exits with a prompt to add the YAML field.

Convention for new Markdown deliverables that will be rendered to PDF: declare the template explicitly in the YAML header so the dispatcher is deterministic.

```yaml
---
sunlit_template: slides     # or: report, letter
...
---
```

```bash
# Default: writes <input>.pdf next to <input>.md, dispatched by YAML/inference
python scripts/md_to_pdf.py generic/deliverable/2026-10-19_...project_intro.md

# Custom output path
python scripts/md_to_pdf.py path/to/input.md -o path/to/out.pdf

# Explicit override
python scripts/md_to_pdf.py path/to/input.md --template report
```

Behind the scenes the dispatcher invokes `md_to_slides.py`, `md_to_sunlit_report.py` or `md_to_letter.py --pdf`. Each underlying wrapper remains available directly when a specific flag (letter `.docx` output, etc.) or a custom code path is needed.

## `md_to_letter.py`

Produces a `.docx` or `.pdf` of a Markdown file on the Sunlit Sea letterhead (SUNLIT SEA wordmark on the first-page header, cream "A" watermark on every page, Letter page size, 1" margins).

- `.docx` path: pandoc with `--reference-doc <letterhead.docx>` — the letterhead's headers, footers, images, page size, margins and styles are kept; the Markdown becomes the body.
- `.pdf` path (`--pdf`): the wrapper extracts the wordmark + watermark PNGs from the letterhead `.docx` on the fly, writes a `eso-pic` LaTeX header-include that places them at the Word positions (wordmark centred ~0.85 in from top of page 1; watermark full-page background on every page), then calls pandoc with `--pdf-engine=xelatex`. No committed image assets, no manual Word step, no LibreOffice.

Default letterhead: `generic/background/2026-10-10_sunlit_sea_letterhead.docx` (override with `--letterhead`). Default output: sibling file next to the input, with `.docx` or `.pdf` as appropriate (override with `-o`).

```bash
# Default: writes <input>.docx next to <input>.md
python scripts/md_to_letter.py funding/2026-10-15_svar_myndighet.md

# Produce PDF instead
python scripts/md_to_letter.py --pdf funding/2026-10-15_svar_myndighet.md

# Custom output path
python scripts/md_to_letter.py funding/2026-10-15_svar_myndighet.md -o generic/deliverable/2026-10-15_svar_myndighet.docx
```

See the *Letter / letterhead output* section of [`pandoc_conversion.md`](pandoc_conversion.md#letter--letterhead-output) for content-shape conventions.

## `md_to_slides.py`

Produces a PDF slide deck in Sunlit Sea's visual profile (Everett headlines + Arial body, yellow #FFE775 and blue #2F354F accents, dark title / section-divider slides) via pandoc → beamer → xelatex. 16:9 widescreen; thin yellow underline below each slide title; footer with `SUNLIT SEA | Årsregnskap 2025` strap and page counter.

The theme lives in `scripts/sunlit_sea_slides_header.tex` and defines the color palette, frame title, footer, and `\bignum{tall}{beskrivelse}` helper. Everett .ttf files are read from `visual_profile/fonts/` — the wrapper writes a tiny prelude at build time that loads them from the absolute path so XeLaTeX finds them without the fonts being system-installed.

```bash
# Default: writes <input>.pdf next to <input>.md
python scripts/md_to_slides.py generic/deliverable/2026-10-13_generalforsamling_arsregnskap_2025_slides.md

# Custom output path
python scripts/md_to_slides.py path/to/deck.md -o path/to/out.pdf
```

Markdown conventions for the deck:

- `## Heading` begins a new frame (pandoc runs with `--slide-level=2`).
- `## {.plain}` begins a chrome-free frame (no title, no footer); use for title slide, section dividers, closing slide. Fill with a raw `\begin{tikzpicture}[remember picture, overlay] ... \end{tikzpicture}` to paint the whole page.
- For section dividers: `\fill[sunlitYellow] (current page.north west) rectangle (current page.south east);` then nodes for the "Del N" label and section title.
- For big-number highlight blocks: `\bignum{2{,}2 MNOK}{Beskrivelse}` inside a `columns` layout.
- Use raw `\begin{tabular}{@{}lrrr@{}}...\end{tabular}` for tables (markdown pipe-tables render but have less control over spacing / column emphasis). Keep inline `\color{sunlitBlue900}` inside raw tabular — pandoc preserves braces in raw latex blocks but escapes them in prose, so avoid `{\color{...}...}` in body text (use `\textcolor{sunlitBlue900}{\textbf{...}}` or plain `**bold**` instead).

Reference deck: `generic/deliverable/2026-10-13_generalforsamling_arsregnskap_2025_slides.md` (annual general assembly presentation for Årsregnskap 2025).

## `md_to_sunlit_report.py`

Produces a long-form PDF report in Sunlit Sea's visual profile — A4 article class, Arial body, Everett section headings, yellow accent under the document title, "SUNLIT SEA" running strap top-left, page numbers bottom-right, auto-generated table of contents. For documents too long or structurally wrong for a slide deck: work instructions, internal briefs, background memos, multi-section reports.

The theme lives in `scripts/sunlit_sea_report_header.tex` and defines the colour palette, section-heading typography (Everett), running header / footer, widow-and-orphan protection, Swedish hyphenation patterns and TOC styling. Everett `.ttf` files are read from `visual_profile/fonts/` via a prelude the wrapper writes at build time; `\graphicspath{}` is also set so relative image refs in raw `\includegraphics{...}` resolve from the markdown's directory.

```bash
# Default: writes <input>.pdf next to <input>.md
python scripts/md_to_sunlit_report.py generic/deliverable/<name>.md

# Custom output path
python scripts/md_to_sunlit_report.py path/to/report.md -o path/to/out.pdf
```

Markdown conventions for the report:

- `## Heading` renders as a numbered section (`1.`, `2.`, …); numbering is manual in the markdown.
- `### Subheading` renders as a numbered subsection in Everett (`1.1`, `7.3`, …).
- Bulleted lists (`- item`) and bold-run-in paragraphs (`**label.** explanation…`) both render cleanly.
- Raw LaTeX blocks (`\begin{tabular}{...}`) pass through.
- Pandoc's TOC is enabled; the TOC title ("Contents") picks up Sunlit Sea styling automatically.

## `md_to_surewave_docx_from_delivered.py`

Builds a SUREWAVE deliverable `.docx` from Markdown on a copy of a deliverable already accepted on the portal (default `surewave/deliverables/2026-11-20_surewave_d7.4_economic_assessment_rev2.docx`), so cover, styles, headers, footers and page setup are those of a file known to work. Everything belonging to the shell deliverable is removed or overwritten: cover number and title, Deliverable details, version table, executive summary, reviewer names and comments in the Deliverable Review table, the cached table of contents (Word rebuilds it on open), the whole body, the shell's figures in the package, comment authors and document properties. The script prints any paragraph that still contains shell text and is not in the Markdown.

```bash
uv run scripts/md_to_surewave_docx_from_delivered.py <input.md> [--meta <meta.yaml>] [-o <out.docx>] [--shell <delivered.docx>]
```

- Input layout: title block, front sections as `## <Heading>` (e.g. Confidentiality notice, Executive summary), then body sections from `## 1. `. Front sections go before the Deliverable Review table in the shell's executive-summary heading style; body headings shift one level up (`##` → Heading 1).
- Meta: `<input>.meta.yaml` (deliverable_number, title, work_package, task, document_name, lead_beneficiary, dissemination_level, deliverable_type, due_date, delivery_date, version_history, optional author).
- Tables get thin grey borders and a shaded header row, no bold. Pandoc body styles map to the shell's `Normal0`.
- Column widths follow the content (2026-11-24): before pandoc runs, each pipe table's separator row is rewritten so every column gets at least its longest word (capitals counted wider, words split at hyphens and slashes) and the remaining width, at least 40 %, goes to the text-heavy columns; pandoc is run with `--columns=20` so the relative widths apply. Table cells are left-aligned, since the shell's justified body style opens gaps in narrow columns. The Markdown source is not changed. Check the result with `scripts/render_docx_pdf.sh` and a page-by-page look; a table with many text-heavy columns can still need fewer columns in the source.
- Packages: python-docx, docxcompose, pyyaml, lxml (PEP 723, `uv run`). Reuses `inject_update_fields` from `md_to_surewave_docx.py`.
- First use: D8.4 (T150), 2026-11-23.

## `md_to_surewave_docx.py`

Produces a SUREWAVE-branded `.docx` from a Markdown source. Uses the SUREWAVE consortium docx template at `surewave/background/2026-10-16_surewave_docx_template.docx` as the starting document (preserving the cover page, headers, footers, section properties), fills cover placeholders from metadata, converts the markdown body with pandoc + `--reference-doc`, appends it with `docxcompose`, and injects `w:updateFields` so Word evaluates PAGE/NUMPAGES fields on open.

Why pandoc `--reference-doc` alone is not enough: it carries styles across, but it *replaces* the body of the reference document — so the template's cover page (banner, hero image, title block, disclaimer, Deliverable details table) is lost. This wrapper starts from the template as the base document and only *appends* the pandoc-generated body, so the cover survives.

Dependencies (`python-docx`, `docxcompose`, `pyyaml`, `lxml`) are declared inline via PEP 723 script metadata — `uv run` installs them on the fly.

```bash
# Default: writes <input>.docx next to <input>.md, uses the default template
uv run scripts/md_to_surewave_docx.py surewave/deliverables/2026-09-28_surewave_d8.3_technical_brochure.md

# Custom output path
uv run scripts/md_to_surewave_docx.py <input.md> -o <output.docx>

# Different template (when a new version arrives, date-prefixed)
uv run scripts/md_to_surewave_docx.py <input.md> --template surewave/background/<new-template>.docx

# Explicit meta sidecar path
uv run scripts/md_to_surewave_docx.py <input.md> --meta <alt.yaml>
```

Metadata source resolution order:

1. **YAML frontmatter** in the `.md` itself (wins on conflict). Example:
   ```yaml
   ---
   deliverable_number: D8.3
   title: Technical Brochure
   work_package: WP8
   task: "8.3"
   document_name: D8.3 – Technical Brochure
   lead_beneficiary: Sunlit Sea AS
   dissemination_level: PU
   deliverable_type: R
   due_date: "2026-09-30"
   delivery_date: "2026-09-28"
   ---
   ```
2. **Sidecar `<input>.meta.yaml`** next to the `.md`. Use when the `.md` is finalised with a different primary output format (e.g. the Technical Brochure `.md` has a LaTeX titlepage for PDF output and no YAML frontmatter).
3. **No metadata** — cover placeholders stay as the template defaults ("DXX" / "XXXXXXX" / "SINTEF" / "SEN" / "28.11.2022"). The wrapper does not error; it just leaves them.

Known fields substituted on the cover:

| YAML key | Template placeholder | Where it lands |
|---|---|---|
| `deliverable_number` | `DX.X` | Text box at top left of cover |
| `title` | `XXXXXXX` | Text box below deliverable number |
| `work_package` | `WP` row, "XX" value | Deliverable details table |
| `task` | `Task` row, "DXX" value | Deliverable details table |
| `document_name` | `Document name:` row | Deliverable details table (not always present) |
| `lead_beneficiary` | `SINTEF` (default value in template) | Deliverable details table |
| `dissemination_level` | `SEN` (default) | Deliverable details table |
| `deliverable_type` | `R` (default) | Deliverable details table |
| `due_date` | `Due delivery date` row | Deliverable details table |
| `delivery_date` | `28.11.2022` (default) | Deliverable details table |

Optional extra fields (added 2026-11-18 so that hand edits made in Word to the circulated D8.3 docx can be reproduced from source):

| Field | Effect |
|---|---|
| `contributing_beneficiaries` | Fills the `Contributing beneficiaries` cell. |
| `version_history` | List of `[version, date, author, comments]` rows written into the cover's Document Version table; rows are added if the template runs out. |
| `disclaimer_authority` | Replaces "the granting authority" in the cover disclaimer (e.g. with the full CINEA name). |
| `number_figures: true` | Prefixes every figure caption with `Figure N:`. Pandoc's docx writer does not number captions. |
| `strip_horizontal_rules: true` | Drops Markdown `---` rules from the docx body. They stay in the LaTeX/PDF build. |

The last two are implemented in `scripts/surewave_docx_filter.lua`, which the wrapper always passes to pandoc (both behaviours are off unless the meta key is set). To keep a block out of the docx but in the PDF, put it in a fenced ```` ```{=latex} ```` raw block.

The wrapper only substitutes the first occurrence of each label, so the SUREWAVE reference tables (Dissemination level definitions, Deliverable type definitions, QA review table) further down the cover are left intact.

Used by the `generate-surewave-docx` skill.

Known limitation: pandoc pipe tables do not survive the SUREWAVE reference doc. The cells render as loose paragraphs (seen in LibreOffice; reproduced with plain `pandoc --reference-doc` on a minimal file), so the fault is in the template, not the wrapper. Use lists instead of tables in SUREWAVE deliverables, or fix the template's table style first.

### D8.3 technical brochure PDF (`brochure_pandoc_header.tex`)

The D8.3 brochure PDF is built with plain pandoc + xelatex using `scripts/brochure_pandoc_header.tex` (float placement, running footer, TikZ cover), then compressed with ghostscript:

```bash
# from surewave/deliverables/ (Git Bash)
pandoc 2026-09-28_surewave_d8.3_technical_brochure.md -o <scratch>/full.pdf --pdf-engine=xelatex \
  --include-in-header=../../scripts/brochure_pandoc_header.tex \
  -V geometry:margin=2cm -V classoption=svgnames -V colorlinks
```

```powershell
# compression: run from PowerShell, because Git Bash rewrites /ebook into a path
& "C:\Program Files\gs\gs10.08.0\bin\gswin64c.exe" --% -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=surewave\deliverables\2026-09-28_surewave_d8.3_technical_brochure.pdf <scratch>\full.pdf
```

Notes:

- No `--toc`: the table of contents was dropped deliberately (T120 third pass).
- `classoption=svgnames` is required for the `MidnightBlue` colour on the cover.
- `geometry:margin=2cm` and `colorlinks` were reconstructed on 2026-11-18. The September build command was never recorded, so these may differ from the first issue.
- Use pandoc sub/superscript syntax (`CO~2~`, `m^3^`) instead of Unicode `₂`/`³`, because Latin Modern has no such glyphs.
- The build takes about 5–6 minutes.

### SUREWAVE newsletters PDF (`newsletter_pandoc_header.tex`)

Newsletters III–V (T153–T155) are built like the D8.3 brochure: plain pandoc + xelatex with `scripts/newsletter_pandoc_header.tex`, then ghostscript compression. The header gives figure placement, `Figure N:` captions, blue section headings, a running footer, a shaded box (`nlbox`) for the project one-liner and contacts, and a TikZ EU emblem (`\euemblem{2cm}`, no image file needed). Each newsletter sets its own footer text at the top of the Markdown with `\renewcommand{\nlfooter}{SUREWAVE $\cdot$ Newsletter III $\cdot$ December 2026}`.

```bash
# from surewave/deliverables/ (Git Bash)
pandoc 2026-11-20_surewave_newsletter_iii.md -o <scratch>/full.pdf --pdf-engine=xelatex \
  --include-in-header=../../scripts/newsletter_pandoc_header.tex --resource-path=. \
  -V geometry:a4paper,margin=2cm -V classoption=svgnames -V colorlinks -V mainfont="Segoe UI"
```

```powershell
# compression (PowerShell; Git Bash rewrites /ebook into a path)
& "C:\Program Files\gs\gs10.08.0\bin\gswin64c.exe" --% -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile=surewave\deliverables\<newsletter>.pdf <scratch>\full.pdf
```

Notes: use pandoc sub/superscript syntax (`CO~2~`, `10^11^`) rather than Unicode; the build takes under a minute. Each issue has a `_sources.md` companion recording the source of every fact and the provenance of every figure.

### SUREWAVE one-page infographics (`infographic_pandoc_header.tex`, `toolchain_figure.py`)

One-page A4 infographics for SUREWAVE (first use: the modelling-toolchain infographic, T159) are built with plain pandoc + xelatex using `scripts/infographic_pandoc_header.tex`: SUREWAVE template colours (`swdark` #1F5373, `swteal`, `swblue`, `swlight`), no page number, compact lists and headings, a TikZ EU emblem (`\euemblem{1.5cm}`) and `\swrule`. Page geometry, font (TeX Gyre Heros, shipped with TeX Live) and size are set in the Markdown YAML. The SUREWAVE logo is `surewave/images/surewave_logo.png`, cropped from the header image of the consortium docx template.

The toolchain diagram is defined once in `scripts/toolchain_figure.py` (boxes, text lines, arrows; standard library only), which writes the same figure as SVG (for web and LinkedIn reuse) and as TikZ (`.tikz.tex`, read by xelatex with `\input`, so no SVG converter such as rsvg-convert or Inkscape is needed). Edit the script, never the generated files.

Rebuild the infographic in one step with `scripts/build_toolchain_infographic.py` (standard library only; needs pandoc and xelatex on PATH). It regenerates the SVG and TikZ figure, renders the page, and checks with `pdfinfo` that the result is exactly one page (exits with an error otherwise). It writes only the three generated files in `surewave/deliverables/`.

```bash
python scripts/build_toolchain_infographic.py
```

Output: `surewave/deliverables/2026-11-22_surewave_modelling_toolchain_infographic.pdf`. The PDF stays on disk for upload but is not tracked: `.gitignore` excludes `surewave/deliverables/*.pdf`, so anyone with the repo recreates it with the command above. Look at a `pdftoppm -r 110 -png` render before use.

## `md_image_to_html.py`

Rewrites Markdown image references `![caption](path){width=Npx}` into HTML `<figure>` / `<img>` / `<figcaption>` blocks. Reason: Pandoc's `{width=Npx}` image-attribute syntax is Pandoc-only — VS Code preview, GitHub Flavored Markdown and most other renderers show it as literal text after the image. HTML `<img>` width attributes work in every renderer that supports raw HTML in Markdown (essentially all of them), and Pandoc passes them through to its docx/pdf output. Wrapping in `<figure>` + `<figcaption>` also makes the caption visible in every renderer, whereas plain `![alt](path)` shows the alt text only when the image fails to load.

Safe default writes a `<name>.htmlimg.md` sibling; use `--in-place` to overwrite once the sibling looks right. `--dry-run` reports how many image references would be rewritten without touching anything.

```bash
# Safe default — writes gen2/norsmaterials_brief.htmlimg.md
python scripts/md_image_to_html.py gen2/norsmaterials_brief.md

# Overwrite in place (only after dry-run looks safe)
python scripts/md_image_to_html.py --in-place gen2/norsmaterials_brief.md

# Different default width (used when the input has no explicit width)
python scripts/md_image_to_html.py --width 600 gen2/norsmaterials_brief.md
```

Preserves indentation, so images that live under bullet points stay under those bullet points in the output.

## `format_docx.py`

Post-processes a Pandoc-generated `.docx` file to fix two things Pandoc handles poorly by default: (1) tables have no visible borders, and (2) all table columns are given equal width regardless of content. The script uses `python-docx` to add thin grey borders (0.5 pt, `#BFBFBF`) to every cell in every table, and sets column widths per table from a `TABLE_WIDTHS_BY_STEM` dict keyed on the input filename stem (basename without `.docx`).

Dependencies are declared inline via PEP 723 script metadata (`python-docx`), so `uv run` installs them on the fly into a user-local ephemeral env — no system install required.

```bash
# In-place: pandoc first, then format the resulting docx
pandoc generic/background/loeypemelding/2026-07-16_loeypemelding.md -o generic/background/loeypemelding/2026-07-16_loeypemelding.docx
uv run scripts/format_docx.py generic/background/loeypemelding/2026-07-16_loeypemelding.docx

# Or output to a different path
uv run scripts/format_docx.py input.docx output.docx

# Borders only, skip column widths (for docs not in TABLE_WIDTHS_BY_STEM)
uv run scripts/format_docx.py input.docx --borders-only
```

Adapted from the same-named script in `../fjordgata30/scripts/` — mechanics are identical, only `TABLE_WIDTHS_BY_STEM` is Sunlit-Sea-tailored. When a new deliverable with tables is generated, add a new dict entry keyed on the input filename stem, with one width row per table in the order they appear in the document.

## `extract_pdf_images.py`

Extracts embedded images from PDF files into per-document folders. Uses `pypdf` + `Pillow` via `uv run` PEP 723 script metadata — no permanent Python install needed. Preserves original image format (PNG/JPEG/JP2) via each embedded image's own bytes.

Output layout: `<output-dir>/<pdf-stem>/img-<page>-<idx>.<ext>`. Skips existing files without `--force`. Prints per-file summary with images-per-page distribution.

```bash
# Extract from four background PDFs into sure/background/images/<stem>/
uv run scripts/extract_pdf_images.py \
  "sure/background/foo.pdf" "sure/background/bar.pdf" \
  --output-dir sure/background/images/

# Overwrite existing extracted images
uv run scripts/extract_pdf_images.py "sure/background/foo.pdf" --output-dir sure/background/images/ --force
```

Use this when a PDF's text extraction (via `pdftotext`) loses embedded figures, photos or diagrams that the .md conversion still needs to reference. Extracted images can then be linked into the .md file as `![](images/<pdf-stem>/img-XXX-YY.png)`.

Alternative for slide-decks where "the image is the whole slide" (vector graphics + text): use `pdftoppm -png -r 150 file.pdf out_prefix` to render each page as an image. This script targets only embedded raster images.

## `insert_pdf_page_images.py`

Inserts inline markdown image references into a pdftotext-derived `.md` file, one image group per PDF page. Companion to `extract_pdf_images.py`: extraction gives you the image files organised by page; this script hooks them back into the text at the appropriate page boundaries so the images render inline in Markdown viewers and downstream Pandoc conversions.

Expects the `.md` file to contain form-feed (`\f`) page separators as pdftotext outputs them, and expects images at `<images-dir>/<md-stem>/img-<page:03d>-<idx>.*` (the layout that `extract_pdf_images.py` produces).

Images are appended at the *end* of each page's text (readers see the source text first, then the visuals). Safe by default — writes to `<name>.imgref.md` sibling; `--promote` overwrites in place.

```bash
# Dry-run
uv run scripts/insert_pdf_page_images.py \
  sure/background/2025-03-12_uv_minipatch_preliminary_results.md \
  --images-dir sure/background/images/

# Promote after verifying
uv run scripts/insert_pdf_page_images.py \
  sure/background/*.md --images-dir sure/background/images/ --promote
```

### Combined recipe: batch PDF → Markdown with linked images

The two scripts above compose into the standard inbox-processing pipeline (used for T100). Both scripts key on the file **stem**, so the `.md` stem must equal the `.pdf` stem — stage copies of the PDFs under their final slug names first, then convert.

```bash
STAGE=/tmp/stage; OUT=<activity>/background/YYYY-MM-DD_<set_name>
mkdir -p "$STAGE" "$OUT/images"
cp "<inbox>/Some Long Name.pdf" "$STAGE/short_slug.pdf"          # 1. stage with final names

for f in "$STAGE"/*.pdf; do                                       # 2. text (\f page breaks preserved)
  pdftotext -layout -eol unix "$f" "$OUT/$(basename "$f" .pdf).md"
done

uv run scripts/extract_pdf_images.py "$STAGE"/*.pdf --output-dir "$OUT/images/"   # 3. images
find "$OUT/images" -name '*.jp2' -exec sh -c 'convert "$1" "${1%.jp2}.png" && rm "$1"' _ {} \;  # 4. JP2 → PNG

uv run scripts/insert_pdf_page_images.py "$OUT"/*.md --images-dir "$OUT/images/" --promote  # 5. link
```

Step 4 matters: `pdfimages`/`pypdf` hand back JPEG 2000 (`.jp2`) for some scanner and CAD output, and no Markdown viewer renders it. Convert before linking.

Prepend a metadata header (document date, issuer, source path, conversion method) to each `.md` after step 2 — the insert script treats a header before the first `\f` as part of page 1 and leaves it alone.

Non-PDF inbox files go through pandoc in the same pass: `pandoc in.docx -t markdown --wrap=none --extract-media="$OUT/images/<stem>" -o "$OUT/<stem>.md"`. Data files (`.csv`, `.xlsx`) are copied over raw — do not convert them to Markdown.

## `nbsp_numbers.py`

Binds thousands-separated number groups in Markdown with non-breaking space (NBSP, U+00A0) so that pandoc + xelatex does not break numbers like `18 570 858` across line boundaries in narrow PDF table columns. Regex-based, idempotent, character-count-neutral (only swaps space for NBSP inside `\d \d{3}` boundaries).

Safe by default — writes to `<name>.cleaned.md` sibling and prints word/line/char counts (should be identical before and after) plus NBSP substitution count plus sample changed lines. Use `--promote` to overwrite in place after inspecting dry-run output.

```bash
# Dry-run — writes funding/*.cleaned.md sibling
python scripts/nbsp_numbers.py funding/2026-07-14_revisorpakke_prinsippendring_aktivering_nedskrivingstest.md

# Overwrite in place after dry-run looks safe
python scripts/nbsp_numbers.py --promote funding/2026-07-14_revisorpakke_prinsippendring_aktivering_nedskrivingstest.md
```

Character/word/line counts must be identical before and after — a delta of anything other than zero means the regex hit something it should not have. The NBSP substitution count should match the number of thousand-separator boundaries actually in the document. Both are visible in the dry-run output.

Renders as ordinary space in every renderer (PDF, DOCX, VS Code preview, GitHub) — only the line-break behaviour changes.

## `clean_investor_updates.py`

Strips mail-header noise, mid-body Gmail page-print repeats, and trailing signature blocks (`Mvh`, contact-info lines, Google Groups unsubscribe boilerplate) from the investor-update `.md` files under `generic/background/loeypemelding/`. Preserves the YAML frontmatter; leaves body content between top and bottom noise untouched.

**Safe default (no in-place edits).** Writes a sibling `<name>.cleaned.md` for each input. Compare, then either rename manually or re-run with `--in-place`.

```bash
# Safe default — writes generic/background/loeypemelding/*.cleaned.md
python scripts/clean_investor_updates.py generic/background/loeypemelding/*.md

# Dry-run — per-file word-count before/after, no writes
python scripts/clean_investor_updates.py --dry-run generic/background/loeypemelding/*.md

# In-place — overwrites originals; only use after --dry-run looks safe
python scripts/clean_investor_updates.py --in-place generic/background/loeypemelding/*.md
```

The dry-run output flags any file that shrinks to below 70% of its original word count with a `!` marker — that is the pattern that would have caught the earlier truncation incident where two files silently lost ~90% of their content to an over-broad signature-start regex. Always dry-run before batch use.

## `eu_proposal_template_format.lua`

Pandoc Lua filter that makes EU proposal-template documents (EIC Transition, Horizon Europe application forms) readable after a `.docx` → Markdown conversion. The Word templates wrap every guidance note, every answer field and every work-package description in a table. Plain Pandoc renders those as ASCII grid tables hundreds of characters wide (a 160 KB `.docx` produced a 499 KB `.md`), and with `-t gfm` the ones Pandoc cannot express as pipe tables come out as raw HTML.

What the filter does:

| Input | Output |
|---|---|
| 1-column table | header row → blockquote (guidance), body rows → ordinary text |
| label/value table (work-package boxes) | `**Label:** value`, or a bold label followed by the block content |
| simple data table | left alone — stays a real Markdown table |
| `1. **Excellence**` list item | `## Excellence` |
| `Task 1.1: …` paragraph | `### Task 1.1: …` |
| bullet list that is only `{.mark}` guidance | blockquote |
| `[text]{.mark}` | plain text |
| `[text]{.underline}` / `Underline` | bold (italics would nest illegally inside the templates' italic guidance runs) |

Nested `**bold**` inside `**bold**` is collapsed, since Markdown cannot express it.

```bash
# raw.md is the unfiltered `pandoc source.docx -t markdown --wrap=none` output
pandoc raw.md -f markdown -t gfm --wrap=none \
  --lua-filter=scripts/eu_proposal_template_format.lua \
  -o generic/background/eic/2026-09-09_sintef.md
```

Non-destructive by design: it only ever writes the `-o` target, so keep the raw Pandoc conversion next to the formatted one. Verify a run by comparing word counts of the plain-text renderings of both files:

```bash
pandoc IN.md  -t plain --wrap=none | tr -s '[:space:]' '\n' | grep -vE '^[-+|]*$' | grep -c .
pandoc OUT.md -f gfm -t plain --wrap=none | tr -s '[:space:]' '\n' | grep -vE '^[-+|]*$' | grep -c .
```

A small drop (well under 1%) is expected: list numbers and trailing colons disappear when list items and task titles become headings.

## `xlsx_to_md.py`

Converts an `.xlsx` workbook to a Markdown document with one Markdown table per sheet. Uses `openpyxl` (no `pandas` required). Trims trailing empty rows and columns; escapes `|` and collapses newlines inside cells; renders integer-valued floats without the trailing `.0`.

```bash
python scripts/xlsx_to_md.py "input.xlsx" "output.md"
```

Written for the WP8 KPI tracker workbook (5 sheets: communication log, publications, KPIs, media links, options). Reusable for any small workbook that needs to be read as flat markdown rather than kept as a binary.

## `emf_to_png.ps1`

Rasterises `.emf` (Enhanced Metafile) vector files to `.png` for inline preview in Markdown viewers and slide decks. Uses Windows `System.Drawing` (GDI+) — Windows-only.

```powershell
powershell -File scripts/emf_to_png.ps1 -Root surewave/images -Scale 2
```

Recursive by default. Writes a sibling `.png` next to each `.emf` at the given scale (default 2×). Skips files that already have a `.png` sibling unless `-Force` is passed. Leaves the `.emf` original in place; delete the source EMFs separately once the PNGs are verified if you don't want to keep both formats.

Used to rasterise the 83 EMF files under `surewave/images/*/` that were extracted from Word deliverables (most Markdown viewers cannot render EMF inline). After rasterisation the EMF sources were removed; PNG-only is the current stored form.

## `check_deprecated_wording.py`

Reports every hit of the outdated phrases listed in `docs/deprecated_wording.md` (pattern, replacement, decision) in the Markdown files of `surewave/deliverables/` and `docs/`. Skips `background/`, `archive/`, work folders (`*_work/`), delivered documents (D8.3, D7.4), the archive of published posts in `linkedin_posts.md` and lines that quote a rule ("Do not use").

```bash
python scripts/check_deprecated_wording.py [path ...]
```

- Exit code 1 on any hit. Standard library only; reads Markdown, writes nothing.
- Run before any outgoing SUREWAVE document (part of `/check-deliverable`) and whenever a fact in `docs/project_facts.md` changes; add the old phrasing to `docs/deprecated_wording.md` at the same time. First use: T167, 2026-11-24.

## `pdf_contact_sheets.py`

Renders every page of a PDF to a small image (`pdftoppm`) and combines them into contact sheets of eight pages, for a fast page-by-page visual check of a rendered deliverable: table column widths, broken words, page breaks, empty pages.

```bash
OUTDIR="$(pwd)/temp/render" bash scripts/render_docx_pdf.sh <file.docx>
uv run scripts/pdf_contact_sheets.py temp/render/<file>.pdf [-o <out_dir>] [--per 8] [--dpi 45]
```

- Output: `<out_dir>/sheet_NN.png` (default `temp/<pdf stem>_sheets/`).
- Needs `pdftoppm` (poppler) on PATH; Python package pillow (PEP 723, `uv run`).
- Reads only the given PDF and writes only into the output folder. First use: D8.4 (T150), 2026-11-24.

## `md_to_template_pptx.py`

Builds a `.pptx` from a Markdown slide source by filling a copy of a reference deck with python-pptx, keeping the deck's masters, layouts, date and slide-number footer and end slide. Written for the SUREWAVE final review meeting (T168), where the coordinator's review deck has layouts pandoc cannot map ("Title", "End slide") and pandoc drops the footer.

```bash
python scripts/md_to_template_pptx.py surewave/deliverables/2026-12-02_surewave_final_review_wp8.md --pdf
```

The template and the footer date come from the deck's YAML front matter (`pptx_template:` as a repo-relative path, `footer_date:`); `--template` and `--date` override them. `--pdf` also renders a PDF next to the pptx through `render_docx_pdf.sh` (sandboxed LibreOffice, optional; the pptx build itself needs no desktop application). The built `.pptx` of the final review decks are git-ignored: the Markdown is the source, and the coordinator's review deck is kept as `surewave/background/2026-11-23_surewave_final_review_template.pptx`.

- Input: Markdown with one `## Heading` per slide; `{layout="Title"}` / `{layout="End slide"}` after a heading picks a layout (default "Title and Content"); `-` bullets with two-space sub-bullets; one pipe table per slide; `![caption](path){side=right|full}` for an image; `::: notes` blocks become speaker notes. YAML front matter is skipped.
- Output: `<deck>.pptx` next to the source (or `-o`). The template's own slides are dropped; the date and slide-number placeholders are cloned from its first content slide, with `--date` replacing the template's automatic date field by fixed text.
- Requires python-pptx and Pillow; `--pdf` also needs LibreOffice and bash.
- Layout: the content area runs from below the template's title to above its footer, aligned with the title; body 22 pt, sub-bullets 19 pt, tables 16 pt.
- Limits: one table and one image per slide; text height is estimated, so check the render for overflow.

## `render_docx_pdf.sh`

Converts a `.docx` to `.pdf` via LibreOffice headless. **Always use this wrapper instead of calling `soffice` directly** when rendering docx on Windows — a bare `soffice --headless --convert-to pdf` triggers Windows "Protected folder access blocked" alerts for `%userprofile%\Documents` because LibreOffice's default user profile initialises paths there.

The wrapper mitigates this by passing `-env:UserInstallation=file:///<tempdir>` to point LibreOffice at a disposable profile directory per invocation. It also adds `--nologo`, `--nolockcheck` and `--norestore` to suppress other noisy startup behaviour. The temp profile is cleaned up on exit via `trap`.

```bash
# Convert one or many docx files; PDFs land in /tmp/sw_pdfs/<stem>.pdf
scripts/render_docx_pdf.sh <input.docx> [<input.docx> ...]

# Override LibreOffice path (default: /c/Program Files/LibreOffice/program/soffice.exe)
SOFFICE=/other/path/soffice.exe scripts/render_docx_pdf.sh <input.docx>

# Override output directory (default: /tmp/sw_pdfs)
OUTDIR=/some/other/dir scripts/render_docx_pdf.sh <input.docx>

# Spreadsheets: recalculate all formulas on load, so charts and formula cells
# show current values instead of the cached ones stored in the file
LO_RECALC=1 scripts/render_docx_pdf.sh <input.xlsx>
```

The wrapper also accepts `.xlsx` and other formats LibreOffice can open. Each output is named `<stem>.pdf`.

Used mainly during iteration on `md_to_surewave_docx.py` / `md_to_letter.py` output when the generated docx needs visual inspection without opening Word.

Environment prerequisites: LibreOffice installed on PATH or at the default location above. `cygpath` must be available (ships with Git Bash) for the `/tmp/...` → Windows path conversion.

## Google Sheets models: `fetch_gsheet.py`, `compare_gsheet_xlsx.py`

A Drive download of a Google Sheet to `.xlsx` is lossy: functions Excel lacks are wrapped in `__xludf.UNSUPPORTED(...)` with a frozen value, and formulas can be replaced by their last result without any trace in the file. Analysis of a model built in Google Sheets therefore starts from an API snapshot, not from a download (rule in `CLAUDE.md`, skill `fetch-gsheet-formulas`).

```bash
python scripts/fetch_gsheet.py <sheet link or ID> [--out surewave/background] [--name surewave_d7.4_costs]
python scripts/compare_gsheet_xlsx.py <snapshot.json> <download.xlsx> [--out report.md]
python -m pytest -p no:cacheprovider scripts/test_compare_gsheet_xlsx.py     # ~15 s, no API needed
```

- `fetch_gsheet.py` reads the sheet with the Google Sheets API (`spreadsheets.get`, `includeGridData`): for every cell the text as entered (formula or typed value) and the value Google computed, plus named ranges, sheet properties and the Drive last-modified time. Writes `<date>_<name>_gsheet_snapshot.json` (full response) and `.md` (per sheet: every formula, every constant, spill cells marked).
- `compare_gsheet_xlsx.py` compares the snapshot with a download cell by cell and writes `<date>_<name>_gsheet_vs_download.md`: formulas lost in the download, formulas wrapped as UNSUPPORTED, formula text that differs, formulas only in the download, typed values that differ, computed values that differ, cells or sheets on one side only. Formula text is compared after removing Excel prefixes (`_xlfn.` etc.), an outer `ARRAYFORMULA(...)`, whitespace and case outside string literals.
- The test builds a fake snapshot from the D7.4 download itself and checks that the self-comparison is clean and that planted differences are caught.
- Sign-in: an OAuth client of type "Desktop app" in `secrets/credentials.json` (git-ignored, per machine; created in Google Cloud Console with the Google Sheets API and the Google Drive API enabled). Scopes are read-only (`spreadsheets.readonly`, `drive.metadata.readonly`). The first run opens the browser for consent and stores `secrets/token.json`; the user runs it, Claude does not start it.
- Not covered: Apps Script bound to the sheet. Check Extensions → Apps Script in the sheet by hand.
- Packages: `google-api-python-client`, `google-auth`, `google-auth-oauthlib`, `openpyxl`, `pytest`.
- The sign-in URL is printed (no browser is opened); Claude runs the script in the background and gives the user the URL, the browser then redirects to localhost and the script continues.

### `fetch_drive_file.py`

```bash
python scripts/fetch_drive_file.py <Drive link or file ID> <output path>
```

Downloads an uploaded Drive file (xlsx, pdf, docx, …) byte for byte (`files.get` with `alt=media`), sets the output's modification time to the Drive last-modified time and prints the Drive metadata (name, MIME type, size, MD5, created and modified time, version). Native Google files are refused; use `fetch_gsheet.py` for those. Use it for xlsx files stored on Drive and edited in Google Sheets, such as the D7.4 cost model: the Sheets API cannot read them, and a "Download as xlsx" from Google Sheets is a re-save. Own token `secrets/token_drive.json`, scope `drive.readonly`; sign-in URL printed as for `fetch_gsheet.py`.

## SUREWAVE D7.4 cost model (T157)

Four scripts maintain the D7.4 techno-economic cost workbook. The deliverable is the Excel workbook; the Python code exists to build it reproducibly and to test it. No desktop applications (Excel, LibreOffice) are needed, so the scripts run on any machine with Python.

Python packages: `openpyxl`, `xlsxwriter`, `formulas` (pulls in `numpy`), `pytest` for the tests (`pip install openpyxl xlsxwriter formulas pytest`).

### `build_d74_workbook.py`

```bash
python scripts/build_d74_workbook.py surewave/background/2025-09-05_surewave_d7.4_costs_v2.xlsx <out.xlsx>     # ~2 min
```

Carries the v2 input sheets over unchanged (plus the end-of-life inputs appended to `in_gen`), and rebuilds `pontoons`, `out_loc`, `cf` (year-by-year cash flows), `summary`, `sens_*` and `README` with formulas that work in desktop Excel. Case columns: 27 main cases plus 45 sensitivity cases (discount rate 2–10 %, subsea cable, pontoon design). Pipeline: `build_openpyxl()` assembles the formulas, `evaluate()` calculates every formula with the `formulas` library, and `write_with_results()` writes the file with xlsxwriter, storing each formula's result next to it, so Excel shows numbers even in Protected View. `evaluate(..., inputs=..., model=...)` recalculates after changing input cells without reloading (~20 s).

### `d74_cost_model.py`

Reads the input sheets of a v2 or v3 workbook. `v2_outputs(inp, case)` reproduces v2 exactly, errors included. `v3_outputs(inp, case, fixes=..., overrides=...)` is the corrected model; `fixes` is a subset of `V3_FIXES` (default: all), so each correction can be switched off to measure its effect; `overrides` takes `discount_rate`, `cable` and `pontoon_design` for sensitivity cases. With all fixes it also returns every out_loc row and the year-by-year cash flows (`o["cf"]`), so every workbook cell has an independent expected value. Command line: `python scripts/d74_cost_model.py <xlsx> --mode v2|v3 --cases m_10 b_10`.

### `test_d74_cost_model.py`

```bash
python -m pytest -p no:cacheprovider scripts/test_d74_cost_model.py     # ~2.5 min
```

15 tests. Builds v3 in a temp folder and evaluates it with `formulas`. Checks:

- v2 replica vs cached v2 values (27 × 31).
- Every formula cell of v3 (62,207) has an expected value from the Python model (coverage test), and every result matches (input variants, inter_gen, pontoon grid, all out_loc rows in all 72 columns, every cf cell, summary, sensitivity sheets).
- The delivered file stores the same formulas and results.
- Every number fits its column in its number format (no `###`, with a negative control).
- No error values, non-portable functions or defined names.
- Every input used or documented-unused.
- Input changes propagate and agree with the model (pontoon price; discount rate with an end-of-life factor).
- IRR, freight-band, pontoon and cash-flow-timing unit tests.

Run after any change to the builder, the model or the v2 inputs. `-p no:cacheprovider` keeps `.pytest_cache` out of the repo.

### `d74_changelog.py`

```bash
PYTHONIOENCODING=utf-8 python scripts/d74_changelog.py <v2.xlsx> [<v3.xlsx>]
```

Prints Markdown tables: base-case results v2 vs v3, and the leave-one-out effect of each correction on the 10 MW cases. With a v3 file it also checks the stored results against the model. Used for `surewave/deliverables/2026-11-20_surewave_d7.4_costs_v3_changelog.md`.

## `rebuild_task_indexes.py`

Regenerates `TASKS_INDEX.md` and `ARCHIVE_INDEX.md` from `TASKS.md` and `ARCHIVE.md`. Both index files are flat per-task TOCs — one line per task with status marker, title and a GitHub-style anchor link into the source file — so a reader does not have to grep the master files to see what is open or what has been solved.

Standard library only; no PEP 723 dependencies.

```bash
# Rewrite both index files from current TASKS.md + ARCHIVE.md
python scripts/rebuild_task_indexes.py

# Check for drift (exits non-zero if the stored indexes do not match
# what regeneration would produce)
python scripts/rebuild_task_indexes.py --check
```

Run after any edit that touches a task header in `TASKS.md` or `ARCHIVE.md`: status toggle, title change, new task, resolution block, or move between the two files. Never hand-edit `TASKS_INDEX.md` or `ARCHIVE_INDEX.md`; the next regeneration will overwrite the edit.

Anchor rule mirrors GitHub's: lowercase the full heading text, replace whitespace with hyphens, strip anything that is not ASCII alphanumeric / hyphen / underscore, collapse repeated hyphens, strip leading/trailing hyphens. Handles the zero-padded T-numbers in this repo (`T01`…`T09`) and the unpadded ones from `T10` onward via the same regex.

Ported from `../stotte/.claude/skills/archive-tasks/archive_tasks.py` (index portion only — this repo keeps task archiving as a manual explicit-ask move rather than as a script).

## `estimate_yield.py`

Preliminary annual AC yield estimator for a floating-PV site. Produces a six-section *Mulighetsstudie*-style Markdown report matching the Sunlit Sea *Simuleringsrapport* format (reference artefact: `generic/background/2026-09-17_simuleringsrapport_blekinge_mulighetsstudie.pdf`). Rendered via `md_to_sunlit_report.py` through the YAML frontmatter `sunlit_template: report`.

Calls PVGIS 5.2 (EU JRC, free, no key) for POA irradiation (via PVcalc at `loss=0`) and GHI (via MRcalc). Computes yield as `E = POA × kWp × PR × (1 + FPV cooling bonus)` where PR comes from the user-supplied loss decomposition (nine named components summing to 10 % by default). PEP 723 inline dependencies (`requests`, `pyyaml`, `matplotlib`); `uv run` installs on the fly.

Minimum input: `--lat`, `--lng`, and either `--kwp` (direct capacity) or `--area` (available water surface in m², capacity derived from panel geometry). Everything else defaults, and every default appears in the output. Full methodology in [`energy_yield_methodology.md`](energy_yield_methodology.md).

```bash
# Area-based (preferred when available water surface is the fixed quantity)
uv run scripts/estimate_yield.py \
  --lat 56.63 --lng 14.65 --area 30000 --panel-wp 750 \
  --location-name "Blekinge/Kronoberg, Sverige" \
  --md-out generic/deliverable/<name>.feasibility_study.md

# Capacity-based (when kWp is the fixed quantity)
uv run scripts/estimate_yield.py \
  --lat 55.6915 --lng 12.0809 --kwp 35 \
  --location-name "DTU Risø, Roskilde" \
  --md-out generic/deliverable/<name>.feasibility_study.md

# From a YAML input file (CLI flags still override)
uv run scripts/estimate_yield.py --yaml site.yaml --md-out out.md

# Override loss components (each --loss-<component> flag independent)
uv run scripts/estimate_yield.py --lat ... --kwp ... \
  --loss-temperature-coefficient 4.0 --loss-soiling 0.2 \
  --fpv-cooling-bonus 3.5 --md-out out.md

# PDF rendering through the dispatcher (reads sunlit_template: report from YAML)
python scripts/md_to_pdf.py <name>.feasibility_study.md
```

Azimuth uses the compass convention (0 = N, 90 = E, 180 = S, 270 = W); the script converts internally to PVGIS aspect. All nine loss components (temperature coefficient, inverter, DC cable, AC cable, mismatch, soiling, LID, availability, transformer) are independently adjustable via `--loss-<name>` flags.

**Over-sea handling.** PVGIS refuses lat/lng that fall over open water. The script catches the error and auto-nudges to the nearest land grid cell in an expanding 500 m-step search out to ~5 km. Because the PVGIS data grid is ~5 km, the nudged value is an acceptable approximation for a near-shore FPV site. The nudged coordinate appears in the assumption audit (Section 6) when nudging happened. Sites farther than 5 km from the nearest land point error out — those need a different data source.

**PVGIS cross-check.** The estimator displays PVGIS's own AC yield at `loss=0` (crystSi model with internal temperature and spectral derating) alongside the user-component-based figure. When the two PR values diverge by more than 1 pp, the report flags the component list as optimistic or conservative relative to PVGIS. This keeps the user-supplied loss decomposition honest.

Used by the `estimate-yield` skill, which drives the script and routes the output through `md_to_pdf.py` for PDF rendering in the Sunlit Sea visual profile. The script is standalone — the skill is a convention wrapper around it, not a hard dependency.

## `fill_hrb_g2m_templates.py`

Fills the Horizon Results Booster (META Group) G2M templates from Markdown sources: characterisation table (`.docx`), exploitation roadmap (`.docx`), risk assessment and priority map (`.xlsx`), BOSAT self-assessment questionnaire (`.xlsx`), Lean Canvas (`.pptx`) and Business Plan (`.docx`). Edits the OOXML parts directly with `lxml` so the BOSAT radio-button form controls, charts, comments and hidden sheets survive (openpyxl would drop them). Never modifies the template; always writes a new output file.

```bash
python scripts/fill_hrb_g2m_templates.py characterisation <template.docx> <source.md> <out.docx>
python scripts/fill_hrb_g2m_templates.py roadmap          <template.docx> <source.md> <out.docx>
python scripts/fill_hrb_g2m_templates.py risk             <template.xlsx> <source.md> <out.xlsx>
python scripts/fill_hrb_g2m_templates.py bosat            <template.xlsx> <source.md> <out.xlsx>
python scripts/fill_hrb_g2m_templates.py lean             <template.pptx> <source.md> <out.pptx>
python scripts/fill_hrb_g2m_templates.py bizplan          <template.docx> <source.md> <out.docx>
```

Source conventions:

- docx kinds: one `## <field label>` section per template row (labels matched ignoring case and punctuation); the KER title comes from `## KER name` (characterisation) or `## KER title` (roadmap). `-` lists become bullet paragraphs; Markdown tables are flattened to one line per row.
- `risk`: one Markdown table with columns Category | Risk | Crit. | Prob. | Intervention | Feas.; categories as in the template (max 5 rows each). Risk grade and conclusion are written as cached values and the workbook is flagged for full recalculation on open. Rows whose text needs more than the template's fixed height are grown (about 50 characters per line in the risk column, 75 in the intervention column).
- `bosat`: one Markdown table Code | Selected answer | Note, answer text verbatim from the questionnaire option. The script writes the option index to the hidden `H` cell, which drives the score and the radar chart. It marks each option in column E as `[x]` (chosen) or `[ ]`, and removes the template's radio buttons (from the sheet's `<controls>`, the `ctrlProps` parts with their rels and content types, and the legacy VML drawing). The group-box controls are kept. The radio buttons were dropped because LibreOffice does not support Excel option-button groups linked to a cell: on opening, it overwrites the linked `H` cells with TRUE/FALSE and shows every button unticked. With text marks, the output looks the same in Excel and LibreOffice. To produce a PDF, use `LO_RECALC=1 scripts/render_docx_pdf.sh <out.xlsx>`, so that the chart is drawn from the current scores. KER name comes from the H1 title after the em dash.
- `lean`: one `## <box>` section per canvas box (Problem, Solution, Key metrics, Unique Value Proposition, Unfair advantage, Channels, Customer segments, Cost structure, Revenue streams), with `### Alternative solutions` under Problem and `### Early adopters` under Customer segments, plus `## KER name`. Line 3 of the file carries the date (`14 November 2026`) and `Iteration #N`. The script keeps the template's red box headings, removes the hint text and inserts the content as 8 pt bullet paragraphs (plain paragraphs for non-list text). Keep each box short: the boxes do not grow. Render with `scripts/render_docx_pdf.sh <out.pptx>` to check fit.
- `bizplan`: one `## <chapter>` section per template chapter to fill, matching the template's Heading 1 text (The organisation, The product/service, The market, The business model and marketing strategy, and so on). Chapters without a section keep the template's yellow guidance text, so the plan can be filled in instalments. Inside a section: `### ` becomes a Heading 2 (numbered by the template), `- ` items use the template's bullet list, lines starting `1. ` stay as separate numbered paragraphs, and Markdown tables become Word tables (template table grid, shaded header row, 9 pt, left-aligned). The KER name for the title comes from the H1 after the em dash and replaces `[name of the KER]`.

Templates live in `surewave/background/` (`*_hrb_g2m_*_template.*`). First used in T141. The T141 outputs are written to `surewave/deliverables/2026-11-11_hrb_g2m_ker1/` under META Group's original file names without the template marker (an exception to the date-prefix convention, so the recipient can match each file to its template), e.g.:

```bash
B=surewave/background D=surewave/deliverables O="$D/2026-11-11_hrb_g2m_ker1"
python scripts/fill_hrb_g2m_templates.py characterisation $B/2025-03-10_hrb_g2m_characterisation_table_template.docx $D/2026-11-11_surewave_hrb_characterisation_table_ker1.md "$O/02_G2M_Characterisation table.docx"
python scripts/fill_hrb_g2m_templates.py roadmap $B/2024-11-29_hrb_g2m_exploitation_roadmap_template.docx $D/2026-11-11_surewave_hrb_exploitation_roadmap_ker1.md "$O/06_G2M_exploitation roadmap.docx"
python scripts/fill_hrb_g2m_templates.py risk $B/2025-12-09_hrb_g2m_risk_assessment_priority_map_template.xlsx $D/2026-11-11_surewave_hrb_risk_assessment_ker1.md "$O/10_G2M_Risks_Assessment_and_Priority_Map.xlsx"
python scripts/fill_hrb_g2m_templates.py bosat $B/2024-02-22_hrb_g2m_bosat_template.xlsx $D/2026-11-11_surewave_hrb_bosat_ker1.md "$O/11_G2M_BOSAT.xlsx"
python scripts/fill_hrb_g2m_templates.py lean $B/2023-11-23_hrb_g2m_lean_canvas_template.pptx $D/2026-11-13_surewave_hrb_lean_canvas_ker1.md "$O/09_G2M_Lean Canvas.pptx"
python scripts/fill_hrb_g2m_templates.py bizplan $B/2024-11-29_hrb_g2m_business_plan_template.docx $D/2026-11-14_surewave_hrb_business_plan_ker1.md "$O/12_G2M_Business_Plan.docx"
```

The `lean` kind and the row-height growth in `risk` were added in T143; the `bizplan` kind in T144.

## `hrb_financial_model.py`

Single source of the assumptions and an independent Python implementation of the Sunlit Sea KER1 financial plan (Horizon Results Booster, T158): income statement, cash flow and balance sheet for 2027–2031 in kEUR, four scenarios for public funding (`base`, `eic`, `eu_upside`, `downside`, set by the switches `sw_sure_ext`, `sw_eic`, `sw_eupi`), sensitivities, a worked unit-economics example for a 3.2 MWp Norwegian plant, and a second worked example (`breakwater_example`, `BW_EXAMPLE`) for a kit-buyer plant with a light breakwater on an inland lake, using `scripts/breakwater_classes.py`. The EIC scenario includes the first commercial plant at the demonstrator lake in 2031 (`eic_followon_mw`). Assumptions are in the `INPUTS` (scalar), `YEARLY` (per year) and `UNIT` dictionaries, each with unit and source note; notes marked `[CONFIRM]` are estimates without a primary figure. Contains Sunlit Sea's costs, prices and pipeline: confidential.

```bash
python scripts/hrb_financial_model.py                                  # summary of all scenarios
PYTHONIOENCODING=utf-8 python scripts/hrb_financial_model.py --md      # Markdown tables used in the plan
PYTHONIOENCODING=utf-8 python scripts/hrb_financial_model.py --md --scenario base
```

`compute(scenario, overrides)` returns every model line per year; `overrides` replaces any input by name (used for sensitivities, including the combined commercial downside). `unit_economics()` (with opex escalation, inverter replacement and the investment support needed to match the host's value), `kpis()` and `breakeven_kit_mw()` (scenario-aware; result before tax or EBITDA, with or without EPC) give the headline figures. `quarterly_cash()` allocates the 2027–2028 annual flows to quarters with stated timing assumptions (quarters add up to the annual net cash flow), `outlook()` gives an indicative EBITDA for 2032–2035, `leverage_table()` EBITDA at different kit volumes and `cap_table()` indicative ownership after the two rounds. Generation 2 development before first use (2027) is capitalised with its grants deferred, as in the 2025 accounting policy (input `capitalise`). Standard library only. The tables in `surewave/deliverables/2026-11-22_surewave_hrb_financial_plan_ker1.md` are pasted from the `--md` output; regenerate and re-paste after changing an assumption.

## `build_hrb_financial_workbook.py`

```bash
python scripts/build_hrb_financial_workbook.py surewave/deliverables/2026-11-22_surewave_hrb_financial_plan_ker1.xlsx     # ~3 s
```

Writes the model as a workbook with formulas (sheets `README`, `inputs`, `yearly`, `model`, `unit`), so readers can change inputs and see the statements update; the `model` sheet ends with a balance check. Saved in the base scenario. Reuses `evaluate()` and `write_with_results()` from `build_d74_workbook.py`, so every formula's result is stored next to it. The output file is git-ignored (rebuild it from the script). Python packages: `openpyxl`, `xlsxwriter`, `formulas`.

## `test_hrb_financial_model.py`

```bash
python -m pytest -p no:cacheprovider scripts/test_hrb_financial_model.py     # ~5 s
```

Checks that the three statements tie in every scenario, that every model and unit-economics cell of the workbook equals the Python model in all four scenarios (switches set through the inputs sheet), that the delivered file stores the results and uses only portable functions, the direction of key inputs, a minimum cash buffer, hand-computed unit-economics values, and the break-even-volume function. Run after any change to the model or the builder.

## `breakwater_classes.py`

Light, medium and heavy floating breakwater classes for mild, medium and rough nearshore wave conditions, with weak, medium and strong anchoring (T162). Plus a coverage formula (T163) that turns plant capacity, exposure sector and class into a breakwater layout (arc, straight or ring), length, units and cost, with an optional host share for dual-use breakwaters.

```bash
PYTHONIOENCODING=utf-8 python scripts/breakwater_classes.py --md              # tables for the note (~20 s)
python scripts/breakwater_classes.py --site 3200 60 medium --host-share 0.5   # one site: kWp, exposure in degrees, class
```

Physics:
- Macagno transmission (as in D3.2 and D5.1), integrated over fetch-limited JONSWAP spectra (SPM 1984 growth curves, adjusted wind).
- Two sizing criteria on the transmitted spectrum: short waves of 3 s and less, and the total height for the platform.
- `search_section()` finds the lightest cross-section per wave class; `roll_period()` gives a rough stability check.
- The end extension uses a straight-edge diffraction approximation.

Costs are built up from the D7.4 v2.0 10 MW ring: material, pontoon installation, anchors and chains, from cost model v3. Assumptions cover what D7.4 does not contain: fabrication, couplings and fenders, transport, supplier factor, mobilisation, open-arc anchoring.

Reference values are in `REF` with their source; assumptions to confirm are in `ASSUMPTIONS`. Used by `surewave/deliverables/2026-11-23_surewave_breakwater_classes_nearshore.md`. Standard library only.

## `test_breakwater_classes.py`

```bash
python -m pytest -p no:cacheprovider scripts/test_breakwater_classes.py     # ~20 s
```

Checks:
- Macagno reproduces D3.2's result for the SUREWAVE unit and does not overflow.
- The dispersion and growth-curve helpers, and that the spectrum without a breakwater returns Hs.
- Every class meets both criteria, and no chosen class is lighter than the search result.
- Class costs are ordered and below the open-sea reference, and the heavy material cost equals D7.4 per metre.
- The ring geometry is within 10 % of D7.4's 1,120 m.
- Coverage is monotonic with the full-ring cap, cost per kWp falls with plant size, and the host share works.
