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

### T74 `[ ]` [FUND] Investor recap for the past year — enrich Eirik's writeup with project content

We want to send our investors an annual recap of the past year (roughly 2025-07 → 2026-07). Eirik will write a short seed writeup that captures the framing, tone and the specific milestones he wants to lead with. My job is to take that seed and elaborate / enrich it with concrete material from this repo:

- **From `sure/`** — the D6.1 delivery, IFE tracked-change round, the analysis / repetition passes, the KPI estimates for aluminium reduction and thermal improvement, the Gen 1 → Gen 2 story, the pressing-pipeline / hydroforming switch, ~1,300 feasible geometries screened, D6.2 in preparation.
- **From `gen2/`** — P3 → P4 progress, P4 mould cast started, Norsmaterials collaboration under exploration (see T72), open architecture questions (cast-on-frame vs. separate-and-mount, thermal bridge reintroduction).
- **From `background/`** — prior investor updates (once populated) to keep tone, cadence and specificity consistent with previous rounds and avoid re-narrating things investors already know.
- **From `funding/` and Sunlit Sea's grant / EU reporting** — Horizon Europe SuRE status, CINEA review posture, funding roadmap.

**Files to produce:** `funding/2026-XX-XX_investor_recap.md` (date-prefix set when finished), Pandoc-ready Markdown for later `.docx` conversion on Eirik's order.

**[BLOCKED — needs input from EIRIK]**: Deliver the seed writeup (rough is fine — bullet list, half a page, whatever) so I can enrich against it rather than guess at the desired framing and tone.

---

### T80 `[x]` [FUND] Anmodning til Skatteetaten om tvangsmulkt-utsettelse for skattemelding 2025

Skatteetaten har varslet vedtak om tvangsmulkt for manglende innlevering av skattemelding for inntektsåret 2025 (brev datert 03.07.2026, referanse SKFIN/2026/64323417). Ordinær leveringsfrist var 30.06.2026. Ny frist for å unngå tvangsmulkt er satt til 13.07.2026. Mulkten er 672,50 kr per dag, med maksbeløp 13 450 kr (20 dager).

Årsoppgjøret er forsinket pga (a) begrenset kapasitet i administrasjonen, (b) bytte av regnskapsfører i perioden. Vi jobber på spreng med revisor. Ønsket ny leveringsdato: 19. august 2026.

Kildebrev fra Skatteetaten: `background/2026-07-01_skatt_varsel_tvangsmulkt.txt`

**Dokumentstruktur:**

- `background/2026-07-09_forsinket_aarsoppgjoer.md` — bakgrunnsnotat om hvorfor årsoppgjøret er forsinket (situasjon, historikk, faktagrunnlag). Ikke skrevet enda av Eirik. Bakgrunn for anmodningen, ikke selve leveransen.
- `background/2026-07-09_anmodning_skatteetaten_tvangsmulkt.md` — selve anmodningsdokumentet som sendes til Skatteetaten. Ikke skrevet enda; skal etableres som ny fil under `background/`. (Opprinnelig i `leveranser/` — mappen ble innført ved T80 og senere flyttet til `background/` i T96.).

**Deliverables i T80:**

- Lovutdrag lagret i `background/lover/`:
  - `2017-01-01_skatteforvaltningsloven_8-1_alminnelig_opplysningsplikt.md`
  - `2024-01-01_skatteforvaltningsloven_8-2_skattemelding_formues_inntektsskatt.md`
  - `2026-01-01_skatteforvaltningsloven_14-1_tvangsmulkt.md`
  - `2017-01-01_skatteforvaltningsloven_14-2_saksbehandlingsregler_tvangsmulkt.md`
  - `2023-07-07_skatteforvaltningsforskriften_14-1-1_utmaaling_tvangsmulkt.md`
- Skriftlig forklaring (i chat) av rettskildene, hvordan slippe å betale, og forslag til struktur for selve anmodningen.

**Solution (2026-07-09):**

Alle fem lovutdrag skrevet. Kort strategisk oppsummering av rettskildene og forslag til fremgangsmåte gitt i chat-svaret som en veiledning for Eiriks utforming av `background/2026-07-09_forsinket_aarsoppgjoer.md`. Praktisk vei fremover:

1. **Primær vei — levere i tide.** Skattemelding levert elektronisk innen 13.07.2026 gir null tvangsmulkt. Dette er den eneste lovhjemlede måten å 100% unngå mulkt på.

2. **Sekundær vei — anmode om utsatt frist / utsatt iverksetting.** Skfvl har ingen direkte hjemmel for å utsette tvangsmulkt-iverksettingstidspunktet etter et vedtak er varslet (skfvl § 14-10 gjelder utsatt iverksetting av tilleggsskatt og overtredelsesgebyr, ikke tvangsmulkt). Men Skatteetaten har praksis for å innvilge kort utsettelse (typisk noen dager–uker) på forhåndsanmodning ved dokumenterte særlige grunner. Bytte av regnskapsfører kombinert med aktiv fremdrift sammen med revisor er tema som brukes i slike anmodninger.

3. **Tertiær vei — klage / anmodning om ettergivelse etter § 14-1 tredje ledd.** Hvis mulkt påløper: skfvl § 14-1 tredje ledd åpner for at Skatteetaten kan frafalle påløpt mulkt ved særlige grunner. I vår anmodning bes det om full ettergivelse (ikke delvis reduksjon). Klagefrist etter § 14-2 og kap. 13 er 6 uker fra brevets mottakelse.

4. **Ikke aktuelt for oss — umulig oppfyllelse.** Skfvl § 14-1 fjerde ledd fritar bare når oppfyllelse er umulig pga forhold som ikke skyldes den ansvarlige. Regnskapsfører-bytte + administrativ kapasitet regnes ikke som slikt forhold i Skatteetatens praksis.

**Forslag til struktur for anmodningsdokumentet i `background/`:**

1. Referanse til Skatteetatens brev (dato + saksnummer)
2. Kort forklaring av forsinkelsen (begrenset kapasitet i administrasjonen + bytte av regnskapsfører i perioden)
3. Bekreftelse på at revisor er engasjert og arbeider på spreng
4. Konkret anmodning: utsettelse av leveringsfrist / tvangsmulkt-iverksettelse til 19. august 2026
5. Subsidiært: anmodning om ettergivelse av eventuell påløpt tvangsmulkt etter skfvl § 14-1 tredje ledd
6. Signatur og kontaktopplysninger

**Anmodningen skrevet:** `background/2026-07-09_anmodning_skatteetaten_tvangsmulkt.md`. Følger malen ovenfor. Plassholdere for signatur (navn/rolle/e-post/telefon) fylles inn av Eirik når det er bestemt hvem som signerer — signeringen krever selskapsrettslig fullmakt (jf. skatteforvaltningsloven § 8-15 tredje ledd), dvs. Per Lindberg som CEO/styreleder eller annen med signaturfullmakt registrert hos Skatteetaten.

`leveranser/`-mappen etablert som ny top-level-mappe i repoet ved denne leveransen. Speiler `../fjordgata30/leveranser/` og holder eksterne leveranse-dokumenter (anmodninger, klager, forespørsler, formelle utgående brev) samlet.

**Files touched:** 5 nye filer i `background/lover/`.

---

### T81 `[x]` [FUND] Revisorspakke: prinsippendring aktivering av SuRE-utviklingskostnader + avskrivningsstopp + nedskrivingstest 2025

Sunlit Sea AS skal levere en samlet informasjonspakke til revisor som dekker (a) prinsippendring i 2025-regnskapet fra kostnadsføring til aktivering av SuRE-utviklingskostnader, (b) reversering av avskrivninger på tidligere aktiveringer fra og med 2024-01-01, og (c) nedskrivingstest på den utvidede utviklingsposten. Pakken vedlegges en mail til regnskapsfører først, med konkrete oppfølgingsspørsmål, før den sendes videre til revisor.

Kravene til leveransen er utviklet i lang chat-diskusjon med Eirik. Denne task-beskrivelsen inneholder ALLE beslutninger og fakta som trengs for at en fresh Claude-kontekst kan gjennomføre arbeidet uten å måtte gjenoppdage detaljene.

**Deliverables:**

1. `funding/2026-07-14_revisorpakke_prinsippendring_aktivering_nedskrivingstest.md` — én selvstendig .md-fil som integrerer alt (prinsippendring, aktivering-oversikt, vilkårsvurdering, tilskuddsbehandling, avskrivningsreversering, avskrivningsstart, balanseeffekt, nedskrivingstest, konklusjon). Filen skal stå på egne ben — ingen kryssreferanser til andre filer i repoet, ingen `../background/lover/`-lenker, ingen `funding/nedskriving_2025.md`-referanser. Alle nødvendige fakta inline. Filnavn ASCII (transliterer æ/ø/å).

2. `funding/2026-07-14_mail_regnskapsforer_revisorpakke.md` — kort mail-tekst som legger pakken ved og stiller de eksplisitte oppfølgingsspørsmålene til regnskapsfører (se pkt "Mail til regnskapsfører" nedenfor).

**Kilder som må leses før implementering:**

- `funding/aktivering_reklassifisering.md` — Eiriks opprinnelige research på prinsippendringen
- `funding/aktivering_regnskapsforer_mail.md` — mail-tråden med regnskapsfører, inkludert konkrete tall
- `funding/background/2025-12-31_kto_1005_aktivert_utvikling.md` — aktivert utvikling saldo per 31.12.2025 og 2025-avskrivninger per aktiveringsår
- `funding/background/2025-12-31_kto_2160_opptjente_tilskudd.md` — opptjente tilskudd saldo per 31.12.2025 og periodiseringer per aktiveringsår
- `funding/nedskriving_2025.md` — eksisterende nedskrivingstest som gir argumentasjonsgrunnlaget (må omarbeides for større balansepost — men fortsatt "ingen nedskrivning"-konklusjon)
- `background/lover/` — relevante lovtekster (regnskapsloven §§ 1-5, 5-1, 5-3, 5-6; NRS 8; NRS(F) Nedskrivning; NRS 4 Offentlige tilskudd)

**Konkrete beslutninger og fakta (bekreftet i dialog med Eirik):**

*Foretaksklassifisering:*
- Sunlit Sea AS = lite foretak etter regnskapsloven § 1-5 annet ledd
- Anvender NRS 8 God regnskapsskikk for små foretak

*Scope for prinsippendringen:*
- SuRE-kostnader kostnadsført på kto 6791 aktiveres:
  - SuRE 2024: 1 017 809 kr
  - SuRE 2025: 817 942 kr
- Skattefunn er UTENFOR scope — allerede implisitt behandlet via skattefradraget (reduserer betalbar skatt). Ingen Skattefunn-beløp reklassifiseres.

*Metode for prinsippendring:*
- Metode B — resultatføring i endringsåret (2025) etter NRS 8-adgang for små foretak, ikke retrospektiv omarbeidelse av 2024-sammenligningstall etter NRS 5. Enklere administrativt og vanlig for lite foretak.

*Argumentasjon for tidspunkt:*
- Gen 2-utvikling for alvor startet 2024-01-01. Dette begrunner både reklassifisering av SuRE-kostnader fra 2024 og avskrivningsstopp fra samme dato.
- Aktiveringsvilkårene i regnskapsloven § 5-6 annet ledd har vært oppfylt kontinuerlig siden selskapet startet i 2019 (gen 1 nådde TRL 7 og er tatt i bruk; gen 2 er nå på TRL 5-6). Vilkåret om fremtidig økonomisk fordel + pålitelig måling har hele tiden vært til stede.

*Avskrivningsstopp:*
- Alle avskrivninger på kto 1005-rester (2022 Surewave, 2023 Surewave, 2024-aktivering) stoppes fra og med 2024-01-01. Restbeløpene er nå knyttet til gen 2-utvikling som ikke er tatt i bruk.
- Reversering gjelder:
  - Alle 2024-avskrivninger som ble tatt (må bekreftes fra regnskapsfører — estimat ca 7,66 MNOK basert på lineær 5-års avskrivning per aktiveringsår)
  - Alle 2025-avskrivninger som er planlagt (6 562 231 kr per kto 1005)
- Total reversering: ca 14,2 MNOK (estimat, presiseres av regnskapsfører)
- Ikke rør 2021-2023 avskrivninger som allerede er tatt — for langt tilbake, revisor har akseptert, gen 1 er tatt i bruk, ville sett rart ut mot Skatteetaten.

*Avskrivningsstart etter reversering:*
- Avskrivning påbegynnes fra det tidspunkt gen 2 er kommersielt tilgjengelig og tatt i bruk. Estimert lansering er 2027, men avskrivningsstart følger faktisk bruksdato, ikke estimat. Formuleringen skal ikke låse oss til 2027.

*Tilskuddsbehandling:*
- Bruttoføring fortsettes for konsistens med eksisterende praksis (kto 2160 viser bruttoført utsatt inntekt). Ingen bytte til nettoføring.
- Se åpent spørsmål i mail til regnskapsfører — noen tilskudd knyttet til de reklassifiserte SuRE-kostnadene kan allerede være periodisert på annet vis; må avklares for å unngå dobbeltbokføring.

*Nedskrivingstest:*
- Vurderingsenhet: foretakets samlede utviklingsplattform for flytende solkraftverk (én integrert enhet, gen 1 og gen 2 er suksessive versjoner av samme produkt).
- Ingen av de syv minimumsindikatorene i NRS(F) pkt. 3 slår ut — argumentasjonen fra `funding/nedskriving_2025.md` gjelder tilsvarende, bare for et utvidet balansegrunnlag.
- Konklusjon: ingen nedskrivning gjennomføres i 2025-regnskapet.

*Balanseeffekt (Metode B — resultatføring i 2025):*
- Startpunkt kto 1005: 5 648 573 kr (bokført saldo per 31.12.2025 slik regnskapet foreløpig står)
- +SuRE 2024 aktivering: +1 017 809 kr
- +SuRE 2025 aktivering: +817 942 kr
- +Reversering 2025-avskrivninger: +6 562 231 kr
- +Reversering 2024-avskrivninger: +`[AVSKRIV_2024_TOTAL]` (bekreftes av regnskapsfører; estimat ~7,66 MNOK)
- Ny saldo kto 1005: ~14,05 MNOK + `[AVSKRIV_2024_TOTAL]` ≈ ~21,7 MNOK
- Utsatt skatt-forpliktelse (22%): ca 3,53 MNOK
- Netto egenkapital-økning i 2025-regnskapet: ca 12,5 MNOK

*Kto 2160 opptjente tilskudd:*
- Nåværende saldo per 31.12.2025: -5 602 142 kr (utsatt inntekt, kredit)
- Periodiseringen "reduksjon avskrivninger" på kto 2160 må stoppes samtidig med at avskrivningen på kto 1005 stoppes, siden de er koblet. Detaljer krever regnskapsfører-bekreftelse.

**Struktur for revisorpakken (én .md-fil):**

1. Innledning og formål (hva revisor bes ta stilling til)
2. Foretaks- og standardgrunnlag (lite foretak, NRS 8 primær, NRS 4 for tilskudd, NRS(F) Nedskrivning for nedskrivingstest, henvisning til rskl §§ 1-5, 5-1, 5-3, 5-6)
3. Prinsippendring: begrunnelse (gen 2-utvikling startet 2024-01-01), hjemmel (NRS 8-adgang for små foretak fra sammenstillingsprinsippet, rskl § 4-1), valgt metode (Metode B — resultatføring i 2025)
4. Vilkårsvurdering etter regnskapsloven § 5-6 annet ledd (vilkårene har vært oppfylt siden 2019; vilkårene begrenser ikke reklassifiseringen, kost/nytte-vurdering setter praktisk grense)
5. Aktivering-oversikt for SuRE-kostnader (tabell: SuRE 2024 1 017 809, SuRE 2025 817 942)
6. Bruttoføring bekreftes for tilskudd (konsistent med kto 2160-praksis)
7. Reversering av avskrivninger fra 2024-01-01 (konkret: 2024 og 2025-avskrivninger på alle rester; ikke rør 2021-2023-avskrivninger som allerede er tatt)
8. Avskrivningsstart for aktivert utvikling — når produktet er tatt i bruk (gen 2 lansering, dato ikke bundet)
9. Balanseeffekt og resultatpåvirkning (tabell med tallene ovenfor + utsatt skatt)
10. Nedskrivingstest på den utvidede balanseposten (integrert; ingen kryssreferanse til `nedskriving_2025.md` — argumentasjonen replikeres inline: vurderingsenhet, 7 indikatorer, konklusjon "ingen nedskrivning")
11. Konklusjon og hva revisor bes bekrefte

**Mail til regnskapsfører (`funding/2026-07-14_mail_regnskapsforer_revisorpakke.md`):**

Kort tekst som:
- Vedlegger revisorpakken
- Ber om bekreftelse/tallmateriale på følgende:
  1. Eksakt total 2024-avskrivning på kto 1005 (både summen og per aktiveringsår-rad). Estimat ~7,66 MNOK basert på lineær 5-år; må bekreftes fra hovedbok.
  2. Hvordan SuRE-tilhørende tilskudd (EU-utbetalinger, Sintef-tilskudd) er periodisert i regnskapet — spesielt om det finnes tilskudd knyttet til SuRE-kostnadene på kto 6791 som allerede er inntektsført, slik at bruttoføring av de reklassifiserte SuRE-kostnadene ikke vil skape dobbeltbokføring på kto 2160.
  3. At "reduksjon avskrivning" på kto 2160 skal stoppes samtidig med at avskrivning på kto 1005 stoppes, siden postene er koblet. Foreslå at samme prinsipp gjelder alle rester fra 2024-01-01.
  4. Bekrefte at Skattefunn (både 2024 kr 1 258 329 og 2025 kr 507 180) holdes utenfor denne prinsippendringen, siden Skattefunn er implisitt behandlet via skattefradraget.
  5. Bekrefte at 2024-raden på kto 1005 (aktivert 2 187 336 kr) består av rest av tidligere aktiveringer knyttet til gen 1-utviklingen (EU/IN-prosjekter), ikke Skattefunn.
- Ber om at regnskapsfører leser gjennom pakken og gir tilbakemelding før den sendes videre til revisor.

**Åpne spørsmål som ikke er avklart før task startes:**

- AVSKRIV_2024_TOTAL: eksakt beløp fra hovedbok. Estimatet ~7,66 MNOK brukes som plassholder i dokumentet inntil regnskapsfører bekrefter.
- Detaljer om kto 2160-periodisering av tilhørende tilskudd knyttet til SuRE — se mail-spørsmål 2 og 3.
- Detaljert underoppdeling av 2024-raden på kto 1005 (2 187 336) er ikke nødvendig for revisorpakken; omtales generisk som "rest av tidligere aktiveringer knyttet til gen 1".

**Krav ved gjennomføring:**

- Dokumentet må stå på egne ben. Ingen kryssreferanser til andre prosjektfiler.
- Ingen bold i brødtekst — bold kun i seksjons-overskrifter.
- Norsk finans-/regnskaps-terminologi (unngå anglisismer).
- Currency-notasjon: valuta etter tall (feks "5 648 573 kr", ikke "kr 5 648 573" der det er unødvendig).
- Filnavn ASCII (transliterer æ→ae, ø→oe, å→aa).
- Markdown-lister skal rendres korrekt — bruk `-`/`1.` for enumereringer, hard line breaks for signatur/adresseblokker.
- ETT dokument, ikke flere bilag. Alle nødvendige tabeller integreres inline.

**Solution (2026-07-14):**

To filer skrevet til `funding/`:

1. `2026-07-14_revisorpakke_prinsippendring_aktivering_nedskrivingstest.md` (3 385 ord) — 12 seksjoner integrert. Innledning, foretaks- og standardgrunnlag, prinsippendring m/hjemmel og Metode B-valg, vilkårsvurdering etter rskl § 5-6, Skattefunn holdt utenfor scope, aktivering-oversikt SuRE 2024/2025, bruttoføring bekreftes, reversering av avskrivninger 2024/2025 med detaljert per-rad-tabell inkludert AVSKRIV_2024_TOTAL-estimatet (~7,66 MNOK), avskrivningsstart etter faktisk bruksdato (ikke bundet til 2027), balanseeffekt/utsatt skatt/resultatpåvirkning, nedskrivingstest integrert med alle syv indikatorer, oppsummering med seks bekreftelses-punkter til revisor. Ingen kryssreferanser til andre prosjektfiler — står på egne ben.

2. `2026-07-14_mail_regnskapsforer_revisorpakke.md` (459 ord) — kort mail til Orkla Regnskap AS med de fem eksplisitte spørsmål/bekreftelses-punkter: eksakt 2024-avskrivning, SuRE-tilskudd og dobbeltbokføring på kto 2160, koblet reversering av "reduksjon avskrivning" på kto 2160, Skattefunn utenfor prinsippendringen, og bekreftelse på at 2024-raden på kto 1005 håndteres generisk uten oppdeling.

Plassholdere som gjenstår i revisorpakken:
- AVSKRIV_2024_TOTAL — eksakt fra regnskapsfører (estimat ~7 655 071 kr basert på lineær 5-års avskrivning per rad, med spesifikk bekreftelse etterspurt i mail pkt 1).
- Signatur (Navn, Rolle, E-post, Telefon) — settes inn før leveranse.

**Files touched:** 2 nye filer i `funding/` (opprinnelig `leveranser/`, flyttet i T96).

---

### T82 `[x]` [FUND] Oppdater revisorpakken basert på regnskapsførers svar i mail 2

Etter møte med regnskapsfører (Orkla Regnskap AS) om revisorpakken `funding/2026-07-14_revisorpakke_prinsippendring_aktivering_nedskrivingstest.md` har regnskapsfører sendt et oppfølgingssvar med bekreftelser, korreksjoner og nye elementer. Oppdatert avstemming er også levert. Pakken må oppdateres før den sendes til revisor.

Denne task-beskrivelsen er selvstendig — alle beslutninger, tall og struktur som trengs for å utføre arbeidet er inkludert her. Overlever compact og clear.

**Deliverable:** Oppdatert versjon av `funding/2026-07-14_revisorpakke_prinsippendring_aktivering_nedskrivingstest.md`. Sannsynligvis best å skrive en ny fil med dato 2026-07-15 og slette den gamle, evt. overskrive og oppdatere dato-metadata. Diskuter med bruker om filnavn/dato før implementering. Struktur beholdes i hovedsak, men innhold i flere seksjoner endres vesentlig.

**Kilder som må leses før implementering:**

- `funding/2026-07-14_revisorpakke_prinsippendring_aktivering_nedskrivingstest.md` — den nåværende pakken som skal oppdateres
- `funding/aktivering_regnskapsforer_mail2.md` — regnskapsførers svar på oppfølgingsspørsmål
- `funding/1005 forskning og utvikling - oppdatert.md` — oppdatert avstemming av kto 1005 fra regnskapsfører
- `funding/2160 SUNLIT SEA AS_opptjente tilskudd - oppdatert avstemming.md` — oppdatert avstemming av kto 2160 fra regnskapsfører (med korreksjonspesifikasjoner)
- `funding/Bilag-383-2025.md` — forklaring på 2021 pressverktøy-omklassifisering
- `funding/aktivering_regnskapsforer_mail.md` — første mail-tråd (kontekst)
- `funding/aktivering_reklassifisering.md` — Eiriks opprinnelige reklassifiseringsnotat (kontekst)

**Bekreftelser fra regnskapsfører (skal reflekteres i oppdatert pakke):**

- AVSKRIV_2024_TOTAL på kto 1005 bekreftet: 7 655 071 kr — mitt estimat traff, plassholder fjernes.
- Ny saldo på kto 1005 etter alle endringer: 21 701 638 kr.
- Kto 2160 startsaldo korrigert: -5 146 838 kr (ikke -5 602 142 som lå i tidligere uttrekk — feilen skyldtes at kto 2160-avstemmingen ikke var oppdatert med korreksjoner/tilbakeføringer på 758 904 kr som ble ført i 2025).
- Kto 2160 avskrivninger 2024: 6 449 816 kr (tilbakeføres mot ny kto 7794).
- Kto 2160 avskrivninger 2025: 6 449 816 kr (slettes direkte).
- Ny saldo kto 2160 etter reversering av begge årenes avskrivninger: -18 046 472 kr.
- Netto resultateffekt av alle korreksjonene: 3 153 432 kr (2024-del: 2 223 073, 2025-del: 930 359).
- Foreløpig årsresultat 2025 etter korreksjonene: underskudd 3 282 483 kr.
- Egenkapital etter korreksjonene: positiv 1 454 838 kr.
- Utsatt skattefordel er IKKE bokført — ingen skattekostnad-effekt bokføres. Merknad skal reflektere dette.

**Nye elementer som må inn:**

1. **Konto 7794 "Korreksjoner tidligere år"** — ny konto som 2024-korreksjonene resultatføres mot. Vises som egen linje i resultatregnskapet, spesifiseres i note. 2025-korreksjonene skjer ved at posteringer i 2025 slettes/korrigerer konto direkte (ikke via kto 7794).
2. **Konto 1205 Pressverktøy** — pressverktøyet ble skilt ut fra aktivert utvikling (kto 1005) i 2024-korreksjonene og overført til kto 1205 med bokført verdi 4 225 837,35 kr. Kilde: Bilag-383-2025. Dette forklarer også hvorfor "korrigert avskrivning 2025" på kto 1005 avviker fra ren lineær 5-års avskrivning for 2021 og 2022 Surewave — grunnlaget for aktivering (og dermed avskrivning) ble redusert etter omklassifiseringen.

**Vesentlige feil i nåværende pakke som må rettes:**

1. Kto 2160-startsaldo (-5 602 142 kr) må rettes til -5 146 838 kr.
2. Balanseeffekt-seksjonen (pkt 10) må gjøres om fullstendig. Jeg hadde IKKE tatt hensyn til at reversering av avskrivningene også reverserer tilskudds-periodiseringen på kto 2160 (kredit-side). Dette reduserer netto resultatpåvirkning fra mitt estimat på 12,5 MNOK ned til regnskapsførers 3,15 MNOK. Nye tall:
   - Kto 1005 bruttoøkning: +16 053 053 kr
   - Kto 2160 reversering av tilskudds-inntektsføring 2024 og 2025: -12 899 632 kr (2 × 6 449 816)
   - Netto resultateffekt: +3 153 432 kr
3. Utsatt skatt-estimat (~3,53 MNOK) må fjernes eller reformuleres som informasjons-punkt om at effekten ikke er inkludert.
4. Metode-seksjonen må presiseres: 2024 mot kto 7794, 2025 direkte-korreksjon.

**Konkrete seksjonsvise oppdateringer:**

**Seksjon 1 (Innledning og formål):** Utvid til å nevne kto 7794 og kto 1205 som del av det revisor skal ta stilling til. Behold hovedstrukturen med tre disposisjoner (prinsippendring + avskrivningsreversering + nedskrivingstest).

**Seksjon 2 (Foretaks- og standardgrunnlag):** Uendret.

**Seksjon 3 (Prinsippendring):** Presiser metode-avsnittet (3.2) — 2024-korreksjoner via kto 7794, 2025-korreksjoner via direkte-korrigering av posteringer.

**Seksjon 4 (Vilkårsvurdering):** Uendret.

**Seksjon 5 (Skattefunn utenfor scope):** Uendret.

**Seksjon 6 (Aktivering-oversikt SuRE):** Uendret. SuRE 2024: 1 017 809 kr, SuRE 2025: 817 942 kr.

**Seksjon 7 (Bruttoføring):** Utvide til å presisere at reversering av avskrivningene på kto 1005 også reverserer tilhørende periodisering av utsatt inntekt på kto 2160 (koblet effekt). Refererer til seksjon 8 og 10 for tallene.

**Seksjon 8 (Reversering av avskrivninger):** Oppdater kto 1005-tabellen med den fullstendige nye avstemmingen fra `1005 forskning og utvikling - oppdatert.md` — inkluder "justert avskrivning etter omklass 2024"-kolonnen. Ny forklaring på hvorfor 2021 og 2022 Surewave-avskrivningene har avvikende satser (pressverktøy-omklassifiseringen fra Bilag-383-2025). Detaljert 2024-avskrivnings-tabell fjernes (var estimat, nå bekreftet) eller erstattes med sitatert eksakt tall 7 655 071. Legg til ny undertabell for kto 2160-siden med tall fra `2160 SUNLIT SEA AS_opptjente tilskudd - oppdatert avstemming.md`, som viser at kto 2160-avskrivning 2024 og 2025 begge er 6 449 816 kr og skal reverseres tilsvarende.

**Seksjon 9 (Avskrivningsstart):** Uendret.

**Seksjon 10 (Balanseeffekt) — GJØRES OM FULLSTENDIG:**

Ny struktur:

Underseksjon 10.1 Konto 1005 Aktivert utvikling:
- Startsaldo 5 648 573 kr
- + SuRE 2024 aktivering: 1 017 809 kr
- + SuRE 2025 aktivering: 817 942 kr
- + Reversering 2025-avskrivninger: 6 562 231 kr
- + Reversering 2024-avskrivninger: 7 655 071 kr (bekreftet, ikke estimat)
- Ny saldo kto 1005: 21 701 638 kr (regnskapsførers tall — merk 12 kr rundingsavvik mot summering)

Underseksjon 10.2 Konto 2160 Opptjente tilskudd:
- Startsaldo (korrigert): -5 146 838 kr
- + Reversering av 2024 avskrivning på kto 2160: -6 449 816 kr (mot kto 7794)
- + Reversering av 2025 avskrivning på kto 2160: -6 449 816 kr (direkte-korrigering)
- Ny saldo kto 2160: -18 046 472 kr

Underseksjon 10.3 Konto 1205 Pressverktøy:
- Skilt ut fra kto 1005 i 2024-korreksjoner
- Bokført verdi 4 225 837,35 kr
- Informasjons-punkt (ikke del av prinsippendringens resultateffekt)

Underseksjon 10.4 Netto resultateffekt:
- 2024-korreksjoner mot kto 7794 (ny linje i resultatregnskapet): 2 223 073 kr
- 2025-korreksjoner (direkte i 2025): 930 359 kr
- Sum resultatøkning: 3 153 432 kr
- Foreløpig årsresultat 2025 etter korreksjoner: underskudd 3 282 483 kr
- Egenkapital etter korreksjoner: positiv 1 454 838 kr

Underseksjon 10.5 Utsatt skatt:
- Aktivering av utvikling utgjør en midlertidig forskjell mellom regnskapsmessig og skattemessig verdi
- Utsatt skattefordel er foreløpig ikke bokført
- Ingen skattekostnad-effekt reflekteres i tallene ovenfor
- Merknad om at dette kan vurderes separat

**Seksjon 11 (Nedskrivingstest):** Uendret argumentasjon og struktur. Balanseført-verdi-referanse i pkt 11.5 justeres til nøyaktig 21 701 638 kr (fra "ca 21,7 MNOK").

**Seksjon 12 (Oppsummering):** Oppdater med:
- Netto resultat- og egenkapital-tall (3 153 432 og 1 454 838 positiv)
- Presisering av at revisor bes bekrefte: (a) prinsippendringen, (b) kto 7794-behandlingen av 2024-korreksjoner, (c) direkte-korreksjonen av 2025-posteringer, (d) bokføringen av kto 1205 pressverktøy, (e) at utsatt skatt kan vurderes separat.

**Struktur for kto 1005-tabellen i seksjon 8 (basert på oppdatert avstemming):**

Faithful gjengivelse av kto 1005-avstemmingen fra `1005 forskning og utvikling - oppdatert.md`:
- 4 hovedrader (2021, Surewave 2022, Surewave 2023, Surewave 2024) med kolonner for aktivert beløp, årlige avskrivninger 2021-2024, rest 31.12.24, justert avskrivning etter omklass 2024, korrigert avskrivning 25, rest 31.12.25
- Sum-rad
- Etterfølgende korreksjons-poster: foreløpig pr 31.12.24, for mye avskrevet bokført, omklassifisert pressverktøy, saldo 31.12.24
- Sammenlignings-post: Anleggskartotek 13 421 313, Diff 2024 -1 210 493
- Pr 31.12.25-linje: 0 rest, 6 562 231 korrigert avskrivning, 5 648 573,20 rest

**Struktur for kto 2160-tabellen i seksjon 8 (basert på oppdatert avstemming):**

Faithful gjengivelse av kto 2160-avstemmingen fra `2160 SUNLIT SEA AS_opptjente tilskudd - oppdatert avstemming.md`:
- 4 uopptjent-inntekt-rader (2021, 2022, 2023, 2024) med grunnlag, årlige avskrivninger 2021-2024, rest 31.12.24, avskrivning 2025, rest 31.12.25
- Sum-rad: -32 249 083 grunnlag, avskr 2025 = 6 449 816, rest = -5 905 742
- Korreksjoner 2025: 758 904
- Uopptjent 21 ferdig avskrevet: 13 656 462
- Rest uopptjent inntekt pr 31.12.25: -17 833 717 grunnlag, -5 146 838 rest (dette er den korrekte startsaldoen)
- Saldo etter reversering av avskrivbninger 2024 og 2025: -18 046 472

**Krav ved gjennomføring:**

- Dokumentet må fortsatt stå på egne ben — ingen kryssreferanser til andre prosjektfiler.
- Ingen bold i brødtekst — bold kun i seksjons-overskrifter.
- Norsk finans-/regnskaps-terminologi (unngå anglisismer).
- Currency-notasjon: valuta etter tall (feks "5 648 573 kr", ikke "kr 5 648 573").
- Markdown-lister skal rendres korrekt — bruk `-`/`1.` for enumereringer, hard line breaks for signatur/adresseblokker.
- ETT dokument — Bilag-383-2025-forklaringen på pressverktøy-omklassifiseringen integreres inline i seksjon 8 (kort, ikke hele bilaget).
- Behold Metode B (resultatføring i endringsåret) som valgt metode.
- Behold vurderingsenhet, indikatorvurdering og konklusjon "ingen nedskrivning" i seksjon 11 uendret.

**Beslutninger tatt før implementering:**

- **Utsatt skatt:** Ikke balanseføres. Sunlit Sea har vesentlig fremførbart skattemessig underskudd som utligner den midlertidige forskjellen fra aktivering; netto skatteposisjon er en utsatt skattefordel. Etter NRS 8 pkt. 6.1.1.2 kan små foretak unnlate å balanseføre netto utsatt skattefordel — selskapet gjør bruk av denne adgangen. Dokumenteres i pkt 10.5 med begrunnelse. Fordi gen 2 ikke er tatt i bruk enda, vil den midlertidige forskjellen fra aktivering først reversere når avskrivning påbegynnes — posisjonen er inntil videre hvilende.
- **Notetekst for kto 7794:** Utformes av utfører (Claude) basert på standard notepraksis for korreksjoner tidligere år + de konkrete tallene fra regnskapsfører.
- **Bilag-383-2025:** Refereres kun kort (pressverktøy overført til kto 1205 med bokført verdi 4 225 837 kr i 2024, årsak til justert avskrivningsgrunnlag på 2021 og 2022 Surewave). Ikke inline detaljert regneteknisk gjennomgang.
- **Filnavn/dato:** Overskriv eksisterende `2026-07-14_revisorpakke_prinsippendring_aktivering_nedskrivingstest.md` (samme filnavn beholdes for kontinuitet). Oppdater `utarbeidet`-feltet i YAML-frontmatter til 2026-07-15.

**Åpne punkter som gjenstår før leveranse:**

- Signatur (Navn, Rolle, E-post, Telefon) — settes inn før pakken sendes til revisor.

**Solution (2026-07-15):**

Oppdatert versjon av `funding/2026-07-14_revisorpakke_prinsippendring_aktivering_nedskrivingstest.md` skrevet (samme filnavn beholdt, YAML `utarbeidet` satt til 2026-07-15). 13 seksjoner. Alle bekreftede tall fra regnskapsførers mail 2 lagt inn:

- Kto 1005 ny saldo: 21 701 638 kr (basert på fullstendig avstemming inkl. justert avskrivning etter omklass 2024)
- Kto 2160 ny saldo: -18 046 472 kr (korrigert startsaldo -5 146 838 kr, reversering 2 × 6 449 816 kr)
- Kto 1205 pressverktøy: 4 225 837 kr (informasjons-punkt, ikke berørt av prinsippendringen)
- Netto resultateffekt: 3 153 432 kr (2024-del 2 223 073 kr mot kto 7794, 2025-del 930 359 kr direkte)
- Foreløpig årsresultat 2025: underskudd 3 282 483 kr
- Egenkapital etter korreksjoner: positiv 1 454 838 kr

Endringer i seksjonsvis oppdatering:

- Seksjon 1: utvidet til å inkludere kto 7794 og kto 1205
- Seksjon 3.2: metode presisert (2024 via kto 7794, 2025 via direkte-korreksjon)
- Seksjon 7: koblet effekt mellom kto 1005-avskrivning og kto 2160-periodisering presisert
- Seksjon 8: full 1005- og 2160-tabell inkludert med fullstendig avstemming, forklaring på avvikende avskrivningssatser for 2021/2022 Surewave (pressverktøy-omklassifiseringen)
- Ny seksjon 9: kort referanse til kto 1205 (Bilag-383-2025 refereres, ikke gjentatt i detalj)
- Seksjon 10: gjort om fullstendig med 5 underseksjoner (10.1 kto 1005, 10.2 kto 2160, 10.3 kto 1205, 10.4 netto resultat, 10.5 utsatt skatt)
- Seksjon 10.5 utsatt skatt: begrunnelse med NRS 8 pkt 6.1.1.2 for små foretaks adgang til ikke å balanseføre utsatt skattefordel; henvisning til fremførbart underskudd og hvilende posisjon inntil gen 2 tas i bruk
- Seksjon 11.5: nedskrivingstest-referanse justert fra "ca 21,7 MNOK" til nøyaktig 21 701 638 kr
- Seksjon 12: fire foreslåtte noter (regnskapsprinsipp, kto 7794 med spesifikasjon av tre komponenter, avskrivninger av aktiverte utviklingsverdier, utsatt skatt)
- Seksjon 13 (tidligere 12): oppdatert oppsummering med 9 bekreftelses-punkter

Signaturblokk lagt inn som plassholder (`[Navn]` / `[Rolle]` / `[E-post]` / `[Telefon]`) med to trailing spaces for hard line breaks — settes inn før utsendelse.

Ingen kryssreferanser til andre prosjektfiler. Ingen bold i brødtekst. Norsk finansterminologi. Valuta etter tall.

**Files touched:** `funding/2026-07-14_revisorpakke_prinsippendring_aktivering_nedskrivingstest.md` (overskrevet).

**Neste steg (Eiriks side, utenfor T82):** Gjennomgå oppdatert pakke, sette inn signatur, sende til revisor.

---

### T83 `[x]` [FUND] Bygg inn teknologiplattform-narrativ (gen 1 / gen 2 / SuRE / Surewave) i revisorpakken

Nåværende revisorpakke `funding/2026-07-14_revisorpakke_prinsippendring_aktivering_nedskrivingstest.md` rammer prinsippendringen som et SuRE-fenomen i innledningen, mens de faktiske balanseeffektene rammer også Surewave-aktiveringene (2022, 2023, 2024) og 2021-basisen. Leseren forstår først i seksjon 8 at reversering av avskrivninger skal gjøres for hele restbeholdningen på kto 1005 — ikke bare SuRE-relatert. Rekkefølgen gjør at Surewave dukker opp som en bisetning i seksjon 4 og deretter som overraskelse i seksjon 8 uten forutgående forklaring. Sammenhengen mellom gen 1, gen 2, og de to Horizon-prosjektene er heller ikke etablert.

**Deliverable:** Ny versjon av `funding/2026-07-14_revisorpakke_prinsippendring_aktivering_nedskrivingstest.md` med teknologiplattform-narrativet integrert. Struktur beholdes i hovedsak; ny seksjon 3 legges inn og relevante seksjoner justeres. TRL-figuren `figures/2026-07-15_trl_utvikling_gen1_gen2.svg` bygges inn.

**Konkrete endringer:**

1. **Ny seksjon 3 «Foretakets teknologiplattform og EU-prosjekter»** (nåværende seksjon 3-13 skyves til 4-14):
   - 3.1 Gen 1 (i drift, TRL 7, Skiftestjørna-anlegget som referanse) og gen 2 (under utvikling, TRL 5-6, planlagt lansering 2027, prototypeserie P3 → P4 → P5)
   - 3.2 Horizon Europe-prosjektene SuRE og Surewave — kort om hva de er, tidsrom, konsortium-partnere (IFE for SuRE, SINTEF for Surewave), leveranser inn til gen 2-plattformen
   - 3.3 Sammenhengen mellom balanseførte utviklingsverdier på kto 1005 (2021-basis, Surewave-aktiveringer for 2022, 2023 og 2024, SuRE-aktiveringer for 2024 og 2025) og gen 2-utviklingsplattformen — etablerer at hele restbeholdningen tilhører samme utvikling og at ingen av den er tatt i bruk
   - TRL-figuren `figures/2026-07-15_trl_utvikling_gen1_gen2.svg` plasseres her med caption

2. **Seksjon 1 (Innledning og formål) omformuleres:**
   - Punkt 1 favner utviklingskostnader for foretakets samlede teknologiplattform (både SuRE og Surewave), ikke bare SuRE
   - Punkt 2 forankres i at hele plattformen er under utvikling og ikke tatt i bruk — dermed avskrivningsstopp for all restbeholdning på kto 1005

3. **Seksjon 4.1 (nå 3.1 om bakgrunn):** SuRE brukes som konkret eksempel, resonnementet gjelder plattformen samlet — inkludert Surewave-restbeholdningen.

4. **Seksjon 8 (reversering av avskrivninger):** Innledende avsnitt refererer tilbake til teknologiplattformen etablert i seksjon 3.3 — ikke ny introduksjon av Surewave.

5. **Seksjon 11.5 (bruksverdi-vurdering):** Kan dra nytte av teknologiplattform-seksjonen for å styrke argumentet for at balanseført verdi er dekket av fremtidig bruksverdi.

**Krav ved gjennomføring:**

- Alle tall og konklusjoner fra nåværende pakke beholdes uendret (kto 1005 ny saldo 21 701 638 kr, kto 2160 ny saldo -18 046 472 kr, netto resultatøkning 3 153 432 kr, etc.).
- Dokumentet må fortsatt stå på egne ben — ingen kryssreferanser til andre prosjektfiler.
- Ingen bold i brødtekst — bold kun i seksjons-overskrifter.
- Norsk finans-/regnskaps-terminologi (unngå anglisismer).
- Valuta etter tall (`21 701 638 kr`, ikke `kr 21 701 638`).
- Markdown-lister rendres korrekt — bruk `-`/`1.` for enumereringer.
- TRL-figuren refereres med relativ Markdown-syntaks `![caption](../figures/2026-07-15_trl_utvikling_gen1_gen2.svg)` — men merk at Pandoc ikke embedder SVG i docx direkte. Hvis docx-produksjon senere blir bestilt, må figuren konverteres til PNG først (utenfor scope for denne task).
- YAML `utarbeidet`-feltet oppdateres til dato for gjennomføring.

**Kildekrav — skjerpet:**

Innholdet i den nye seksjon 3 (og alle justeringer som følger av den) må baseres på primærkilder, ikke andrehåndskunnskap eller conversation-sammendrag. Utfører må lese kildene faktisk før skriving — ikke gjenbruke tidligere formuleringer uten verifisering. Regel jf. memory `feedback_recheck_background_before_writing`.

For hvert konkret faktum som havner i seksjon 3 må utfører kunne peke på hvilken kilde det kom fra. Faktapåstander uten kildegrunnlag markeres eksplisitt for Eirik («ikke bekreftet i kilde X — verifiser»), i stedet for å gjettes eller utelates.

**Kilder som må leses før implementering:**

Repo-interne:

- `funding/2026-07-14_revisorpakke_prinsippendring_aktivering_nedskrivingstest.md` — nåværende pakke som skal oppdateres
- `figures/2026-07-15_trl_utvikling_gen1_gen2.svg` — TRL-figur som skal integreres
- `sure/report.md` — særlig kap. 1 (introduksjon + gen 1 → gen 2), kap. 2 (gen 2-arkitektur), kap. 3 (prototyping / mould-workflow), kap. 5 (materialer / miljøeksponering). Rapporten er hovedkilden for teknisk beskrivelse av både gen 1 og gen 2.
- `gen2/norsmaterials_brief.md` — kompakt gen 1 vs gen 2-sammenligning, prototypeserie P3 → P4 → P5, PU-rolle, målestatus
- `background/loeypemelding/*.md` — grep for «Surewave», «SuRE», «gen 1», «Skiftestjørna», «Enova», «Skattefunn», «Innovasjon Norge». Historiske investoroppdateringer inneholder tidsrom, milepæler, partnerkonstellasjoner og motivasjonen bak hvert utviklingssteg.
- `funding/`-filer (aktivering-notater, regnskapsuttrekk) — for å finne hvilke støtteprosjekter 2021-basisen på kto 1005 (18 570 858 kr) faktisk stammer fra

Ekstern (nabo-prosjekt, eksplisitt lest med Eiriks tillatelse):

- `../stotte/data/sunlit_sea/project_cards.json` — presise tidsrom, konsortium-strukturer og arbeidspakke-oppdeling for fire støtteprosjekter (SUREWAVE, SURE, Enova 1, SkatteFUNN). Bruk prosjektnavn, `DurationFrom`/`DurationTo`, `ConsortiumPartners` og `workpackages`-oversikten for å gi et rikere bilde av utviklingsløpet. **Ikke bruk budsjett-tall** derfra — alle regnskapstall skal komme fra denne øktas datagrunnlag (regnskapsførers avstemminger). Stotte-JSON er kun for kontekst-berikelse av selve prosjekt-beskrivelsene.

**Presiseringer basert på stotte-data (som utfører kan bruke direkte):**

- Surewave (SUREWAVE i stotte): Horizon Europe grant 101083342 (HORIZON-CL5-2021-D3-03), varighet 2022-09-01 til 2026-12-31, Sunlit Sea er partner 2 av 7 i konsortium ledet av SINTEF. Sunlit Sea leder WP2 «Global framework & specifications» og WP8 «Dissemination, communication & exploitation». Sunlit Sea bidrar i WP1 (SINTEF), WP6 «Technical validation» (SINTEF) og WP7 «Integrated sustainability assessment» (IFEU). Øvrige konsortium-partnere: Ceit, MARIN, ACCIONA, Clement Germany, IFEU.
- SuRE: Horizon Europe, varighet 2024-10-01 til 2027-08-31, Sunlit Sea er partner i konsortium ledet av IFE (WP3 og WP8). Sunlit Sea leder WP6 «Sunlit's integrated FPV technology» (hoved-arbeidspakken for Sunlit Sea, 27 PM). Øvrige partnere: Fraunhofer, TNO, CT1, ZIM, Compaz.
- Enova 1 «Flytende Solkraft for Norske Forhold»: varighet 2023-07-01 til 2025-07-01, Sunlit Sea som lead recipient i konsortium med EV PowerCharge AS og Endra AS. Grant reference 23/12577.
- SkatteFUNN «Robusthet i flytende solkraft»: varighet 2023-01-01 til 2026-12-31, prosjektnummer 350626.

**Åpne kildespørsmål før seksjon 3 kan skrives ferdig:**

- 2021-basisen på kto 1005 (18 570 858 kr): hvilket eller hvilke støtteprosjekter denne aktiveringen stammer fra er ikke tydelig fra stotte-data (som starter 2022). Må sjekkes mot `background/`-materialet, regnskapsførers avstemmingsnotater og eventuelt eldre løypemeldinger. Kandidater å undersøke: eldre Enova-tilskudd, IN-tilskudd, Skattefunn-perioder før 2023, EU EIT-tilskudd. Uten kildegrunnlag skal seksjon 3.3 ikke gjette — bruk formuleringen «2021-basis knyttet til foretakets tidligere utviklingsarbeid; sammensetning per støtteprosjekt er dokumentert i regnskapsførers avstemminger» eller lignende inntil kilde foreligger.
- Skiftestjørna-anlegget (105 kWp, PPA med EV PowerCharge, «produksjon over forventning»): faktapunkter må verifiseres mot løypemeldingene 2024-10-01 og 2025-10-07, ikke fra sammendraget.
- TRL-nivåer for gen 1 og gen 2: må verifiseres mot D6.1 eller løypemelding, ikke bare fra figuren.

**Solution (2026-07-16):**

Oppdatert `funding/2026-07-14_revisorpakke_prinsippendring_aktivering_nedskrivingstest.md` med ny teknologiplattform-narrativ. YAML `utarbeidet` oppdatert til 2026-07-16. Alle tall og konklusjoner beholdt uendret.

Endringer i seksjonsstruktur:

- Seksjon 1 (Innledning) omformulert: punktene favner nå hele utviklingsplattformen (SuRE og Surewave) og gjør eksplisitt at reverseringen av avskrivninger gjelder samtlige aktiveringer, herunder 2021-basisen og Surewave-aktiveringene
- Ny seksjon 3 «Foretakets teknologiplattform og EU-prosjekter» lagt inn med tre underseksjoner: 3.1 gen 1 og gen 2 (inkludert Skiftestjørna og TRL-figuren), 3.2 Horizon Europe-prosjektene SuRE og Surewave (varigheter, konsortium-partnere, arbeidspakker, hva som mater inn i gen 2), 3.3 sammenhengen mellom balanseførte utviklingsverdier på kto 1005 og gen 2-plattformen
- TRL-figuren integrert som Figur 1 i seksjon 3.1: `![Figur 1. ...](../figures/2026-07-15_trl_utvikling_gen1_gen2.svg)`
- Alle etterfølgende seksjoner (3-13) skyvet én posisjon opp til 4-14
- Alle interne kryssreferanser oppdatert til nye seksjonsnumre (verifisert med grep)
- Seksjon 9 (Reversering av avskrivninger) refererer nå til seksjon 3.3 istedenfor å introdusere Surewave som ny informasjon
- Seksjon 12.5 (bruksverdi-vurdering) uendret innhold — henvisning til seksjon 3.1 for Skiftestjørna-driftsdokumentasjon
- Seksjon 14 (oppsummering) presiserer at reverseringen av avskrivninger gjelder samtlige aktiveringer

Kildebruk (per skjerpet kildekrav):

- Gen 1 teknisk beskrivelse: `sure/report.md` kap 1 (Fig 1-1 og 1-2), `gen2/norsmaterials_brief.md` gen 1 vs gen 2-tabell
- Gen 2 arkitektur og prototypeserie: `sure/report.md` kap 2, `gen2/norsmaterials_brief.md`, `background/loeypemelding/2025-11-17_loeypemelding.md` (TRL 5-6)
- Skiftestjørna-anlegget: `background/loeypemelding/2024-10-01_loeypemelding.md` (105 kWp, install 10. oktober, first develop-operate-sell, PPA med EV PowerCharge) og `background/loeypemelding/2025-10-07_loeypemelding.md` («produksjon over forventning»)
- Gen 1-avvikling: `background/loeypemelding/2025-10-07_loeypemelding.md` (styret besluttet avvikling)
- Surewave: `../stotte/data/sunlit_sea/project_cards.json` (grant, varighet, konsortium, WPer), `background/loeypemelding/2026-07-08_loeypemelding.md` (12-måneders forlengelse pga ACCIONA), `background/loeypemelding/2024-04-28_loeypemelding.md` (Clement Systems breakwater-samarbeid)
- SuRE: `../stotte/data/sunlit_sea/project_cards.json` (varighet, konsortium, WPer), `sure/report.md` kap 1 (WP6-objektiver O6.1.1 og O6.2.1, D6.1 vs D6.2)
- 2021-basis komposisjon: `background/loeypemelding/2021-06-23_loeypemelding.md` (IN miljøteknologistøtte 8.4 MNOK juni 2021, matching investors Holta Invest AS); detaljert sammensetning per støtteprogram henvist til regnskapsførers avstemminger og bilagsdokumentasjon (ikke gjettet)

Ingen faktapunkter i seksjon 3 uten kildegrunnlag. Alle konkrete beløp fra regnskapsførers avstemminger. Ingen bold i brødtekst. Norsk finansterminologi. Valuta etter tall. Ingen kryssreferanser til andre prosjektfiler.

**Files touched:** `funding/2026-07-14_revisorpakke_prinsippendring_aktivering_nedskrivingstest.md` (oppdatert).

**Neste steg (Eiriks side, utenfor T83):** Gjennomgå oppdatert pakke, verifisere at 2021-basis-omtalen (18 570 858 kr fra tidligere IN miljøteknologistøtte og øvrige tidligere støtteprogrammer) er tilstrekkelig for revisor eller om Eirik ønsker mer detaljert støtteprogram-oppdeling — kilde ligger i regnskapsførers avstemmingsnotater. TRL-figuren refereres som `.svg`; hvis docx-produksjon bestilles må figuren konverteres til PNG først (Pandoc embedder ikke SVG i docx direkte).

---

### T84 `[x]` [FUND] PDF-layoutfiks i revisorpakken — NBSP i tall og mindre tabellfont

Ved konvertering av `funding/2026-07-14_revisorpakke_prinsippendring_aktivering_nedskrivingstest.md` til PDF via pandoc + xelatex brytes lange tall som `18 570 858` på tvers av linjer i trange tabellkolonner, fordi vanlig mellomrom (U+0020) er et gyldig brytepunkt for LaTeX. I tillegg er de brede tabellene (særlig kto 1005-avstemmingen i seksjon 9.2 med 12 kolonner) trange på A4-portrett.

**Deliverable:** To endringer i revisorpakken:

1. Alle tallgrupper med tusen-skille-mellomrom bindes med NBSP (U+00A0). Fikser rot-årsaken til `18\n570 858`-brudd. Gir samme visuelle mellomrom i PDF, DOCX og alle Markdown-previews — bare uten linjebrytings-mulighet.
2. YAML `header-includes` utvidet med LaTeX-preamble som setter `\small` for alle tabeller globalt. Krymper tabellfonten fra 10pt til ~9pt for bedre plass i brede tabeller.

**Nytt persistent skript i `scripts/`:**

- `scripts/nbsp_numbers.py` — regex-basert NBSP-substitusjon. Regex `(\d) (\d{3})(?=\D|$)` binder alle 3-sifrede grupper med et sifret prefix. Idempotent (kan kjøres flere ganger uten endring). Dry-run som standardmodus (per `feedback_no_inplace_batch_without_backup` og T73-hendelsen): skriver til `<file>.cleaned.md`-sibling og printer word/line/char delta + antall NBSP-substitusjoner + eksempler på endrede linjer. `--promote` flag for overskriving etter menneskelig godkjenning. Dokumenteres i `README.md` seksjon `## Scripts`.

**YAML header-includes-endring (rett i revisorpakken):**

```yaml
header-includes:
  - \usepackage{etoolbox}
  - \AtBeginEnvironment{longtable}{\small}
  - \AtBeginEnvironment{tabular}{\small}
```

Bare aktivt ved LaTeX-basert PDF-produksjon; ingen effekt på DOCX. `etoolbox`s `\AtBeginEnvironment` er ren og gjenbrukbar for framtidige tabellstørrelsesendringer.

**Krav ved gjennomføring:**

- Skript-konvensjonen: dry-run standardmodus, `--promote` for overskriving. Ordtelling identisk før og etter (siden vi kun bytter tegn, ikke fjerner eller legger til). Karaktertelling identisk. Linjetelling identisk. NBSP-antall vises som separat metrikk.
- Ikke omgå dry-run selv om brukeren har sagt «gjør trinn 1 og 2» — pattern eksisterer for å unngå silent regex-katastrofer (jf. T73).
- Ingen andre endringer i revisorpakken.
- `README.md` scripts-seksjon oppdatert med `nbsp_numbers.py`-beskrivelse.

**Ikke i scope for T84:**

- Variable kolonnebredder for de brede tabellene (trinn 3 fra betraktningen — avvent til vi ser om trinn 1+2 er nok).
- Landskap-orientering på seksjon 9-tabellene.
- Konvertering av selve dokumentet til PDF/DOCX (brukeren håndterer det).

**Solution (2026-07-16):**

Trinn 1 (NBSP i tall) og trinn 2 (mindre tabellfont) gjennomført.

Nytt skript: `scripts/nbsp_numbers.py`. Regex `(\d) (\d{3})(?=\D|$)` (multiline) med idempotent loop. Dry-run som standard skriver `<file>.cleaned.md`-sibling og printer stats. `--promote` for overskriving.

Dry-run-resultat mot revisorpakken:
- Ord: 5822 → 5822 (delta 0)
- Linjer: 429 → 429 (delta 0)
- Tegn: 42639 → 42639 (delta 0)
- NBSP-substitusjoner: 272

Etter Eiriks bekreftelse ble skriptet kjørt med `--promote` og sibling-fila slettet.

Trinn 2 lagt inn i YAML-frontmatter:

```yaml
header-includes:
  - \usepackage{etoolbox}
  - \AtBeginEnvironment{longtable}{\small}
  - \AtBeginEnvironment{tabular}{\small}
```

Kun aktivt ved LaTeX-basert PDF-produksjon. Ingen effekt på DOCX.

`README.md` `## Scripts`-seksjonen oppdatert med `nbsp_numbers.py`-beskrivelse (plassert før `clean_investor_updates.py`).

**Files touched:**
- `scripts/nbsp_numbers.py` (ny)
- `funding/2026-07-14_revisorpakke_prinsippendring_aktivering_nedskrivingstest.md` (NBSP-substitusjon + YAML header-includes)
- `README.md` (Scripts-seksjonen)

**Neste steg (Eiriks side, utenfor T84):** Kjør pandoc PDF-konvertering på nytt og verifiser at (a) tallene ikke lenger brytes over linjer, og (b) tabellfonten er merkbart mindre. Hvis brede tabeller fortsatt er trange, vurder trinn 3 (variable kolonnebredder eller landskap-orientering) i egen task.

---

### T85 `[x]` [FUND] Avrunding av alle beløp i revisorpakken til hele tusen kroner

Etter T84 var tabellene fortsatt for brede — kolonnene skrev over hverandre i PDF selv med `\tiny`-font. Iterativ font-skalering ble prøvd (`\small` → `\tiny`) uten å løse breddeutfordringen. Rot-årsaken er at tallene inneholder mange sifre og 2 desimaler (f.eks. `3 714 171,60`). Løsning: avrund alle beløp til nærmeste tusen kroner. Fjerner desimalene og krymper hvert tall med 3-4 tegn.

**Deliverable:**

1. Backup-fil `funding/2026-07-14_revisorpakke_prinsippendring_aktivering_nedskrivingstest_eksakte_belop.md` — eksakt kopi av revisorpakken før avrunding, som referanse hvis nøyaktige tall trengs senere.
2. Oppdatert `funding/2026-07-14_revisorpakke_prinsippendring_aktivering_nedskrivingstest.md`:
   - Alle beløp avrundet til nærmeste tusen kroner
   - Global unit-note under H1-tittelen som forklarer avrundingen og at eksakte tall er tilgjengelige på forespørsel
   - Tabellhoder endret fra `Beløp (kr)` til `Beløp (tusen kr)`
   - I løpende tekst er alle beløp-mentions endret fra `X kr` til `X tusen kr`
   - Tabellene i pkt. 9.2 og 9.3 fikk merknad «Alle tall i tusen kroner» under overskriften siden headerne ikke har enhetsangivelse
   - «Alle beløp uttrykkes i norske kroner» i pkt. 11 fjernet (dekket av global note)
   - «Rundingsavvik på 9 kr» og «avvik 9 kr...» notiser fjernet (obsolete på tusen-nivå — begge 2 223 064 og 2 223 073 runder til 2 223)

**Krav ved gjennomføring:**

- Alle sum-rader verifisert: hvor mulig, sum av avrundede komponenter = avrundet totalsum. Der uavhengig avrunding gir ±1 avvik dekker unit-noten opp for det.
- NBSP fortsatt aktiv på alle multi-sifret tall (kjørt `scripts/nbsp_numbers.py --promote` etter avrundingen).
- Ingen andre endringer i strukturen eller argumentasjonen.
- Backup-filen står som read-only referanse — endres ikke selv om arbeidsversjonen itereres videre.

**Solution (2026-07-16):**

Gjennomført. Backup opprettet via `cp`. Arbeidsversjonen skrevet på nytt med Write-verktøyet og alle beløp avrundet manuelt. NBSP bundet igjen med `nbsp_numbers.py --promote` (128 substitusjoner denne gangen — færre enn før pga færre siffergrupper). Character/word/line-antall identisk gjennom NBSP-binding.

Verifiserte sumrader:
- Pkt. 7: 1 018 + 818 = 1 836 ✓
- Pkt. 9.4 kto 2160 total: -5 147 + -6 450 + -6 450 = -18 047 vs justert saldo -18 046 (avvik 1 dekket av unit-note)
- Pkt. 11.1: 5 649 + 1 018 + 818 + 6 562 + 7 655 = 21 702 ✓
- Pkt. 11.4: 2 223 + 930 = 3 153 ✓
- Pkt. 11.4 2024-del: 1 018 + 7 655 - 6 450 = 2 223 ✓ (obsolete 9-kr-note fjernet)
- Pkt. 13.2 samme som 11.4: sum stemmer ✓

**Files touched:**
- `funding/2026-07-14_revisorpakke_prinsippendring_aktivering_nedskrivingstest_eksakte_belop.md` (ny, backup med eksakte tall)
- `funding/2026-07-14_revisorpakke_prinsippendring_aktivering_nedskrivingstest.md` (avrundet + unit-note + tabellhoder oppdatert + obsolete rundingsavvik-notiser fjernet)

**Neste steg (Eiriks side, utenfor T85):** Kjør pandoc PDF-konvertering på nytt. Med kortere tall i tabellene skal kolonnene passe innenfor A4-portrett-bredden. Hvis fonten nå kan økes tilbake til `\small` eller `\footnotesize` uten at kolonnene sprekker igjen, gjør det for bedre lesbarhet — bytt `\tiny` i `header-includes`.

---

### T86 `[x]` [FUND] Rett TRL-nivå for gen 2 fra TRL 5-6 til TRL 4 i revisorpakken og TRL-figuren

Under gjennomgang av revisorpakken oppdaget Eirik at TRL-nivået for gen 2 er feil angitt. Faktisk vurdering: TRL 4. Nåværende dokumentasjon sier TRL 5-6. Må rettes i revisorpakken og i TRL-figuren.

**Konsekvens for argumentasjonen:** Ingen tall, konklusjoner eller strukturelle grep påvirkes. TRL 4 styrker faktisk argumentet for at gen 2 ikke er «tatt i bruk» i regnskapsmessig forstand — og dermed også begrunnelsen for både aktiveringen og avskrivningsreverseringen. Prototypeserien P1→P5 er konsistent med TRL 4 (fortsatt prototypefase, ikke pilotering).

**Deliverable — i scope for T86:**

1. `funding/2026-07-14_revisorpakke_prinsippendring_aktivering_nedskrivingstest.md`:
   - Seksjon 3.1: «Foretaket vurderer nåværende tilstand til å være TRL 5-6» → «TRL 4»
   - Figur-bildeteksten (rett under seksjon 3.1): «er på TRL 5-6 per 2025» → «er på TRL 4 per 2025»
   - Seksjon 5 (vilkårsvurdering): «Gen 2 er nå på TRL 5-6» → «Gen 2 er nå på TRL 4»
2. `figures/2026-07-15_trl_utvikling_gen1_gen2.svg`:
   - Justere gen 2-kurven slik at den treffer TRL 4 ved 2026 (nåværende kurve passerer TRL 6 rundt 2026). Kurven fortsetter opp mot TRL 9 ved 2027 — det gir en brattere sluttfase, som er en tolkningssak (kan diskuteres om lansering fortsatt er realistisk 2027; per foreløpig plan holdes 2027).
   - Legend-teksten: «gen 2 (under utvikling, TRL 5-6, lansering estimert 2027)» → «gen 2 (under utvikling, TRL 4, lansering estimert 2027)»
3. Regenerere PNG-versjonen av figuren med ImageMagick (samme kommando som ved forrige oppdatering): `magick -density 200 /cygdrive/c/dev/src/sure-d61/figures/2026-07-15_trl_utvikling_gen1_gen2.svg /cygdrive/c/dev/src/sure-d61/figures/2026-07-15_trl_utvikling_gen1_gen2.png` — Eirik kjører selv i cygwin.

**Ikke i scope for T86 (andre steder som nevner TRL 5-6):**

- `funding/...revisorpakke..._eksakte_belop.md` — backup fra T85, skal per konvensjon stå urørt (dokumenterer tallsituasjonen på et gitt tidspunkt, ikke sannheten). TRL-feilen i backupen noteres kun her.
- `background/loeypemelding/2025-11-17_loeypemelding.md` — historisk løypemelding, ikke ment for endring i etterkant.
- `gen2/norsmaterials_brief.md` — ekstern-vendt samarbeidsdokument til Norsmaterials. Kan oppdateres separat om Eirik ønsker.
- `sure/sure_cinea_review_wp6_sunlitsea_presentation.md` og `sure/sure_dow_extract.txt` — historiske dokumenter knyttet til SuRE-rapportering.

Om Eirik vil oppdatere noen av disse fires kilder, opprett egne tasks.

**Krav ved gjennomføring:**

- Alle tre tekstforekomster i revisorpakken oppdateres.
- SVG-figuren redigeres i tekst (er en enkel håndskrevet SVG med path-koordinater — bezier-kurven må justeres nedover).
- PNG regenereres etter SVG-endring — men kjøres av Eirik selv i cygwin (jeg har ikke tilgang til å kjøre ImageMagick der).
- Ingen andre endringer i revisorpakken.

**Solution (2026-07-16):**

Revisorpakken oppdatert — TRL 5-6 → TRL 4 tre steder:

- Seksjon 3.1: «Foretaket vurderer nåværende tilstand til å være TRL 4»
- Figur-bildeteksten: «er på TRL 4 per 2025»
- Seksjon 5 (vilkårsvurdering): «Gen 2 er nå på TRL 4»

SVG-figuren oppdatert:

- Gen 2-kurven redesignet med to bezier-segmenter: TRL 2 (2024) → langsomt opp til TRL 4 (2026) → bratt opp til TRL 9 (2027). Ny path: `M 410 375 C 490 380, 560 320, 630 285 C 670 275, 700 100, 740 60`. Y-koordinat 285 tilsvarer TRL 4 (60 + 5×45 = 285 med 45 units per TRL-nivå).
- Gen 2-tekst-labelen flyttet fra (600, 215) til (555, 305) for å ligge nær den nye kurven ved TRL 4-nivået.
- Legend-tekst: «gen 2 (under utvikling, TRL 4, lansering estimert 2027)».
- SVG-kommentar oppdatert: «Gen 2 curve: start 2024 at TRL 2, slow rise to TRL 4 by 2026, steep rise to TRL 9 by end 2027».

**Files touched:**

- `funding/2026-07-14_revisorpakke_prinsippendring_aktivering_nedskrivingstest.md` (3 tekstforekomster)
- `figures/2026-07-15_trl_utvikling_gen1_gen2.svg` (path, label-posisjon, legend, kommentar)

**Neste steg (Eiriks side, utenfor T86):** Regenerere PNG med ImageMagick i cygwin: `magick -density 200 /cygdrive/c/dev/src/sure-d61/figures/2026-07-15_trl_utvikling_gen1_gen2.svg /cygdrive/c/dev/src/sure-d61/figures/2026-07-15_trl_utvikling_gen1_gen2.png`. Deretter pandoc PDF-konvertering av revisorpakken.

---

### T87 `[x]` [FUND] Oppdater løypemeldingen 2026-07-08 med prinsippendring-narrativ

Etter T82-T86: prinsippendringen for aktivering av utviklingskostnader er levert til revisor. Hvis den godkjennes, gir den positiv egenkapital ved årsslutt 2025 (~1,5 MNOK) og fjerner det tidligere skisserte umiddelbare behovet for å hente 2 MNOK i frisk kapital fra investorer.

Løypemeldingen `background/loeypemelding/2026-07-08_loeypemelding.md` reflekterer situasjonen før prinsippendringen. Må oppdateres.

**Deliverable — endringer i `background/loeypemelding/2026-07-08_loeypemelding.md`:**

1. **Intro (avsnitt 1):** Reformulere så det ikke lenger står at vi «trenger 2 MNOK i frisk kapital». Erstatt med kort omtale av at prinsippendringen — hvis revisor godkjenner — sikrer positiv egenkapital og fjerner det umiddelbare kapitalbehovet.
2. **Seksjon 2 (Gen 2), TRL-referanse:** «TRL-nivået vurderes til 5-6» → «TRL-nivået vurderes til 4» (konsistent med T86-beslutningen).
3. **Seksjon 2 (Gen 2), video-referanse:** Fjern setningen «Se vedlagt video fra P3-besøket i Kina høsten 2025.» — ingen vedlegg til denne løypemeldingen.
4. **Seksjon 2 (Gen 2), TRL-figur:** Embed TRL-figuren fra revisorpakken (`figures/2026-07-15_trl_utvikling_gen1_gen2.png`) etter TRL-omtalen som visuelt anker. Relativ path fra `background/` er `../figures/...png`.
5. **Seksjon 6 (Regnskap og kapital):** Erstatt paragrafene om kapitalbehov + emisjonsmekanikk med en beskrivelse av prinsippendring-prosessen:
   - Hva endringen består i (aktivering av SuRE-utgifter, reversering av 2024/2025-avskrivninger på hele restbeholdningen)
   - Hvorfor (gen 2 ikke tatt i bruk, kostnader er investeringer, ikke drift)
   - Netto resultateffekt ~3,15 MNOK i 2025
   - Konsekvens: positiv egenkapital ~1,5 MNOK ved årsslutt 2025, ikke behov for 2 MNOK-emisjonen
   - Forutsetning: revisor godkjenner (pakke levert, regnskapsfører står bak)
   - Contingency: emisjonsplanen står ved hvis revisor ikke godkjenner
   - Signal til investorer: dialog med langsiktige investorer er fortsatt verdifull
   - Nedskrivingstest-omtalen beholdes (kort)
6. **Seksjon 7 milepælstabell:** Fjern raden «Rettet emisjon (2 MNOK)».
7. **Avsluttende avsnitt:** Erstatt «Det kortsiktige kapitalbehovet er begrenset og løses gjennom en rettet emisjon» med noe som reflekterer prinsippendrings-løsningen.

**Ikke i scope for T87:**

- Andre løypemeldinger (ingen tilbakevirkende endringer på historiske investoroppdateringer).
- Endring av dato eller filnavn på løypemeldingen (den er datert 2026-07-08 og det står — vi bare oppdaterer innholdet).

**Krav ved gjennomføring:**

- Behold tonen og stilen fra draften (uformelt norsk, spesifikke tall, direkte).
- Ingen bold i brødtekst (jf. memory feedback_no_bold_in_body_text).
- Ingen kryssreferanser til andre prosjektfiler i selve løypemeldingen (jf. feedback_deliverable_standalone). TRL-figuren embeddes som bilde, ikke som fil-referanse i tekst.
- Løypemeldingen skal stå på egne ben — investor skal ikke trenge å slå opp i revisorpakken for å forstå prinsippendringen.

**Solution (2026-07-16):**

Alle punktene gjennomført:

1. Intro (avsnitt 1): reformulert. «trenger 2 MNOK i frisk kapital» erstattet med kort omtale av at prinsippendringen forventes å sikre positiv egenkapital og fjerne det umiddelbare kapitalbehovet (forutsatt revisors godkjenning).
2. Seksjon 2, TRL: «TRL-nivået vurderes til 5-6» → «TRL-nivået vurderes til 4».
3. Seksjon 2, video-ref: fjernet.
4. Seksjon 2, TRL-figur: embeddet som `![...](../figures/2026-07-15_trl_utvikling_gen1_gen2.png)` rett etter TRL-omtalen. Caption inneholder samme narrativ som i revisorpakken.
5. Seksjon 6 fullstendig omskrevet: tre gamle paragrafer (aktiveringer + kapitalbehov + emisjonsmekanikk) erstattet med fire nye paragrafer:
   - Faktagrunnlag: hva som var balanseført vs kostnadsført (rettet feil i draften — SuRE-utgifter var IKKE balanseført, som draften hevdet, det er hele poenget med prinsippendringen)
   - Hva prinsippendringen består i: aktivering av SuRE fra 1.1.2024 + reversering av 2024/2025-avskrivninger på hele restbeholdningen, med begrunnelse
   - Konsekvens: +3,15 MNOK resultat i 2025, positiv egenkapital ~1,5 MNOK, dekker støttekvalifisering, ingen 2 MNOK-emisjon nødvendig. Nedskrivingstest kort omtalt her.
   - Forbehold + contingency: forutsetter revisor-godkjenning, ellers faller vi tilbake på emisjonen. Investor-dialog fortsatt verdifull.
6. Milepælstabellen: «Rettet emisjon (2 MNOK)» erstattet med «Revisor-godkjenning av prinsippendring» (samme tidsrom Q3-Q4 2026, contingency-note).
7. Avsluttende avsnitt: «Det kortsiktige kapitalbehovet er begrenset og løses gjennom en rettet emisjon» erstattet med prinsippendrings-formulering.

**Files touched:** `background/loeypemelding/2026-07-08_loeypemelding.md` (7 endringer, samme fil).

**Neste steg (Eiriks side, utenfor T87):** Gjennomlese, korrigere detaljer om nødvendig. Hvis prinsippendringen godkjennes, oppdater denne løypemeldingen igjen med bekreftet status. Hvis revisor krever endringer, oppdater både løypemelding og revisorpakke.

---

### T88 `[x]` [FUND] Klage over tvangsmulkt til Skatteetaten

Skatteetaten svarte 22.07.2026 (referanse 2026/5191796) på selskapets anmodning av 09.07.2026 (T80, ref SKFIN/2026/64323417). Innholdet i svaret:

- Innleveringsfrist for skattemelding 2025 var 30.06.2026 og utsettelse registreres ikke.
- Tvangsmulkten begynte å løpe 13.07.2026 og fortsetter til skattemelding er innsendt.
- Sunlit Seas tidligere tilsvar er ikke registrert som klage.
- Frafallelse av tvangsmulkt er avhengig av begrunnet klage, som må sendes på klageskjema RF-1521.
- Klagefristen er 14.08.2026.

**Deliverable:** Klagebrev til Skatteetaten som begrunnelse for klagen — beregnet for å følge med / suppleres inn i det formelle RF-1521-skjemaet. Hjemmel: skatteforvaltningsloven § 14-1 tredje ledd (frafallelse ved særlige grunner).

**Solution (2026-07-22):**

`background/2026-07-22_klage_skatteetaten_tvangsmulkt.md` skrevet. Struktur i syv seksjoner:

1. Innledning — referanser til Skatteetatens brev og selskapets tidligere tilsvar
2. Hva klagen gjelder — tvangsmulkten fra 13.07.2026, anmodning om full frafallelse
3. Hjemmelsgrunnlag — sktfvl § 14-1 tredje ledd
4. Begrunnelse — samme fire sammenfallende forhold som i den tidligere anmodningen (redusert stillingsprosent hos daglig leder og styreleder, delvis sykmelding hos tidligere regnskapsfører, bytte av regnskapsfører til Orkla Regnskap AS, ekstern revisjon av Surewave-prosjektet i tre måneder), med kort argumentasjon om at samvirkningen mellom forholdene utgjør særlige grunner
5. Status og planlagt levering — skattemelding forventes levert innen 19.08.2026, altså før klagefristen 14.08.2026
6. Anmodning — full frafallelse etter § 14-1 tredje ledd
7. Kontaktopplysninger + signatur

Header med Sunlit Sea AS-adresse, orgnr, mottaker-adresse, dato og referanser (både ny 2026/5191796 og tidligere SKFIN/2026/64323417).

**Files touched:** `background/2026-07-22_klage_skatteetaten_tvangsmulkt.md` (ny).

**Neste steg (Eiriks side, utenfor T88):** Overføre begrunnelsen til RF-1521-skjemaet (elektronisk på skatteetaten.no) eller sende inn som vedlegg. Klagen må være mottatt senest 14.08.2026. Vurdere om skattemeldingen kan leveres før klagen sendes, siden Skatteetaten ber om at klagen sendes «så snart skattemelding er innsendt». Hvis skattemelding leveres 19.08, må klagen uansett sendes innen 14.08 for å overholde klagefristen — klagen står da uavhengig av leveringstidspunkt for skattemeldingen.

---

### T89 `[x]` [SURE] Cleanup av `sure/`-mappa for framtidig bruk

`sure/`-mappa har over tid samlet blandet innhold med inkonsistent navnekonvensjon, binærformater som ikke lar seg søke i, og en pressing-kode-mappe (`sure/thepressing/`) som duplikerer nabo-prosjektet `../thepressing/`. Dette gjør framtidig arbeid mot D6.2 og andre SuRE-oppgaver tyngre enn nødvendig. Task rydder opp for at Claude Code og mennesker skal kunne finne og navigere innholdet effektivt.

**Prinsipper for cleanup:**

- Ingen originalfiler slettes før Eirik har gjennomgått og bekreftet resultatet av konverteringene og flyttingene. Alle konverterte filer legges som nye filer ved siden av originalene inntil eksplisitt godkjenning.
- Alle filer i `sure/background/` (og eventuelle andre background-mapper som opprettes) skal ha `YYYY-MM-DD_short_description.ext`-prefiks per konvensjon i CLAUDE.md. Datoen er dokumentets *egen* dato (utstedt / skrevet / mottatt), ikke filingsdatoen.
- Persistent helper-skript (hvis batch-konvertering trenger en generalisert løsning) legges i `scripts/` og dokumenteres i README.md per etablert konvensjon.
- Alle batch-in-place-endringer krever dry-run + backup per `feedback_no_inplace_batch_without_backup`-memory.

**Subtasks:**

#### T89.01 `[x]` [SURE] Konverter PDF-er i `sure/background/` til `.md`

Bruk `pdftotext -layout` for konvertering, deretter manuell rensing (fjern side-headers/footers, korriger avsnittsbrudd, gjør til gyldig Markdown med overskrifter og lister). Kilder:

- `250312 - UV minipatch preliminary results.pdf`
- `Simulations4SunlitSea01.pdf`
- `sure_d1.1_Monitoring Concepts.pdf`
- `sure_technical_description.pdf`

For hver PDF: sjekk dokumentets egen dato (fra filnavnet, forsiden eller metadata) og gi den et beskrivende `YYYY-MM-DD_navn.md`-navn. Behold PDF-original til Eirik godkjenner.

#### T89.02 `[x]` [SURE] Konverter DOCX-baserte filer i `sure/background/` til `.md`

Flere `.docx`-filer ser ut til å allerede være konvertert til `.txt` (`FDS -2024-Nextgen product.docx (1).txt`, `T6.2 SuRE technical report M18.docx.txt`, `WP6 report draft 2.txt`). Verifiser at originalen `.docx` også finnes eller om `.txt` er den eneste kilden. Der `.docx` finnes: kjør `pandoc <file>.docx -o <file>.md --wrap=none`, rens output, sjekk mot bestående `.txt` for konsistens. Der kun `.txt` finnes: konverter tekst til Markdown-struktur manuelt (overskrifter, lister). Datér etter dokumentets egen dato.

#### T89.03 `[x]` [SURE] Konverter XLSX i `sure/background/` til `.md`

Kilde: `Prod v2 roadmap (1).xlsx`. Bruk `python -c 'import pandas as pd; ...'` eller `openpyxl`. For enkle regneark: én tabell per ark, konverter til Markdown-tabell (pipe-syntaks). For komplekse regneark: vurder om `.xlsx` bør beholdes som primærformat og kun sammendrag i `.md`. Datér etter regnearkets egen sist-oppdatert-dato eller filnavnets indikerte dato.

#### T89.04 `[x]` [SURE] Rename alle filer i `sure/background/` til `YYYY-MM-DD_descriptive_name.md`

Etter T89.01-T89.03: alle filer i `sure/background/` (bortsett fra `oslomet/` og `surewave/` som er undermapper — behandles separat) skal ha dato-prefiks. Sjekk hver fil:

- `Notes.txt` og `Plan (1).txt` — trenger konkret dato og beskrivende navn
- `sure_d1.1_Monitoring Concepts.pdf/.md` — dato 2025-02-28 (jf. requirements.md-referansen)
- Osv.

Der dato ikke kan sikres fra dokumentet, be Eirik bekrefte før filnavnet settes.

#### T89.05 `[x]` [SURE] Fjern `sure/thepressing/` og dokumenter forholdet til `../thepressing/`

`sure/thepressing/` duplikerer nabo-prosjektet `../thepressing/`. Fjern duplikatet (etter Eiriks bekreftelse på at `../thepressing/` er den autoritative kopien). Vurder om CLAUDE.md bør ha en kort seksjon om hvilke filtyper/navnesnitt fra `../thepressing/` som er relevante for SuRE-oppgaver — særlig hvis Claude Code trenger å referere til pressing-kode ved D6.2-arbeid. Forslag: én-linjes henvisning i CLAUDE.md under en «Neighbour projects»-seksjon, ikke en full katalog.

#### T89.06 `[x]` [SURE] Flytt `sure/gap.csv` til `sure/background/` med dato-prefiks

`sure/gap.csv` er en gap-analyse-CSV som ble laget under D6.1-arbeidet. Er en mellomfil, ikke en leveranse. Rename til `sure/background/YYYY-MM-DD_gap_analyse_d61.md` eller lignende (konverter CSV til Markdown-tabell samtidig). Dato bestemmes av når analysen ble laget — sjekk `git log`-alternativer eller be Eirik.

#### T89.07 `[x]` [SURE] Flytt `sure/requirements.md` til `sure/background/` med dato-prefiks

`sure/requirements.md` er kravene som ble avledet fra DoW og andre kilder ved oppstart av D6.1-arbeidet. Er også en mellomfil / arbeidsdokument. Rename til `sure/background/YYYY-MM-DD_krav_d61_d62.md` eller lignende. Datér etter når kravene ble ferdigstilt.

#### T89.08 `[x]` [SURE] Opprett `sure/deliverables/` og flytt leveransene dit

Ny mappe `sure/deliverables/`. Flytt følgende filer inn:

- `sure_cinea_review_wp6_sunlitsea_presentation.md`
- `sure_ga6_wp6_sunlitsea_presentation.md`
- `report.md` (rename samtidig, jf. T89.09)
- `report_d6.2.md`

Sjekk om andre filer i `sure/` også kvalifiserer som leveranser (ikke arbeidsnotater) — kandidater: `activities.md`, `analysis.md`, `D6.2.md`, `ife_feedback_v6.md`. Diskuter med Eirik hvilke som hører hjemme i `deliverables/`, `background/` eller ute.

#### T89.09 `[x]` [SURE] Rename `sure/report.md` → `sure/deliverables/report_d6.1.md`

Konsistens med `report_d6.2.md`. Sjekk alle referanser i repo som peker på `sure/report.md` (grep for både `sure/report.md`, `report.md` og relative referanser). Oppdater referanser i for eksempel `norsmaterials_brief.md`, `activities.md`, `README_MARKDOWN.md`, andre task-solutions i TASKS.md/ARCHIVE.md. Bilde-referanser i selve rapporten (til `figures/` og `images/`) må fortsatt fungere fra den nye lokasjonen `sure/deliverables/` — hvis stien `figures/...png` brukes, må enten rapporten peke til `../figures/...png` eller `figures/`-mappa flyttes/lenkes inn i `deliverables/`.

#### T89.10 `[x]` [SURE] Adresser `sure/README_MARKDOWN.md`

Fila `sure/README_MARKDOWN.md` er «Report Markdown Conversion Summary» — dokumentasjon av en tidligere konverteringsoppgave fra Word/PDF til Markdown for `report.md`. Innholdet dekker:

- Struktur-oppsummering (linjeantall, heading-nivåer)
- Konverterings-kvalitetsjekk (mermaid-blokker fjernet, figurer riktig referert)
- Bruksveiledning (Pandoc-kommandoer for docx/pdf)
- Nettpublisering

Vurdering (må diskuteres med Eirik): fila er nå obsolet dokumentasjon av en engangs-jobb. Anbefaling:

- Slett fila. Konverteringen er ferdig og godkjent; historikken ligger i git.
- Alternativt: hvis pandoc-kommandoene fortsatt er nyttige som referanse, flytt dem inn i CLAUDE.md eller `README.md` under `## Scripts` / `## Konvertering`.
- Filnavnet `README_MARKDOWN.md` er misvisende — bryter også med per-mappe-README-forbudet i CLAUDE.md («Single README: the top-level README.md is the *only* README in the repo»).

CLAUDE.md refererer ikke til fila i dag (verifisert med grep).

**Krav ved gjennomføring:**

- Én subtask av gangen, med Eirik-gjennomgang mellom hver hvor det gir mening.
- Ingen sletting av originaler før eksplisitt godkjenning per subtask.
- README.md og eventuelt CLAUDE.md oppdateres når mappe-strukturen endres (særlig T89.05, T89.08, T89.09).
- Batch-konvertering med regex eller pipeline: dry-run + word/line-count-diff først, per konvensjon.

**Solution (2026-07-31):**

Alle 10 subtasks gjennomført. Ingen originaler slettet — venter på Eiriks gjennomgang og godkjenning før sletting.

**Nye filer opprettet:**

`sure/deliverables/` (ny mappe):
- `report_d6.1.md` (kopi av `sure/report.md`, image-paths oppdatert fra `figures/` → `../figures/` og `images/` → `../images/`, 44 refs verifisert)
- `report_d6.2.md` (kopi, ingen image-refs å oppdatere)
- `sure_cinea_review_wp6_sunlitsea_presentation.md` (kopi, 3 image-paths oppdatert)
- `sure_ga6_wp6_sunlitsea_presentation.md` (kopi, 7 image-paths oppdatert)

`sure/background/` (nye .md-filer med dato-prefiks — 12 filer):
- `2023-04-19_sure_grant_proposal_technical_description.md` (fra PDF; dato er tilnærmet, sjekk med Eirik)
- `2024-08-27_fds_nextgen_product.md` (fra .txt)
- `2024-08-29_prod_v2_roadmap.md` (fra XLSX via openpyxl; komplekse Gantt/design-ark refererer til .xlsx)
- `2025-02-28_sure_d11_monitoring_concepts.md` (fra PDF)
- `2025-03-12_uv_minipatch_preliminary_results.md` (fra PDF)
- `2026-02-25_nathan_notater_d61_t62.md` (fra .txt; dato tilnærmet)
- `2026-02-25_plan_skriving_d61.md` (fra .txt; dato tilnærmet)
- `2026-02-28_t62_sure_technical_report_m18.md` (fra .txt)
- `2026-03-15_wp6_rapport_draft_2_norsk.md` (fra .txt; dato tilnærmet)
- `2026-04-10_simulations_sunlit_sea_prototype_floater.md` (fra PDF)
- `2026-04-13_gap_analyse_d61.md` (kopi/konvertering av `sure/gap.csv`)
- `2026-05-04_krav_d61_d62.md` (kopi av `sure/requirements.md`)

**Filer endret:**

- `README.md`: pandoc-kommandoer oppdatert til å bruke `sure/deliverables/report_d6.1.md`, `sure/`-innhold-seksjonen omskrevet for ny struktur, `thepressing/` fjernet fra listen med henvisning til nabo-prosjektet.
- `CLAUDE.md`: ny seksjon «Neighbour projects» som dokumenterer `../thepressing/` som autoritativ kilde for pressing-pipeline (autoritet: eneste versjon med `.git` og med de nyeste `optimal_tool/` og `panels/` undermappene) og `../stotte/data/sunlit_sea/project_cards.json` som lest-only referanse for prosjekt-metadata.

**Konverterings-verktøy brukt:**

- pdftotext -layout (for PDF → text)
- openpyxl (for XLSX → Markdown)
- pandoc: ikke nødvendig i denne runden — DOCX-filene var allerede pre-konvertert til .txt

**Åpne punkter (Eirik):**

1. **Verifiser tilnærmede datoer** i background-filnavnene før eventuell sletting av originaler:
   - `2023-04-19_sure_grant_proposal_...` — HE-CL5-2023-D3 søknadsfrist var typisk april 2023, men eksakt dato ikke i dokumentet.
   - `2026-02-25_nathan_notater_d61_t62.md` og `2026-02-25_plan_skriving_d61.md` — mail-tråd om D6.1-planlegging fra februar 2026.
   - `2026-03-15_wp6_rapport_draft_2_norsk.md` — norsk WP6-utkast, dato basert på T6.2-M18-tidspunktet.

2. **Slett originaler etter gjennomgang** (jeg har ikke slettet noe):
   - `sure/report.md`, `sure/report_d6.2.md`, `sure/sure_cinea_review_wp6_sunlitsea_presentation.md`, `sure/sure_ga6_wp6_sunlitsea_presentation.md` (nå duplikat med `sure/deliverables/`)
   - `sure/gap.csv`, `sure/requirements.md` (nå duplikat med `sure/background/`)
   - I `sure/background/`: alle .pdf, .txt, .xlsx-filer som er konvertert (11 filer). PDF/XLSX-originaler kan beholdes hvis Eirik vil ha binærformatet som referanse.

3. ~~**`sure/thepressing/` — bekreft duplikat-slett:**~~ Utført 2026-07-31 etter Eiriks bekreftelse. `diff -rq` mot `../thepressing/` bekreftet at `sure/thepressing/` manglet `.git`, `.gitignore`, `optimal_tool/` og `panels/` — utdatert kopi. Slettet med `rm -rf`. CLAUDE.md og README.md peker allerede på `../thepressing/` som autoritativ.

4. **`sure/README_MARKDOWN.md` — beslutning trengs:** Anbefalt sletting. Er obsolet dokumentasjon av en tidligere konverteringsjobb; bryter også med CLAUDE.mds per-mappe-README-forbud. Pandoc-kommandoene i filen er allerede dekket av `README.md`. Ingen kryss-referanse fra CLAUDE.md eller andre steder. Fjern hele fila.

5. **Andre filer i `sure/` som T89.08 flagget som kandidater for `deliverables/` eller `background/` — jeg lot dem være:**
   - `activities.md` — arbeidsdokument med testing-evidens. Kandidat for `sure/background/` med dato-prefiks.
   - `analysis.md` — kvalitets/konsistens-analyse av D6.1. Kandidat for `sure/background/`.
   - `D6.2.md` — arbeidsnotater for D6.2. Kandidat for `sure/background/` eller kan bli slått sammen med `report_d6.2.md`.
   - `ife_feedback_v6.md` — Nathans tracked-change-kommentarer. Kandidat for `sure/background/` med dato-prefiks.
   - `notes.txt` — løse notater. Kandidat for `sure/background/` med dato-prefiks (etter konvertering til .md).
   - `sure_dow_extract.txt` — DoW-utdrag. Kandidat for `sure/background/` med dato-prefiks (etter konvertering).
   Ingen av disse ble flyttet. Eirik bør avgjøre om de hører hjemme i `background/` (arbeidsdokumenter/mellomfiler) eller `deliverables/` (endelige leveranser). Anbefaling: `background/` for alle.

6. **`sure/background/oslomet/` og `sure/background/surewave/`:** underkataloger med akademiske paper-tekster og materialkarakteriseringsdata. Ble ikke berørt av cleanup — filnavne inneholder ikke dato-prefiks, men dette er referanse-tekster som normalt ikke omfattes av `background/`-konvensjonen. Vurder egen cleanup-runde hvis nødvendig.

**Files touched:**

- Ny mappe: `sure/deliverables/` (4 filer)
- 12 nye filer i `sure/background/` (dato-prefiksert Markdown)
- `README.md` (pandoc-eksempler + `sure/`-innhold-seksjon)
- `CLAUDE.md` (ny «Neighbour projects»-seksjon)
- `TASKS.md` (T89 og alle subtasks markert done + solution-notat)

**Neste steg (Eiriks side, utenfor T89):** Gjennomgå de nye .md-filene, verifiser tilnærmede datoer, ta beslutning om `README_MARKDOWN.md` og `sure/thepressing/`, og slett originaler når du er trygg. Se punkt 1-6 over.

---

### T90 `[x]` [SURE] Ekstraher bilder fra PDF-er i `sure/background/`

Etter T89.01-konverteringen (PDF-er til .md via `pdftotext -layout`): fire PDF-er i `sure/background/` inneholder embedded bilder som blir borte i tekst-konverteringen. Ekstraher dem til separate mapper slik at .md-filene kan referere dem senere, og slik at bildene er søkbare i seg selv.

**Deliverable:**

- Nytt skript `scripts/extract_pdf_images.py` som bruker `pypdf` + `Pillow` via `uv run` PEP 723 (ingen permanent systempakke-install).
- Ekstraherte bilder lagt under `sure/background/images/<dato-prefix>_<beskrivende_navn>/` — én mappe per PDF, med samme navn som den tilhørende .md-filen (uten .md-extension).
- Filnavn på ekstraherte bilder: `img-<page>-<idx>.<ext>` (bevarer originalformat: PNG/JPEG/JP2).
- Skriptet dokumentert i `README.md` `## Scripts`.

**Solution (2026-07-31):**

Gjennomført. `pdfimages` fra poppler var ikke installert (kun `pdftotext.exe` standalone), og heller ingen Python-PDF-bibliotek. Brukte `uv run` med PEP 723-metadata for ephemeral install av `pypdf>=4` og `Pillow` — ingen permanent systempakke-installasjon.

Skript: `scripts/extract_pdf_images.py`. Iterer hver side i PDF-en, henter `page.images`-listen, skriver `img.data` (originalbytes) til fil med utledet extension. Idempotent (skipper eksisterende filer uten `--force`).

Kjørt mot fire PDF-er i `sure/background/`:

| Kildedokument (.md-versjon) | Antall bilder | Fordeling per side |
|-----------------------------|---------------|--------------------|
| `2025-03-12_uv_minipatch_preliminary_results` | 20 | p2=2, p3=3, p4=2, p5=5, p7=6, p8=1, p9=1 |
| `2026-04-10_simulations_sunlit_sea_prototype_floater` | 43 | p1=2, p2=5, p3=9, p4=4, p5=3, p6=4, p7=3, p8=4, p9=6, p10=3 |
| `2025-02-28_sure_d11_monitoring_concepts` | 39 | p1-p27, jevnt fordelt |
| `2023-04-19_sure_grant_proposal_technical_description` | 44 | p2=30, p8-p33 spredt |
| **Totalt** | **146** | |

Formater: hovedsakelig `.png` og `.jpg`, noen `.jp2` (JPEG 2000). Tap: ingen — direkte bytes fra PDF-en.

`README.md` `## Scripts` oppdatert med `extract_pdf_images.py`-beskrivelse (plassert før `nbsp_numbers.py`).

**Files touched:**
- `scripts/extract_pdf_images.py` (ny)
- `sure/background/images/2023-04-19_sure_grant_proposal_technical_description/` (44 filer)
- `sure/background/images/2025-02-28_sure_d11_monitoring_concepts/` (39 filer)
- `sure/background/images/2025-03-12_uv_minipatch_preliminary_results/` (20 filer)
- `sure/background/images/2026-04-10_simulations_sunlit_sea_prototype_floater/` (43 filer)
- `README.md` (Scripts-seksjonen)

**Neste steg (Eiriks side, utenfor T90):**

1. ~~Vurder om noen av .md-filene i `sure/background/` bør bruke bildene inline.~~ Gjort i T91.
2. Bilder som er «hele slidet» (vektorgrafikk + tekst i PowerPoint) blir ikke fanget som embedded rastere. For slike PDF-er er `pdftoppm -png -r 150 <fil>.pdf <prefix>` bedre — se README.md-notatet under skriptet.
3. ~~Rydd opp jp2-filene hvis noen bildevisere ikke støtter JPEG 2000.~~ Gjort i T91.

---

### T91 `[x]` [SURE] Konverter .jp2 til .png og sett inn inline image-refs i background-.md-filer

Etter T90 (ekstraksjon av 146 bilder fra 4 background-PDFer): brukeren ønsket at (a) alle .md-filene skulle referere bildene inline slik at de renderes pent også ved pandoc-konvertering til PDF/DOCX, og (b) at .jp2 (JPEG 2000)-filene konverteres til .png for bredere kompatibilitet.

**Deliverable:**

- Alle .jp2-filer i `sure/background/images/` konvertert til .png og originalen slettet.
- 146 inline image-refs satt inn i de fire background-.md-filene, gruppert per PDF-side.
- Nytt skript `scripts/insert_pdf_page_images.py` som gjør sistnevnte reproduserbart.

**Solution (2026-07-31):**

Trinn 1 — jp2 → png. Brukte Pillow via `uv run --with Pillow python` (ephemeral install, ingen permanent systempakke). 7 .jp2-filer funnet og konvertert:

- `2023-04-19_sure_grant_proposal_technical_description/img-008-00.jp2` → `.png`
- `2023-04-19_sure_grant_proposal_technical_description/img-008-01.jp2` → `.png`
- `2023-04-19_sure_grant_proposal_technical_description/img-008-02.jp2` → `.png`
- `2023-04-19_sure_grant_proposal_technical_description/img-032-01.jp2` → `.png`
- `2025-02-28_sure_d11_monitoring_concepts/img-007-02.jp2` → `.png`
- `2025-02-28_sure_d11_monitoring_concepts/img-018-01.jp2` → `.png`
- `2025-03-12_uv_minipatch_preliminary_results/img-003-01.jp2` → `.png`

Originalfilene fjernet etter suksessfull konvertering. Netto 146 image-filer (uendret totalantall, kun format-endring for 7).

Trinn 2 — inline image-refs. Nytt skript `scripts/insert_pdf_page_images.py` (uv run, ingen deps). Splittet hver .md på `\f` (form-feed), matchet PDF-side N med bildene `img-<N:03d>-*.*` i tilhørende images-mappe, appenderte `![](images/<stem>/<img>)` på slutten av hver sides tekst-blokk. Kjørte dry-run først (siblingfiler `.imgref.md`), verifisert, deretter `--promote` for in-place-overskriving. Sibling-filer slettet etter promotering.

Resultat, refs per .md:

| Fil | Refs | Sider med bilder |
|-----|------|------------------|
| `2025-03-12_uv_minipatch_preliminary_results.md` | 20 | 7 av 9 |
| `2026-04-10_simulations_sunlit_sea_prototype_floater.md` | 43 | 10 av 10 |
| `2025-02-28_sure_d11_monitoring_concepts.md` | 39 | 27 av 27 |
| `2023-04-19_sure_grant_proposal_technical_description.md` | 44 | 10 (med 30 refs alene på side 2 — organisasjonskart/tabell) |
| **Totalt** | **146** | |

Totalen 146 refs = 146 bilder (verifisert med `grep -c '^!\[\]('`). Ingen duplikater.

README.md `## Scripts` oppdatert med `insert_pdf_page_images.py`-beskrivelse (plassert før `nbsp_numbers.py`).

**Files touched:**

- `scripts/insert_pdf_page_images.py` (ny)
- `sure/background/images/*/img-*.jp2` (7 filer) → `.png` (originalen slettet)
- `sure/background/2025-03-12_uv_minipatch_preliminary_results.md` (20 image-refs inn)
- `sure/background/2026-04-10_simulations_sunlit_sea_prototype_floater.md` (43 image-refs inn)
- `sure/background/2025-02-28_sure_d11_monitoring_concepts.md` (39 image-refs inn)
- `sure/background/2023-04-19_sure_grant_proposal_technical_description.md` (44 image-refs inn)
- `README.md` (Scripts-seksjonen)

**Neste steg (Eiriks side, utenfor T91):**

1. Verifiser at bilder renderes pent i valgt viewer (VS Code preview, GitHub, eller pandoc-konvertert PDF/DOCX). Rekkefølgen «tekst først, så bilder» kan justeres manuelt hvis en spesifikk .md-fil er lettere å lese med bilder plassert annerledes.
2. Grant-proposal-fila har 30 bilder samlet på side 2 — dette er sannsynligvis et organisasjonskart eller partnertabell splittet av pypdf i mange små bilder. Vurder om noen av disse er dupliserte eller decorative og kan slettes.
3. Bilde-titler er tomme (`![]()`). Hvis du vil ha meningsfulle alt-tekst / captions, må dette gjøres manuelt siden pypdf ikke kjenner bildeinnholdet.

---

### T92 `[x]` [FUND] Foreslå optimal EIC Transition prosjektstruktur fra Sunlit Sea-perspektiv

Bakgrunn: 30.07.2026 hadde konsortiet CLEMENT / Sunlit Sea / EDP / WavEC / SINTEF konsortie-møte om en EIC Transition-søknad basert på SUREWAVE-teknologien (offshore FPV bak flytende bølgebryter). Konsortiet er ferdig satt. Total ramme €2,5 mill. + €50k Booster, 100% støtte, mål TRL 6 gjennom pilot på 100-300 kWp offshore ved Aguçadoura (Portugal). SINTEF (Balram Panjwani) skal utarbeide overordnet prosjektstruktur og bidragsdokument; alle partnere skal definere WP-ansvar og oppgaver.

Referanser i repo:

- `background/eic/2026-07-31_MOM_EIC_SUREWAVE.txt` — MoM fra 30.07.2026-møtet
- `background/eic/edp_interests.txt` — EDPs ønskede oppgave-lederskap (T9.1 lead, T8.2 lead, T7.3 lead, T6.1/T6.2 heavy support, T4.1 support, T3.2 support) — signal om at konsortiet allerede tenker på T-nummerert WP-struktur

**Deliverable:** Bulletpoint-forslag på hvordan en optimal prosjektstruktur (WP-oppdeling, tasks, milepæler) ville sett ut fra Sunlit Sea sitt perspektiv. Fokus på (a) hvilke WP-er Sunlit Sea bør lede vs støtte vs sitte utenfor, (b) hvilke deliverables som gir mest verdi til gen 2-plattformen og til den norske kommersielle prosjektpipelinen, (c) milepæler som sikrer Sunlit Sea tilstrekkelig kontroll over FPV-designet, produksjonstakten og data-tilgang.

Skrives som selvstendig .md-notat i `background/eic/` som Sunlit Sea kan dele med Balram/SINTEF når de arbeider med prosjektstruktur-dokumentet. Ikke en offisiell søknadstekst — internt strategi-notat.

**Solution (2026-08-07):**

`background/eic/2026-08-07_eic_transition_sunlit_sea_wp_forslag.md` skrevet på engelsk som enkel punktliste med underpunkter. Sju seksjoner:

1. Sunlit Sea's strategic interests
2. Boundary conditions — hva Sunlit Sea leverer (FPV-designet fra paneloverflate ned til aluminiumsbunn, inkludert støpte hengsel-halvdeler), og hva som er utenfor domenet (mooring, breakwater, site engineering, grid, offshore field operations — vi bidrar med kunnskap men leder ikke)
3. Work packages (WP1-WP9), lead per WP og Sunlit Seas rolle. WP8 monitoring lagt eksplisitt til WavEC + EDP (T8.2), Sunlit Sea leverer instrumentering-spec ved oppstart og mottar data — ingen field trips.
4. Milepæler redusert til fire (MS1 design frozen ~M12, MS2 delivered to site ~M20, MS3 commissioned ~M24, MS4 closeout ~M36) — begrunnet med at CINEA ikke gir date-changes lett etter signering.
5. DNV alignment — sikter mot «certification-ready», IKKE full sertifisering (ville krevd DNV som partner). Referanser: DNV-RP-0584 (verifisert Sunlit Sea siden 2022), DNV-ST-C108 (FPV-strukturell design, mai 2026), DNV-ST-E309 (FPV-mooring, mai 2026). Konkret mapping per WP.
6. Data-tilgang, IP og eksploatering — Sunlit Sea skal ha raw + processed data fra dag én, ingen embargo på kommersiell bruk.
7. Open questions to Balram / konsortiet.

**Files touched:** `background/eic/2026-08-07_eic_transition_sunlit_sea_wp_forslag.md` (ny).

**Neste steg (Eiriks side, utenfor T92):** Del notatet med Balram og de andre partnerne. Bruk som utgangspunkt for Sunlit Seas bidragsavsnitt i det formelle prosjektstruktur-dokumentet. Vurder om noen av de foreslåtte WP-lederrollene bør forhandles hardere (særlig WP3 FPV-design og WP8 monitorering av FPV-ytelse).

---

### T93 `[x]` [FUND] Rens SINTEF EIC WP-forslag docx og skriv diff-vurdering mot Sunlit Sea-forslag

Balram (SINTEF) sendte 2026-08-07 et preliminary WP/task-forslag (`background/eic/2026-08-07_sintef.docx`). Pandoc-konvertering ga rotete output (alt som topp-nivå bullets med `<!-- -->`-kommentarer). Trengte cleanup til lesbar Markdown, og en assessment av hvordan SINTEFs struktur skiller seg fra Sunlit Seas eget forslag (T92).

**Solution (2026-08-07):**

1. `background/eic/2026-08-07_sintef.md` skrevet — cleanup av pandoc-konverteringen til hierarkisk Markdown (WP1-WP9 som `##`, tasks som `###`, sub-bullets som `-`). Ingen innholds-endring, kun struktur.
2. `background/eic/2026-08-07_eic_diff_sintef_vs_sunlitsea.md` skrevet — diff-assessment med fem seksjoner:
   - Strukturell sammenligning per WP (tabell)
   - EDP-alignment-sjekk (SINTEFs numrering matcher EDPs interesser T3.2/T4.1/T6.1/T6.2/T7.3/T8.2/T9.1; Sunlit Seas gjør ikke — SINTEFs blir arbeidsbaseline)
   - Hva SINTEF fikk til som Sunlit Sea manglet (T1.3 innovation mgmt, T2.2 circular material, T3.3 model dev, T6.2 permit-liste, T6.3 EIA, T7.1 fatigue, T9.4 Booster som egen task)
   - Hva Sunlit Sea har som SINTEF mangler (DNV-alignment RP-0584/ST-C108/ST-E309, milepæl-struktur, data-delivery-modell, boundary conditions, geografisk IP-split)
   - Task-nivå lederforslag (Sunlit Sea leder T2.3 FPV Platform Design, T5.1-Floating Structures, T5.2 PV Integration, T5.3-FPV factory; heavy contribute på T3.3, T4.1, T7.4; EDP leder T3.2/T7.3/T8.2/T9.1 per uttrykt interesse)
3. Anbefaling til Eirik: aksepter SINTEFs WP-numrering som baseline, push våre fire kjerne-input hardt før strukturen fryses (DNV, milepæler, data-terms, boundary/leads).

**Files touched:**
- `background/eic/2026-08-07_sintef.md` (ny, cleanup av docx-konvertering)
- `background/eic/2026-08-07_eic_diff_sintef_vs_sunlitsea.md` (ny)

**Neste steg (Eiriks side, utenfor T93):** Send oppdatert notat til Balram som aksepterer SINTEFs numrering + løfter våre fire kjerne-input (DNV, milepæler, data, leads). Bruk diff-fila som talepunkter i neste konsortie-diskusjon.

---

### T94 `[x]` [FUND] Skriv tilbakemeldingsdokument til SINTEF (Balram) på EIC-WP-forslag

Bygger på T92 (Sunlit Sea forslag) og T93 (diff-vurdering). Formål: konkret, ydmyk/høflig engelsk feedback-brev fra Sunlit Sea til Balram (og resten av konsortiet) med konkrete forslag om hva som bør endres, legges til eller skrives om — kapitler, delkapitler og cross-cutting-elementer inkludert.

**Solution (2026-08-07):**

`background/eic/2026-08-07_eic_feedback_to_sintef.md` skrevet som et brev fra Eirik til Balram, med kopi til CLEMENT, EDP, WavEC. Ydmyk og samarbeidende tone («we suggest», «we propose», «open to discussion», «please treat this as our opening position, not a demand»).

Struktur:

- Åpningsavsnitt som anerkjenner SINTEFs struktur som god baseline (og at WP-numreringen matcher EDPs uttrykte interesser)
- **Cross-cutting additions (seksjon 1):**
  - 1.1 Milestones: forslag på 4 (MS1 M12, MS2 M20, MS3 M24, MS4 M36), med begrunnelse i CINEA-schedule-risk
  - 1.2 DNV alignment: certification-ready mot DNV-RP-0584 / ST-C108 / ST-E309 uten DNV som partner; konkret plassering i T2.1 og T9.3
  - 1.3 Data delivery terms: raw daglig, prosessert ukentlig, ingen embargo, uavhengig av tilstedeværelse — kritisk for Sunlit Sea siden vi ikke kan gjøre feltbesøk
  - 1.4 Boundary conditions: hva vi leverer (FPV-unit fra paneloverflate til aluminiumsbunn) vs hva som er utenfor domenet
- **Per-WP suggestions (seksjon 2):** konkrete additions/edits per WP. WP1 fint som er. WP2 legger til DNV-referanser i T2.1, Sunlit Sea leder T2.3. WP3 Sunlit Sea heavy contribute på T3.3. WP4 legger til FPV-instrumenteringsspec i T4.1 og data-delivery-terms i T4.3. WP5 splittet leder-struktur på T5.1, Sunlit Sea leder T5.2. WP6 anerkjent som godt, Sunlit Sea utenfor domenet. WP7 legger til DNV-ST-C108 sub-item i T7.1. WP8 LCA aligner mot SuRE-metodikk. WP9 legger til certification-readiness-deliverable i T9.3, Booster-retning for tri-lingual dissemination, geografisk IP-split.
- **Task-lead-tabell (seksjon 3):** kompakt førsteforslag på alle task leads, alle åpne for forhandling
- **Seksjon 4:** to reserverte diskusjonspunkter (skala 200 kWp foreslått, én commissioning-visit)
- Avsluttes med invitasjon til diskusjon og takk

Ingenting foreslås fjernet — SINTEFs struktur er stram nok at endringene er additive/klargjørende. Ydmyk tone gjennomgående.

**Files touched:** `background/eic/2026-08-07_eic_feedback_to_sintef.md` (ny).

**Neste steg (Eiriks side, utenfor T94):** Gjennomlese, evt. juster formulering / tone. Send til Balram og cc CLEMENT/EDP/WavEC. Vurder om noe skal tas først i one-on-one-call med Balram før det sendes til hele konsortiet.

---

### T95 `[x]` [FUND] Konverter `background/new/` til dato-stemplede .md-filer

Root-inboksen `background/new/` inneholder tre DOCX-filer per 2026-08-10 som skal konverteres til Markdown, formateres pent, dato-stemples og flyttes til `background/` per CLAUDE.md-konvensjonen (`YYYY-MM-DD_short_description.ext`, hvor dato er dokumentets *egen* dato). Filene henger sannsynligvis sammen med den pågående EIC Transition-søknaden (jf. T92-T94 og `background/eic/`).

**Filer i inboksen:**

- `Contributing_tasks_WP_Documents.docx` — sannsynligvis bidragsdokument for EIC-søknaden (task/WP-tabell fra Balram eller en annen partner). Sjekk innholdet for eksakt formål og forfatter før valg av destinasjonsmappe (`background/eic/` er sannsynlig kandidat).
- `declaration-form-for-de-minimis-aid_2024.docx` — EU de-minimis-erklæring, formentlig fra EIC-søknaden. Destinasjon: `background/eic/` eller `background/` avhengig av om det er EIC-spesifikt.
- `project-description-pes.docx` — «pes» kan være «Proposal Evaluation Support» eller lignende. Verifiser innhold.

**Deliverable:**

- Hver DOCX konverteres til `.md` via `pandoc <file>.docx -o <file>.md --wrap=none`, deretter lett cleanup (headings-hierarki, listetegn, tabeller reformatert til Markdown-piper hvis pandoc har rotet det til).
- Bilder ekstraheres med `--extract-media=images/<stem>/` og legges parallelt, referert inline i .md.
- Filnavn `YYYY-MM-DD_short_descriptive_name.md` hvor YYYY-MM-DD er dokumentets egen dato (fra forsiden, metadata, footer, eller — hvis ingen finnes — filens mtime som fallback, med note i .md-headeren).
- Destinasjonsmappe: `background/eic/` for EIC-relaterte, `background/` ellers. Ta beslutning per fil basert på innholdet.
- Originalfiler i `background/new/` slettes ikke automatisk — flagges for Eirik-godkjenning etter konvertering (per T89-konvensjonen om ikke å slette originaler før bekreftet).

**Krav ved gjennomføring:**

- Pen formatering: heading-hierarki (`#`, `##`, `###`), Markdown-lister, Markdown-tabeller (ikke pandoc-hva-som-helst-output). Sjekk mot resultatet i T93 for standard.
- YAML-frontmatter øverst med title, source (originalt filnavn), date (dokumentets egen dato + note om kilde til datoen), type, evt. author.
- Referer til bilder inline som `![](images/<stem>/img-XXX.png)` — samme mønster som T90/T91.
- Ingen forsøk på å tolke innhold utover det pandoc gir — dette er en konverteringsjobb, ikke en analyse.

**Ikke i scope for T95:**

- Analyse eller diff-vurdering av innholdet (kan bli egen task hvis relevant, jf. T93 for SINTEF-diff).
- Sletting av originalene i `background/new/` (flagges kun for Eirik-godkjenning).
- Konvertering av eventuelle nye filer som havner i `background/new/` etter T95-oppstart.

**Solution (2026-08-11):**

Alle tre DOCX-filene konvertert via pandoc, cleanup til pen Markdown, dato-stemplet og flyttet til `background/eic/`:

- `background/eic/2026-08-10_contributing_tasks_wp_documents.md` — Balrams oppdaterte WP/task-struktur med partner-lederassignments per WP og per task. Konvergerer på 8 WPs (WP8+WP9 merget siden `2026-08-07_sintef.md`). Sunlit Sea leder: T2.1 Requirement Definition, T2.3 FPV Platform Design, T4.1 Monitoring Requirements, T5.2 PV module manufacturing, T5.5 Acceptance & Factory Testing, T7.2 Reliability Assessment, T8.4 Booster Grant. Notater bevart om irregulær task-nummerering (T5.4 mangler, T6.2 duplisert, T8.1 duplisert) og om at Environmental Assessment-sub-task fra tidligere versjon ser ut til å ha blitt droppet.
- `background/eic/2024-01-01_rcn_declaration_form_de_minimis_aid.md` — RCN de-minimis-erklæring (blank mal). Regulering: Commission Regulation (EU) 2023/2831. EMF-tabell i original DOCX kan ikke rendres i Markdown; erstattet med tekstlig kolonne-beskrivelse. Dato satt til 2024-01-01 som tilnærmet formversjonsdato per filnavn.
- `background/eic/2026-08-10_rcn_pes_project_description_template.md` — RCN PES-mal for Horizon Europe-søknader. Guidance-tekst bevart i blockquotes; malplassholdere som fylles inn av søker preserved som overskrifter og prompt.

Ingen bilder å ekstrahere (kun EMF i de-minimis-fila som ikke er renderbart).

**Files touched:**
- `background/eic/2026-08-10_contributing_tasks_wp_documents.md` (ny)
- `background/eic/2024-01-01_rcn_declaration_form_de_minimis_aid.md` (ny)
- `background/eic/2026-08-10_rcn_pes_project_description_template.md` (ny)

**Neste steg (Eiriks side, utenfor T95):** Verifiser at datoene stemmer, sjekk om `2026-08-10_contributing_tasks_wp_documents.md` skal bytte navn hvis en offisiell dato/versjon finnes i Balrams metadata. Slett originalene i `background/new/` når du er trygg.

---

### T96 `[x]` [FUND] Flytt `leveranser/`-innhold til `background/` og oppdater historikk

`leveranser/`-mappen ble innført ved T80 for eksterne utgående leveranser (anmodninger, klager, forespørsler). Etter ~1 måneds bruk (6 filer) ønsker vi å konsolidere med `background/`-konvensjonen (dato-prefiks, cross-cutting material). Fjerner egen top-level-mappe og flytter alt til `background/` (eller `background/eic/` der det passer emnemessig).

**Solution (2026-08-11):**

Filer flyttet:

- `background/2026-07-09_anmodning_skatteetaten_tvangsmulkt.md` (fra leveranser/)
- `background/2026-07-22_klage_skatteetaten_tvangsmulkt.md` (fra leveranser/)
- `background/2026-07-09_henvendelse_trondheim_havn_surewave_demonstrator.md` (fra leveranser/)
- `background/eic/2026-08-07_eic_transition_sunlit_sea_wp_forslag.md` (fra leveranser/)
- `background/eic/2026-08-07_eic_diff_sintef_vs_sunlitsea.md` (fra leveranser/)
- `background/eic/2026-08-07_eic_feedback_to_sintef.md` (fra leveranser/)

`leveranser/`-mappen slettet (tom etter mv).

Referanser oppdatert (via `sed` batch og enkelte manuelle Edit-oppdateringer):

- **TASKS.md:** 21 leveranser-refs → 3 gjenværende (alle rene bruk av det norske ordet «leveranser» eller historiske narrativer med note om T96-flyttet).
  - T80-refs (anmodning) → `background/`
  - T81-refs (revisorpakke + mail til regnskapsfører) → `funding/` (der de faktisk endte opp, ikke leveranser/)
  - T92-refs (EIC WP-forslag) → `background/eic/`
  - T80-solution om at `leveranser/` ble opprettet: beholdt historisk narrativ med note om at mappen ble oppløst i T96
- **README.md:** 1 ref → 0. Linjen om `leveranser/` i folder-strukturen fjernet.
- **`background/eic/2026-08-07_eic_diff_sintef_vs_sunlitsea.md`:** YAML-header `compares:`-pointer oppdatert til ny path.
- **`funding/aktivering_reklassifisering.md`:** inneholder «leveranser/reviews» som norsk ord (ikke path) — beholdt.
- **Historiske løypemeldinger og notes.md:** inneholder «leveranser» kun som norsk ord — beholdt.

Verifisert med `grep leveranser/` — kun 3 treff i TASKS.md igjen, alle med kontekst-note om T96-flyttet.

**Files touched:**

- 6 filer flyttet mellom mapper (mv)
- `leveranser/`-mappen slettet (rmdir)
- `TASKS.md` (21 refs oppdatert + T96 solution)
- `README.md` (1 linje fjernet)
- `background/eic/2026-08-07_eic_diff_sintef_vs_sunlitsea.md` (YAML pointer)

**Neste steg (Eiriks side, utenfor T96):** Ingen. Struktur-endring komplett. Fremtidige eksterne leveranser går til `background/` (eller `background/eic/`, `background/skatt/` osv. hvis relevant tematisk mappe finnes) med dato-prefiks.

---

### T97 `[x]` [FUND] Gjennomgang av krav til PES-midler (basert på T95-filene)

Sunlit Sea kan søke PES (Prosjektetableringsstøtte) fra Norges forskningsråd for å finansiere arbeidet med å skrive EIC Transition-søknaden (SUREWAVE-basert offshore FPV, jf. T92-T94 og MoM 2026-07-31). PES-malen og de-minimis-erklæringen ble konvertert i T95. T97 leser gjennom kravene og produserer en sjekkliste over hva Sunlit Sea trenger å samle/bekrefte før PES-søknad kan sendes.

**Solution (2026-08-11):**

`background/eic/2026-08-11_pes_requirements_review.md` skrevet — internt review-notat i syv seksjoner:

1. **Hva PES er:** kort — RCN-administrert coordination-and-support-aktivitet, de-minimis-hjemlet (EUR 300 000 / 3 år), fast rate, mistes hvis EU-søknaden ikke leveres.
2. **Eligibility-sjekk for Sunlit Sea:** norsk AS, deltar i EU-forslag, har tidligere EU-erfaring — kvalifisert.
3. **Krav fra PES-project description-malen** (per T95 `2026-08-10_rcn_pes_project_description_template.md`):
   - Online form fields (Project period, Budget, Objectives, Summary, Impact, Partners) — status per felt: ready / need input / need consortium
   - Background section (NCP-kontakt, tidligere EU-erfaring)
   - EU project proposal info (title, role, call ID, deadline, application type, budget, African/Ukraine deltakelse)
   - PES-application-specific info (other Norwegian actors)
   - Horizon Europe Project Outline (one-pager attachment) — provisional content utarbeidet for alle seks felter
4. **Krav fra de-minimis-erklæringen** (per T95 `2024-01-01_rcn_declaration_form_de_minimis_aid.md`):
   - Kompiler liste over de-minimis-støtte 2024-2026
   - Sjekk «linked enterprises» per Art. 2(2) i Kommisjonsforordning (EU) 2023/2831
   - Ceiling EUR 300 000
   - Preliminær sjekk av Sunlit Seas de-minimis-eksponering (Enova, IN, Skattefunn, Horizon)
5. **Timing:** EU-deadline september 2026 (verifiser eksakt dato), PES-søknad så tidlig som mulig etter at call er publisert, ~2-4 person-uker søknadsskriving.
6. **Åpne punkter som krever input:** 9 items — call ID (Balram), deadline (Balram), koordinator-bekreftelse (Balram), SINTEF PES-arrangement (Balram), NCP-kontakt (Eirik), de-minimis-liste (Orkla Regnskap AS), linked enterprises-sjekk (regnskapsfører + legal), sekundær-objektiv (Eirik), PES-rates 2026 (RCN).
7. **Anbefalte neste steg:** 5 punkter — ett email til Balram, ett email til regnskapsfører, draft one-pager, verifiser My RCN Web-tilgang, send inn 2-4 uker før proposal-writing starter.

**Files touched:** `background/eic/2026-08-11_pes_requirements_review.md` (ny).

**Neste steg (Eiriks side, utenfor T97):** Send de to email-forespørslene identifisert i notatets seksjon 7 (Balram + regnskapsfører). Verifiser call ID / deadline på EU Funding & Tenders portal parallelt. Fyll ut PES-søknaden i My RCN Web når fakta er bekreftet.

---

### T98 `[x]` [FUND] Lag søknadsmal (utkast med feltinnhold) for PES-søknad ES765081 EIC_SUREWAVE_DEMO

Eirik har startet PES-søknad ES765081 med kortnavn EIC_SUREWAVE_DEMO på RCNs nettside (PESORDNING, Coordination and Support Activity), og copy-pastet websidenes innhold til `background/new/pes_web_application_copy_paste.txt`. Fila viser sidestrukturen, feltnavn, tegn-grenser, og noen felter som allerede har defaulttekst (fra en tidligere søknad; skal overskrives). Task: lage én sammenhengende søknadsmal (utkast) som strukturerer alle 6 sidene av søknaden med provisorisk innhold Sunlit Sea kan copy-paste inn i web-skjemaet.

Grunnlag:

- `background/new/pes_web_application_copy_paste.txt` — websidenes struktur, feltnavn, tegn-grenser, guidelines-hint
- `background/eic/2026-08-10_rcn_pes_project_description_template.md` — RCN PES-mal (hva som skal med i attachment)
- `background/eic/2024-01-01_rcn_declaration_form_de_minimis_aid.md` — de minimis-erklæring (N/A for oss)
- `background/eic/2026-08-11_pes_requirements_review.md` — vår gjennomgang av kravene med provisorisk innhold
- `background/eic/2026-07-31_MOM_EIC_SUREWAVE.txt` — konsortie-MoM
- `background/eic/2026-08-10_contributing_tasks_wp_documents.md` — WP-struktur med partner-leads
- `background/eic/2026-08-07_eic_transition_sunlit_sea_wp_forslag.md`, `..._eic_diff_sintef_vs_sunlitsea.md`, `..._eic_feedback_to_sintef.md` — Sunlit Seas EIC-innsats

**Deliverable:** `background/eic/2026-08-11_pes_soknadsutkast_eic_surewave_demo.md` — én selvstendig fil som følger web-skjemaets 6-sidestruktur og for hvert felt gir (a) feltnavn og tegn-grense fra RCN, (b) korte RCN-guidelines-notater, (c) provisorisk Sunlit Sea-innhold som utkast, (d) merking av felter som trenger konsortie-bekreftelse (call ID, deadline osv.).

**Solution (2026-08-11):**

`background/eic/2026-08-11_pes_soknadsutkast_eic_surewave_demo.md` skrevet — én sammenhengende fil som følger web-skjemaets 6-sidestruktur. For hvert felt: navn + tegn-grense, RCN guidelines-hint, provisorisk utkast fra Sunlit Sea med tegn-telling under maks, `[verify]`-flagg der konsortie- eller RCN-bekreftelse trengs.

Innhold per side:

- **Overall setup:** application type 207, programme PESORDNING, English, kortnavn EIC_SUREWAVE_DEMO
- **Page 1 Project partners:** Sunlit Sea som prosjektansvarlig (org.nr. 922 633 924, Eirik Larsen kontakt); SINTEF-status flagget som [verify] (framework grant vs joint PES)
- **Page 2 Project info:** tittel (91 chars av 140), primary/secondary objectives (~750 av 1000), project summary (~1300 av 2000), outcomes/impacts (~700 av 1000)
- **Page 3 Funding scheme:** topic flagget som [verify] fra call-tekst, discipline satt til Solar energy, other relevant programmes fylt inn (SUREWAVE grant 101083342 + SuRE); Yes til relaterte prosjekter
- **Page 4 Progress plan:** PES-periode 2026-08-15 til 2026-10-15 (~1 mnd forbi EU-deadline for wrap-up), 6 milepæler alle i Q3 2026, dissemination-felt fylt med kort forklaring om at det ikke er aktuelt for PES
- **Page 5 Budget:** 4 tabeller (costs per partner, cost plan, cost code, funding plan) — alle med Sunlit Sea som eneste raden og all PES-støtten på payroll-linjen; 2 Specification-felter med draft-tekst som eksplisitt overskriver defaulttekstene fra tidligere søknad (Havlabben NTNU-referansen og aksjekapital-tekstene er ikke relevante for PES); note om at PES er 100 % finansiert; de-minimis-status N/A
- **Page 6 Attachments:** to obligatoriske (project description via RCN PES-mal + Eirik CV via RCN CV-mal), tre optional-slots ikke aktuelt

Slutter med to seksjoner: (a) 7 items som må bekreftes før innsending (call ID, deadline, koordinator, SINTEF PES, PES-rate 2026, Letter of Intent, defaulttekst-overskriving), (b) 2 attachments å forberede separat (project description PDF + CV).

**Files touched:** `background/eic/2026-08-11_pes_soknadsutkast_eic_surewave_demo.md` (ny).

**Neste steg (Eiriks side, utenfor T98):** Bekreft de 7 [verify]-punktene (bl.a. via email til Balram). Skriv Project description PDF fra RCN PES-malen med innhold fra søknadsutkastet. Copy-paste feltinnholdet inn i My RCN Web. Husk å overskrive defaulttekstene i de to Specification-feltene (budget + funding plan) — teksten som ligger der nå er fra en tidligere annen søknad.

---

### T99 `[x]` [FUND] Skriv PES-vedlegg for ES765081 EIC_SUREWAVE_DEMO

Fra T98s Page 6-beskrivelse: to obligatoriske vedlegg (Project description + CV Eirik) og potensielt et de-minimis-vedlegg (kun hvis RCN ber om det). Alle utkast skrives som Markdown; PDF-eksport gjøres av Eirik i Word/Google Docs når innholdet er verifisert.

**Solution (2026-08-11):**

Tre vedlegg-utkast skrevet:

- `background/eic/2026-08-11_pes_attachment_project_description.md` — obligatorisk Project description. Følger RCN PES-mal-strukturen (Background → EU project proposal info → PES application info → one-pager Project Outline → Impact of PES). Alle bekreftede tall inn (call ID HORIZON-EIC-2026-TRANSITIONOPEN, deadline 2026-09-16, €2,5M totalbudsjett, 5-partner konsortium). Sunlit Seas leder-tasks per WP-struktur (T2.1, T2.3, T4.1, T5.2, T5.5, T7.2, T8.4) listet konkret.
- `background/eic/2026-08-11_pes_attachment_cv_eirik_larsen.md` — obligatorisk CV. Følger typisk RCN CV-mal-struktur (personal info → current role → education → employment → research project roles → skills → publications → additional). Fylt inn med det som er kjent fra repo-konteksten (Sunlit Sea CFO fra 2026-01, seconded fra KodeWorks, rolle i SUREWAVE/SuRE/Enova/Skattefunn); `_[fill in]_`-plassholdere for personlige data (fødselsdato, adresse, utdanning, tidligere arbeidsgivere, publikasjoner).
- `background/eic/2026-08-11_pes_attachment_declaration_de_minimis.md` — optional (kun hvis RCN ber om det). Fylt inn med N/A per Sunlit Seas de-minimis-status (0 kr mottatt siste 3 år). Andre offentlige støtteordninger (Horizon, Skattefunn, Enova, IN) klassifisert som utenfor de-minimis-regimet. Signaturplaceholder for Eirik.

**Files touched:**
- `background/eic/2026-08-11_pes_attachment_project_description.md` (ny)
- `background/eic/2026-08-11_pes_attachment_cv_eirik_larsen.md` (ny)
- `background/eic/2026-08-11_pes_attachment_declaration_de_minimis.md` (ny)

**Neste steg (Eiriks side, utenfor T99):**

1. Fyll ut CV-plassholderne (fødselsdato, adresse, utdanning, arbeidshistorikk, publikasjoner). Last ned RCNs offisielle CV-mal og overfør innholdet inn i den — RCN krever eksakt mal-format.
2. Verifiser Project description-innholdet mot din siste dialog med Balram (koordinator-status, SINTEF PES-arrangement, at Innovation Action-klassifiseringen stemmer for EIC Transition Open 2026).
3. Vurder om «Confirmation from partner(s)»-slot krever Letter of Intent — sjekk call-teksten på EU-portalen. Hvis ja: be Balram om LoI fra SINTEF som koordinator.
4. Eksporter alle vedlegg til PDF via Microsoft Print to PDF (per RCN-instruks om å unngå passordbeskyttelse og elektroniske signaturer i PDF).
5. Last opp i My RCN Web.
6. Behold de-minimis-erklæringen klar — last kun opp hvis RCN eksplisitt ber om den (per call-tekst eller under behandling).

