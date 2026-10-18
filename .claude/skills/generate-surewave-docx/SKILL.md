---
name: generate-surewave-docx
description: Produce a SUREWAVE-branded `.docx` from a Markdown source via `scripts/md_to_surewave_docx.py`. The wrapper starts from the SUREWAVE consortium docx template (keeping cover page, headers, footers), fills cover placeholders from YAML frontmatter or a sidecar `.meta.yaml`, converts the markdown body with pandoc + `--reference-doc`, appends it to the template using `docxcompose`, and injects `w:updateFields` so Word evaluates page numbers on open. Trigger when the user asks to "generate the SUREWAVE docx", "apply the SUREWAVE template", "convert this to a SUREWAVE deliverable", or when a `.md` in `surewave/deliverables/` is ready for consortium-branded `.docx` output (D-reports, WP8 outputs, consortium brochure sections). Different brand from Sunlit Sea letters.
---

# generate-surewave-docx

## When to use

- User asks for a SUREWAVE deliverable (`.md` under `surewave/deliverables/`) as a `.docx` in the SUREWAVE consortium brand.
- Deliverables filed inside the consortium (D-reports, WP8 outputs, status snapshots that go to the consortium, Technical Brochure sections, Exploitable Results Report, Business Plan, meeting minutes with consortium chrome).

**Do not use** for:

- Sunlit Sea letters — use `generate-letter` instead (different brand, different wrapper, different letterhead).
- Sunlit Sea slide decks — use `generate-slides` instead.
- SUREWAVE presentations — use `generate-surewave-pptx` instead.
- SuRE / D6.1 / D6.2 reports — those are plain pandoc with the standard flags from `docs/pandoc_conversion.md` (EU-deliverable format, not SUREWAVE-branded).
- Internal working documents, draft notes, task solution notes — Markdown source is enough.

## Procedure

### 1. Make sure metadata is available

The wrapper needs cover-page metadata — deliverable number, title, work package, task, document name, lead beneficiary, dissemination level, deliverable type, due date, delivery date. Two sources, with YAML frontmatter winning on conflict:

- **YAML frontmatter in the `.md`** (preferred for new deliverables):

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

- **Sidecar `<input>.meta.yaml`** next to the `.md` (use when the `.md` is already finalised and you don't want to touch it, or when the `.md` is authored for a different primary output format):

  ```yaml
  deliverable_number: D8.3
  title: Technical Brochure
  # ...same fields
  ```

If neither is present, cover placeholders stay as "DXX" / "XXXXXXX" / "SINTEF" / "SEN" / "28.11.2022" — pandoc runs and the body is appended, but the cover is not filled in. The wrapper does not error on missing metadata.

### 2. Confirm the source `.md` is a SUREWAVE deliverable

Check it lives (or will live) under `surewave/deliverables/` and has consortium-facing content. If the content is a Sunlit Sea pitch or a SuRE deliverable, surface that — the wrong template is a bigger problem than no template.

### 3. Verify content conventions before converting

- Global rules: no bold in body text (`**...**` only for titles), no emphasis-by-assertion phrasing, lead with the positive claim, avoid Norwegian idioms in English deliverables.
- External-deliverable stand-alone rule: no repo paths, no task numbers, no "offered to X", no `(see funding/background/…)`. Cite consortium Grant Agreement articles and DoA deliverables by their canonical reference (`Grant Agreement 101083342 Article X`, `DoA Task 8.2`, `Annex 1 Part B §…`) — never by internal file path.
- Image references in the `.md` use relative paths (e.g. `../images/<basename>/imageN.*`); the wrapper passes `--resource-path` so pandoc resolves them relative to the `.md`.
- Mermaid diagrams in fenced code blocks need `mermaid-filter` on PATH (not used by default; add the `-F mermaid-filter.cmd` flag inside the wrapper if the deliverable uses them).

### 4. Run the wrapper

```bash
# Default: writes <input>.docx next to <input>.md
uv run scripts/md_to_surewave_docx.py surewave/deliverables/2026-09-28_surewave_d8.3_technical_brochure.md

# Custom output path
uv run scripts/md_to_surewave_docx.py <input.md> -o <output.docx>

# Different template version
uv run scripts/md_to_surewave_docx.py <input.md> --template surewave/background/<new-template>.docx

# Explicit meta sidecar path
uv run scripts/md_to_surewave_docx.py <input.md> --meta <alt-meta.yaml>
```

Dependencies (`python-docx`, `docxcompose`, `pyyaml`, `lxml`) are declared via PEP 723 inline metadata; `uv run` installs them on the fly into an ephemeral env.

### 5. Check the rendered output

Open the `.docx` in Word (or LibreOffice if that's the chosen renderer) and verify:

- Cover page: SUREWAVE/EU wordmark header, hero banner, deliverable number ("D8.3"), title ("Technical Brochure"), disclaimer paragraph intact, "Deliverable details" table filled in (WP, Task, Dissemination level, Deliverable type, Lead beneficiary, Due date, Delivery date all showing the YAML values rather than template placeholders).
- Headers/footers on page 2+: SUREWAVE funding strap + sequential page numbers. Note: Word may still show the cached page number ("1" everywhere) until the first field refresh. The wrapper sets `w:updateFields`, which tells Word to recalculate on open; some Word versions still require Ctrl+A → F9 the first time.
- Body: sections, images, captions, tables rendered using the template's styles (pandoc's "Heading 2" maps to the template's `Overskrift2` style via styles.xml merge).
- No duplicate cover content (the wrapper replaces, not appends, the cover placeholders).

### 6. Report back

Source `.md` → output `.docx` path, template version used, number of metadata fields loaded, pandoc stderr summary, final file size.

## Known pitfalls

- **Missing metadata** → cover placeholders remain "XXX..." / "SINTEF" / "SEN" / "28.11.2022". The wrapper does not error; it just leaves the template defaults. Always confirm YAML frontmatter or sidecar is present before running.
- **Wrong template file** → using the Sunlit Sea letterhead (`generic/background/2026-10-10_sunlit_sea_letterhead.docx`) or a different consortium template produces a document with the wrong brand. The wrapper's default is `surewave/background/2026-10-16_surewave_docx_template.docx`; override with `--template` only when a newer SUREWAVE template arrives (also date-prefixed).
- **Stale page numbers in Word**: `w:updateFields=true` is set but some Word versions only honour it on first open after save-as. If pages show the same number, Ctrl+A → F9 forces a field refresh.
- **Image paths**: pandoc runs on a tmp copy of the body, so relative image paths in the `.md` must resolve from the original `.md`'s directory. The wrapper passes `--resource-path` to pandoc to handle this. If a `.md` uses absolute paths or paths relative to an unexpected directory, add the directory with `--resource-path` manually inside the wrapper.
- **Reference-table placeholders unchanged**: the SUREWAVE template contains reference tables below the cover (Dissemination level definitions, Deliverable type definitions, QA review table). The wrapper does *not* fill or remove those — they stay as reference material. If the deliverable needs them removed, do so manually in Word.
- **"Title" cell in deliverable-details table**: the SUREWAVE template has a cell labelled "Title" in the cover table that is a column header, not a label-value pair. The wrapper's title substitution works through the text-box title at the top of the cover (which is substituted correctly); this spare "Title" cell is left untouched.
- **Mermaid-filter not auto-enabled**: unlike the pandoc commands in `docs/pandoc_conversion.md`, the wrapper does not pass `-F mermaid-filter.cmd` by default. If a SUREWAVE deliverable uses mermaid, add the flag in the wrapper's pandoc call or convert the mermaid blocks to pre-rendered images first.
- **Content conventions still apply**: the wrapper does *not* enforce CLAUDE.md typography rules on the input `.md`. Run `check-deliverable` on the source `.md` before invoking this skill.

## Applicable rules

- CLAUDE.md "**Pandoc is the chosen conversion tool**" — the wrapper uses pandoc internally for body conversion; the `--reference-doc` mechanism provides style compatibility.
- CLAUDE.md "**Do not convert to docx automatically**" — only convert on explicit user order.
- CLAUDE.md "**External deliverables stand alone**" — SUREWAVE deliverables go to CINEA / consortium partners; the stand-alone rule applies in full.
- CLAUDE.md "**No bold in body text**", "**Markdown lists render correctly**", "**Avoid emphasis-by-assertion phrasing**", "**Lead with the positive claim**" — all apply.
- CLAUDE.md "**Mermaid deliverables**" — fenced code blocks + `.mmd` sidecars in the activity's `figures/` folder.
- CLAUDE.md "**Converted `.md` files must be self-contained**" — same spirit for `.docx`: no "the source `.md` is at X" asides.
- CLAUDE.md "**'Done' means end-to-end functional**" — this skill was reopened once because the first version flagged file-existence as "done" without running the pipeline against a real deliverable.
- `docs/pandoc_conversion.md` — Pandoc + mermaid-filter installation.
- `docs/scripts.md` → `md_to_surewave_docx.py` — full script reference.
- `docs/scripts.md` → `format_docx.py` — optional table-border post-processing if the deliverable has load-bearing tables that need visible borders.

## Historical references

- T109 — SUREWAVE D8.3 Technical Brochure (SIS lead, co-authored with SINTEF). First end-to-end use case for the wrapper.
- T110 — SUREWAVE D8.4 Exploitation Pathways & Definitive Business Plan.
- T111 — SUREWAVE consortium status report.
- T114 — Enrich SUREWAVE Technical Brochure (D8.3) with SINTEF's framing.
- T116 — SUREWAVE D1.7 (Data Management Plan Release 2) — Sunlit Sea review.
- T118 — SUREWAVE WP/task/deliverable authoritative index.
- T120 — SUREWAVE D8.3 Technical Brochure review passes.
- T121 — Update the exploitation report against CINEA/HE exploitation requirements.
- T128 — this skill's definition and the wrapper's implementation.
- `surewave/background/2026-10-16_surewave_docx_template.docx` — current consortium docx template.
- `surewave/background/2026-10-16_surewave_pptx_template.pptx` — the matching pptx template (used by `generate-surewave-pptx`).
- `generic/background/new/SUREWAVE_D2.2_Requirements_for_surface_mooring_system.docx` — real D2.2 deliverable used as a reference for template structure and placeholder field names (should be processed and moved out of `new/`).
