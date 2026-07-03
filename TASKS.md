# Sunlit Sea – Task list

## Legend
- `[x]` Done
- `[~]` Started / in progress
- `[ ]` Not started

Tasks are identified with IDs on the form **T01**, **T02** etc. Use these IDs when referring to tasks in commits, chat and documents. Solutions are documented under each task in this file. Completed tasks stay here until the user explicitly asks for them to be archived — then they are moved to `ARCHIVE.md`.

Blocked items are tagged **[BLOCKED — needs input from …]** with the specific person/organisation waiting on.

## New items (unprocessed)

--

## Tasks

### T01 `[ ]` [SURE] Reduce repetition (Comment 446)
*(was A1.10.)*

Awaiting specific paragraph-level flags from Nathan or Eirik before acting. No action until flags are provided.

**[BLOCKED — needs input from NATHAN/IFE or EIRIK]**

---

### T02 `[ ]` [SURE] Deliver missing IFE figures
*(was A3.1 in the open-items section.)*

Nathan's tracked text references Figures 5-2 (CFD dark vs off-white slice), 5-3 (UV chamber before/after ~480 h on P3 sample) and 5-4 (FEM stress on P4 with magnified distortion), but image files have not been delivered.

**[BLOCKED — needs input from NATHAN/IFE]**: Deliver PNGs and confirm figure numbering.

---

### T03 `[ ]` [SURE] Add References section to the report
*(was A2.12; earlier A5.1.)*

The report cites Aretz 2005 (Yld2003), Voce 1948, ISO 10113:2020, ISO 16808:2014, ISO 12004-2:2009, IEC TS 62788-7-2, and Roosloot et al. 2024 inline but has no formal bibliography. Required for an EU deliverable. Eirik confirmed "include all of them" — do NOT include OsloMet/Tveit tensile-test papers or the Speira aluminium material card.

---

### T04 `[ ]` [SURE] Add abbreviation list
*(was A2.13.)*

Terms like FDS, FEM, CFD, PU, LCA, FPV, DoW, SSC, DEAP, ML, CAD are used throughout without a collected definitions list. Standard for EU deliverables.

---

### T05 `[ ]` [SURE] Add list of figures
*(was A2.14.)*

With 41 figures, a list of figures after the table of contents aids navigation and is standard for EU deliverables.

---

### T06 `[ ]` [SURE] Resolve or flag TODO comments before submission
*(was A2.17.)*

Six HTML comments remain in the report addressed to IFE and TNO. Appropriate for the working draft but must be either resolved (with partner input) or removed/softened for the submitted version.

---

### T07 `[ ]` [SURE] Resolve I-2 TODOs with IFE
*(was B1.1.)*

Fix STEP version (AP214 vs AP242), document geometric simplifications, define material property handover. Target: automate FreeCAD→STEP→SiSim pipeline.

**[BLOCKED — needs input from EIRIK + NATHAN/IFE]**

---

### T08 `[ ]` [SURE] Implement I-3 (thickness field transfer)
*(was B1.2.)*

Agree LS-DYNA thickness export format and SiSim/PATRAN ingestion path; confirm coordinate-system convention.

**[BLOCKED — needs input from EIRIK + NATHAN/IFE]**

---

### T09 `[ ]` [SURE] Resolve I-4 TODOs with IFE
*(was B1.3.)*

Confirm geometry reuse for thermal CFD; agree full material property list; agree CFD output format.

**[BLOCKED — needs input from EIRIK + NATHAN/IFE]**

---

### T10 `[ ]` [SURE] Formalise I-5 (LCA with TNO)
*(was B1.4.)*

Replace ad-hoc emails with versioned template; confirm functional unit and system boundary; version-track design iterations.

**[BLOCKED — needs input from EIRIK + TNO]**

---

### T11 `[ ]` [SURE] Design 3DFloat→SiSim interface
*(was B1.5.)*

Confirm IFE status on 3DFloat→SiSim coupling and "second half 2026" delivery timeline. If delayed, draft interface spec document.

**[BLOCKED — needs input from EIRIK + NATHAN/IFE]**

---

### T12 `[ ]` [SURE] Measure off-white PU absorptivity
*(was B2.1.)*

Dark blue was 0.88–0.91; off-white expected ~0.35 but not measured. To be measured as part of D6.2 work.

---

### T13 `[ ]` [SURE] Run thermal CFD for P4 geometry
*(was B2.2.)*

With off-white PU properties. Thermal tests to be decided in D6.2, possibly combined with load test.

---

### T14 `[ ]` [SURE] Complete white PU UV testing at IFE
*(was B2.3.)*

Condition A1 protocol. TODO left for Nathan in §5.3.3. Status update needed from IFE.

**[BLOCKED — needs input from NATHAN/IFE]**

---

### T15 `[ ]` [SURE] Complete adhesion testing on P3 samples
*(was B2.4.)*

Shear (PU-glass long sides) and tensile (loose hinges) after UV exposure. TODO left for Nathan in §5.3.3.

**[BLOCKED — needs input from NATHAN/IFE]**

---

### T16 `[ ]` [SURE] Get TNO LCA results
*(was B2.5.)*

Expected Q2 2026. TODO left for TNO in §5.4.2.

**[BLOCKED — needs input from TNO]**

---

### T17 `[ ]` [SURE] Complete P4 prototype
*(was B3.1.)*

Mould cast has been started. Progress to be reported in D6.2.

---

### T18 `[ ]` [SURE] Mechanical simulation (SiSim) on P4
*(was B3.2.)*

IFE runs this. They will adapt load cases to their capabilities and report in D6.2.

---

### T19 `[ ]` [SURE] Resolve cast-on-frame vs separate-and-mount architecture decision
*(was B3.3.)*

Must be decided before P5. P4 mould tests combined with UV/fatigue tests in D6.2 will inform this. Primer reports 20-year aquatic life; target is 25 years — dedicated testing needed to determine real-conditions performance.

---

### T20 `[ ]` [SURE] Multi-domain design screening
*(was B3.4.)*

The ~1,300 feasible pressing geometries (generated in Ch 4–7 of D6.1) must each be evaluated across four performance dimensions before a final design can be selected: (1) manufacturing feasibility (already filtered in the pressing pipeline), (2) structural performance (peak stresses and deformation from SiSim, interface I-2/I-3), (3) thermal performance (peak PU temperature from CFD, interface I-4), and (4) life-cycle impact (material masses and process data to TNO, interface I-5). The screening applies each domain's pass/fail threshold in sequence, reducing the 1,300 candidates to a short-list of structurally and thermally viable geometries with acceptable LCA profiles. Headline D6.2 deliverable; depends on T07–T11 model chain integration.

**[BLOCKED — needs input from EIRIK]**: Confirm whether screening can run with current tooling or must wait for T07–T11.

---

### T21 `[ ]` [SURE] Full experimental testing details for D6.2
*(was B4.1.)*

Tensile, UV, adhesion results currently in D6.1 §5.3.3 (as environmental coupling basis). Full write-up deferred to D6.2.

**[BLOCKED — needs input from EIRIK + NATHAN/IFE]**: Confirm scope and timing.

---

### T22 `[ ]` [SURE] Structural modelling with infill
*(was B4.3.)*

Current SiSim omits infill; flagged as D6.2 target in §5.3.4.

**[BLOCKED — needs input from EIRIK + NATHAN/IFE]**: Confirm IFE has been tasked with adding infill domain and expected timeline.

---

### T23 `[ ]` [SURE] D6.2 must deliver on inter-model data-transfer
*(was B5.1.)*

Josefine flagged CINEA red-flag risk.

**[BLOCKED — needs input from EIRIK + JOSEFINE]**: Confirm Josefine's role and D6.2 deadline so model-chain rollout can be planned backwards from it.

---

### T24 `[ ]` [SURE] D6.2 framing
*(was B5.2.)*

Core claim: "We built the model chain described in D6.1, connected the tools, ran it on the evolving prototype, and here are the design decisions it enabled." All interface table entries currently "manual / targeted for D6.2" must show "implemented" by D6.2.

**[BLOCKED — needs input from EIRIK]**: Once T07–T11 answers and D6.2 deadline are known, draft the D6.2 structure and plan to flip each interface row.

---

### T71 `[x]` Broaden project scope from SuRE WP6 to all Sunlit Sea activities

Right now `CLAUDE.md`, `README.md` and the task board are framed around SuRE D6.1/D6.2. But SuRE WP6 is only one of several ongoing Sunlit Sea activities that need context, background material, tasks and deliverables tracked in one place. Rework the information architecture so this repo becomes a Sunlit Sea working hub, with SuRE (and D6.1/D6.2 inside it) as one activity among several.

**Solution (2026-07-03):**

Eirik confirmed four activity streams and picked *folder-per-activity* with *prefix tag in title* for the single T-numbered sequence.

1. **Activity streams (4):** SuRE WP6, Gen 2 product development, Commercial, Funding / EU reporting.
2. **Tag vocabulary:** `[SURE]`, `[GEN2]`, `[COM]`, `[FUND]`. Every new task title starts with an activity tag. Documented in `CLAUDE.md` under *Activity tagging on tasks*.
3. **Folder layout:** created four top-level folders (`sure/`, `gen2/`, `commercial/`, `funding/`). All existing SuRE artefacts moved into `sure/` — `report.md`, `report_d6.2.md`, `D6.2.md`, `D6.1 Sunlit model chain_v7.docx`, `analysis.md`, `ife_feedback_v6.md`, `activities.md`, `requirements.md`, `gap.csv`, `notes.txt`, `README_MARKDOWN.md`, `sure_cinea_review_wp6_sunlitsea_presentation.md/.pptx`, `sure_ga6_wp6_sunlitsea_presentation.md`, `sure_dow_extract.txt`, and the whole `figures/`, `images/`, `background/`, `thepressing/` directories. Relative paths inside `report.md` (44 image references) stayed intact because `figures/` and `images/` moved with it. Placeholder README added to each of `gen2/`, `commercial/`, `funding/` describing scope; full `sure/README.md` written listing all SuRE files. Root now holds only `CLAUDE.md`, `README.md`, `TASKS.md`, `ARCHIVE.md`, `.gitignore`, `.git/`, `.claude/` + the four activity folders.
4. **CLAUDE.md** reframed as a Sunlit Sea working repo with a per-activity table, activity-tagging rules, generalised working rules, and the SuRE image descriptions moved under a `sure/images/` section.
5. **README.md** (top level) reframed to describe the multi-activity repo and repo-wide conversion tooling; pandoc commands updated to `cd sure && pandoc report.md …`.
6. **Existing tasks retagged:** T01–T24 all prefixed with `[SURE]` (via `sed -i -E 's/^(### T(0[1-9]|1[0-9]|2[0-4]) \`\[ \]\`) (.*)$/\1 [SURE] \3/'`). T71 itself left untagged as a meta / repo-management task (the rule applies to future tasks).
7. **Files touched:** `CLAUDE.md` (rewritten), `README.md` (rewritten), `TASKS.md` (title changed, T01–T24 retagged, T71 marked done), `sure/README.md`, `gen2/README.md`, `commercial/README.md`, `funding/README.md` (all new), plus the file moves listed in point 3.

**Follow-up not done in this task:** `sure/background/Prod v2 roadmap (1).xlsx` and `sure/background/FDS -2024-Nextgen product.docx (1).txt` are Gen 2 material sitting under `sure/` — flag for later relocation to `gen2/background/` once Gen 2 has active content. Not urgent.

---

### T72 `[~]` [GEN2] Norsmaterials partner brief (PU casting collaboration)

Sunlit Sea is exploring a collaboration with **Norsmaterials** — a PU-casting specialist — to help develop the Gen 2 PU tests (mould design, test casts, iterative feedback per test, step-by-step progression toward Gen 2). They have signalled willingness to advise on test design and interpret results with us. To make the collaboration productive we need to bring them up to speed on where we are, how we got here, and what we want to learn from each test.

**Single deliverable — one Markdown file that keeps evolving:** `gen2/norsmaterials_brief.md`. No separate presentation; images and (if useful) Mermaid diagrams are embedded directly in the brief so it can be shared as-is or converted to `.docx`/`.pdf`/`.pptx` on demand.

The brief should cover:

- Who Sunlit Sea is and what Gen 2 is (short).
- The road from Gen 1 → Gen 2 → P3 → P4, and why (relevant SuRE D6.1 context: the risk-based development model, the pressing pipeline, the shift to hydroforming, PU role as infill/thermal layer).
- Current state of Gen 2 PU: measured Gen 1 dark-blue absorptivity 0.88–0.91, Gen 2 off-white PU with expected ~0.35 (T12 still to measure), UV testing status at IFE (T14), adhesion testing status on P3 (T15), P4 mould cast in progress (T17).
- What we want from Norsmaterials specifically: mould design help, test casting, per-test feedback loop, joint test-plan iteration.
- Open questions we want their input on (cast-on-frame vs separate-and-mount decision T19; long-term aquatic durability vs 25-year target vs primer's 20-year figure; PU-glass and PU-aluminium adhesion under UV; anything else).

**Images to consider embedding** (from `sure/images/` — relative path from `gen2/norsmaterials_brief.md` is `../sure/images/…`): `fpv_gen1_assembly.png`, `fpv_gen1_float.png`, `cup_shape.png`, `gen1_cooling_of_pv_from_heat_transfer_to_water.png`, the Gen 2 Prototype 4 overview figures, and pressing / hydroforming visuals. Mermaid diagrams (fenced blocks) are fine where they clarify flow (e.g. the model chain, the P3 → P4 → P5 iteration loop, the per-cast feedback loop) — mermaid-filter will render them at conversion time.

**Sub-step (research):** Look up Norsmaterials before writing/expanding the brief — company profile, product range, prior collaborations, published capabilities on PU casting for marine / outdoor / photovoltaic applications. Done; notes in `gen2/notes_norsmaterials.md`.

**Files:** `gen2/norsmaterials_brief.md` (the deliverable), `gen2/notes_norsmaterials.md` (research notes, kept alongside).

**Progress:**

- **Research** (2026-07-03) — `gen2/notes_norsmaterials.md` written: company profile (Sandane, Strukturplast heritage), product families (NORSelast® variants 01/02/S4/EL/PIR/Spray/AF + NORSfoam®), served industries (maritime, energy, aquaculture, defence), capabilities (in-house casting, R&D collaboration model, circular-economy focus), and an explicit list of technical data *not* on the public page (hardness, temperature window, UV data, adhesion data) to bring to the first meeting rather than guess.
- **Initial brief draft** (2026-07-03) — `gen2/norsmaterials_brief.md` written: Purpose, Who we are, Gen 1 → Gen 2 story (with comparison table), Where PU sits in Gen 2 (with the two open architectural questions A and B), Measurement status table (including the Al 5083-H111 material card), Development pipeline they'd plug into, What we want from them (six concrete asks), Open questions (five), What we can share (figures / CAD / material data), Practical (timeline, next step, contact). Skips PU-101 per the calibration note in the research doc. No images or Mermaid embedded yet — that comes with the next iteration when Eirik has reviewed the text.
- **Next iteration:** embed images from `sure/images/` and any useful Mermaid diagrams; incorporate Eirik's review comments.

---

### T73 `[ ]` Adopt root-level `background/` convention with `new/` inbox and timestamp-prefixed files

Generic (non-activity-specific) background material should live in a top-level `background/` folder. The folder has been created (currently empty). The convention, copied from the `../fjordgata30` project:

- `background/` — historical / processed background material for the repo as a whole. Files carry a date-prefix on the form **`YYYY-MM-DD_description.ext`** (e.g. `2025-11-14_investor_update_q3.md`). Activity-specific background stays under the activity folder (`sure/background/`, `gen2/background/` etc.); `background/` at root is for material that spans activities or predates them (e.g. company-level investor updates, legal docs, funding history).
- `background/new/` — **inbox** for files that have not been processed yet. Typically pictures, PDFs, DOCX or other formats that should be converted to Markdown. Once processed, the resulting `.md` (and the original if worth keeping) is date-prefixed and moved to `background/`. The bullet says old investor updates have been placed into `background/`; the folder is currently empty on disk, so those files are either not yet copied in or the description was of intent.

**Conversion pipeline for `background/new/`:**

| Source format | Tool | Command shape |
|---|---|---|
| `.pdf` | `pdftotext` | `pdftotext -layout "background/new/foo.pdf" background/new/foo.txt` then hand-tidy into `.md` |
| `.docx`, `.pptx`, `.odt`, `.rtf`, `.html` | `pandoc` | `pandoc "background/new/foo.docx" -o background/new/foo.md --wrap=none` |
| `.md`, `.txt` | (already text) | tidy, then timestamp-prefix and move |
| `.png`, `.jpg`, `.jpeg` and other true binary evidence | keep as-is | timestamp-prefix and move; do not attempt conversion |

After conversion: review the `.md`, add a short front-matter or preamble noting the source file and (if known) the original date, rename with `YYYY-MM-DD_description.md` prefix, move to `background/`. Remove the intermediate `.txt` from `pdftotext`. Keep the original binary in `background/` only if it is the authoritative source (signed PDFs, presentations we might want to redistribute); otherwise the `.md` supersedes it.

**Concrete actions:**

1. Create `background/new/` (currently missing).
2. Add a short `background/README.md` documenting the convention (root-generic vs. activity-specific; `new/` inbox flow; timestamp-prefix format `YYYY-MM-DD_description.ext`; PDF → `pdftotext -layout` → `.md`; keep pictures as-is with a timestamped filename).
3. Add a rule to the top-level `CLAUDE.md` under working rules: at the start of a task, check `background/new/` (and any `*/background/new/`) for unprocessed files and ask the user whether to process them, in parallel with the existing check on the `## New items` bullet section of `TASKS.md`.
4. Add a rule to `CLAUDE.md` covering the timestamp-prefix format, so future files added to `background/` follow it automatically.
5. Update the top-level `README.md` folder layout to include `background/` and the inbox convention.

**No files to process right now** — `background/new/` will be empty until Eirik drops in whatever old investor updates were meant for it. Then a separate task (or an ad-hoc processing session) converts them.

---

### T74 `[ ]` [FUND] Investor recap for the past year — enrich Eirik's writeup with project content

We want to send our investors an annual recap of the past year (roughly 2025-07 → 2026-07). Eirik will write a short seed writeup that captures the framing, tone and the specific milestones he wants to lead with. My job is to take that seed and elaborate / enrich it with concrete material from this repo:

- **From `sure/`** — the D6.1 delivery, IFE tracked-change round, the analysis / repetition passes, the KPI estimates for aluminium reduction and thermal improvement, the Gen 1 → Gen 2 story, the pressing-pipeline / hydroforming switch, ~1,300 feasible geometries screened, D6.2 in preparation.
- **From `gen2/`** — P3 → P4 progress, P4 mould cast started, Norsmaterials collaboration under exploration (see T72), open architecture questions (cast-on-frame vs. separate-and-mount, thermal bridge reintroduction).
- **From `background/`** — prior investor updates (once populated) to keep tone, cadence and specificity consistent with previous rounds and avoid re-narrating things investors already know.
- **From `funding/` and Sunlit Sea's grant / EU reporting** — Horizon Europe SuRE status, CINEA review posture, funding roadmap.

**Files to produce:** `funding/2026-XX-XX_investor_recap.md` (date-prefix set when finished), Pandoc-ready Markdown for later `.docx` conversion on Eirik's order.

**[BLOCKED — needs input from EIRIK]**: Deliver the seed writeup (rough is fine — bullet list, half a page, whatever) so I can enrich against it rather than guess at the desired framing and tone.
