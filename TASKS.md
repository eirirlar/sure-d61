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


