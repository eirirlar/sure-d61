# Sunlit Sea – working repo

Working repository for Sunlit Sea's ongoing activities, organised by **activity** (top-level folder per activity) with a single T-numbered task sequence across the whole repo.

Activities:

- `sure/` – SuRE WP6 (Horizon Europe FPV model chain, D6.1 delivered, D6.2 in preparation)
- `gen2/` – Gen 2 product development (P3 → P4 → P5)
- `funding/` – Grants, EU reporting, financial

Repo-level context and working rules are in `CLAUDE.md`. Task list is in `TASKS.md`; closed tasks in `ARCHIVE.md`.

**Single README:** this file is the only README in the repo. Do not create per-folder README files — describe folder contents here, in the *Activity contents* section below.

---

## PDF text extraction

Sources under `background/` and `sure/background/` are mostly PDF. Always convert to text with `pdftotext` before reading — do **not** open PDFs page-by-page with the Read tool, it is expensive and loses structure.

```bash
pdftotext -layout "sure/background/somefile.pdf" - > sure/background/somefile.txt
```

`-layout` preserves columns and tables reasonably. Drop it if the layout produces artefacts. Regenerate text extractions when the underlying PDF changes.

---

## Document conversion (Pandoc)

Pandoc is the chosen conversion tool for `.docx`, `.pptx` and `.pdf`. All conversions in this project must support Mermaid diagrams inline in the Markdown source (e.g. `sure/deliverables/report_d6.1.md` embeds Mermaid in fenced code blocks). This is handled by **`mermaid-filter`** — a Pandoc filter that intercepts ```` ```mermaid ```` blocks, renders them to PNG at conversion time and embeds the images in the output. The filter must be system-installed (not `node_modules/` per project).

### Prerequisites – installation

The project needs three system packages: `pandoc` (conversion), **Node managed via nvm** + `mermaid-filter` (mermaid rendering), and TeX Live with xelatex (PDF only). Node is installed via `nvm` (Node Version Manager) so the Node version is explicit and user-local — not tied to the system package manager.

**Windows (Chocolatey, PowerShell as administrator):**

```powershell
choco install pandoc
choco install nvm
# Open a new PowerShell/CMD for nvm to appear on PATH:
nvm install lts
nvm use lts
npm install -g mermaid-filter
# For PDF: TeX Live 2026 (download installer from https://tug.org/texlive/)
```

**Linux (Ubuntu/Debian):**

```bash
sudo apt install pandoc
sudo apt install texlive-xetex texlive-fonts-extra   # for PDF
```

Install nvm by following the command from the README at <https://github.com/nvm-sh/nvm> (the install-script URL has a version number that changes — use the official one). Then:

```bash
# After nvm-install, start a new shell or: source ~/.bashrc
nvm install --lts
nvm use --lts
npm install -g mermaid-filter    # note: no sudo – nvm is user-local
```

**Manual Chromium download (critical on Node 24+):** `mermaid-filter` pulls in puppeteer 19 (outdated), and the install hook that should download Chromium silently skips on modern Node (24+). Without Chromium the filter fails with `spawn … chrome.exe ENOENT`. Run the download manually after `npm install -g mermaid-filter`:

```bash
# Windows (Git Bash) – adjust the Node version in the path if needed:
cd /c/ProgramData/nvm/v<version>/node_modules/mermaid-filter/node_modules/puppeteer
node install.js

# Linux (nvm):
cd ~/.nvm/versions/node/v<version>/lib/node_modules/mermaid-filter/node_modules/puppeteer
node install.js
```

End result: Chromium (~150 MB) downloaded to `~/.cache/puppeteer/chrome/win64-<revision>/` (Windows) or `~/.cache/puppeteer/chrome/linux-<revision>/` (Linux). One-time per machine.

**Fallback – point to an already-installed Chrome/Edge:** If manual download fails, point puppeteer at a system-installed Chromium-based browser:

```bash
# Windows – Chrome:
export PUPPETEER_EXECUTABLE_PATH="/c/Program Files/Google/Chrome/Application/chrome.exe"
# Windows – Edge (also Chromium):
export PUPPETEER_EXECUTABLE_PATH="/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
# Linux:
export PUPPETEER_EXECUTABLE_PATH=/usr/bin/google-chrome
```

Add to `~/.bashrc` for permanent effect.

**Note on nvm and `npm -g`:** With nvm, everything is installed user-locally under `~/.nvm/versions/node/<version>/`. Never use `sudo npm install -g` — it breaks PATH and creates write-permission chaos.

**Note on Ubuntu <22.04 / minimal installs:** Puppeteer-Chromium needs a set of shared libraries that normally come with desktop installs. If mermaid-filter fails with "missing library", run: `sudo apt install libnss3 libatk-bridge2.0-0 libxkbcommon0 libgbm1 libasound2`.

### Usage – standard commands

Runtime environment: **Git Bash on Windows** (MINGW64) is standard in this project. On Linux/macOS replace `mermaid-filter.cmd` with `mermaid-filter` — see the platform note below.

**DOCX (the D6.1 / D6.2 delivery format):**

```bash
cd sure/deliverables
pandoc report_d6.1.md -o "D6.1 Sunlit model chain_v8.docx" -F mermaid-filter.cmd --toc --toc-depth=2
```

**PDF:**

```bash
cd sure/deliverables
pandoc report_d6.1.md -o report_d6.1.pdf \
  -F mermaid-filter.cmd \
  --pdf-engine=xelatex \
  -V documentclass=scrartcl \
  -V geometry:margin=1in \
  -V mainfont="Times New Roman" \
  -V monofont="Consolas" \
  --number-sections=false
```

Explanation of the flags:

| Flag | Effect |
|---|---|
| `-F mermaid-filter.cmd` | Pandoc filter that pre-processes the AST and replaces mermaid blocks with rendered PNGs. Works on inline mermaid in the `.md` and on blocks imported via `include`. No effect if the `.md` has no mermaid – safe to keep as a default flag. |
| `--pdf-engine=xelatex` | Uses xelatex from TeX Live (needed for Unicode characters – "≥", "–", "€" – and TrueType fonts). |
| `-V documentclass=scrartcl` | KOMA-Script article class – cleaner typography and better margin handling than the default `article`. |
| `-V geometry:margin=1in` | 1 inch margin on all sides. |
| `-V mainfont="Times New Roman"` | Main body font (system font on Windows; installed via TeX Live `fonts-extra` on Linux). |
| `-V monofont="Consolas"` | Mono font for code blocks. The default (Latin Modern Mono) lacks Unicode box-drawing characters (├, ─, └, │) and produces "Missing character" warnings on ASCII trees. Consolas is Windows standard and covers the full box-drawing range. Linux alternative: `DejaVuSansMono` (in `texlive-fonts-extra`). |
| `--number-sections=false` | Do not auto-number headings – the report already uses explicit numbering. |

**Platform note – filter name:** On Windows npm creates three files per bin (`mermaid-filter`, `mermaid-filter.cmd`, `mermaid-filter.ps1`). Pandoc does an *exact filename* lookup and does not respect Windows' `PATHEXT` mechanism, so from **Git Bash / MINGW64** the `.cmd` suffix must be included. From **PowerShell/CMD** `-F mermaid-filter` also works. From **Linux/macOS** only `mermaid-filter` exists (no `.cmd`) — use that.

**Note – long code lines in PDF:** The default pandoc setup does *not* automatically break long lines in code blocks – lines wider than the page are visually cut (the text is still intact in the output, just not visible). Accepted for this project. Keep code lines short in the source when possible.

---

## Mermaid figures

For each activity that produces reports (currently only `sure/`), figures live under `<activity>/figures/` as both a `.mmd` source and a rendered `.png`:

```
sure/figures/
├── fig_2-1_system_architecture.mmd
├── fig_2-1_system_architecture.png
├── fig_3-1_development_framework.mmd
├── fig_3-1_development_framework.png
├── fig_4-1_pressing_pipeline.mmd
├── fig_4-1_pressing_pipeline.png
├── fig_6-1_model_chain.mmd
└── fig_6-1_model_chain.png
```

The `.mmd` files are the canonical source (edit these). The `.png` files are what the report embeds when read outside a Mermaid-aware renderer; `mermaid-filter` regenerates them at Pandoc time from the inline fenced blocks in `deliverables/report_d6.1.md`.

---

## Background convention

`background/` at the repo root holds **cross-cutting** background material — the material that spans activities (SuRE, Gen 2, Commercial, Funding) or predates the activity split. Company-level investor updates, legal documents, funding history, board correspondence, general Sunlit Sea history all belong here. Activity-specific background stays under `sure/background/`, `gen2/background/` etc.

### File-naming convention

Every file in any `background/` folder (root or activity-level) carries a date prefix:

```
YYYY-MM-DD_short_description.ext
```

Examples:

- `2025-11-14_investor_update_q3.md`
- `2024-02-01_shareholder_agreement.pdf`
- `2023-06-08_board_meeting_minutes.md`

The date is the date of the document (when it was written / issued / sent), not the day it was filed. When the exact date is unknown, use the best approximation and note the uncertainty in the file body.

### Inbox: `background/new/`

Files that have not been processed yet land in `background/new/`. Typical sources: PDFs (scanned or exported), Word documents, PowerPoint decks, photos and screenshots, plain-text notes.

At the start of every working session, check `background/new/` (and any `*/background/new/`) for unprocessed files. The `CLAUDE.md` working rules document this.

### Conversion pipeline

| Source format | Tool | Command shape |
|---|---|---|
| `.pdf` | `pdftotext` | `pdftotext -layout "background/new/foo.pdf" background/new/foo.txt` then hand-tidy into `.md` |
| `.docx`, `.pptx`, `.odt`, `.rtf`, `.html` | `pandoc` | `pandoc "background/new/foo.docx" -o background/new/foo.md --wrap=none` |
| `.md`, `.txt` | (already text) | tidy, then timestamp-prefix and move |
| `.png`, `.jpg`, `.jpeg` and other true binary evidence | keep as-is | timestamp-prefix and move; do not convert |

After conversion:

1. Review the `.md` and add a short preamble at the top noting the source file name and the document's original date (if known).
2. Rename to `YYYY-MM-DD_description.md`.
3. Move to `background/`.
4. Remove the intermediate `.txt` from `pdftotext` — only the `.md` needs to stick around.
5. Keep the original binary in `background/` **only** if it is the authoritative source (signed PDFs, signed contracts, presentations we might redistribute). Otherwise the `.md` supersedes it and the original can be dropped.

---

## Scripts

Persistent helper scripts live in `scripts/` at the repo root — never scattered inside data folders like `background/`, `sure/`, etc. Follows the same pattern as the neighbouring `../fjordgata30` project.

### `scripts/md_image_to_html.py`

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

### `scripts/format_docx.py`

Post-processes a Pandoc-generated `.docx` file to fix two things Pandoc handles poorly by default: (1) tables have no visible borders, and (2) all table columns are given equal width regardless of content. The script uses `python-docx` to add thin grey borders (0.5 pt, `#BFBFBF`) to every cell in every table, and sets column widths per table from a `TABLE_WIDTHS_BY_STEM` dict keyed on the input filename stem (basename without `.docx`).

Dependencies are declared inline via PEP 723 script metadata (`python-docx`), so `uv run` installs them on the fly into a user-local ephemeral env — no system install required.

```bash
# In-place: pandoc first, then format the resulting docx
pandoc background/loeypemelding/2026-07-16_loeypemelding.md -o background/loeypemelding/2026-07-16_loeypemelding.docx
uv run scripts/format_docx.py background/loeypemelding/2026-07-16_loeypemelding.docx

# Or output to a different path
uv run scripts/format_docx.py input.docx output.docx

# Borders only, skip column widths (for docs not in TABLE_WIDTHS_BY_STEM)
uv run scripts/format_docx.py input.docx --borders-only
```

Adapted from the same-named script in `../fjordgata30/scripts/` — mechanics are identical, only `TABLE_WIDTHS_BY_STEM` is Sunlit-Sea-tailored. When a new deliverable with tables is generated, add a new dict entry keyed on the input filename stem, with one width row per table in the order they appear in the document.

### `scripts/extract_pdf_images.py`

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

### `scripts/insert_pdf_page_images.py`

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

### `scripts/nbsp_numbers.py`

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

### `scripts/clean_investor_updates.py`

Strips mail-header noise, mid-body Gmail page-print repeats, and trailing signature blocks (`Mvh`, contact-info lines, Google Groups unsubscribe boilerplate) from the investor-update `.md` files under `background/`. Preserves the YAML frontmatter; leaves body content between top and bottom noise untouched.

**Safe default (no in-place edits).** Writes a sibling `<name>.cleaned.md` for each input. Compare, then either rename manually or re-run with `--in-place`.

```bash
# Safe default — writes background/*.cleaned.md
python scripts/clean_investor_updates.py background/*.md

# Dry-run — per-file word-count before/after, no writes
python scripts/clean_investor_updates.py --dry-run background/*.md

# In-place — overwrites originals; only use after --dry-run looks safe
python scripts/clean_investor_updates.py --in-place background/*.md
```

The dry-run output flags any file that shrinks to below 70% of its original word count with a `!` marker — that is the pattern that would have caught the earlier truncation incident where two files silently lost ~90% of their content to an over-broad signature-start regex. Always dry-run before batch use.

---

## Activity contents

### `sure/` — SuRE WP6 (Sunlit Sea contribution)

Sunlit Sea's contribution to the Horizon Europe project **SuRE**, Work Package 6.

- **D6.1 Model chain description** – delivered as `D6.1 Sunlit model chain_v7.docx` (regenerated from `deliverables/report_d6.1.md` on request).
- **D6.2 Multi-domain design screening** – in preparation (`deliverables/report_d6.2.md`, `D6.2.md`).

Contents:

- `deliverables/` – finished and in-progress deliverables (reports, presentations to CINEA / GA).
  - `report_d6.1.md` – D6.1 report source (canonical Markdown).
  - `report_d6.2.md` – D6.2 report source (work in progress).
  - `sure_cinea_review_wp6_sunlitsea_presentation.md` – CINEA review deck.
  - `sure_ga6_wp6_sunlitsea_presentation.md` – GA6 deck.
- `D6.2.md` – working notes for D6.2 scoping / interface status.
- `D6.1 Sunlit model chain_v7.docx` – latest delivered docx.
- `analysis.md` – quality/consistency analysis of the D6.1 report.
- `ife_feedback_v6.md` – Nathan's tracked-change comments (v6).
- `activities.md` – collected evidence and testing activities.
- `notes.txt` – loose working notes.
- `sure_dow_extract.txt` – DoW extract.
- `figures/` – Mermaid sources (`.mmd`) + rendered PNGs used inline in the reports.
- `images/` – photos, CAD/mesh screenshots, empirical figures used in the reports. See `CLAUDE.md` for per-image descriptions.
- `background/` – DoW extract, external reports, source PDFs (and Markdown conversions of them) and other date-prefixed background material. Some files here (e.g. `Prod v2 roadmap`) may move to `gen2/background/` when Gen 2 material is separated.

The aluminium pressing simulation pipeline lives as a neighbouring project at `../thepressing/` — not part of this repo.

Partners: **IFE** (Nathan Roosloot – FEM/CFD), **TNO** (LCA), **MariSol/Accura** (physical forming trials). Open SuRE tasks carry the `[SURE]` tag in `TASKS.md`.

### `gen2/` — Gen 2 product development

Sunlit Sea Gen 2 FPV product development: prototype evolution (P3 → P4 → P5), mould / cast decisions, materials testing, supplier work. Overlaps with SuRE WP6 (the D6.1/D6.2 model chain evaluates Gen 2 geometries) but has its own product-development lifecycle beyond the EU deliverable.

Current contents:

- `norsmaterials_brief.md` – partner brief for Norsmaterials PU-casting collaboration (T72).
- `notes_norsmaterials.md` – research notes on Norsmaterials for the brief.

Content to migrate here when the split makes sense:

- `sure/background/Prod v2 roadmap (1).xlsx`
- `sure/background/FDS -2024-Nextgen product.docx (1).txt`

Open Gen 2 tasks carry the `[GEN2]` tag in `TASKS.md`.

### `funding/` — Grants, EU reporting, financial

Grant applications, Horizon Europe periodic reporting, CINEA reviews, financial reporting.

Note: SuRE deliverables (D6.1, D6.2) live under `sure/` because they are the technical work products, not the funding-and-reporting side. Track funding-side artefacts here (periodic reports, financial statements, grant application drafts, CINEA correspondence, investor recaps).

Current contents:

- `nedskriving_2025.md` — the substantive impairment test for the 2025 annual accounts (T79). All 7 indicators explicitly assessed with concrete reasoning drawn from the løypemelding narrative; conclusion is that no impairment is required. Only NOK amounts remain as placeholders, filled from the general ledger.
- `nedskriving_mal.md` — company-independent template for impairment tests under Norwegian accounting rules (rskl § 5-3, NRS 8, NRS(F) Nedskrivning, NRS 4). 12 sections + checklist, applicable to micro/small/medium/large foretak. Reference for future testing years or other companies (T78).
- `nedskriving_draft.md` — Eirik's short note framing the 2025 argument (external validation from Sintef/IFE, gen 1 → gen 2 transferability). Basis for T79.
- `nedskriving.md` — original T75 draft. Placeholder-heavy; superseded by `nedskriving_2025.md` for the 2025 test but retained per instruction.

Open funding tasks carry the `[FUND]` tag in `TASKS.md`.

---

## Folder layout (top level)

```
sure-d61/
├── CLAUDE.md                  – AI project context and working rules
├── TASKS.md                   – open task list (T-numbered, single sequence across activities)
├── ARCHIVE.md                 – closed tasks
├── README.md                  – this document (only README in the repo)
├── background/                – cross-cutting background material (date-prefixed files)
│   ├── new/                   – inbox for unprocessed files (PDFs, DOCX, images → converted to .md)
│   ├── lover/                 – excerpts of Norwegian statutes and accounting standards (regnskapsloven, NRS, skfvl)
│   ├── loeypemelding/         – historical investor updates (løypemeldinger), date-prefixed
│   └── eic/                   – EIC Transition proposal material (WP structure, MoM, feedback, PES application drafts)
├── scripts/                   – persistent helper scripts (see the *Scripts* section above)
├── sure/                      – SuRE WP6 activity
├── gen2/                      – Gen 2 product development
└── funding/                   – Grants, EU reporting, financial
```

Repo name `sure-d61` predates the multi-activity restructure and has been retained.
