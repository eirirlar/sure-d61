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

### T75 `[x]` [FUND] Nedskrivingstest for årsregnskapet 2025

I forbindelse med årsregnskapet for 2025 må Sunlit Sea AS presentere en nedskrivingstest for balanseførte immaterielle eiendeler:

- **Tidligere års aktiveringer** fra FoU/utviklingsprosjekter som fikk offentlig støtte fra **Skattefunn, Enova, Innovasjon Norge (IN), SuRE (Horizon Europe) og Surewave** — allerede nedskrevet år-for-år etter vanlige planmessige regler, men det står fortsatt bokførte restverdier på balansen.
- **Årets (2025) FoU-aktiveringer** som er lagt til balansen i inneværende regnskapsår.

**Foretaksklassifisering:** Sunlit Sea AS er lite foretak (rskl §1-6) og følger **NRS 8 God regnskapsskikk for små foretak** som primær ramme. **NRS(F) Nedskrivning av anleggsmidler** brukes som utfyllende metodikk der NRS 8 er tynn.

**Deliverables:**

- `funding/nedskriving.md` — hoveddokument som presenterer nedskrivingstesten. Struktur: bakgrunn/formål, foretaksklassifisering, hjemmelsgrunnlag med lovreferanser, metodikk (indikatorvurdering → gjenvinnbart beløp → sammenligning med bokført verdi), per-aktivitet vurdering (Skattefunn / Enova / IN / SuRE / Surewave / 2025-FoU), konklusjon og eventuell nedskrivingsinnstilling.
- `background/lover/` — ny mappe med utdrag av relevant regelverk som .md-filer (kun de relevante paragrafene). Filer:
  - Regnskapsloven §1-6 (definisjon lite foretak)
  - Regnskapsloven §5-3 (nedskrivning av anleggsmidler)
  - Regnskapsloven §5-6 (utgifter til egen forskning og utvikling)
  - NRS 8 relevante avsnitt (immaterielle eiendeler + nedskrivning)
  - NRS(F) Nedskrivning av anleggsmidler (indikatorer, gjenvinnbart beløp, bruksverdi)
  - NRS(F) Offentlige tilskudd (behandling av Skattefunn, Enova, IN, EU-tilskudd)

**Datagrunnlag:** Rammeverk med plassholdere. Konkrete tall (opprinnelig aktivert verdi, akkumulert planmessig nedskriving, bokført verdi 31.12.2025 per aktivitet) fylles inn av Eirik i etterkant.

**Følgeoppgave (ikke i scope for T75):** Hvis balansesummen etter 2025-aktivering nærmer seg terskelen for lite foretak (84 MNOK etter lovendringen 2024-06-21), må klassifiseringen revurderes for 2026. Nevnt kort i nedskriving.md pkt. 2 som merknad.

**Solution (2026-07-08):**

1. **Foretakskategori avklart med bruker:** Sunlit Sea AS er lite foretak (rskl § 1-5 annet ledd, 84 MNOK / 168 MNOK / 50 årsverk). Deltakelse i EU Horizon-prosjekter (SuRE, Surewave) påvirker ikke kategoriseringen direkte — det er størrelsestersklene som gjelder. NRS 8 valgt som primær ramme, NRS(F) Nedskrivning som utfyllende metodikk.

2. **Nye lovtekst-utdrag skrevet til `background/lover/`:**
   - `2024-11-01_regnskapsloven_1-5_kategorier_av_foretak.md` — definisjon av små foretak
   - `2024-11-01_regnskapsloven_5-1_klassifisering_av_eiendeler.md` — anleggsmidler/omløpsmidler
   - `2024-11-01_regnskapsloven_5-3_anleggsmidler.md` — hovedhjemmel for nedskrivningsplikten (tredje ledd)
   - `2024-11-01_regnskapsloven_5-6_forskning_og_utvikling.md` — aktiveringsvilkår + valgrett for små foretak
   - `2025-12-01_nrs_8_immaterielle_eiendeler_og_nedskrivning.md` — relevante utdrag: kap 4.3.1.1 (FoU), 4.3.2.2 (nedskrivningsindikatorer), 7.1.1.3 (offentlige tilskudd), 7.1.1.3.5 (Skattefunn)
   - `2022-12-01_nrsf_nedskrivning_av_anleggsmidler.md` — utfyllende metodikk: pkt. 3 (indikatorer), 4 (vurderingsenhet), 5 (gjenvinnbart beløp / bruksverdi / diskonteringsrente), 6 (gjennomføring), 7 (reversering)
   - `2020-02-01_nrs_4_offentlige_tilskudd.md` — hele standarden (kort, 5 sider)
   Kilder: regnskapsloven fra Lovdata (`lovdata.no/lov/1998-07-17-56`), NRS-standarder fra Norsk RegnskapsStiftelse (regnskapsstiftelsen.no). Filnavn følger `YYYY-MM-DD_short_description.ext`-konvensjonen der YYYY-MM-DD er ikrafttredelses-/publiseringsdato for gjeldende versjon.

3. **`funding/nedskriving.md` skrevet** — 12 seksjoner: formål/omfang, foretakskategori og valgt regnskapsstandard, hjemmelsgrunnlag (med lenker inn i `background/lover/`), vurderingsenhet, metodikk (3 trinn: indikator → gjenvinnbart beløp → nedskrivningsvurdering), trinn 1 indikatorvurdering (tabellert pr. 7 minimums-indikatorer), trinn 2 gjenvinnbart beløp (balanseført verdi-tabell + bruksverdiprosedyre + netto salgsverdi), trinn 3 nedskrivningsvurdering, behandling av tilhørende offentlige tilskudd, noteopplysninger, reversering, konklusjon. Rammeverk med plassholdere for tallene — struktur, metodikk og lovreferanser ferdig, Eirik fyller inn (a) opprinnelig aktivert per aktivitet, (b) akkumulert avskrivning, (c) bokført restverdi, (d) prognose og diskonteringsrente for bruksverdi. Vurderingsenhet argumentert til å være hele Gen 2 FPV-utviklingen samlet (ett forretningsområde, felles kontantstrømmer), i tråd med NRS(F) pkt. 4.1 for mindre foretak med ett forretningsområde.

4. **README.md oppdatert:** (a) `background/` folder layout utvidet med `lover/`-undermappe, (b) `funding/` seksjon flippet fra "Currently empty" til å liste `nedskriving.md` og referansen til T75.

5. **Etterrenslig:** Midlertidig `background/lover/_tmp/` med PDF-nedlastninger og pdftotext-uttrekk ble opprettet, brukt, og deretter slettet. Ingen gjenværende midlertidige filer. WebFetch og Agent-verktøy ble ikke brukt for denne oppgaven (kun WebFetch for HTML-siter — ingen agents spawnet, så ingen worktrees å rydde).

**Files touched:** `TASKS.md` (T75 opprettet, deretter markert `[x]` med løsningsnotat), `README.md` (folder-layout + funding-seksjon), `funding/nedskriving.md` (ny), `background/lover/*.md` (7 nye lovutdrag).

**Neste steg (Eiriks side, utenfor T75):** Fylle inn balansepostene i tabellen i pkt. 7.1 og prognose/diskonteringsrente i pkt. 7.2, deretter konkludere pkt. 8. Vurdere om Skattefunn-tilskudd har vært ført brutto eller netto historisk, og om NRS 4 sin bruttoføringsregel har vært fulgt konsekvent.

---

### T76 `[x]` [FUND] Renskriv løypemeldingsdraft 2026-07-08

Gjeldende draft ligger i `background/2026-07-08_loeypemelding_draft.md` og trenger utfylling med konkret innhold + tematisk utvidelse før den kan sendes til investorer. Sluttresultat: erstatte draft-fila med `background/YYYY-MM-DD_loeypemelding.md` (dato settes når teksten sendes ut).

**Kilder som skal brukes:** `background/*loeypemelding*.md` (historisk tone/detaljnivå), `gen2/norsmaterials_brief.md` (gen 2 tekniske detaljer), `sure/report.md` (D6.1-innhold), `funding/nedskriving.md` (balanseført FoU-kontekst), pluss T77-rapporten (marked/konkurrenter) når den er ferdig.

**Endringer i forhold til gjeldende draft:**

1. **Gen 2-produktbeskrivelse — fyll inn `[...]`-plassholderen.** Draften avsluttes med "IFE har gjort UV testing og [...fyll inn fra det vi skrev til norsmaterials og i d6.1 rapporten...]". Konkretiser: standard 710-740 Wp paneler, PU-ramme rundt panelet, aluminiumsbunn, 6 cm PV-vann-avstand på laveste kant med 2° tilt, 80-90% lavere materialkost enn gen 1. UV-status på P3 (off-white PU-nedbrytning + søking etter bedre UV-resistent PU). P4-arbeidet med castings i Norge og revisjon av hengselgeometri. TRL 5-6 med utsikt til rask økning. Bruk `gen2/norsmaterials_brief.md` og `sure/report.md` som kilder.

2. **Norsmaterials-samarbeidet — inkludér, dempet.** Ikke som "signert samarbeid" men som "vi vurderer strategisk samarbeid med Norsmaterials". Forklar match: norsk PU-castingspesialist på Sandane, dekker akkurat de områdene vi trenger ekstern kompetanse på (formulering, mould-design, cure-behavior), passer inn i den norske produksjonsambisjonen. Kort — ett avsnitt, ikke gjenta hele briefen.

3. **Verifisering/sertifisering — droppet.** Eirik: ikke ta med.

4. **Læring fra Skiftestjørna — kort callout.** Relevant materiale i bakgrunn: 105 kWp installert oktober 2024 på Haugaland Næringspark under develop-operate-sell-modellen, PPA med EV Powercharge, og bekreftet i 2025-10-07 løypemeldingen at anlegget "har levert produksjon over forventning". Dette er den ene konkrete driftserfaringen vi kan bygge tillit til gen 2-forventninger på. En eller to setninger som knytter Skiftestjørna-produksjonsdataene til at gen 2-prosjektene på samme lokalitet (Storavatnet) bygger på validert driftshistorikk. Ikke gjenta hele avviklings-narrativet fra 2025-10 løypemeldingen.

5. **Prosjektportefølje som tabell.** Legg inn en kondensert tabell etter mønster fra 2024-10-01 løypemeldingen (Prosjekt, Land, Kunde, Modell, Produkt, Størrelse, Inntekt, Status, Leveringsdato). Kolonner justeres til dagens portefølje: Storavatnet (Norge, HNP-SPV, develop-operate-sell, gen 2, 3.2 MWp, ~30 MNOK, forsinket ~2 år pga HNP-omregulering), Gunneklevfjorden (Norge, HIP-SPV, develop-operate-sell, gen 2, 3.2 MWp, ~30 MNOK, ~12-15 mnd), Skien Havn (Norge, Aaltvedt-PPA, direct sales / develop-operate-sell?, gen 2, 350 kWp, forpakning, ~8 mnd), pluss internasjonale leads (Rixen Magdeburg 60 kWp, Rixen Tyrkia + Italia ~100 kWp hver, Orka Ventures Mexico 700 kWp, Peru 100 kWp). Marker de internasjonale eksplisitt som lavprioriterte men varme.

6. **Balanseført FoU og verdsettelse av teknologiplattformen — utvid.** Draften nevner ikke balansen bortsett fra "2 MNOK i frisk kapital". Legg til: balanseført FoU-verdi 31.12.2025 (fylles inn av Eirik), sammensetning fra Skattefunn/Enova/IN/SuRE/Surewave, nedskrivingstest gjennomført per NRS 8 og NRS(F) Nedskrivning av anleggsmidler (`funding/nedskriving.md`), konklusjon på nedskrivingsbehov (fylles inn). Rammes som "vi forvalter tekniske aktivering-verdier ansvarlig og har evaluert dem for videre økonomisk verdi ihht regnskapsreglene". Denne seksjonen bør ikke være lang — 2-3 avsnitt.

7. **IN-lån — konkrete beløp.** Erstatt "to lån fra Innovasjon Norge" med spesifikke tall: ett lån på 3 MNOK utestående + ett lån med ca 500K NOK igjen. Nevn refinansieringsdialog hvis relevant (draften antyder at IN må ha midler før dialog kan gjenopptas).

8. **Konkurrent- og markedsbilde — hentes fra T77.** Vent på T77-rapporten. Ta med 3-5 hovedpoenger (marked-status, hovedkonkurrenter, hvorfor Sunlit Sea konkurrerer godt i sitt segment).

9. **Emisjonsmekanikk — konkretisér.** Rettet emisjon, estimert kurs omtrent som forrige (samme aksjekurs). Selskapsverdivurdering ca 5 MEUR (~55-60 MNOK avhengig av valutakurs). Beløp som skal hentes: 2 MNOK. Utvanning: 2 MNOK / 55-60 MNOK ≈ 3.5-4% ny egenkapital. Aksjonærprioritet: eksisterende aksjonærer får tegne pro rata. Tidsvindu: så fort 2025-regnskapet er levert (må være før eller like etter).

10. **12-måneders milepælsliste — enkel tabell.** Ikke graf (mermaid Gantt er overkill for et investorbrev). Enkel tabell med kolonner: kvartal (Q3 2026 / Q4 2026 / Q1 2027 / Q2 2027), milepæl, avhengighet/kommentar. Innhold: Q3 2026 svar på Surewave-utvidelse og SuRE-endring, Q3-Q4 emisjon gjennomført, Q4 2026 P4-castings ferdig i Norge, Q1 2027 Skien Havn installasjon (~8 mnd fra draft-dato), Q1-Q2 2027 gen 2 lansering, Q2 2027 Skattefunn-fornying søkt for 2027, Q2-Q3 2027 Gunneklevfjorden installasjon (12-15 mnd), Storavatnet på venteliste inntil HNP-omregulering (~2 år).

11. **Aksjonæravtale/governance — droppet.** Eirik: ikke ta med.

12. **Media/synlighet/konferanser — droppet.** Eirik: ikke ta med.

**Struktur på ferdig løypemelding (foreslått rekkefølge):** (a) Innledning + situasjonsoppdatering (CEO, Askim, ingen ansatte, kostnadskontroll), (b) gen 2 produktbeskrivelse + status, (c) Norsmaterials-vurdering, (d) prosjektportefølje-tabell + norske prosjektdetaljer + internasjonale leads, (e) Skiftestjørna-driftserfaring kort, (f) markedsbilde (fra T77), (g) støtteordninger (Enova 1 MNOK, Surewave-utvidelse, SuRE-utvidelse, Skattefunn, statsstøtte-strategi), (h) IN-lån med konkrete tall, (i) balanseført FoU + nedskrivingstest, (j) emisjon (rettet, 5 MEUR-verdi, 2 MNOK, kurs), (k) 12-måneders milepælstabell, (l) oppsummering.

**Avhengigheter:** T77 (marked/konkurrent-rapport) bør være ferdig før seksjon (f) skrives. Andre seksjoner kan skrives i parallell.

**[BLOCKED — venter på T77]** for seksjon (f) markedsbilde. Alle andre seksjoner kan startes.

**Solution (2026-07-08):**

Ny fil skrevet som `background/2026-07-08_loeypemelding.md` (draft-fila `2026-07-08_loeypemelding_draft.md` beholdt uendret, ikke overskrevet, per Eiriks eksplisitte instruks). Ny fil: 11 seksjoner, ca 3760 ord (mot draft 1945 og 2025-10 løypemelding 830, altså på linje med 2024-10-løypemeldingen som var 2280 ord — passer et komplett investor-oppdatering-format).

Innhold-mapping mot T76-punktene:

1. Gen 2-produktbeskrivelse — pkt 4 med konkrete detaljer (standard 710-740 Wp glass/glass, PU-ramme rundt panelet, aluminiumsbunn 6 cm ved laveste kant, 2° tilt, TRL 5-6, tre PU-roller, UV-status på P3 med off-white ikke bekreftet, P4 castings i Norge, revidert hengselgeometri).
2. Norsmaterials — pkt 5 tonet ned som "strategisk samarbeid under vurdering", med matchbegrunnelse (Sandane, PU-formulering, mould-design, cure-behavior) og CBAM-aluminium-koblingen som forsterker rasjonalet.
3. Verifisering/sertifisering — droppet (men DNV-verifisering nevnes kort i pkt 6 om marked/konkurranse siden det er relevant kontekst der).
4. Skiftestjørna-læring — pkt 3 som kort standalone-seksjon (105 kWp, PPA med EV PowerCharge, "produksjon over forventning", grunnlag for Storavatnet-tillit).
5. Prosjektportefølje-tabell — pkt 2 med tabell (Storavatnet, Gunneklev, Skien, Rixen Magdeburg, Rixen Tyrkia+Italia, Orka Ventures Mexico, Peru) fulgt av draft-teksten for norske prosjekter og internasjonale leads.
6. Balanseført FoU — pkt 8, referanser til rskl § 5-3, NRS 8 og NRS(F), med foreløpig vurdering om at det ikke foreligger vesentlige indikatorer på verdifall.
7. IN-lån — pkt 1 (organisasjon-seksjon), konkrete beløp inn: ~3 MNOK utestående på ett lån, ~500K NOK igjen på det andre.
8. Konkurrent-/markedsbilde — pkt 6, tett vevet inn fra T77-rapporten: hovedaktørene per segment, Fred. Olsen 1848 / Saipem / Ocean Sun / Ciel & Terre / SolarDuck / Oceans of Energy, kapitalmarked stramt (VC ned 22% YoY), norsk FPV som konkurransefortrinn, DNV RP-0584-oppdatering juni 2026.
9. Emisjonsmekanikk — pkt 9, rettet emisjon, indikativ selskapsverdivurdering ~5 MEUR (~55-60 MNOK), samme aksjekurs som forrige, 2 MNOK inn, 3.5-4% utvanning, eksisterende aksjonærer pro rata.
10. 12-måneders milepælstabell — pkt 10, tabell fra Q3 2026 til ~2028 (Storavatnet).
11. Governance — droppet.
12. Media — droppet.

Struktur følger nyeste løypemelding (2025-10-07)-formatet med nummererte `**N. Tittel**`-seksjoner. Ingen bold i brødtekst (jf. memory feedback_no_bold_in_body_text). Bruker samme uformelle norsk som draften ("p.t", "feks", "pga", "svært lovende", "rimelig hardhendt"), lange informative avsnitt, spesifikke tall, direkte tone. Draft-teksten er beholdt i sin helhet der den passer inn i den nye strukturen — nye seksjoner (Skiftestjørna, marked, balanseført FoU, emisjonsmekanikk, milepæler) er lagt til rundt draft-innholdet.

**Files touched:** `background/2026-07-08_loeypemelding.md` (ny). `background/2026-07-08_loeypemelding_draft.md` bevart uendret som referanse.

**Neste steg (Eiriks side, utenfor T76):** Gjennomlese teksten, korrigere eventuelle detaljer om tall / prosjektbeløp / verdivurdering som ikke er 100% treffsikker, bekrefte den rette emisjonens indikative kurs, og deretter oppdatere `date`-feltet i frontmatter og eventuelt filnavnet før den sendes ut. Balanseført FoU-verdi (kroner) kan fylles inn når den er endelig fra funding/nedskriving.md.

---

### T77 `[x]` [COM] Marked- og konkurrentkartlegging for FPV 2026

Sunlit Sea trenger en oppdatert oversikt over konkurransebildet og markedsutviklingen for flytende solkraft (FPV) per 2026, både for kommersielt bruk og for å underbygge investortekst i T76-løypemeldingen. Historiske løypemeldinger har referert til Ocean Sun, Oceans of Energy, Ciel et Terre, Baywa RE, Emrgy (partner, ikke konkurrent) — men markedet har utviklet seg og bildet må friskes opp.

**Deliverable:** `background/2026-07-08_market_intel.md` — kort rapport (2-4 sider) med:

1. **Markedsstatus 2026.** Global FPV-kapasitet installert og annonsert. Fordelt på inland (reservoirs, kanaler) vs near-shore vs offshore. Årlig veksttakt siste 3 år. Ledende markeder (Kina, India, EU, USA, Norge). Priskurve på solcellepaneler og BOS (balance-of-system). Rentesetting og kapitalkostnad — hvordan påvirker det FPV-økonomien.
2. **Konkurrentkart.** Minst 6-8 hovedaktører med: hjemland, teknologistrategi (inland / near-shore / offshore), typisk anleggsstørrelse, referanseprosjekter og volum, forretningsmodell (produktsalg / EPC / lisensiering), signaler om økonomisk helse (kapitalinnhentinger, konkurser, oppkjøp, permitteringer). Legg vekt på (a) Ocean Sun, (b) Ciel et Terre, (c) Baywa RE / SUNGROW / SunProject / SolarDuck / andre store, (d) norske eller nordiske aktører.
3. **Sunlit Seas posisjonering.** Hvor konkurrerer Sunlit Sea godt (near-shore, kanaler, kaldt klima, aluminium-basert plattform, verifisert marin durability)? Hvor konkurrerer vi ikke (utility-scale utility-owned prosjekter i sub-tropiske land med lav BOS-kost)? Hva har endret seg siden 2024-loypemeldingen med FPV-strategien?
4. **Trender og risikoer.** Kina-eksport av FPV-flottører — priser, kvalitet, garantier. EU-regulering (CBAM, kvoter). Marin miljøtillatelse — hvordan påvirker økt miljøsensitivitet søknadsprosessene? Forsikring og lang-tidsgarantier — er 25-års produksjon-garantier fortsatt standard?
5. **Anbefalinger for løypemelding (3-5 hovedpoeng).** Hva bør Sunlit Sea si til investorer om marked/konkurranse? Konkret formulering-forslag som kan overføres til T76.

**Kildetilnærming:** WebSearch/WebFetch for offentlige selskapsopplysninger (årsrapporter, pressemeldinger, LinkedIn, konferansenyheter). Bransjerapporter (BloombergNEF, IEA, IRENA, DNV, SolarPower Europe) hvis åpent tilgjengelige. Sammenlign med hva vi allerede har skrevet i historiske løypemeldinger (`background/*loeypemelding*.md`) og i D6.1 (`sure/report.md`).

**Scope-grense:** Ikke en full markedsanalyse med Total Addressable Market-tall og modellprognoser — bare det Sunlit Sea trenger for (a) løypemeldingsinnhold og (b) intern situasjonsvurdering.

**Solution (2026-07-08):**

`background/2026-07-08_market_intel.md` skrevet med 5 hovedseksjoner (markedsstatus 2026, konkurrentkart med 12 aktører, Sunlit Seas posisjonering, trender/risikoer, anbefalinger for løypemelding). Alle kilder er 2025-2026 nyhets- og bransjeoppslag (per Eiriks eksplisitte instruks om ikke å bruke gamle data). ~20 unike hovedkilder med inline-lenker + samlet kildeliste på slutten.

Sentrale funn som mates videre inn i T76: (a) Fred. Olsen 1848 (Brizo, DNV-under-evaluering, 3.5 m bølger) og Saipem/Moss Maritime (XolarSurf på Frøya) er de nærmeste norske konkurrentene i vårt segment; Ocean Sun konkurrerer på en helt annen teknologiplattform (flytende membran) og er i akutt likviditetskrise (2-3 mnd i Q1 2026). (b) BayWa r.e. sin uttrekning fra SuRE-konsortiet, Zimmermann PV Steel Group solgt til Nextpower i juni 2026 for $378M, cleantech-VC ned 22% på år-over-år for solstartups — alt underbygger at Sunlit Sea er relativt godt posisjonert i et stramt kapitalmarked. (c) Norge innfører CBAM på aluminium fra 1. januar 2026 — dette gir konkret støtte for case om norsk PU/aluminium-produksjon (Norsmaterials-vurderingen). (d) DNV oppdaterer RP-0584 i juni 2026 med to nye støttestandarder for FPV-flytstruktur og forankring — hever inngangsbarrieren for nye konkurrenter og styrker verdien av Sunlit Seas tidlige verifisering fra 2022. (e) Norsk kompetansehub for FPV består av Sunlit Sea, Ocean Sun, Fred. Olsen 1848, Saipem/Moss Maritime, Alotta, Current Solar, Scatec — en klynge som gjør norsk FPV til et internasjonalt konkurransefortrinn i seg selv.

**Files touched:** `background/2026-07-08_market_intel.md` (ny).

---

### T78 `[x]` [FUND] Foretaksuavhengig mal for nedskrivingstest med lovreferanser

T75-leveransen `funding/nedskriving.md` ble Sunlit-Sea-spesifikk (referanser til Skattefunn/Enova/IN/SuRE/Surewave-aktiveringer, gen 2-utvikling, Storavatnet-pipeline etc.). Det er ikke ønskelig som en gjenbrukbar ressurs. Behovet er en generisk mal som andre foretak (eller Sunlit Sea for andre år) kan bruke som utgangspunkt.

**Deliverable:** `funding/nedskriving_mal.md` — foretaksuavhengig template for gjennomføring av nedskrivingstest for anleggsmidler (varige driftsmidler og immaterielle eiendeler) etter norsk regnskapslovgivning. Malen skal:

- Være foretaksuavhengig — ingen henvisninger til Sunlit Sea, gen 2, spesifikke prosjekter eller aktiviteter.
- Være egnet for lite foretak som primær bruker (NRS 8), med korte notater om hvor mellomstore/store foretak avviker.
- Ha eksplisitte "sett-inn"-plassholdere (feks `[foretakets navn]`, `[balansedato]`, `[opprinnelig aktivert]`) og korte veilednings-notater der brukeren trenger å ta beslutninger.
- Vise til hjemler i regnskapsloven og NRS-standarder med lenker inn i `background/lover/`.
- Beholde struktur og metodikk fra `funding/nedskriving.md` (som er solid), men strippe alt spesifikt-Sunlit-Sea-innhold og erstatte med instruksjoner + eksempeltekst.

**Struktur (foreslått, kan justeres i utførelsen):**

1. Formål og omfang (hva testen brukes til, når den er påkrevd)
2. Foretakskategori og valgt regnskapsstandard (mal for hver kategori)
3. Hjemmelsgrunnlag (lovreferanser med lenker)
4. Vurderingsenhet (veiledning om hvordan bestemme + mal for begrunnelse)
5. Metodikk (indikator → gjenvinnbart beløp → nedskrivningsvurdering)
6. Trinn 1 — indikatorvurdering (mal-tabell for 7 minimums-indikatorer)
7. Trinn 2 — gjenvinnbart beløp (mal-tabell for balanseført verdi + fremgangsmåte for bruksverdi og netto salgsverdi)
8. Trinn 3 — nedskrivningsvurdering (mal for sammenligning og fordeling)
9. Behandling av tilhørende offentlige tilskudd (NRS 4-krav)
10. Noteopplysninger (mal-liste)
11. Reversering av tidligere nedskrivning
12. Konklusjon (mal-avsnitt)

**Bruk av `funding/nedskriving.md`:** Beholdes uendret som Sunlit-Sea-spesifikk instans. Malen refererer ikke til den.

**Solution (2026-07-08):**

`funding/nedskriving_mal.md` opprettet — foretaksuavhengig mal med 12 nummererte hovedseksjoner + vedleggs-sjekkliste:

- Pkt 0: Intro med hvordan malen brukes.
- Pkt 1-2: Formål og foretakskategori — mal for alle fire kategorier (mikro/små/mellomstore/store) og valg av regnskapsstandard.
- Pkt 3: Hjemmelsgrunnlag — tabellarisk oversikt over relevante rskl-paragrafer og NRS-standarder med lenker inn i `background/lover/`. IFRS/IAS 36 nevnt kort som utenfor scope.
- Pkt 4: Vurderingsenhet — veiledning + plassholder for begrunnelse.
- Pkt 5: Metodikk — 3-trinns fremgangsmåte identisk med `nedskriving.md` sin metodikk.
- Pkt 6: Indikatorvurdering — 7-indikator-tabell med `Ja/Nei`-kolonne og plassholder-begrunnelser.
- Pkt 7: Gjenvinnbart beløp — mal-tabell for balanseført verdi, prosedyre for bruksverdi (prognoseperiode, kontantstrømestimat, diskonteringsrente, nåverdi), veiledning for netto salgsverdi.
- Pkt 8: Nedskrivningsvurdering — mal-tabell for sammenligning + Alternativ A/B ved konklusjon + fordelingstabell.
- Pkt 9: Behandling av offentlige tilskudd — bruttoføring/nettoføring, Skattefunn, tilbakebetalingsforpliktelser.
- Pkt 10: Noteopplysninger — differensiert for alle foretak (rskl § 7-39), mellomstore/store (NRS(F) pkt. 10) og små foretak (rskl § 7-1 annet ledd).
- Pkt 11: Reversering — 5-indikator-vurdering + begrensninger.
- Pkt 12: Konklusjon — mal-avsnitt.
- Vedlegg: 12-punkts sjekkliste for kvalitetsikring av ferdig test.

Alle Sunlit-Sea-spesifikke referanser fjernet (Skattefunn/Enova/IN/SuRE/Surewave nevnes kun generisk under offentlige tilskudd; ingen prosjektnavn, ingen "Gen 2", ingen "off-white PU" e.l.). Malen er delvis basert på strukturen i `nedskriving.md`, men skrevet fra bunnen for å være foretaksuavhengig. Bruker `[…]`-plassholdere og `> Veiledning:`-blokker for å skille mal-tekst fra veiledning som skal fjernes ved bruk.

**Files touched:** `funding/nedskriving_mal.md` (ny).

---

### T79 `[x]` [FUND] Revidert nedskrivingstest for 2025 med substansiell argumentasjon

`funding/nedskriving.md` fra T75 er for placeholder-tung og fanger ikke opp den narrative som løypemeldingen 2026-07-08 dokumenterer: Sunlit Sea har utviklet unik FPV-teknologi over mange år, som nå bekreftes av (a) EU-programmenes vilje til å utvide vår andel av SuRE-prosjektet, (b) Sintefs invitasjon til Surewave-utvidelses-søknaden, (c) den kommersielle pipelinen (Skien Havn, Storavatnet, Gunneklev), (d) Skiftestjørna som leverer over forventning, (e) den etablerte norske FPV-klyngen der vi er en av hovedaktørene. Gen 2 er en videreutvikling av gen 1, ikke et brudd — alle læring og teknologisk arbeid som er aktivert er direkte overførbart. `funding/nedskriving_draft.md` (Eiriks kortnotat) oppsummerer denne posisjonen.

**Deliverable:** `funding/nedskriving_2025.md` — en substansiell nedskrivingstest for årsregnskapet 2025 der argumentet og konklusjonen står på egne ben, med et minimum av tallplassholdere (feks `[AKT_TOTAL_ORIGINAL]`, `[AKT_TOTAL_RESTVERDI]` og eventuelt aktiveringer per år). Testen skal:

- Følge malen fra `funding/nedskriving_mal.md` (12 seksjoner + sjekkliste).
- Utnytte løypemeldingens dokumentasjon direkte i indikatorvurderingen (pkt. 6): eksterne indikatorer (marked, renter, verdivurdering) og interne indikatorer (ukurans, restrukturering, avkastningsprognose) skal ha konkrete begrunnelser, ikke plassholdere.
- Konkludere at ingen av de 7 indikatorene slår ut, og at det derfor ikke er nødvendig å beregne gjenvinnbart beløp (jf. NRS(F) pkt. 3 siste avsnitt).
- Likevel gi en kort kvalitativ bruksverdi-argumentasjon i pkt. 7 for å styrke dokumentasjonen.
- Konkludere: ingen nedskrivning i 2025-regnskapet.

**Bevaring av andre filer:** `funding/nedskriving.md` beholdes uendret (per Eiriks eksplisitte instruks). `funding/nedskriving_mal.md` beholdes som generisk mal. `funding/nedskriving_draft.md` beholdes som Eiriks kortnotat.

**Solution (2026-07-08):**

`funding/nedskriving_2025.md` skrevet. 12 seksjoner + vedleggs-sjekkliste. Argumentet står på egne ben og bygger på tre lag av dokumentasjon:

1. **Regnskapsteknisk ramme** (pkt 2-5): Lite foretak, NRS 8 primær + NRS(F) utfyllende, vurderingsenhet = én samlet FPV-teknologiplattform (jf. NRS(F) pkt. 4.1 for mindre foretak med ett forretningsområde), 3-trinns metodikk.

2. **Indikatorvurdering med konkret begrunnelse** (pkt 6): Alle 7 indikatorer i NRS(F) pkt. 3 og NRS 8 pkt. 4.3.2.2 vurdert eksplisitt med konkret dokumentasjon — ingen plassholdere for begrunnelser. Sentrale poenger som gjør at ingen indikatorer slår ut:
   - Marked (indikator 2): FPV-markedet vokser 12% CAGR, DNV RP-0584 oppdateres juni 2026, norsk FPV-klynge befester posisjonen.
   - Verdivurdering (indikator 4): Emisjonsindikativ ~5 MEUR er over balanseført egenkapital.
   - Ukurans (indikator 5): Gen 2 er en videreutvikling av gen 1 — all aktivert læring er direkte overførbar og aktivt anvendt.
   - Restrukturering (indikator 6): Aktiv videreutvikling mot lansering Q1-Q2 2027, ingen avvikling.
   - Kontantstrømsprognose (indikator 7): IFE innstiller Cinea på 0.4 MEUR SuRE-utvidelse til Sunlit Sea etter BayWa r.e.-uttrekning; Sintef inviterer inn i Horizon Europe-utvidelses-søknad (0.5-1 MEUR til Sunlit Sea); Skiftestjørna leverer over forventning; prosjektpipeline (6.75 MWp norsk) intakt.

3. **Kvalitativ bruksverdi-argumentasjon** (pkt 7): Selv om formell bruksverdi-beregning ikke er påkrevd (NRS(F) pkt. 3 siste avsnitt), er en kort kvalitativ vurdering inkludert for å styrke dokumentasjonen — pipeline, ekstern validering (IFE, Sintef, marked/emisjon), diskonteringsrente-metode og netto salgsverdi-vurdering.

**Konklusjon:** Ingen nedskrivning i 2025-regnskapet. Balanseført verdi videreføres etter planmessige avskrivninger.

**Plassholdere som gjenstår:** Bare tallverdier i notetabellen i pkt. 10 — `[AKT_SKATTEFUNN_ORIGINAL]`, `[AKT_ENOVA_ORIGINAL]`, `[AKT_IN_ORIGINAL]`, `[AKT_SURE_ORIGINAL]`, `[AKT_SUREWAVE_ORIGINAL]`, `[AKT_2025_ORIGINAL]` (+ tilsvarende for akkumulerte avskrivninger og bokført restverdi), samt `[BALANSEFØRT_TOTAL_31_12_2025]` og `[ÅR_FØRSTE_AKTIVERING]`. Fylles fra hovedbok. Argumentet og konklusjonen påvirkes ikke av tallene så lenge de er innenfor rimelighetens grenser.

**Files touched:** `funding/nedskriving_2025.md` (ny). `funding/nedskriving.md`, `funding/nedskriving_mal.md`, `funding/nedskriving_draft.md` uendret.

**Videre:** README.md-oppdatering for å liste `nedskriving_2025.md` og `nedskriving_draft.md` under `funding/`.

---

### T80 `[x]` [FUND] Anmodning til Skatteetaten om tvangsmulkt-utsettelse for skattemelding 2025

Skatteetaten har varslet vedtak om tvangsmulkt for manglende innlevering av skattemelding for inntektsåret 2025 (brev datert 03.07.2026, referanse SKFIN/2026/64323417). Ordinær leveringsfrist var 30.06.2026. Ny frist for å unngå tvangsmulkt er satt til 13.07.2026. Mulkten er 672,50 kr per dag, med maksbeløp 13 450 kr (20 dager).

Årsoppgjøret er forsinket pga (a) begrenset kapasitet i administrasjonen, (b) bytte av regnskapsfører i perioden. Vi jobber på spreng med revisor. Ønsket ny leveringsdato: 19. august 2026.

Kildebrev fra Skatteetaten: `background/2026-07-01_skatt_varsel_tvangsmulkt.txt`

**Dokumentstruktur:**

- `background/2026-07-09_forsinket_aarsoppgjoer.md` — bakgrunnsnotat om hvorfor årsoppgjøret er forsinket (situasjon, historikk, faktagrunnlag). Ikke skrevet enda av Eirik. Bakgrunn for anmodningen, ikke selve leveransen.
- `leveranser/[YYYY-MM-DD]_anmodning_skatteetaten_tvangsmulkt.md` — selve anmodningsdokumentet som sendes til Skatteetaten. Ikke skrevet enda; skal etableres som ny fil under `leveranser/`-mappen (mappen finnes ikke enda i repoet, må opprettes ved første leveranse-fil).

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

**Forslag til struktur for anmodningsdokumentet i `leveranser/`:**

1. Referanse til Skatteetatens brev (dato + saksnummer)
2. Kort forklaring av forsinkelsen (begrenset kapasitet i administrasjonen + bytte av regnskapsfører i perioden)
3. Bekreftelse på at revisor er engasjert og arbeider på spreng
4. Konkret anmodning: utsettelse av leveringsfrist / tvangsmulkt-iverksettelse til 19. august 2026
5. Subsidiært: anmodning om ettergivelse av eventuell påløpt tvangsmulkt etter skfvl § 14-1 tredje ledd
6. Signatur og kontaktopplysninger

**Anmodningen skrevet:** `leveranser/2026-07-09_anmodning_skatteetaten_tvangsmulkt.md`. Følger malen ovenfor. Plassholdere for signatur (navn/rolle/e-post/telefon) fylles inn av Eirik når det er bestemt hvem som signerer — signeringen krever selskapsrettslig fullmakt (jf. skatteforvaltningsloven § 8-15 tredje ledd), dvs. Per Lindberg som CEO/styreleder eller annen med signaturfullmakt registrert hos Skatteetaten.

`leveranser/`-mappen etablert som ny top-level-mappe i repoet ved denne leveransen. Speiler `../fjordgata30/leveranser/` og holder eksterne leveranse-dokumenter (anmodninger, klager, forespørsler, formelle utgående brev) samlet.

**Files touched:** 5 nye filer i `background/lover/`.

---

### T81 `[x]` [FUND] Revisorspakke: prinsippendring aktivering av SuRE-utviklingskostnader + avskrivningsstopp + nedskrivingstest 2025

Sunlit Sea AS skal levere en samlet informasjonspakke til revisor som dekker (a) prinsippendring i 2025-regnskapet fra kostnadsføring til aktivering av SuRE-utviklingskostnader, (b) reversering av avskrivninger på tidligere aktiveringer fra og med 2024-01-01, og (c) nedskrivingstest på den utvidede utviklingsposten. Pakken vedlegges en mail til regnskapsfører først, med konkrete oppfølgingsspørsmål, før den sendes videre til revisor.

Kravene til leveransen er utviklet i lang chat-diskusjon med Eirik. Denne task-beskrivelsen inneholder ALLE beslutninger og fakta som trengs for at en fresh Claude-kontekst kan gjennomføre arbeidet uten å måtte gjenoppdage detaljene.

**Deliverables:**

1. `leveranser/YYYY-MM-DD_revisorpakke_prinsippendring_aktivering_nedskrivingstest.md` — én selvstendig .md-fil som integrerer alt (prinsippendring, aktivering-oversikt, vilkårsvurdering, tilskuddsbehandling, avskrivningsreversering, avskrivningsstart, balanseeffekt, nedskrivingstest, konklusjon). Filen skal stå på egne ben — ingen kryssreferanser til andre filer i repoet, ingen `../background/lover/`-lenker, ingen `funding/nedskriving_2025.md`-referanser. Alle nødvendige fakta inline. Filnavn ASCII (transliterer æ/ø/å).

2. `leveranser/YYYY-MM-DD_mail_regnskapsforer_revisorpakke.md` — kort mail-tekst som legger pakken ved og stiller de eksplisitte oppfølgingsspørsmålene til regnskapsfører (se pkt "Mail til regnskapsfører" nedenfor).

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

**Mail til regnskapsfører (`leveranser/YYYY-MM-DD_mail_regnskapsforer_revisorpakke.md`):**

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

To filer skrevet til `leveranser/`:

1. `2026-07-14_revisorpakke_prinsippendring_aktivering_nedskrivingstest.md` (3 385 ord) — 12 seksjoner integrert. Innledning, foretaks- og standardgrunnlag, prinsippendring m/hjemmel og Metode B-valg, vilkårsvurdering etter rskl § 5-6, Skattefunn holdt utenfor scope, aktivering-oversikt SuRE 2024/2025, bruttoføring bekreftes, reversering av avskrivninger 2024/2025 med detaljert per-rad-tabell inkludert AVSKRIV_2024_TOTAL-estimatet (~7,66 MNOK), avskrivningsstart etter faktisk bruksdato (ikke bundet til 2027), balanseeffekt/utsatt skatt/resultatpåvirkning, nedskrivingstest integrert med alle syv indikatorer, oppsummering med seks bekreftelses-punkter til revisor. Ingen kryssreferanser til andre prosjektfiler — står på egne ben.

2. `2026-07-14_mail_regnskapsforer_revisorpakke.md` (459 ord) — kort mail til Orkla Regnskap AS med de fem eksplisitte spørsmål/bekreftelses-punkter: eksakt 2024-avskrivning, SuRE-tilskudd og dobbeltbokføring på kto 2160, koblet reversering av "reduksjon avskrivning" på kto 2160, Skattefunn utenfor prinsippendringen, og bekreftelse på at 2024-raden på kto 1005 håndteres generisk uten oppdeling.

Plassholdere som gjenstår i revisorpakken:
- AVSKRIV_2024_TOTAL — eksakt fra regnskapsfører (estimat ~7 655 071 kr basert på lineær 5-års avskrivning per rad, med spesifikk bekreftelse etterspurt i mail pkt 1).
- Signatur (Navn, Rolle, E-post, Telefon) — settes inn før leveranse.

**Files touched:** 2 nye filer i `leveranser/`.

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
- `background/*loeypemelding*.md` — grep for «Surewave», «SuRE», «gen 1», «Skiftestjørna», «Enova», «Skattefunn», «Innovasjon Norge». Historiske investoroppdateringer inneholder tidsrom, milepæler, partnerkonstellasjoner og motivasjonen bak hvert utviklingssteg.
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
- Gen 2 arkitektur og prototypeserie: `sure/report.md` kap 2, `gen2/norsmaterials_brief.md`, `background/2025-11-17_loeypemelding.md` (TRL 5-6)
- Skiftestjørna-anlegget: `background/2024-10-01_loeypemelding.md` (105 kWp, install 10. oktober, first develop-operate-sell, PPA med EV PowerCharge) og `background/2025-10-07_loeypemelding.md` («produksjon over forventning»)
- Gen 1-avvikling: `background/2025-10-07_loeypemelding.md` (styret besluttet avvikling)
- Surewave: `../stotte/data/sunlit_sea/project_cards.json` (grant, varighet, konsortium, WPer), `background/2026-07-08_loeypemelding.md` (12-måneders forlengelse pga ACCIONA), `background/2024-04-28_loeypemelding.md` (Clement Systems breakwater-samarbeid)
- SuRE: `../stotte/data/sunlit_sea/project_cards.json` (varighet, konsortium, WPer), `sure/report.md` kap 1 (WP6-objektiver O6.1.1 og O6.2.1, D6.1 vs D6.2)
- 2021-basis komposisjon: `background/2021-06-23_loeypemelding.md` (IN miljøteknologistøtte 8.4 MNOK juni 2021, matching investors Holta Invest AS); detaljert sammensetning per støtteprogram henvist til regnskapsførers avstemminger og bilagsdokumentasjon (ikke gjettet)

Ingen faktapunkter i seksjon 3 uten kildegrunnlag. Alle konkrete beløp fra regnskapsførers avstemminger. Ingen bold i brødtekst. Norsk finansterminologi. Valuta etter tall. Ingen kryssreferanser til andre prosjektfiler.

**Files touched:** `funding/2026-07-14_revisorpakke_prinsippendring_aktivering_nedskrivingstest.md` (oppdatert).

**Neste steg (Eiriks side, utenfor T83):** Gjennomgå oppdatert pakke, verifisere at 2021-basis-omtalen (18 570 858 kr fra tidligere IN miljøteknologistøtte og øvrige tidligere støtteprogrammer) er tilstrekkelig for revisor eller om Eirik ønsker mer detaljert støtteprogram-oppdeling — kilde ligger i regnskapsførers avstemmingsnotater. TRL-figuren refereres som `.svg`; hvis docx-produksjon bestilles må figuren konverteres til PNG først (Pandoc embedder ikke SVG i docx direkte).

---

### T84 `[ ]` [FUND] PDF-layoutfiks i revisorpakken — NBSP i tall og mindre tabellfont

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


