# Scripts

Persistent helper scripts live in `scripts/` at the repo root — never scattered inside data folders like `generic/`, `sure/`, `funding/`, `gen2/`. Follows the same pattern as the neighbouring `../fjordgata30` project.

## Contents

- [`md_to_letter.py`](#md_to_letterpy) — Markdown → DOCX/PDF on the Sunlit Sea letterhead
- [`md_to_slides.py`](#md_to_slidespy) — Markdown → PDF slide deck in the Sunlit Sea visual profile
- [`md_to_surewave_docx.py`](#md_to_surewave_docxpy) — Markdown → SUREWAVE consortium branded DOCX (cover + body)
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

The wrapper only substitutes the first occurrence of each label, so the SUREWAVE reference tables (Dissemination level definitions, Deliverable type definitions, QA review table) further down the cover are left intact.

Used by the `generate-surewave-docx` skill.

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
```

Used mainly during iteration on `md_to_surewave_docx.py` / `md_to_letter.py` output when the generated docx needs visual inspection without opening Word.

Environment prerequisites: LibreOffice installed on PATH or at the default location above. `cygpath` must be available (ships with Git Bash) for the `/tmp/...` → Windows path conversion.
