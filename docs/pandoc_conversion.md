# Document conversion (Pandoc)

Pandoc is the chosen conversion tool for `.docx`, `.pptx` and `.pdf`. All conversions in this project must support Mermaid diagrams inline in the Markdown source (e.g. `sure/deliverables/report_d6.1.md` embeds Mermaid in fenced code blocks). This is handled by **`mermaid-filter`** — a Pandoc filter that intercepts ```` ```mermaid ```` blocks, renders them to PNG at conversion time and embeds the images in the output. The filter must be system-installed (not `node_modules/` per project).

## Prerequisites – installation

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

## Usage – standard commands

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

## Letter / letterhead output

Outgoing official letters on the Sunlit Sea letterhead are generated from a `.md` source via `scripts/md_to_letter.py`. The letterhead template at `generic/background/2026-10-10_sunlit_sea_letterhead.docx` is the single source of truth: for `.docx` it is passed to pandoc as `--reference-doc` so the SUNLIT SEA wordmark, cream "A" watermark, page size, margins and styles come across; for `.pdf` the wrapper extracts the wordmark + watermark PNGs from the same `.docx` on the fly and places them via an `eso-pic` LaTeX header-include that reproduces the Word positions.

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

**Prerequisites:** `pandoc` on PATH (both formats), and `xelatex` from TeX Live on PATH (`--pdf` only). Both are already set up on the standard dev environment per the *Prerequisites – installation* section above.

**Content conventions when writing the `.md`:** The template is intended for letter-shape content (address block, date, salutation, body, signature). Keep headings minimal — a short bold subject line as the opening is usually enough. If a heading is needed, use H2+ (H1 competes visually with the wordmark). Stacked address and signature blocks must have two trailing spaces at the end of each line (or a trailing `\`) so they do not fold into one paragraph (see the top-level *Markdown lists render correctly* rule) — the merge is especially visible in PDF output.

**Signature block convention — single signer:** Use escaped underscores (`\_`) for the signature line and two-space line breaks for name/title stacking. Add 2–3 blank paragraphs (`\` on its own line) above the signature line to leave room for a physical signature:

```
Oslo, 9. oktober 2026

\

\

\

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
Per Lindberg  
Styreleder
```

The backslash-escapes prevent pandoc from reading the underscores as a Markdown horizontal rule (which LaTeX would centre on the page, disconnecting the line from the name). With `\_` the underscores render as inline text — left-aligned, with the name and title on their own lines directly below. Works in both `.docx` and `.pdf` output.

**Signature block convention — two signers side by side (PDF only):** Use pandoc's raw-LaTeX block syntax with `minipage`:

~~~
Oslo, 9. oktober 2026

\

\

\

```{=latex}
\noindent
\begin{minipage}[t]{0.45\textwidth}
\rule{\linewidth}{0.4pt}\\
Per Lindberg\\
Styreleder
\end{minipage}
\hfill
\begin{minipage}[t]{0.45\textwidth}
\rule{\linewidth}{0.4pt}\\
Eirik Larsen\\
Styremedlem
\end{minipage}
```
~~~

This renders two signature blocks side by side with the signature lines drawn by `\rule`. The `0.45\textwidth` minipages leave ~10% whitespace between the two blocks. `\hfill` pushes the second block to the right margin. Works in `.pdf` only — pandoc silently drops the raw-LaTeX block when producing `.docx`, so the `.docx` output will have no signature block in its place. For a `.docx` with side-by-side signatures, add them manually in Word after `md_to_letter.py` has produced the base `.docx`.

**When the letterhead `.docx` is updated:** replace `generic/background/2026-10-10_sunlit_sea_letterhead.docx` with the new version (keep the date-prefixed filename pointing at the current one, or add a `--letterhead` flag to the call for a transition period). Both `.docx` and `.pdf` outputs pick up the new wordmark/watermark automatically on the next run.
