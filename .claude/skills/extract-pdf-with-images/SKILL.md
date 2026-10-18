---
name: extract-pdf-with-images
description: Convert a batch of PDF files to Markdown with embedded images inlined per page, using the combined `pdftotext` + `scripts/extract_pdf_images.py` + `scripts/insert_pdf_page_images.py` recipe. Trigger when the user asks to "convert these PDFs with images", "process the PDF set", "run the T100 pipeline", or when a `background/new/` inbox contains PDFs whose text extraction would lose embedded figures or diagrams. Standardises the staging-under-final-slug step so image stems match.
---

# extract-pdf-with-images

## When to use

- A set of PDFs needs to become Markdown and the PDFs contain figures / embedded images that the `.md` must reference inline.
- User asks for "the T100 pipeline", "the combined recipe", "the PDF-with-images conversion", "extract and inline the images".
- Image fidelity matters (scanned reports, technical drawings, slide-deck PDFs with inline graphics).

**Do not use** for pure-text PDFs — the simpler `pdftotext -layout` pipeline from `docs/background_convention.md` is enough. The extra steps here are overhead when the PDF has no figures worth preserving.

## Procedure

Both helper scripts key on the file **stem**, so the `.md` stem must equal the `.pdf` stem. Stage copies of the PDFs under their final slug names *before* converting.

```bash
STAGE=/tmp/stage
OUT=<activity>/background/YYYY-MM-DD_<set_name>
mkdir -p "$STAGE" "$OUT/images"
```

### 1. Stage with final names

```bash
cp "<inbox>/Some Long Name.pdf" "$STAGE/short_slug.pdf"
# ... one line per PDF in the set
```

The staging names determine the final `.md` filenames and the folder names under `images/`. Choose slugs that make sense in the final `background/` layout.

### 2. Extract text (preserving `\f` page breaks)

```bash
for f in "$STAGE"/*.pdf; do
  pdftotext -layout -eol unix "$f" "$OUT/$(basename "$f" .pdf).md"
done
```

`-eol unix` keeps line endings consistent across platforms. The `\f` form-feed page separators are what the inline-image script keys off in step 5.

### 3. Extract embedded images

```bash
uv run scripts/extract_pdf_images.py "$STAGE"/*.pdf --output-dir "$OUT/images/"
```

Outputs `<images-dir>/<pdf-stem>/img-<page>-<idx>.<ext>` where `<ext>` is the native format of the embedded image (PNG, JPEG, or JP2).

### 4. Convert JP2 → PNG

```bash
find "$OUT/images" -name '*.jp2' -exec sh -c 'convert "$1" "${1%.jp2}.png" && rm "$1"' _ {} \;
```

Mandatory step. `pdfimages` / `pypdf` hand back JPEG 2000 for some scanner output and CAD output, and no Markdown viewer renders `.jp2`. Convert before linking. Requires ImageMagick's `convert` to be on PATH.

### 5. Prepend a metadata header to each `.md`

Write a short preamble at the top of each `.md` with:

- Document date (if known).
- Issuer / sender / recipient (if applicable).
- Short note on what the document is.

The insert-images script in step 6 treats everything before the first `\f` as part of page 1 and leaves the header alone, so the preamble sits at the top of the final file.

Do not add a YAML `source:` field pointing at the `.pdf` — the resulting `.md` must stand alone (CLAUDE.md "Converted `.md` files must be self-contained").

### 6. Inline the images

```bash
uv run scripts/insert_pdf_page_images.py "$OUT"/*.md --images-dir "$OUT/images/" --promote
```

Appends inline image references at the end of each page's text, so readers see the source text first and the visuals after. Default is safe-mode (writes `.imgref.md` siblings); `--promote` overwrites in place after you have verified a dry run on at least one file.

### 7. Non-PDF inbox files in the same pass

```bash
pandoc in.docx -t markdown --wrap=none --extract-media="$OUT/images/<stem>" -o "$OUT/<stem>.md"
```

Data files (`.csv`, `.xlsx`) are copied over raw — do not convert them to Markdown.

### 8. Clean up and report

- Remove the `$STAGE/` folder once the output is verified.
- Report per-file: source PDF → `.md` stem → image count extracted → page count.
- Confirm the destination folder (`<activity>/background/YYYY-MM-DD_<set_name>/`) is correct for the material (cross-cutting → `generic/background/`; activity-specific → `*/background/`).

## Applicable rules

- CLAUDE.md "**PDF conversion**" — always use `pdftotext` (never Read page-by-page).
- CLAUDE.md "**`background/new/` inbox check**" — the pipeline typically runs out of an inbox; confirm scope with the user first.
- CLAUDE.md "**Date-prefix naming convention**" + `docs/rules/date-prefix.md` — slug names in the staging step must follow `YYYY-MM-DD_short_description`.
- CLAUDE.md "**Converted `.md` files must be self-contained**" — no `source:` YAML, no "converted from X" body text in the preamble.
- CLAUDE.md "**Batch in-place edits require dry-run + backups**" + `docs/rules/batch-edits.md` — step 6 default is non-destructive; promote only after inspection.
- `docs/scripts.md` → `extract_pdf_images.py`, `insert_pdf_page_images.py`, and the "Combined recipe" subsection.

## Historical references

- T90 — initial image extraction from `sure/background/` PDFs; precedent for `extract_pdf_images.py`.
- T91 — JP2 → PNG conversion plus inline image refs; precedent for mandatory step 4.
- T100 — Vollsfjorden PDF set (10 PDFs + 9 image folders + raw CSV); established the full combined recipe.
- T108 — SUREWAVE background conversion used an adapted pandoc path (step 7) for the `.docx` sources alongside this recipe for the `.pdf`s.

## Known pitfalls

- **Stem mismatch**: converting a PDF called `Some Long Name.pdf` directly produces `Some Long Name.md`, which the insert script will not match against the staged image folder (`short_slug/`). Always stage under final slug names first.
- **Missing JP2 conversion**: skipping step 4 produces `.md` files with `![](images/stem/img-01-00.jp2)` references that no renderer displays. The images are there, just invisible.
- **Promoting without a dry-run**: step 6 default writes `.imgref.md` siblings for a reason — run at least one file in dry mode first and verify the per-page image placement is sensible.
- **Images under YAML frontmatter**: the insert script treats everything before the first `\f` as page 1. A YAML block there means page-1 images will land after the YAML, not where you may expect. Pre-check the output of step 2 before step 5.
- **Over-wide `-layout` output**: on PDFs with aggressive multi-column layout, `-layout` can produce `.md` with absurd whitespace. Drop `-layout` for those specific files if the output is unreadable, but accept the loss of table shape.
- **ImageMagick missing**: step 4's `convert` command requires ImageMagick. On a fresh machine, install permission is required — see CLAUDE.md "Installing system packages or tools requires explicit permission".
