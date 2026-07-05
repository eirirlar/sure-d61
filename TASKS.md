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
- **Second-pass enrichment from `background/` løypemeldinger** (2026-07-03) — after processing 27 investor updates into `background/*.md`, read the Gen 2 / PU / casting-relevant ones and folded these facts into the brief:
  - **Existing supplier relationship with Strukturplast (now Norsmaterials)** since ≥2022 for Gen 1 connectors (`koblingspunkter`) — this changes the brief from a cold approach to an expansion of a working relationship. Added a new "Prior relationship with Strukturplast (now Norsmaterials)" section right after "Who we are".
  - **Product name is Sunlit Sea CONNECT gen. 2** with architecture "standard 710–740 Wp panels + cast PU frame + aluminium bottom", 80–90% cheaper than Gen 1. Updated the Gen 1→Gen 2 comparison table with PV type, module size, hinge, manufacturing location, cost target rows.
  - **PU has three distinct roles, not two** — cast structural frame, thermal-bridge-blocking infill, and connector-rod PU-foam. Rewrote the "Where PU sits in Gen 2" section accordingly.
  - **Current manufacturing at Tongge (Weihai, China)** for prototype 3 (Oct 2025 visit); Sunlit Sea explicitly considering Norway-based prototype casting with 3D-printed moulds before further Chinese orders. Added this as ask #2 in "What we want from Norsmaterials" — it's the exact gap Norsmaterials fills.
  - **Hinge revision from Surewave wave-tank findings** — added a specific ask (#4) about castability of the revised hinge and connector-rod formulation.
  - **Storavatnet reference pilot** — Haugaland Næringspark, 3.2 MWp phase 1, 30–50 MW long-term. Added to "Who we are" and "Practical" as the flagship deployment target.
  - **TRL 5–6** currently — added to "Practical".
- **Third-pass enrichment from a full D6.1 read** (2026-07-05) — Eirik pointed out that I had not systematically read `sure/report.md` end-to-end before writing the brief. Corrected that: read Section 3.5 (prototyping / mould workflow), Section 5.2 (thermal / PU optical properties), Section 5.3 (mechanical / adhesion / UV), and figure captions throughout Chapter 2. Also corrected the Strukturplast wording from "predecessor company" (implies legal succession) to "you were called Strukturplast until you renamed" (name change only). Folded in:
  - **Measurements-and-methods table rebuilt.** Now includes: absorptivity 0.88–0.91 with the measurement methodology; emissivity ε = 0.85 with methodology; the informal PU-softens-after-2h-at-45°C observation; PU tensile data across 70A/80A/90A Shore grades with numerical values; the failed condition-A3 UV run at 209 h (chamber 65 °C / black-panel 90 °C / 0.8 W/m² at 340 nm / 80 % RH; darkening + burn marks; 70A/80A softened, 90A stayed hard; ~95 °C sample T) and the revised condition-A1 protocol; the 70 °C design limit used for PU-hinge peak T in modelling; the P3 adhesion-test methodology adaptation (tempered glass shattered on cutting); the P4 SiSim stress results (Al approaching yield, PU exceeded yield locally, glass sensitive to PU-ring attachment); the P4 buoyancy shortfall (half of bottom plate submerged under self-weight).
  - **New "Design constraints Norsmaterials should know about" section.** Hinge halves cast integrally with float-structure on all four sides; PU-foam connector rods on all four sides (structural + buoyancy); grounding pins passing through cast PU; hinge design principle (loads through connection centre, away from PU-glass and PU-Al interfaces = water-ingress paths); the six-load-case × six-measurement-point structural test framework; combined UV+heat > either alone; P4 buoyancy shortfall; puzzle-fit PU-foam infill as alternative concept.
  - **Mould workflow expanded.** Documented the existing four-step process (FreeCAD parametric mould → 3D-printed mould → casting onto mock panels → metal mould promotion). Called out that Norsmaterials fits in two places (Norway prototype casting + metal-mould promotion advice).
  - **"What we want" list grew from 6 to 9 asks** — adding grounding-pin integration, lower-density formulation for buoyancy, and expanded mould-design collaboration (3D-print and metal).
  - **"Open questions" list grew from 5 to 9** — adding combined UV+heat safety margin, Norway prototype turnaround, metal-mould promotion strategy, grounding-pin integration, low-density formulation.
  - **"What we can share" list expanded** with the specific figures from D6.1 (metal casting mould, P4 connector mould with carabiner mechanism, puzzle-fit infill, grounding-pin concept), PU tensile data across three hardness grades, UV protocols and 209-h failure, the six-load-case matrix, the Roosloot / Selj / Otnes 2024 IEEE JPV paper on Gen 1 edge-sealant durability that the current adhesion methodology builds on.
- **Fourth-pass — Strukturplast section removed** (2026-07-05). Eirik: prior relationships are not relevant to a forward-looking brief about the work we are doing and how to collaborate. Dropped the "Prior relationship — you were Strukturplast until you renamed" section entirely.
- **Fifth-pass — 10 images embedded** (2026-07-05). Approved by Eirik. Picks driven by how each image is annotated and used in `sure/report.md`:
  - Fig 1 `gen2_matrix_installed_rendered_still_water.png` in *Who we are* — D6.1 uses it as Fig 1-3 for the same "opening ambition shot" purpose.
  - Fig 2 `fpv_gen1_float.png` and Fig 3 `gen2_prototyp4_freecad_model.png` after the Gen 1 → Gen 2 comparison table — D6.1 Fig 1-1 and Fig 3-3.
  - Fig 4 `fpv_top.png` (D6.1 Fig 2-2 a — cast PU frame + integrated hinge halves), Fig 5 `gen2_freecad_infill_split_PUfoam.png` (D6.1 Fig 2-6), and Fig 6 `..._connector_buoyant_PUfoam_rods_4sides.png` (D6.1 Fig 2-12), indented under the three PU-role list items in *Where PU sits in Gen 2*.
  - Fig 7 `gen2_prototyp4_freecad_hinge_left.png` (D6.1 Fig 2-10) and Fig 8 `groundings.png` (D6.1 Fig 2-9) indented under the hinge-integrality and grounding-pins bullets in *Design constraints*.
  - Fig 9 and Fig 10 `gen2_prototyp3_casting1.png` and `_casting2.png` (D6.1 Fig 3-4 / Fig 3-5) as a pair after the four-step mould-workflow list — before/after the metal-mould promotion step.
  - Captions trimmed from D6.1's formal "Figure X-Y. [full description]" to shorter brief-tone phrasing while preserving the specific features D6.1 names. No image file was modified; paths use `../sure/images/<filename>.png`.
- **Sixth-pass — Norwegian project pipeline expanded** (2026-07-05). Eirik added two projects to the pipeline the collaboration would feed: **Skien havn** (~300 kWp, near-term) and **Gunnekleivfjorden inside Hærøya Industripark** (3.2 MWp, a bit later than Storavatnet). Updated both the *Who we are* pipeline list and the *Practical* timeline paragraph so Norsmaterials sees three concrete Norwegian deployments — near-term, flagship, and mid-term — rather than the single Storavatnet mention.
- **Seventh-pass — module size correction** (2026-07-05). The Gen 1 → Gen 2 comparison table stated Gen 2 module size as ~55 × 70 cm. Eirik corrected: that dimension is for **prototypes P3 and P4 only** (scaled-down for iteration speed). The **end product** uses utility-scale panels at **2384 × 1303 mm** per module (matching the 710–740 Wp panel size already listed in the PV row of the same table). Rewrote the row to state end-product target first and prototype dimension second, so Norsmaterials sees the correct scale.
- **Eighth-pass — aluminium forming softened** (2026-07-05). The brief claimed the Gen 2 aluminium bottom is "pressed via hydroforming rather than punch/die" as if the forming decision was locked in. Eirik corrected: hydroforming is **not set in stone**, and a **flat sheet attached to the PV panel frame is currently more likely** than any forming route. Updated three places:
  - Aluminium-sheet row of the Gen 1 → Gen 2 comparison table — now states "Base case: flat sheet ... Hydroforming ... is under evaluation as an alternative ... but flat is currently the more likely choice for the shipping product."
  - "Two evolutions" narrative below the table — reframed to say the current base case is flat, with pressed as an evaluated alternative; kept the point that IF we form, hydroforming avoids the tool-wear / thinning risks of punch/die (that finding stands and is worth conveying).
  - The Cast-on-frame vs. separate-and-mount open question A — changed "pressed-aluminium float body" to "aluminium float body (flat sheet or pressed cup, depending on the pending forming decision)".
- **Ninth-pass — infill row spatial detail + infill variants** (2026-07-05). Eirik: (a) the cast PU frame needs a spatial description; (b) the interior infill has three variants, not one. Updated three places:
  - Infill / structure row of the comparison table — cast PU frame now described as "**wrapping around the PV panel frame and bonded to the panel glass and the aluminium bottom plate**"; interior infill is "most likely a cast-in-place PU foam, possibly reinforced with a large-cell aluminium honeycomb, or alternatively pre-cast PU pieces fitted in place with a gel-like adhesive".
  - PU role #2 in the *Where PU sits in Gen 2* section — retitled to "Interior infill (most likely PU foam)" and expanded to list the three variants (cast-in-place foam / pre-cast pieces with gel adhesive / foam + honeycomb reinforcement), with a cross-reference to open question B on whether to reintroduce a thermal bridge.
  - "Alternative infill under consideration" bullet in *Design constraints* — expanded from just puzzle-fit into "Alternative infill **concepts** under consideration" listing both puzzle-fit (with gel-like adhesive emphasis) and the honeycomb-reinforced variant.
- **Tenth-pass — off-white PU status corrected** (2026-07-05). The brief presented off-white PU as the Gen 2 answer with only absorptivity still to measure. Eirik: off-white has now been **evaluated on Prototype 3 and UV damage is still unacceptable**. Actively searching for a better UV-resistant PU. Updated five places:
  - PU-top-layer row of the comparison table — flipped from "expected absorptivity ~0.35, not yet measured" to "off-white was first choice, improves thermal, **UV damage still unacceptable** on P3 evaluation, actively searching for a better UV-resistant PU as a top ask of the Norsmaterials collaboration."
  - Narrative paragraph below the table — added a sentence noting the off-white evaluation outcome and framing "finding a PU that solves both thermal and UV" as one of the top reasons for the collaboration.
  - Measurements table row "Gen 2 P3 UV on white PU (condition A1)" — flipped from "In progress at IFE" to "Evaluated — UV damage still unacceptable on the off-white PU."
  - "What we want" ask #1 (PU formulation choice for three roles) — added the off-white failure as concrete context under (a) the cast structural frame, and flagged "a better UV-resistant PU for the top layer is our most urgent open item."
  - Open question #2 (Combined UV + heat safety margin) — added the off-white A1 failure alongside the earlier dark-PU A3 failure and reframed to ask which of their variants would actually get us to 25 years.
- **Eleventh-pass — PV-water distance clarified** (2026-07-05). The comparison-table cell for the Gen 2 PV-to-water distance said "6 cm (with a 2° panel tilt)" but did not specify that 6 cm is the elevation at the **lowest edge** — the tilt puts the opposite edge higher. Updated the cell to "6 cm at the lowest edge — the panel sits at a 2° tilt, so the opposite edge sits higher."
- **Twelfth-pass — manufacturing framing updated** (2026-07-05). The brief presented P4 Norway-casting as something Norsmaterials would kick off from scratch. Eirik: **in-house prototype casting has already started in Norway**; we're **looking for a collaboration partner** to accelerate and inform it; **open to full Norwegian production for the shipping product if it can be cost-competitive** with Tongge. Updated three places:
  - Manufacturing row of the comparison table — explicit that in-house Norway casting has started and that we're open to full Norwegian shipping-product production if economics work.
  - "Where Norsmaterials fits" paragraph in *Development pipeline* — reframed from "casting P4 prototypes in Norway" to "collaborating on the in-house prototype casting we have already started in Norway", with the long-term Norway-production ambition appended.
  - "What we want" ask #2 — retitled from "Norway-based prototype casting to close our current gap" to "Collaboration on our in-house Norway prototype casting" and rewritten to name the specific expertise we lack (PU formulation, mould design, cure behaviour), plus the long-term shift-to-Norway ambition.
- **Thirteenth-pass — bold stripped from body text** (2026-07-05). Eirik: no bold (`**...**`) inside sections — only in titles/subtitles. Ran `sed 's/\*\*//g'` after dry-run confirmed word count identical (4150 before/after) and figure captions intact. All 70 in-section bold markers removed from paragraphs, list items and table cells. YAML `title:` and `subtitle:` and Markdown `##` / `###` headers untouched (they don't use `**`). Rule saved as memory feedback `feedback-no-bold-in-body-text.md` for future writing.
- **Fourteenth-pass — cost target reframed to market economics** (2026-07-05). Eirik: don't link the cost target to Gen 1. Link it to the global EPC market: glass/glass PV panels ~€130/kWp from China; turnkey EPC solar-park delivery €300–€1800/kWp; goal is to compete across that whole range; therefore Sunlit Sea production cost on top of the panel cost must be ≤ €70/kWp, leaving ~€100/kWp for logistics, inverters, electrical, installation (with the low end of the EPC range excluding some of these). Updated two places:
  - Cost-target row of the comparison table — Gen 1 column now says "n/a — Gen 1 was a small-volume specialty product; cost was never targeted at commodity EPC scale"; Gen 2 column carries the full market framing with the numeric build-up.
  - "Who we are" intro — replaced "targets 80–90% lower material and production cost than Gen 1" with "targets the cost point where floating PV competes with turnkey EPC solar-park economics globally (€300–€1800/kWp depending on market)."
- **Fifteenth-pass — consistent image widths (first attempt, wrong syntax)** (2026-07-05). Applied Pandoc image-attribute syntax `{width=451px}` to all 10 image references. Eirik reported it rendered as literal text after each image — turns out Pandoc's attribute syntax is Pandoc-only; VS Code preview, GitHub Flavored Markdown and most other renderers do not understand it. WebSearch confirmed. Rolled back to HTML approach (see next pass).
- **Sixteenth-pass — HTML `<figure>` / `<img>` / `<figcaption>` rewrite** (2026-07-05). Wrote `scripts/md_image_to_html.py` to transform `![CAPTION](PATH){width=Npx}` into an HTML `<figure>` block with `<img … width="N" />` and a visible `<figcaption>`. HTML is passed through by every Markdown renderer including Pandoc, so the width attribute now works in VS Code preview, GitHub, and Pandoc-generated docx/pdf. Bonus: figcaption makes the caption visible in every renderer, whereas the previous `![alt](path)` syntax only showed alt text when the image failed to load. Ran the script default (safe: writes sibling `.htmlimg.md`); inspected output including the four list-nested images (indentation preserved); then promoted with `mv`. All 10 images now use `width="451"`, matching the smallest image's native width. Script documented under `## Scripts` in the top-level `README.md`.
- **Seventeenth-pass — off-white PU history corrected** (2026-07-05). The brief had been describing off-white PU as "the first Gen 2 choice" or "the switch to off-white PU in Gen 2" or "the off-white replacement we selected for Gen 2". Eirik: off-white was tried on **Gen 2 Prototype 3** alongside the primary water-ingress test on dark blue PU. Prototypes P1, P2 and P3 all used dark blue PU as the primary top layer. Off-white is under evaluation, not selected — and evaluation has shown UV damage. Updated six places:
  - Comparison-table PU top layer row — now describes P1/P2/P3 all using dark blue with off-white tried alongside on P3; says "Off-white is not a confirmed Gen 2 direction".
  - Narrative paragraph below the table — replaced "drove the switch to off-white PU in Gen 2" with "motivated an off-white PU evaluation on Gen 2 Prototype 3, run alongside the primary water-ingress test on dark blue PU".
  - Measurements-table row for off-white absorptivity — retitled from "Gen 2 off-white PU absorptivity" to "Off-white PU absorptivity (tried alongside dark blue on Gen 2 Prototype 3)".
  - Measurements-table row for the P3 UV test — retitled to "Gen 2 P3 UV on off-white PU (condition A1)" and appended "Off-white is not confirmed for Gen 2".
  - What-we-want ask #1 — changed "the off-white replacement we selected for Gen 2 has since also shown unacceptable UV damage on Prototype 3" to "the off-white variant we tried alongside on Gen 2 Prototype 3 has since also shown unacceptable UV damage".
  - Open question #2 — same "selected" → "tried alongside dark blue" correction.
- **Next iteration:** incorporate Eirik's review comments after he reads the brief with images; possibly add one or two Mermaid diagrams if useful for the mould-workflow or per-cast feedback loop.

---

### T73 `[x]` Adopt root-level `background/` convention with `new/` inbox and timestamp-prefixed files

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

**Solution (2026-07-03):**

1. Created `background/new/` (root-level inbox folder).
2. Documented the convention in the top-level `README.md` under a *Background convention* section: what belongs at root vs. under an activity, the `YYYY-MM-DD_short_description.ext` filename format, the inbox flow, the conversion pipeline table (`pdftotext -layout` for PDFs, `pandoc … --wrap=none` for DOCX/PPTX/ODT/RTF/HTML, keep pictures as-is), and the post-conversion tidy + rename + move steps. Originally written as `background/README.md` but consolidated into the root README when the *single-README* rule was adopted (see the "consolidate sub-READMEs" turn).
3. Added two working rules to top-level `CLAUDE.md` under `## Working rules`:
   - **`background/new/` inbox check** — at the start of every working session, check `background/new/` (root) and `*/background/new/` (activity-level) for files and ask the user whether to process them, mirroring the existing `## New items` check for `TASKS.md`.
   - **`background/` naming convention** — every file in a `background/` folder must have a `YYYY-MM-DD_short_description.ext` prefix, applied immediately on add; un-prefixed files get renamed at next touch.
4. Updated top-level `README.md` folder layout to include `background/` alongside the four activity folders.
5. No files to process — `background/new/` is empty on disk.

**Files touched:** `background/` (created), `background/new/` (created), `CLAUDE.md` (two rules added), `README.md` (folder layout + Background convention section added).

**Addendum (2026-07-03) — processed the 27 files that turned out to be in `background/new/`.** Eirik had dropped them in earlier; I missed them at first because my initial checks were too early and my T73 verification only listed the parent `background/`, not `background/new/` itself. He asked me to process them:

- 14 PDFs (2020-02-05 → 2022-03-29) converted with `pdftotext -layout -enc UTF-8` (first pass mangled Norwegian letters; re-ran with `-enc UTF-8` to fix `løypemelding`, `å`, `ø`, `æ`).
- 13 DOCX (2022-06-01 → 2025-11-17) converted with `pandoc … --wrap=none`.
- Word counts sanity-checked: range 373 – 2 278 words per document; no empty or near-empty extractions.
- All 27 renamed to the convention format: `YYYY-MM-DD_lopemelding.{md,pdf,docx}` for Løypemelding, `2024-01-29_lopemelding_draft.*`, `2024-10-01_progress_report.*`, `2025-06-10_arsmelding.*` for the odd ones. YAML preamble added to each `.md` recording original source filename, date, and document type.
- Inbox `background/new/` is now empty.
- **Convention was not followed on the first pass** — I kept all originals alongside the `.md`, rationalising it as "docx has embedded content pandoc may miss." Eirik corrected this ("Don't diverge from instructions") and deleted the `.pdf` / `.docx` originals himself. Investor updates are not signed contracts / signed PDFs / redistributable presentations, so per the T73 convention the `.md` supersedes and the originals were correctly dropped. The mistake is recorded in memory (feedback: don't deviate from a rule I just wrote).

---

### T74 `[ ]` [FUND] Investor recap for the past year — enrich Eirik's writeup with project content

We want to send our investors an annual recap of the past year (roughly 2025-07 → 2026-07). Eirik will write a short seed writeup that captures the framing, tone and the specific milestones he wants to lead with. My job is to take that seed and elaborate / enrich it with concrete material from this repo:

- **From `sure/`** — the D6.1 delivery, IFE tracked-change round, the analysis / repetition passes, the KPI estimates for aluminium reduction and thermal improvement, the Gen 1 → Gen 2 story, the pressing-pipeline / hydroforming switch, ~1,300 feasible geometries screened, D6.2 in preparation.
- **From `gen2/`** — P3 → P4 progress, P4 mould cast started, Norsmaterials collaboration under exploration (see T72), open architecture questions (cast-on-frame vs. separate-and-mount, thermal bridge reintroduction).
- **From `background/`** — prior investor updates (once populated) to keep tone, cadence and specificity consistent with previous rounds and avoid re-narrating things investors already know.
- **From `funding/` and Sunlit Sea's grant / EU reporting** — Horizon Europe SuRE status, CINEA review posture, funding roadmap.

**Files to produce:** `funding/2026-XX-XX_investor_recap.md` (date-prefix set when finished), Pandoc-ready Markdown for later `.docx` conversion on Eirik's order.

**[BLOCKED — needs input from EIRIK]**: Deliver the seed writeup (rough is fine — bullet list, half a page, whatever) so I can enrich against it rather than guess at the desired framing and tone.
