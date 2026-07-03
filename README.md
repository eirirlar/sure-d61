# Sunlit Sea – working repo

Working repository for Sunlit Sea's ongoing activities, organised by **activity** (top-level folder per activity) with a single T-numbered task sequence across the whole repo.

Activities:

- `sure/` – SuRE WP6 (Horizon Europe FPV model chain, D6.1 delivered, D6.2 in preparation)
- `gen2/` – Gen 2 product development (P3 → P4 → P5)
- `commercial/` – Market, customers, sales
- `funding/` – Grants, EU reporting, financial

Repo-level context and working rules are in `CLAUDE.md`. Task list is in `TASKS.md`; closed tasks in `ARCHIVE.md`. Each activity folder has its own README with contents and scope.

---

## PDF text extraction

Sources in `sure/background/` (and any future `*/background/`) are mostly PDF. Always convert to text with `pdftotext` before reading — do **not** open PDFs page-by-page with the Read tool, it is expensive and loses structure.

```bash
pdftotext -layout "sure/background/somefile.pdf" - > sure/background/somefile.txt
```

`-layout` preserves columns and tables reasonably. Drop it if the layout produces artefacts. Regenerate text extractions when the underlying PDF changes.

---

## Document conversion (Pandoc)

Pandoc is the chosen conversion tool for `.docx`, `.pptx` and `.pdf`. All conversions in this project must support Mermaid diagrams inline in the Markdown source (e.g. `sure/report.md` embeds Mermaid in fenced code blocks). This is handled by **`mermaid-filter`** — a Pandoc filter that intercepts ```` ```mermaid ```` blocks, renders them to PNG at conversion time and embeds the images in the output. The filter must be system-installed (not `node_modules/` per project).

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
cd sure
pandoc report.md -o "D6.1 Sunlit model chain_v8.docx" -F mermaid-filter.cmd --toc --toc-depth=2
```

**PDF:**

```bash
cd sure
pandoc report.md -o report.pdf \
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

The `.mmd` files are the canonical source (edit these). The `.png` files are what the report embeds when read outside a Mermaid-aware renderer; `mermaid-filter` regenerates them at Pandoc time from the inline fenced blocks in `report.md`.

---

## Folder layout (top level)

```
sure-d61/
├── CLAUDE.md                  – AI project context and working rules
├── TASKS.md                   – open task list (T-numbered, single sequence across activities)
├── ARCHIVE.md                 – closed tasks
├── README.md                  – this document
├── sure/                      – SuRE WP6 activity (see sure/README.md for contents)
├── gen2/                      – Gen 2 product development (see gen2/README.md)
├── commercial/                – Market/customer/sales (see commercial/README.md)
└── funding/                   – Grants, EU reporting, financial (see funding/README.md)
```

Repo name `sure-d61` predates the multi-activity restructure and has been retained.
