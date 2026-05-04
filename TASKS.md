# TASKS

> **Session note (Claude):** Items marked **[CLAUDE: DONE]** were completed in the latest pass. Items beginning with **[BLOCKED — needs input from …]** are waiting on a specific person/organisation. The block tag explicitly names who must respond and what they must provide.

## A. D6.1 — IFE review feedback (Nathan, v6_comments.docx)

See `ife_feedback_v6.md` for full comment text and tracked changes.

### A1. Structural / content issues

- [x] **A1.1: Move experimental details to D6.2** — Nathan (comments 14, 87) suggests all experimental testing details (tensile, UV, adhesion) are better suited for D6.2 as part of evaluating prototype designs. Keep D6.1 purely modelling. Decision needed: move now or leave and expand in D6.2?
  - Eirik: Confirmed.
  - **[CLAUDE: DONE]** Applied Nathan's middle-ground rewrite. The experimental content (PU tensile, UV exposure, P3 adhesion) has been folded into §5.3.3 "Coupling with environmental effects" and reframed as the experimental basis for environmental coupling in the model chain. Subsections renumbered: §5.3.2 = Structural modelling (was 5.3.3), §5.3.3 = Coupling with environmental effects (was 5.3.4, now contains the experimental content), §5.3.4 = Role in design development (was 5.3.5). Cross-references in §2.2.3, §2.2.4, §5.2.4 and §6.3 (Interface I-2) updated. Full migration of experimental details to D6.2 (per Nathan's stronger reading) deferred there as a B4.1 task.

- [x] **A1.2: Clarify WP6 vs pre-existing contributions (Ch 3)** — Comment 387.
  - Eirik: This was developed in WP6 as part of SuRE.
  - **[CLAUDE: DONE]** Added a paragraph at the top of §3.1 stating that the Product Development Framework — FDS (§3.2), functional/engineering domains (§3.3), prioritisation approach (§3.4), model-supported cycle (§3.5), parameter framework (§3.6) — was developed in WP6 of SuRE and is one of WP6's contributions alongside the domain models in Ch 4–5.

- [x] **A1.3: FDS background and rationale (§3.2)** — Comment 394.
  - Eirik: Update according to specs in `sure_technical_description.pdf` and/or IFE's comments. Leave a comment for IFE.
  - **[CLAUDE: DONE]** Found in DoW: SSC 4 deployment envelope (Hs 1.25–2.5 m, WMO classification) corresponds to current FC7=1.5 Hs / merged-FC1 3 m/s scope, while SSC 5 (Hs 2.5–4 m, DoW SO4 / 2.1d) is the broader project ambition handled in D6.2 / D6.4. Added paragraph in §3.2 explaining this and noting that wind is currently treated qualitatively, with refinement expected through 3DFloat coupling in WP2/WP6. Added an HTML comment for IFE asking whether they have a numerical wind-speed bound for FC6.

- [x] **A1.4: Clarify FP2 certification (§3.2)** — Comment 399.
  - Eirik: Leave comment for IFE — they are better suited to describe the relevant cert based on what they've seen in the market/in collaborations.
  - **[CLAUDE: DONE]** Added a sentence noting that DNV is the working baseline (the DoW states "Sunlit's design has received preliminary DNV verification") and an HTML comment in §3.2 asking IFE to firm up the specific standard/scheme.

- [x] **A1.5: Add environmental ageing to FDS constraints** — Comment 400.
  - Eirik: Indeed, should be included in requirement spec. Add it.
  - **[CLAUDE: DONE]** Added FC10 to §3.2: "resistance to environmental ageing — the system must retain its functional performance throughout the design lifetime under combined exposure to UV, moisture, saltwater, soiling and temperature cycling, with degradation rates of materials and interfaces low enough that none of FC1–FC9 are violated by end of life." No quantitative lifetime/degradation-rate target stated since none was provided; that can be added later if a specific number becomes available.

- [x] **A1.6: Merge FC1 and FC4 or clarify difference** — Comment 403.
  - Eirik: Difference is negligible (loaded vs. unloaded — people walking, snow/ice load). Free to merge or keep — Claude's call.
  - **[CLAUDE: DONE]** Merged FC4 into FC1 in §3.2. Single FC1 now reads "flotation under static and operational loading … at rest and under representative live loads (people walking, accumulated snow or ice) without becoming submerged, and must continue to do so under current exposure up to 3 m/s." Subsequent FCs renumbered (FC5–FC9 unchanged in number; the previous FC4 slot is now closed and FC10 = environmental ageing per A1.5). A note explains the merge so existing references (e.g. caption of Figure 2-10 still names "FC4") remain interpretable.

- [x] **A1.7: Risk-based prioritisation needs substance** — Comment 443.
  - Eirik: Rephrase as qualitative judgement of effort against reward. Resource factors: manhours, material, calendar time, chance of usable result. Benefit factors: influence on future design choices, time-to-market impact, magnitude of improvement against system requirements.
  - **[CLAUDE: DONE]** Renamed §3.4 to "Prioritisation of engineering investigations" and rewrote it around two grouped factor lists (resource, benefit) matching Eirik's wording. The "uncertainty × impact × effort" framing is dropped; the section now explicitly states this is qualitative engineering judgement, not a formal numerical risk register, and gives concrete examples (forming-limits prioritisation, hydroforming pivot, PU thermal/UV characterisation).

- [x] **A1.8: Remove or reference I1–I19 interface list (§2.3)** — Comment 350.
  - Eirik: Keep the list. Explain that I1–I19 will be used in D6.2 as measurement points for FEM/CFD simulations.
  - **[CLAUDE: DONE]** Added a paragraph after the I1–I19 list in §2.3 explaining that the list is retained primarily for forward use in D6.2 — each I-entry corresponds to a physical location at which stress, displacement, temperature, water-ingress or sealing performance is to be probed in the multi-domain screening, and the same labels will be used as measurement points in the FEM and CFD simulations.

- [x] **A1.9: Explain how model outputs link to other models (§5.2, §5.3)** — Comments 580, 746. **[CLAUDE: DONE]** Forward-reference paragraphs added to §5.2.4 (links thermal CFD to interface I-4 in §6.3 and to Stage 3 of screening in §7.3) and §5.3.5 (links structural model to interfaces I-2 and I-3 and to screening in §7.3, plus flags D6.2 work to add infill to SiSim).

- [ ] **A1.10: Reduce repetition throughout report** — Comment 446.
  - Eirik: Don't do it. Need exact flags on where repetition is observed.
  - **[NOT DOING]** Awaiting specific paragraph-level flags from Nathan or Eirik. The chapter-summary tightening done under A1.12 already addresses some of the overlap with the executive summary.

- [x] **A1.11: Shorten Ch 4 non-essential sections** — Comment 480.
  - Eirik: §4.5 a little, §4.1 to bullet list of params with min/max, leave §4.2 and §4.7 alone.
  - **[CLAUDE: DONE]** §4.1 nine parameter blocks collapsed into a single bullet list (one line per parameter with range and brief description); the floater-size paragraphs trimmed and folded with the A4.2 cross-domain note. §4.5 two-parameter-study paragraph shortened from ~7 lines to 3. §4.2 and §4.7 left unchanged.

- [x] **A1.12: Summary consistency** — Comment 566.
  - Eirik: Add summary to Ch 2 and 3 (short). Revisit other chapter summaries and tighten where they overlap with the exec summary.
  - **[CLAUDE: DONE]** Added §2.5 Summary (interfaces-first reading of the system; seven engineering challenges) and §3.7 Summary (FDS → domains → prioritisation → cycle → parameter framework). Tightened §5.5 (one sentence covering thermal CFD findings, PU tensile, UV, and SiSim outputs), §6.6 (one sentence on Table 6-1 status of I-1 to I-6), and §7.7 (one sentence on the 3,900 → 1,300 reduction and the screening role). §4.7 left as-is per Eirik's instruction not to shorten it.

### A2. Figures and visuals

- [ ] **A2.1: Figure 3-1 not legible** — Comment 406. Re-export at higher resolution or redesign.
  - **[BLOCKED — needs input from EIRIK]**: Provide the original .mmd source for Fig 3-1 (or confirm `figures/fig_3-1_development_framework.mmd` is current) so Claude can regenerate at higher resolution. Alternatively re-export PNG at higher DPI.

- [ ] **A2.2: Colour-code Figure 3-1 sections** — Comment 408: "Suggest to colour the different sections differently."
  - **[BLOCKED — needs input from EIRIK]**: Same dependency as A2.1; once .mmd source is confirmed, Claude can add Mermaid `classDef` colouring per functional/engineering/risk/cycle section. Confirm preferred colour scheme or "use your judgement".

- [x] **A2.3: Add CAD drawing to Float-structure section (§2.2.2)** — Comment 152.
  - Eirik: provided exploded-view image set (May 2026, dropped in `new_images/`).
  - **[CLAUDE: DONE]** New images moved to `images/`. §2.2.2 now ends with Figure 2-5 (a/b) showing the cast PU float-structure of Gen 2 Prototype 4 in isolation — long-side and end-side profiles with the integrated hinge halves visible. Six other float_system_*.png images (top/bottom × side/top combinations) are also in `images/` and available for D6.2 if more angles are needed.

- [x] **A2.4: Merge Hinges and Connectors, show connected system** — Comment 306.
  - Eirik: provided `float_p3_matrix.png` — a 3 × 3 matrix of Prototype 3 units interconnected with rods (May 2026).
  - **[CLAUDE: DONE]** The image more than answers Nathan's request — it shows nine units interconnected rather than two, which makes the array-level reading of the hinge-and-connector concept much clearer than a two-unit pairing would. Inserted at the end of §2.2.7 as Figure 2-14, with explanatory text linking back to the isolated hinge halves in Figs 2-11/2-12 and forward to the load-transfer modelling in Ch 5. Old Figure 2-14 (gen1 in flowing water in §2.4.2) renumbered to Figure 2-15 with cross-references updated. §2.5 summary updated to mention the array-level figure.

- [ ] **A2.5: Consider removing Fig 2-2 (gen1 25kWp layout)** — Comment 106: "rest of the document does not really talk about the mooring, and as this design is for Gen 1 anyways."
  - **[BLOCKED — needs input from EIRIK]**: Decide remove vs keep+justify. If remove, Claude will also drop the surrounding sentence in §2.1 that references it.

- [ ] **A2.6: Better image for Fig 4-1 (raw sheet vs pressed)** — Comment 482: "Do you have a better picture, or two different ones?"
  - **[BLOCKED — needs input from EIRIK]**: Supply replacement photograph(s). Two separate images (raw sheet, pressed cup product) would address Nathan's suggestion.

- [ ] **A2.7: Remove Fig 4-7 (meshed punch/die)** — Comment 537: "punch and die assembly already discarded for Gen 2." *Claude can do once confirmed.*
  - **[BLOCKED — needs input from EIRIK]**: Confirm OK to remove (and confirm whether the meshing description remains relevant for the hydroforming workflow).

- [ ] **A2.8: Move P3/P4 CAD figures to D6.2** — Comments 451, 452, 457: design evolution belongs in D6.2.
  - **[BLOCKED — needs input from EIRIK]**: Decide whether to move Figs 3-2, 3-3 to D6.2 (with a replacement illustration of the parametric approach in §3.5) or keep in D6.1.

- [x] **A2.9: Show full Gen 2 concept figure under §2** — Comment 102 + 451.
  - Eirik: provided exploded-view image set (May 2026).
  - **[CLAUDE: DONE]** A new Figure 2-3 has been inserted at the end of §2.1, before §2.2 starts, showing the assembled Gen 2 Prototype 4 unit from three angles (a) top, (b) side, (c) underside. The introductory sentence framing §2.2 has been reworded to describe the Gen 2 unit as taken apart in the following subsections — i.e. §2.2 now reads as an exploded view, with each component group described separately and shown in its own figure. The component-level figures inserted (PV panel close-ups Figure 2-4, float-structure isolation Figure 2-5, groundings Figure 2-10) reinforce this structure.

### A3. Terminology and editorial (from tracked changes)

- [x] **A3.1: Apply Nathan's tracked changes** — 136 changed paragraphs. **[CLAUDE: DONE — fully applied modulo Nathan's three new figures.]** Applied: abbreviation consistency (floating photovoltaic → FPV, photovoltaic panel → PV panel, polyurethane → PU after first use, FDS expansion); gen1/gen2 → Gen 1/Gen 2 throughout the prose (filenames left untouched); FP/FC/FS expansions in §3.2; "hard requirements" → "requirements"; rewording of executive summary, §1.1, §1.2, §1.3 framings; Float-structure rewrite in §2.2.2 (casting-on concept); Hinges/Connectors merge text and Figure 2-7/2-8 cross-references; environmental ageing wording in §3.3.1; structural-results rewrites in §5.3.2 ("Prototype 4" specified where generic); polyurethane → PU in Table 6-1; restructure of §5.3.2 → §5.3.3 (per A1.1 — experimental content folded into "Coupling with environmental effects"); misc tightening in Ch 4 and Ch 5. **Still blocked:**
  - **[BLOCKED — needs input from NATHAN/IFE]**: New Figures 5-2 (CFD dark vs off-white slice), 5-3 (UV chamber before/after ~480 h on P3 sample) and 5-4 (FEM stress on P4 with magnified distortion) are referenced in Nathan's tracked text but the image files have not been delivered. Need the PNGs (and confirmation of figure numbering — current report has no Figs 5-2/5-3/5-4 yet).

- [x] **A3.2: Shorten gripper ring discussion (keep narrative)** — Comment 507.
  - Eirik: Don't remove. Keep as an example of the risk-based approach: tried Gen 1 punch/die first (high reuse upside), then evaluated and switched to fluid forming for greater overall improvement.
  - **[CLAUDE: DONE]** §4.2 rewritten: the punch/die framing now leads with the high-upside reuse argument, the gripper-ring evaluation is kept (single sentence + Figs 4-4 / 4-5 retained), and the switch to hydroforming is explicitly framed as a WP6 outcome of weighing the upside of fluid forming against incremental punch/die refinement — pointing back to §3.4. Figures 4-4 and 4-5 captions adjusted to reflect this framing.

### A4. Technical questions to resolve

- [x] **A4.1: r90 vs r0 — which is lowest Lankford coefficient?** — Comments 536, 560.
  - Eirik: Check `thepressing/*.k` files.
  - **[CLAUDE: DONE]** Found in `thepressing/die.k.hbs` `*MAT_WTM_STM` block: r00 = 0.7142, r45 = 0.8357, r90 = 0.641, rbb = 1.1263. Therefore r90 is the lowest, matching the OsloMet dataset and the existing claim in the report. Nathan's correction was based on the older numerical values printed in the report text (r0 ≈ 0.66, r45 ≈ 0.84, r90 ≈ 0.71) which were inconsistent with the calibrated material card. Updated §4.2 to use the actual material-card values: "r0 ≈ 0.71, r45 ≈ 0.84, r90 ≈ 0.64, rbb ≈ 1.13 (taken from the `*MAT_WTM_STM` block of the LS-DYNA keyword file used for the production runs)". §4.5 reference to "r90 being the lowest" is now consistent.

- [x] **A4.2: Floater size affects more than LCA** — Comment 492.
  - Eirik: Affects container packing, walkability, buoyancy, stress distribution; deemed solvable for any panel size, so largest economic panel (2384 × 1303 mm) chosen.
  - **[CLAUDE: DONE]** Added to §4.1 (after the bulleted parameter list): "Floater overall size … is nevertheless a system-level design variable that affects container packing density, walkability, buoyancy distribution and stress paths through the array, and is recognised in §2.2.1. We have judged it solvable for any of the candidate panel formats and have therefore selected the largest economic panel class (2384 × 1303 mm) as the current reference, with the 1770 × 1770 mm Gen 1-class square panel kept as an alternative."

- [x] **A4.3: Was punch-die → hydroforming an outcome of WP6?** — Comment 501.
  - Eirik: Yes WP6.
  - **[CLAUDE: DONE]** §4.2 now attributes the punch/die → hydroforming switch as a WP6 outcome of comparing the two routes ("Within WP6, closer simulation evaluation of the punch/die route alongside an alternative hydroforming concept showed that the upside of the hydroforming route was substantially greater… On this basis, the gripper-ring punch/die concept was abandoned and hydroforming was adopted as the target manufacturing route for Gen 2.")

- [ ] **A4.4: Al thermal conductivity claim** — Comment 515: Nathan points out polystyrene/air gap limits the thermal bridge effect in practice.
  - **[BLOCKED — needs input from EIRIK]**: Confirm whether Gen 2 designs preserve the thermal-bridge route (e.g. where cups contact glass directly without polystyrene). If not exploited, Claude removes the claim from §4.2 and §5.2; if exploited only in some variants, Claude adds the clarifying scope.

- [x] **A4.5: Clarify normalised parameter hash** — Comments 540, 546. **[CLAUDE: DONE]** §4.3 now states each of the nine parameters has its own 0–1 value (a vector, not a single combined value) and the input_hash is a SHA-256 over the concatenated parameter values used purely as a row identifier — not a normalised parameter value.

- [x] **A4.6: Explain DEAP fallback** — Comment 556. **[CLAUDE: DONE]** §4.4 now describes DEAP as a small genetic-algorithm loop over the nine normalised parameters, applying mutation/crossover and returning the first candidate that passes the Stage-1 geometric/parameter pre-screen (Section 7.3) when iterative search and the ML model both fail.

- [x] **A4.7: How many more datapoints needed?** — Comment 555.
  - Eirik: No more needed for the pressing model. 1,300 is even more than necessary. Many rounds were needed to arrive at the right selection/culling algorithm. Random sampling in early rounds gave poor and slow ML predictions.
  - **[CLAUDE: DONE]** Added a paragraph to §4.4 explaining that the iterative-search + ML + culling combination is itself a WP6 result of several rounds of trial; that random sampling alone was insufficient because boundary points were too sparse to train the ML model effectively; and that the curated 1,300-point dataset is considered well-characterised for D6.2's multi-domain screening, retained at this size to support sensitivity studies as downstream constraints (structural, thermal, LCA) are refined.

- [x] **A4.8: Who did the forming tests, under which project?** — Comment 535.
  - Eirik: MariSol project with partner Accura (UK), pre-SuRE.
  - **[CLAUDE: DONE]** §4.5 now states "The physical forming reference was obtained partly through Sunlit Sea's earlier collaboration in the MariSol project with the UK partner Accura, where the punch/die runs that establish the Gen 1 forming envelope were carried out…"

- [ ] **A4.9: Nathan left off at Ch 6** — Change 132: "NR: LEFT OFF HERE".
  - **[BLOCKED — needs input from EIRIK + NATHAN/IFE]**: Eirik to follow up with Nathan to extend the v6 review to Ch 6–9. Until then, no IFE comments exist for those chapters.

### A5. Outstanding from earlier task list (D6.1)

- [ ] **A5.1: Build references section** — (old T6). Do NOT include OsloMet/Tveit publications or Speira material card. Formalise existing body references.
  - **[BLOCKED — needs input from EIRIK]**: Confirm whether to include foundational method references (e.g. Aretz 2005 on Yld2003, Voce 1948 on hardening, IEC TS 62788-7-2 on UV testing, ISO 10113/16808/12004 series on tensile/biaxial/FLC tests, Roosloot et al. 2024 — already cited inline). Claude can build the list as soon as the inclusion rule is confirmed.

---

## B. D6.2 — Preparation and scoping

### B1. Model chain integration (blocking — core D6.2 deliverable)

*All B1 items are coordination tasks between Eirik, IFE (Nathan) and TNO. Claude can draft interface spec documents once the technical answers exist.*

- [ ] **B1.1: Resolve I-2 TODOs with IFE**
  - **[BLOCKED — needs input from EIRIK + NATHAN/IFE]**: Schedule a working meeting to fix STEP version (AP214 vs AP242), document geometric simplifications applied before meshing, and define the material property handover mechanism. Target: automate FreeCAD→STEP→SiSim pipeline.

- [ ] **B1.2: Implement I-3 (thickness field transfer)**
  - **[BLOCKED — needs input from EIRIK + NATHAN/IFE]**: Agree LS-DYNA thickness distribution export format and SiSim/PATRAN ingestion path; confirm coordinate-system convention; pass as-formed thickness map for at least one design point. Sunlit can prepare a CSV export once IFE specifies the format.

- [ ] **B1.3: Resolve I-4 TODOs with IFE**
  - **[BLOCKED — needs input from EIRIK + NATHAN/IFE]**: Confirm whether the structural STEP file is reused for thermal CFD or a simplified geometry is preferred; agree the full list of material properties needed by CFD (k, cp, ρ per domain plus surface optical properties); agree output format/archiving for CFD results.

- [ ] **B1.4: Formalise I-5 (LCA with TNO)**
  - **[BLOCKED — needs input from EIRIK + TNO]**: Replace ad-hoc email exchanges with a structured versioned template (suggest spreadsheet keyed by material × project component); confirm functional unit (1 MWh produced electricity, per Surewave?) and system boundary; agree which WP6 outputs feed LCA directly; version-track design iterations.

- [ ] **B1.5: Design 3DFloat→SiSim interface**
  - **[BLOCKED — needs input from EIRIK + NATHAN/IFE]**: Get current IFE status on 3DFloat→SiSim coupling and whether "second half 2026" delivery is still on track. If not on track for D6.2, Claude can draft the interface specification document so the deliverable still demonstrates the design.

### B2. New measurements and testing (feeds D6.2 content)

*B2 items are IFE/Sunlit lab work. Claude cannot do these — only track status and write them up once results exist.*

- [ ] **B2.1: Measure off-white PU absorptivity** — Dark blue was 0.88–0.91; off-white expected ~0.35 but not measured.
  - **[BLOCKED — needs input from EIRIK]**: Confirm owner (Sunlit or IFE) and whether the measurement has been requested. Required before B2.2 can run.

- [ ] **B2.2: Run thermal CFD for P4 geometry** — With off-white PU properties.
  - **[BLOCKED — needs input from EIRIK + NATHAN/IFE]**: Confirm IFE has been formally tasked with this CFD run. Depends on B2.1 result.

- [ ] **B2.3: Complete white PU UV testing at IFE** — After ~480 h already showing significant darkening.
  - **[BLOCKED — needs input from EIRIK + NATHAN/IFE]**: Provide current chamber-time status and expected completion date so D6.2 can plan around it.

- [ ] **B2.4: Complete adhesion testing on P3 samples** — Shear testing of PU-glass interface (long sides) and tensile testing (loose hinges) after UV exposure.
  - **[BLOCKED — needs input from EIRIK + NATHAN/IFE]**: Provide current status and expected completion date.

- [ ] **B2.5: Get TNO LCA results** — Expected Q2 2026.
  - **[BLOCKED — needs input from EIRIK + TNO]**: Confirm whether Q2 2026 deadline still holds and whether preliminary results can be shared into the D6.2 draft.

### B3. Prototype and design (feeds D6.2 content)

*B3 items are Sunlit engineering work. Claude can help with simulation scripting (B3.2, B3.4) if asked.*

- [ ] **B3.1: Complete P4 prototype**
  - **[BLOCKED — needs input from EIRIK]**: Provide current status of P4 (casting iteration, mould readiness, lab schedule).

- [ ] **B3.2: Run mechanical simulation rig on P4** — Load cases 1a–1f, measurement points 2a–2f.
  - **[BLOCKED — needs input from EIRIK + NATHAN/IFE]**: Confirm whether SiSim runs at IFE or Sunlit drives this. Confirm start status.

- [ ] **B3.3: Resolve architecture decision** — Cast-on-frame vs separate-and-mount. Must be decided before P5.
  - **[BLOCKED — needs input from EIRIK]**: Decision timeline; what primer/adhesion/fatigue/moisture data is still missing before the call can be made.

- [ ] **B3.4: Multi-domain screening** — Apply manufacturing + structural + thermal + LCA filters to the ~1,300 feasible designs. Headline D6.2 result.
  - **[BLOCKED — needs input from EIRIK]**: Confirm whether this can be executed with current tooling or whether it depends on B1 (model chain integration). If feasible now, Claude can scaffold the screening pipeline.

### B4. Content that Nathan suggests moving from D6.1 to D6.2

- [ ] **B4.1: Experimental testing details** — Tensile, UV, adhesion results. Currently in D6.1 §5.3.2.
  - **[BLOCKED — needs input from EIRIK]**: Linked to A1.1 decision (full move vs. Nathan's middle-ground reframe vs. keep). Same blocker.

- [ ] **B4.2: Prototype design evolution (P3→P4 differences)** — Comments 452, 457.
  - **[BLOCKED — needs input from EIRIK]**: Linked to A2.8 decision.

- [ ] **B4.3: Structural modelling with infill** — Current SiSim simulation omits infill.
  - **[BLOCKED — needs input from EIRIK + NATHAN/IFE]**: Confirm whether IFE has been formally asked to add the infill domain to SiSim and the expected timeline.

### B5. CINEA / reporting risk management

- [ ] **B5.1: D6.2 must deliver on inter-model data-transfer** — Debt from D6.1; Josefine flagged CINEA red-flag risk.
  - **[BLOCKED — needs input from EIRIK + JOSEFINE]**: Confirm Josefine's role in D6.2 planning and the D6.2 deadline so the model-chain rollout can be planned backwards from it.

- [ ] **B5.2: D6.2 framing** — Core claim: "We built the model chain described in D6.1, connected the tools, ran it on the evolving prototype design, and here are the design decisions it enabled." All interface table entries currently "manual / targeted for D6.2" must show "implemented" by D6.2.
  - **[BLOCKED — needs input from EIRIK]**: Once B1 answers and the D6.2 deadline are known, Claude can draft the D6.2 report structure and a concrete plan to flip each interface row to "implemented".

---

## C. Completed (D6.1 earlier tasks)

- [x] **T14: Fix figure ordering violation in §2.1**
- [x] **T13: Add gen1→gen2 transition text in §1.1**
- [x] **T15: Strengthen §1.3 "Data structures" paragraph**
- [x] **T16: Replace FloatStructure camelCase throughout report**
- [x] **T17: Relocate gen2_prototyp4_freecad_mold.png from §2.2.7 to §3.5**
- [x] **T18: Insert gen2 P4 hinge FreeCAD side-view images in §2.2.6/§2.2.7**
- [x] **T19: Insert buoyant PU foam rods connector image in §2.2.7**
- [x] **T20: Insert three new bottom/infill images in §2.2.3 and §2.2.4**
- [x] **T21: Insert gen2_freecad_infill_split_PUfoam.png in §2.2.3**
- [x] **T10: Justify fixing sheet thickness at 0.8 mm (§4.1)**
- [x] **T12: Integrate unreferenced figures into body text** (T12a–T12l all done)
- [x] **T11: Place new_images into report** (T11a–T11g all done)
