# TASKS

> Items beginning with **[BLOCKED — needs input from …]** are waiting on a specific person/organisation.

## A. D6.1 — IFE review feedback (open items)

- [ ] **A1.10: Reduce repetition** — Comment 446. Awaiting specific paragraph-level flags from Nathan or Eirik before acting. No action until flags are provided.

- [ ] **A3.1: IFE figures missing** — Nathan's tracked text references Figures 5-2 (CFD dark vs off-white slice), 5-3 (UV chamber before/after ~480 h on P3 sample) and 5-4 (FEM stress on P4 with magnified distortion), but image files have not been delivered.
  - **[BLOCKED — needs input from NATHAN/IFE]**: Deliver PNGs and confirm figure numbering.

- [ ] **A5.1: Add a References section to the report** — The report currently cites several published works inline (the Yld2003 yield function, the Voce hardening law, ISO test standards, the IEC UV standard, and the Roosloot et al. 2024 IFE paper) but has no formal References section at the end where these are listed with authors, year, and journal. Do NOT include the OsloMet/Tveit tensile test papers or the Speira aluminium material card.
  - **[BLOCKED — needs input from EIRIK]**: Confirm whether you want a References section, and if so, whether it should include the foundational method papers (Yld2003, Voce, ISO standards, IEC standard, Roosloot et al.) or just a subset. Claude will build the section once confirmed.

---

## A2. D6.1 — Report quality (from analysis.md)

### Repetition

- [ ] **A2.1: Reduce repetition of 3,900/1,300 numbers** — These appear 8+ times (Exec, §4.3, §4.4, §4.7, §6.4, §7.3, §7.7, §8.2). Recommend keeping 3 occurrences: first introduction in §4.3, one reminder in §7.3, and one in the Executive Summary. Remove or soften the rest to generic phrasing like "the curated dataset" or "the simulation campaign."

- [ ] **A2.2: Reduce repetition of thermal colour-change story** — The dark-blue → off-white finding and its cause appear 6 times (Exec, §3.4, §5.2.4, §5.3.3, §5.5, §8.2). Primary telling should be §5.2.4; others should be shortened to one-sentence cross-references.

- [ ] **A2.3: Reduce repetition of "model chain partially implemented"** — Said 5 times (Exec, §6.1, §6.5, §8.4, §9.1). Keep in Exec and §9.1 (the key places a reviewer reads); trim from §6.1 and §6.5 to just describe the current state without the hedging disclaimer.

- [ ] **A2.4: Reduce repetition of hydroforming switch narrative** — Appears 4 times (Exec, §3.4, §4.2, §4.7). Primary telling is §4.2; others should be one-line references.

- [ ] **A2.5: Reduce repetition of PU absorptivity/emissivity values** — Cited with full numbers 5 times (§5.2.2, §5.2.4, §5.5, §6.3, §8.2). Keep in §5.2.2 (measurement) and §6.3 (interface spec); others should say "the measured values (§5.2.2)" or similar.

- [ ] **A2.6: Reduce repetition of buoyancy/stress findings** — Stated 4 times (Exec, §5.3.2, §6.3, §8.2). Primary telling is §5.3.2; Exec and §8.2 can keep one-sentence versions; §6.3 should cross-reference.

### Coherence

- [ ] **A2.7: Disambiguate interface numbering** — Ch 2 defines 19 physical interfaces (I1–I19: component-to-component) while Ch 6 defines 6 data interfaces (I-1 to I-6: model-to-model). Both use "I-" notation. A reader jumping between chapters could confuse them. Options: rename physical set to "PI-1..PI-19", rename data set to "DI-1..DI-6", or add a clarifying note where Ch 6 numbering begins.

- [ ] **A2.8: Shorten thermal-bridge duplication between §4.2 and §5.2.1** — Both passages explain the Gen 1 thermal bridge, the Gen 2 PU-foam blocking it, and the open question about reintroduction. Suggest keeping the full narrative in §5.2.1 (its natural home) and reducing §4.2 to a one-sentence cross-reference.

- [ ] **A2.9: Reduce Executive Summary / Conclusions overlap** — §8.1–8.2 substantially restate the Executive Summary. Consider making Conclusions more evaluative (what worked, what didn't, what surprised) rather than re-summarising what was done.

### Structure

- [ ] **A2.10: Consider trimming Ch 2 length** — At ~200 lines (~23% of the report), Ch 2 is disproportionately long for a modelling deliverable. Much component-level description (PV panel options, grounding concepts, connector variants) provides context but is only loosely connected to the modelling work. Possible actions: shorten subsections that don't directly feed Ch 4–7, or add a sentence justifying why system architecture detail is needed for the model chain.

- [ ] **A2.11: Acknowledge thin Ch 7** — The Screening chapter (~50 lines) is thin relative to its conceptual importance as the culmination of the framework. This is appropriate for D6.1 (methodology described, execution deferred to D6.2) but the chapter could benefit from a short paragraph setting expectations — e.g. "This chapter documents the screening methodology; its full execution across all four domains is the headline contribution of D6.2."

### Missing elements

- [ ] **A2.12: Add References section** — The report cites Aretz 2005 (Yld2003), Voce 1948, ISO 10113:2020, ISO 16808:2014, ISO 12004-2:2009, IEC TS 62788-7-2, and Roosloot et al. 2024 inline but has no formal bibliography. Required for an EU deliverable. (Previously A5.1, now unblocked — user confirmed "include all of them.")

- [ ] **A2.13: Add abbreviation list** — Terms like FDS, FEM, CFD, PU, LCA, FPV, DoW, SSC, DEAP, ML, CAD are used throughout without a collected definitions list. Standard for EU deliverables.

- [ ] **A2.14: Add list of figures** — With 41 figures, a list of figures after the table of contents aids navigation and is standard for EU deliverables.

### KPIs and quantification

- [ ] **A2.15: Add preliminary KPI estimate for aluminium reduction** — The 50% aluminium reduction KPI is mentioned in §3.4 as a target but never evaluated numerically. Even a rough estimate (e.g. "0.8 mm vs 1.5 mm sheet thickness represents a 47% mass reduction per unit area before accounting for cup geometry differences") would give CINEA reviewers something concrete to assess.

- [ ] **A2.16: Add preliminary KPI estimate for thermal improvement** — The ~3% thermal-loss reduction KPI is mentioned but the thermal work focuses on material safety (over-temperature) rather than efficiency gain. A sentence acknowledging this gap or providing an estimate of efficiency improvement from the colour change would help.

### Cleanup

- [ ] **A2.17: Resolve or flag TODO comments before submission** — Six HTML comments remain in the report addressed to IFE and TNO. These are appropriate for the working draft but must be either resolved (with partner input) or removed/softened for the submitted version.

- [ ] **A2.18: Clean up unreferenced image files** — Several images in `images/` are no longer referenced: `fpv_matrix_and_mooring_system_for_25kwp.png` (removed Fig 2-2), four `*_bak.png` backups, and unused views (`bottom.png`, `infill.png`, `rods.png`, several `float_system_*_side.png` variants). Not urgent but reduces clutter.

---

## B. D6.2 — Preparation and scoping

### B1. Model chain integration

- [ ] **B1.1: Resolve I-2 TODOs with IFE** — Fix STEP version (AP214 vs AP242), document geometric simplifications, define material property handover. Target: automate FreeCAD→STEP→SiSim pipeline.
  - **[BLOCKED — needs input from EIRIK + NATHAN/IFE]**

- [ ] **B1.2: Implement I-3 (thickness field transfer)** — Agree LS-DYNA thickness export format and SiSim/PATRAN ingestion path; confirm coordinate-system convention.
  - **[BLOCKED — needs input from EIRIK + NATHAN/IFE]**

- [ ] **B1.3: Resolve I-4 TODOs with IFE** — Confirm geometry reuse for thermal CFD; agree full material property list; agree CFD output format.
  - **[BLOCKED — needs input from EIRIK + NATHAN/IFE]**

- [ ] **B1.4: Formalise I-5 (LCA with TNO)** — Replace ad-hoc emails with versioned template; confirm functional unit and system boundary; version-track design iterations.
  - **[BLOCKED — needs input from EIRIK + TNO]**

- [ ] **B1.5: Design 3DFloat→SiSim interface** — Confirm IFE status on 3DFloat→SiSim coupling and "second half 2026" delivery timeline. If delayed, Claude drafts interface spec document.
  - **[BLOCKED — needs input from EIRIK + NATHAN/IFE]**

### B2. New measurements and testing

- [ ] **B2.1: Measure off-white PU absorptivity** — Dark blue was 0.88–0.91; off-white expected ~0.35 but not measured. To be measured as part of D6.2 work.

- [ ] **B2.2: Run thermal CFD for P4 geometry** — With off-white PU properties. Thermal tests to be decided in D6.2, possibly combined with load test.

- [ ] **B2.3: Complete white PU UV testing at IFE** — Condition A1 protocol. TODO left for Nathan in §5.3.3. Status update needed from IFE.
  - **[BLOCKED — needs input from NATHAN/IFE]**

- [ ] **B2.4: Complete adhesion testing on P3 samples** — Shear (PU-glass long sides) and tensile (loose hinges) after UV exposure. TODO left for Nathan in §5.3.3.
  - **[BLOCKED — needs input from NATHAN/IFE]**

- [ ] **B2.5: Get TNO LCA results** — Expected Q2 2026. TODO left for TNO in §5.4.2.
  - **[BLOCKED — needs input from TNO]**

### B3. Prototype and design

- [ ] **B3.1: Complete P4 prototype** — Mould cast has been started. Progress to be reported in D6.2.

- [ ] **B3.2: Mechanical simulation (SiSim) on P4** — IFE runs this. They will adapt load cases to their capabilities and report in D6.2.

- [ ] **B3.3: Resolve cast-on-frame vs separate-and-mount architecture decision** — Must be decided before P5. P4 mould tests combined with UV/fatigue tests in D6.2 will inform this. Primer reports 20-year aquatic life; target is 25 years — dedicated testing needed to determine real-conditions performance.

- [ ] **B3.4: Multi-domain design screening** — The ~1,300 feasible pressing geometries (generated in Ch 4–7 of D6.1) must each be evaluated across four performance dimensions before a final design can be selected: (1) manufacturing feasibility (already filtered in the pressing pipeline), (2) structural performance (peak stresses and deformation from SiSim, interface I-2/I-3), (3) thermal performance (peak PU temperature from CFD, interface I-4), and (4) life-cycle impact (material masses and process data to TNO, interface I-5). The screening applies each domain's pass/fail threshold in sequence, reducing the 1,300 candidates to a short-list of structurally and thermally viable geometries with acceptable LCA profiles. This is the headline D6.2 deliverable and depends on B1 model chain integration.
  - **[BLOCKED — needs input from EIRIK]**: Confirm whether screening can run with current tooling or must wait for B1.

### B4. Content moving from D6.1 to D6.2

- [ ] **B4.1: Full experimental testing details** — Tensile, UV, adhesion results currently in D6.1 §5.3.3 (as environmental coupling basis). Full write-up deferred to D6.2.
  - **[BLOCKED — needs input from EIRIK + NATHAN/IFE]**: Confirm scope and timing.

- [ ] **B4.3: Structural modelling with infill** — Current SiSim omits infill; flagged as D6.2 target in §5.3.4.
  - **[BLOCKED — needs input from EIRIK + NATHAN/IFE]**: Confirm IFE has been tasked with adding infill domain and expected timeline.

### B5. CINEA / reporting risk management

- [ ] **B5.1: D6.2 must deliver on inter-model data-transfer** — Josefine flagged CINEA red-flag risk.
  - **[BLOCKED — needs input from EIRIK + JOSEFINE]**: Confirm Josefine's role and D6.2 deadline so model-chain rollout can be planned backwards from it.

- [ ] **B5.2: D6.2 framing** — Core claim: "We built the model chain described in D6.1, connected the tools, ran it on the evolving prototype, and here are the design decisions it enabled." All interface table entries currently "manual / targeted for D6.2" must show "implemented" by D6.2.
  - **[BLOCKED — needs input from EIRIK]**: Once B1 answers and D6.2 deadline are known, Claude can draft the D6.2 structure and plan to flip each interface row.

---

## C. Completed

### D6.1 — IFE review feedback (Nathan, v6_comments.docx)

- [x] **A1.1** — Experimental content reframed as §5.3.3 "Coupling with environmental effects"; subsections renumbered; cross-references updated.
- [x] **A1.2** — WP6 origin paragraph added to §3.1.
- [x] **A1.3** — FDS rationale updated from DoW (SSC4/5 envelope); HTML comment left for IFE on FC6 wind bound.
- [x] **A1.4** — DNV baseline noted in §3.2; HTML comment for IFE to firm up standard.
- [x] **A1.5** — FC10 (environmental ageing) added to §3.2.
- [x] **A1.6** — FC4 merged into FC1; subsequent FCs renumbered; merge note added.
- [x] **A1.7** — §3.4 rewritten as qualitative resource/benefit judgement with concrete examples.
- [x] **A1.8** — Paragraph added after I1–I19 list explaining forward use in D6.2.
- [x] **A1.9** — Forward-reference paragraphs added to §5.2.4 and §5.3.5.
- [x] **A1.11** — §4.1 collapsed to bullet list; §4.5 shortened.
- [x] **A1.12** — §2.5 and §3.7 summaries added; §5.5, §6.6, §7.7 tightened.
- [x] **A2.1** — Fig 3-1 re-rendered at 3× scale.
- [x] **A2.2** — Fig 3-1 colour-coded: FDS blue, RISK amber, functional green, engineering purple, cycle orange, params grey.
- [x] **A2.3** — Float-structure isolation views (Fig 2-4 a/b) inserted in §2.2.2.
- [x] **A2.4** — 3×3 matrix image inserted as Fig 2-13 in §2.2.7.
- [x] **A2.5** — Fig 2-2 (gen1 mooring layout) removed; all Ch 2 figures renumbered.
- [x] **A2.6** — Fig 4-1 split into 4-1a (alu_sheet.jpg) and 4-1b (alu_pressed.jpg).
- [x] **A2.7** — Fig 4-7 updated to meshed_fluid_die.png with hydroforming caption.
- [x] **A2.8** — P3/P4 CAD figures kept in D6.1.
- [x] **A2.9** — Gen 2 Prototype 4 overview (Fig 2-2 a/b/c) inserted at end of §2.1.
- [x] **A3.1** — Nathan's 136 tracked-change paragraphs applied. IFE images for Figs 5-2/5-3/5-4 still outstanding (tracked as A3.1 above).
- [x] **A3.2** — Gripper-ring narrative reframed as risk-based prioritisation example in §4.2.
- [x] **A4.1** — Lankford values corrected to material-card values (r0 ≈ 0.71, r45 ≈ 0.84, r90 ≈ 0.64, rbb ≈ 1.13).
- [x] **A4.2** — Floater-size system implications paragraph added to §4.1.
- [x] **A4.3** — Punch/die → hydroforming switch attributed to WP6 in §4.2.
- [x] **A4.4** — Thermal bridge claim scoped to Gen 1 in §4.2 and §5.2.1. Gen 2 (PU foam infill) noted as blocking the bridge path; frame and bottom plate identified as dominant heat-dissipation routes. Reintroduction via pressed-cup or honeycomb aluminium infill flagged as open D6.2 question.
- [x] **A4.5** — Normalised parameter vector vs. input_hash clarified in §4.3.
- [x] **A4.6** — DEAP genetic-algorithm fallback described in §4.4.
- [x] **A4.7** — Iterative dataset growth rationale and 1,300-point adequacy explained in §4.4.
- [x] **A4.8** — Forming tests attributed to MariSol project / Accura (UK) in §4.5.
- [x] **B4.2** — P3→P4 design evolution kept in D6.1 (per A2.8 decision); no move to D6.2 required.

### D6.1 — earlier tasks

- [x] T10–T21 (figure placement, camelCase cleanup, section strengthening) — all completed in prior sessions.
