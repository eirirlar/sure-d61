# Sunlit Sea – working repo

Working repository for Sunlit Sea's ongoing activities, organised by **activity** (top-level folder per activity) with a single T-numbered task sequence across the whole repo.

Activities:

- `sure/` – SuRE WP6 (Horizon Europe FPV model chain, D6.1 delivered, D6.2 in preparation)
- `gen2/` – Gen 2 product development (P3 → P4 → P5)
- `funding/` – Grants, EU reporting, financial
- `surewave/` – SUREWAVE Horizon Europe project (Grant Agreement 101083342) — consortium deliverables and grant paperwork. Sunlit Sea is a beneficiary; SINTEF coordinates.
- `generic/` – cross-cutting / shared material that spans the three activities (historical investor updates, legal excerpts, market intel, outgoing customer correspondence). Split into `generic/background/` (inputs) and `generic/deliverable/` (outputs).

Repo-level context and working rules are in `CLAUDE.md`. Task list is in `TASKS.md`; closed tasks in `ARCHIVE.md`.

**Single README:** this file is the only README in the repo. Do not create per-folder README files — describe folder contents here, in the *Activity contents* section below.

## Contents

- [PDF text extraction](#pdf-text-extraction) — `pdftotext -layout` for all PDF reading
- [Document conversion (Pandoc)](#document-conversion-pandoc) — pointer to `docs/pandoc_conversion.md`
- [Mermaid figures](#mermaid-figures) — `<activity>/figures/` layout
- [Background convention](#background-convention) — pointer to `docs/background_convention.md`
- [Scripts](#scripts) — pointer to `docs/scripts.md`
- [Activity contents](#activity-contents) — per-folder file inventory
- [Folder layout (top level)](#folder-layout-top-level)

See also the `docs/` directory:

- [`docs/pandoc_conversion.md`](docs/pandoc_conversion.md) — full Pandoc + mermaid-filter installation, DOCX/PDF commands, Letter/letterhead output
- [`docs/scripts.md`](docs/scripts.md) — reference for every helper script in `scripts/`
- [`docs/background_convention.md`](docs/background_convention.md) — background inbox pipeline and conversion recipes
- [`docs/sure_images.md`](docs/sure_images.md) — descriptions of images in `sure/images/`
- [`docs/rules/`](docs/rules/) — long-form elaboration of individual working rules

And the `cases/` directory for cross-cutting threads (pointers only, no file duplication):

- [`cases/prinsippendring_arsregnskap_2025/INDEX.md`](cases/prinsippendring_arsregnskap_2025/INDEX.md) — prinsippendring, aktivering FoU, nedskrivingstest, fortsatt drift (årsregnskap 2025 cycle)
- [`cases/eic_transition_surewave/INDEX.md`](cases/eic_transition_surewave/INDEX.md) — EIC Transition SUREWAVE application thread

---

## PDF text extraction

Sources under `generic/background/` and `*/background/` (`sure/background/`, `funding/background/`, `gen2/background/` etc.) are mostly PDF. Always convert to text with `pdftotext` before reading — do **not** open PDFs page-by-page with the Read tool, it is expensive and loses structure.

```bash
pdftotext -layout "sure/background/somefile.pdf" - > sure/background/somefile.txt
```

`-layout` preserves columns and tables reasonably. Drop it if the layout produces artefacts. Regenerate text extractions when the underlying PDF changes.

---

## Document conversion (Pandoc)

Pandoc is the chosen conversion tool for `.docx`, `.pptx` and `.pdf`. All conversions in this project support Mermaid diagrams inline in the Markdown source via `mermaid-filter`.

Full installation steps (pandoc, nvm + Node + mermaid-filter, TeX Live), standard DOCX / PDF command invocations, and letter/letterhead output are documented in [`docs/pandoc_conversion.md`](docs/pandoc_conversion.md).

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

`generic/background/` holds **cross-cutting** background material; activity-specific background stays under the activity's own folder (`sure/background/`, `gen2/background/`, `funding/background/`). Date-prefix naming convention `YYYY-MM-DD_short_description.ext` applies throughout.

Full file-naming convention, `*/background/new/` inbox handling, and the conversion pipeline for incoming PDF/DOCX/PPTX/images are in [`docs/background_convention.md`](docs/background_convention.md).

---

## Scripts

Persistent helper scripts live in `scripts/` at the repo root. Each script is documented in [`docs/scripts.md`](docs/scripts.md) with purpose, invocation, inputs/outputs and safety notes.

Current scripts:

- `md_to_letter.py` — Markdown → DOCX/PDF on the Sunlit Sea letterhead
- `md_to_slides.py` — Markdown → PDF slide deck in the Sunlit Sea visual profile
- `md_image_to_html.py` — rewrite Markdown image refs into HTML `<figure>` blocks
- `format_docx.py` — post-process Pandoc docx (table borders + column widths)
- `extract_pdf_images.py` — extract embedded images from PDFs
- `insert_pdf_page_images.py` — inline image refs into pdftotext `.md`
- `nbsp_numbers.py` — NBSP between thousand-separator digit groups
- `clean_investor_updates.py` — strip mail-headers / signatures from investor updates
- `eu_proposal_template_format.lua` — Pandoc Lua filter for EU proposal templates
- `xlsx_to_md.py` — xlsx workbook → one Markdown table per sheet
- `emf_to_png.ps1` — rasterise `.emf` to `.png` (Windows GDI+)

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
- `images/` – photos, CAD/mesh screenshots, empirical figures used in the reports. Per-image descriptions in [`docs/sure_images.md`](docs/sure_images.md).
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

Layout: outbound documents (letters, mails, notes, applications, board resolutions) live under `funding/deliverables/`. Working drafts, templates and accountant-sourced reconciliations stay at the activity root. Date-prefixed background inputs live under `funding/background/`.

At the activity root:

- `nedskriving_2025.md` — the substantive impairment test for the 2025 annual accounts (T79). All 7 indicators explicitly assessed with concrete reasoning drawn from the løypemelding narrative; conclusion is that no impairment is required. Only NOK amounts remain as placeholders, filled from the general ledger.
- `nedskriving_mal.md` — company-independent template for impairment tests under Norwegian accounting rules (rskl § 5-3, NRS 8, NRS(F) Nedskrivning, NRS 4). 12 sections + checklist, applicable to micro/small/medium/large foretak. Reference for future testing years or other companies (T78).
- `cinea_sellin_template.md` — reusable template for CINEA-facing project descriptions (used to rebuild the SuRE extension project description in T105).
- `aktivering_reklassifisering.md`, `aktivering_regnskapsforer_mail.md`, `aktivering_regnskapsforer_mail2.md` — in-progress working notes and draft mails on the FoU-aktivering / reklassifisering line of work. No date prefix because they are drafts rather than filed outputs.
- `1005 forskning og utvikling - oppdatert.md`, `2160 SUNLIT SEA AS_opptjente tilskudd - oppdatert avstemming.md` — accountant-sourced reconciliation reports for the FoU asset account and the deferred-grant liability. Un-prefixed names kept from the regnskapsfører's own filing.
- `2025-12-31_bilag_383_prinsippendring.md` — regnskapsfører's calculation note for Bilag 383 (2025) covering the FoU 2021 opening balance, cumulative depreciation 2021–2024, the equity-side reversal, the reclassification to konto 1205 (pressverktøy), and the full depreciation of the remaining FoU 2021 balance in 2025.

`funding/deliverables/` — outbound funding documents authored by Sunlit Sea (letters, cover mails, auditor packs, tax-return attachments, board resolutions, grant-application text):

- `2026-07-14_mail_regnskapsforer_revisorpakke.md` — cover mail to Orkla Regnskap transmitting the first revisorpakke on prinsippendring, aktivering and nedskrivingstest.
- `2026-07-16_revisorpakke_prinsippendring_aktivering_nedskrivingstest.md` — the auditor-pack itself, 13 sections, standalone deliverable to revisor. Covers prinsippendring, aktivering overview, vilkårsvurdering, tilskuddsbehandling, avskrivningsreversering, avskrivningsstart, balanseeffekt, nedskrivingstest, konklusjon. Rounded amounts; the `_eksakte_belop` sibling keeps the exact figures. The `.cleaned.md` variant is a mechanical cleanup of the same file.
- `2026-07-16_revisorpakke_prinsippendring_aktivering_nedskrivingstest_eksakte_belop.md` — reference copy of the revisorpakke with exact (non-rounded) NOK amounts, kept alongside the rounded delivery copy.
- `2026-07-16_revisorpakke_prinsippendring_aktivering_nedskrivingstest.cleaned.md` — cleanup-script output of the revisorpakke.
- `2026-08-26_dialog_revisor_prinsippendring.md` — transcript / referat of the dialogue with revisor on how to split the prinsippendring into separate 2024 and 2025 effects, how to present the equity note, and how to structure the nedskrivingstest at two balance dates.
- `2026-08-26_endringer_arsregnskap_2025_prinsippendring.md` — spec of the changes to the 2025 annual accounts stemming from the prinsippendring.
- `2026-09-10_vedlegg_skattemelding_2025_prinsippendring.md` — short justification of the 2025 accounting principle change, for attachment to the 2025 tax return. Follows the auditor's 2026-09-10 guidance (2024 effect directly against retained earnings; 2024 tax depreciation reversed in the 2025 return).
- `2026-09-11_sure_extension_budget_sunlit.md` — internal working draft of the budget to be entered into the SuRE extension budget sheet, with per-cell reasoning and cell references.
- `2026-09-11_sure_extension_project_description.md` — outbound project description for the SuRE extension application, rebuilt from `cinea_sellin_template.md` in T105.
- `2026-09-17_mail_regnskapsforer_fortsatt_drift.md` — request to Orkla Regnskap for the numeric basis the board needs before responding to the auditor's forthcoming numbered letter on going-concern uncertainty (T106.01). Covers cash position, debt service schedule, fixed costs, tax/VAT/tvangsmulkt status, receivables, grant disbursements, equity composition, and the status of the T81 principle change.
- `2026-09-17_styrets_vurdering_fortsatt_drift.md` — formal board assessment of going concern (T106.04). Standalone deliverable to auditor with cash position, inflows over 12 months, dokumenterte debt service plans (IN quarterly avdrag + SB1 renegotiated plan), risk assessment (aged supplier debt, receivables written down, pantstillelse), and conclusion that going-concern basis is upheld. Signed by Per Lindberg (styreleder) and Eirik Larsen (styremedlem), Oslo 17.09.2026.
- `2026-09-17_note_fortsatt_drift_arsregnskap.md` — draft note for the 2025 annual accounts summarising the board's going concern assessment (T106.06). Written for insertion after existing note 11, gives basis for auditor to issue an emphasis-of-matter paragraph (ISA 570 pkt. 22) with unmodified opinion instead of a qualified opinion. Uses "vesentlig usikkerhet" wording explicitly.
- `2026-09-17_mail_revisor_note_fortsatt_drift.md` — cover mail to auditor proposing the going concern note above, in response to her offer of the emphasis-of-matter route.
- `2026-09-28_note_immaterielle_eiendeler_arsregnskap.md` — draft note on immaterielle eiendeler for the 2025 annual accounts.
- `eupi_pv/` — subfolder for the HORIZON-CL5-2026-11-D3-14 (EUPI-PV Partnership) grant-application thread. Authored material only: meeting prep, budget position, proposal text. Companion background (call text, internal opportunity assessment) lives in `funding/background/eupi_pv/`.
  - `2026-10-01_balram_meeting_eupi_pv_talking_points.md` — talking points for the Balram (SINTEF) meeting on the EUPI-PV call. Positions Sunlit Sea as FPV-technology partner for one site, flags EIC Transition SUREWAVE dependency, lists mandatory consortium roles.
  - `2026-10-13_sunlit_sea_budget_proposal_eupi_pv.md` — Sunlit Sea's proposed scope and budget for the EUPI-PV consortium (T125). Positions Sunlit Sea as technical lead for 5000 kWp FPV delivery across two EU nearshore sites, plus a project-dedicated FOAK pilot production line. Site split: Gunneklevfjorden (3.2 MWp) end-to-end by Sunlit Sea incl. electrical + grid connection + permitting + light mooring on the capped seabed; Clement's Portuguese nearshore site (~1.8 MWp) with Sunlit Sea on FPV + DC electrical, Clement on permitting + mooring + grid. Claims €3.75M of the €7.5M lump sum (50 %), backed by €5.4M in estimated real costs + €1.65M in own co-financing. Addresses the portal Q&A on construction-cost eligibility by framing the ask as the FOAK innovation delta. Flags that Hainer See (lake) fails eligibility under the offshore/nearshore scope restriction, so the second site must be Portuguese nearshore. Includes a scope fallback (single-site Gunneklevfjorden only, ~€0.8-1.5M) if EIC Transition SUREWAVE is not awarded or the envelope cannot accommodate the full share. Standalone English, no companion-doc dependencies.
- `2026-10-09_genfors_sak_fullmakt_egne_aksjer.md` — generalforsamling case: styrefullmakt for erverv av egne aksjer.
- `2026-10-09_styreprotokoll_svar_revisors_nummerert_brev_nr2_2025.md` + `.docx` — board resolution responding to the auditor's numbered letter no. 2 (2025).
- `2026-10-09_vedlegg_skattemelding_2025_prinsippendring_kort.md` — short-form tax-return attachment on the 2025 accounting principle change.

`funding/background/` holds date-prefixed background material for the funding stream, plus the `nye/` inbox for unprocessed files. Per-application subfolders hold grouped material for a specific grant thread.

- `2026-08-21_vollsfjorden_solkraftanlegg/` — the Vollsfjorden floating-solar document set (T100), converted from the `nye/Vollsfjorden Solkraftanlegg/` inbox. 10 `.md` files + 9 extracted images in `images/<doc-stem>/` + one raw `.csv`. Two groups: `tillatelse_*` (Kystverket permit, Prosolar site plan D1, Grenland Havn referral letter, Skien kommune and Statsforvalteren consultation replies) and `ppa_*` / `enova` / `gammel_tuf_soknad_*` (PPA template + Vollsfjorden PPA draft in both PDF and DOCX form, Enova application draft, old Telemark utviklingsfond application 2025-0039). Folder date is the filing date, not a document date — the set spans 2025-02 to 2025-09.
- `eupi_pv/` — HORIZON-CL5-2026-11-D3-14 (EUPI-PV Partnership) grant-application thread. €7.5M lump-sum HORIZON-IA for TRL 7-8 floating PV demonstration ≥5 MW across multiple EU sea zones, deadline 2026-12-01. Holds the retrieved call text and Sunlit Sea's internal opportunity assessment. Companion authored material (meeting prep, budget position, proposal text) lives in `funding/deliverables/eupi_pv/`.

Open funding tasks carry the `[FUND]` tag in `TASKS.md`.

### `surewave/` — SUREWAVE Horizon Europe project

Consortium repository for the SUREWAVE project — *Structural reliable offshore floating PV solution integrating circular concrete floating breakwater* (Horizon Europe, Grant Agreement 101083342, HORIZON-CL5-2021-D3-03). Coordinator: SINTEF AS. Beneficiaries: SINTEF, Sunlit Sea, Ceit, MARIN, ACCIONA, Clement Germany, IFEU. Different project from SuRE (`sure/`) — the two are distinct EU projects with overlapping technical themes (offshore FPV, breakwaters, LCA).

Sunlit Sea's role in SUREWAVE is smaller than in SuRE; this folder is primarily a reference archive of consortium deliverables that other Sunlit Sea work (SuRE, Gen 2, funding proposals) references.

Contents:

- `background/` — date-prefixed archive of SUREWAVE consortium material: deliverables filed by other consortium partners, the Grant Agreement, the Proposal, Annex 1 Part B, one non-deliverable technical note (CFD simulations on plate), plus internal working documents produced by Sunlit Sea that stay inside the consortium (status snapshots, curated indexes, WP-leader reference material). All items sit as flat `.md` files (with `.pdf` / `.xlsx` companions where relevant) at this level.
  - Deliverables span WP1 (management), WP2 (requirements), WP3 (design), WP4 (materials & prototype), WP5 (structural integrity & SHMS), WP6 (ultimate strength), WP7 (sustainability: environmental, social, integrated), WP8 (dissemination, societal needs).
  - Grant Agreement 101083342 (signed 2022-09-20) and the original Proposal (submitted 2022-02-23) are kept as authoritative PDFs alongside their pdftotext `.md` renditions.
  - D7.4 cost data kept raw as `.xlsx` next to the corresponding Economic Assessment `.md`.
  - Consortium templates: `2026-10-16_surewave_docx_template.docx` and `2026-10-16_surewave_pptx_template.pptx`. Used as pandoc `--reference-doc` targets by the `generate-surewave-docx` and `generate-surewave-pptx` skills.
  - Working documents produced by Sunlit Sea for internal / WP-leader use: `2026-09-28_status.md` (project status snapshot), `2026-09-29_surewave_technical_system_images.md` (curated index of technical-system images from `background/`), `2026-09-29_surewave_wp_task_deliverable_index.md` (authoritative index of WPs, tasks and deliverables compiled from the GA and Annex 1), `2026-09-30_exploitation_requirements_reference.md` (comprehensive WP8 exploitation-requirements reference consolidating GA articles, DoA commitments, CINEA guidance and Continuous Reporting Module structure).
- `images/` — pandoc-extracted images from every `.docx`-sourced background deliverable, organised in per-deliverable subfolders whose names match the `.md` basename (e.g. `images/2024-04-16_surewave_d5.1/imageN.*`). Image references in the background `.md` files use `../images/<basename>/imageN.*` so they resolve regardless of file location. Curated index at `background/2026-09-29_surewave_technical_system_images.md`.
- `background/new/` — inbox for future SUREWAVE material.
- `deliverables/` — Sunlit Sea authored SUREWAVE outputs (Sunlit Sea leads Work Packages 2 and 8 and is the lead beneficiary for eight DoA deliverables; those authored here live in this folder). Follows the same pattern as `sure/deliverables/`. Also holds the WP8-leader distributable **partner exploitation input template** (`2026-09-30_surewave_partner_exploitation_input_template.md` + `.docx` companion) — a CRM-aligned form partners fill in with their Results, Results Ownership List, Publications, Datasets, IPR, Standards, Other results, Dissemination, Communication and Individual Exploitation Plan entries.

Open SUREWAVE-related tasks currently carry the `[GENERIC]` tag (folder introduction is cross-cutting infra). A dedicated `[SUREWAVE]` tag may be introduced later if enough project-specific tasks accumulate.

### `generic/` — cross-cutting / shared

Material that spans SuRE, Gen 2 and Funding, or predates the activity split. Two subfolders:

- `generic/background/` — cross-cutting background inputs (date-prefixed). Contains company-level correspondence, historical investor updates, market intel, legal excerpts, and any other input material that is not the property of a single activity. Current subfolders:
  - `new/` — inbox for unprocessed files (PDFs, DOCX, images → converted to .md).
  - `lover/` — excerpts of Norwegian statutes and accounting standards (aksjeloven, regnskapsloven, NRS, skfvl). All paragraph files are verbatim from Lovdata — see `docs/rules/lovparagrafer.md` and the `last-ned-paragraf` skill for the download/verification pipeline.
  - `loeypemelding/` — historical investor updates (løypemeldinger), date-prefixed.
  - `eic/` — EIC Transition proposal material (WP structure, MoM, partner correspondence, feedback, PES application drafts, proposal revision strategy, full Part B rewrite, archived call rules and web sources).
  - `leads/` — commercial leads and prospect material (date-prefixed under per-lead subfolders).
- `generic/deliverable/` — outgoing cross-cutting material (customer replies, quotes and pre-tender responses, generic company-level deliverables that do not belong to a single activity). Same `YYYY-MM-DD_short_description.ext` date-prefix convention as `background/`.

Open cross-cutting tasks carry the `[GENERIC]` tag in `TASKS.md`.

---

## Folder layout (top level)

```
sure-d61/
├── CLAUDE.md                  – AI project context and working rules
├── TASKS.md                   – open task list (T-numbered, single sequence across activities)
├── ARCHIVE.md                 – closed tasks
├── README.md                  – this document (only README in the repo)
├── docs/                      – topic-level documentation
│   ├── pandoc_conversion.md   – Pandoc + mermaid-filter installation and commands, Letter/letterhead output
│   ├── scripts.md             – reference for every helper script in scripts/
│   ├── background_convention.md – background inbox pipeline, date-prefix rules, conversion recipes
│   ├── sure_images.md         – per-image descriptions for images in sure/images/
│   └── rules/                 – long-form elaboration of individual working rules
├── cases/                     – case indexes for cross-cutting threads (pointers only, no file duplication)
│   ├── prinsippendring_arsregnskap_2025/INDEX.md
│   └── eic_transition_surewave/INDEX.md
├── generic/                   – cross-cutting / shared material
│   ├── background/            – date-prefixed background inputs
│   │   ├── new/               – inbox for unprocessed files (PDFs, DOCX, images → converted to .md)
│   │   ├── lover/             – excerpts of Norwegian statutes and accounting standards (aksjeloven, regnskapsloven, NRS, skfvl)
│   │   ├── loeypemelding/     – historical investor updates (løypemeldinger), date-prefixed
│   │   ├── eic/               – EIC Transition proposal material (WP structure, MoM, partner correspondence, feedback, PES application drafts, proposal revision strategy, full Part B rewrite, archived call rules and web sources)
│   │   └── leads/             – commercial leads and prospect material
│   └── deliverable/           – outgoing cross-cutting deliverables (customer replies, quotes, pre-tender responses)
├── scripts/                   – persistent helper scripts (see docs/scripts.md)
├── sure/                      – SuRE WP6 activity
├── gen2/                      – Gen 2 product development
├── funding/                   – Grants, EU reporting, financial
│   ├── background/            – date-prefixed background inputs (nye/ inbox)
│   └── deliverables/          – outbound funding documents (auditor packs, mails, notes, applications, board resolutions)
└── surewave/                  – SUREWAVE Horizon Europe project (Grant Agreement 101083342)
    ├── background/            – Filed consortium deliverables, Grant Agreement, Proposal, Annex 1 Part B
    ├── images/                – pandoc-extracted images per deliverable
    └── deliverables/          – Sunlit Sea authored SUREWAVE outputs
```

Repo name `sure-d61` predates the multi-activity restructure and has been retained.
