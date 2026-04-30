# TASKS

## A. D6.1 — IFE review feedback (Nathan, v6_comments.docx)

See `ife_feedback_v6.md` for full comment text and tracked changes.

### A1. Structural / content issues

- [ ] **A1.1: Move experimental details to D6.2** — Nathan (comments 14, 87) suggests all experimental testing details (tensile, UV, adhesion) are better suited for D6.2 as part of evaluating prototype designs. Keep D6.1 purely modelling. Decision needed: move now or leave and expand in D6.2? **NEEDS EIRIK: decision — move or keep?**

- [ ] **A1.2: Clarify WP6 vs pre-existing contributions (Ch 3)** — Comment 387: "It is not clear to me what of this was already present before SuRE and what has been developed in WP6." Add explicit attribution throughout Chapter 3. **NEEDS EIRIK: which elements of Ch 3 (FDS, domains, risk framework, development cycle) existed before SuRE vs developed in WP6?**

- [ ] **A1.3: FDS background and rationale (§3.2)** — Comment 394: "Can you give background on how these functions were found? Some are quite specific (FC4 and FC7), while others are much more general. Why specific current and wave limits but not wind?" Add derivation context. **NEEDS EIRIK: where do FC4 (3 m/s current) and FC7 (1.5 Hs) come from? Why no wind limit? Were these from Surewave testing, customer requirements, deployment site specs?**

- [ ] **A1.4: Clarify FP2 certification (§3.2)** — Comment 399: "What certification does this entail? Do these not include criteria now mentioned in the FC/FSs?" **NEEDS EIRIK: what certification standard/body is envisioned? DNV? IEC?**

- [ ] **A1.5: Add environmental ageing to FDS constraints** — Comment 400: "What about resistance against environmental ageing/minimized degradation?" Missing from current FC list. **NEEDS EIRIK: should this be a new FC (e.g. FC10) or is it implicitly covered? If new, what's the requirement?**

- [ ] **A1.6: Merge FC1 and FC4 or clarify difference** — Comment 403: "What is the difference between [FC4 submergence resistance] and FC1 [flotation]? Can they be merged?" **NEEDS EIRIK: FC1 = stays afloat, FC4 = doesn't get pushed under by currents up to 3 m/s? If that's the distinction, I can draft clarifying text.**

- [ ] **A1.7: Risk-based prioritisation needs substance** — Comment 443: "Is this uncertainty*impact*effort calculation carried out in practice? There are no numbers to show for it. I would notice this if I were an EU reviewer." Either add concrete examples/numbers or soften the claim. **NEEDS EIRIK: was this done formally (e.g. risk matrix) or is it an informal engineering judgement approach? If informal, better to rewrite §3.4 as qualitative engineering judgement rather than implying quantitative risk scoring.**

- [ ] **A1.8: Remove or reference I1–I19 interface list (§2.3)** — Comment 350: abbreviations I1–I19 are never referenced later. Either remove the list or add cross-references. Also overlap with §2.1 interface discussion — consider consolidating. *Claude can do: once decision is made (keep/remove).*

- [ ] **A1.9: Explain how model outputs link to other models (§5.2, §5.3)** — Comments 580, 746: thermal and mechanical sections describe the models but don't explain how their outputs can systematically be integrated into the model chain. "Something on how outputs can be integrated with the other models should be included." *Claude can draft: forward-reference to Ch 6 interfaces from each model section.*

- [ ] **A1.10: Reduce repetition throughout report** — Comment 446: "quite a lot of repetition... difficult to know exactly what to merge or skip. But there is room for tightening if needed." *Claude can do.*

- [ ] **A1.11: Shorten Ch 4 non-essential sections** — Comment 480: "I think 4.3, 4.4 and 4.6 are the most interesting/best fit the deliverable text. Would suggest making other sections a lot shorter." *Claude can do.* **NEEDS EIRIK: agree with Nathan's assessment? OK to shorten §4.1, §4.2, §4.5?**

- [ ] **A1.12: Summary consistency** — Comment 566: Chapters 2 and 3 have no summaries but later chapters do. Either add summaries to all or remove all (executive summary already exists). **NEEDS EIRIK: preference — add to all or remove all?**

### A2. Figures and visuals

- [ ] **A2.1: Figure 3-1 not legible** — Comment 406. Re-export at higher resolution or redesign. **NEEDS EIRIK: provide the .mmd source or re-export. Claude can regenerate the Mermaid if source is available.**

- [ ] **A2.2: Colour-code Figure 3-1 sections** — Comment 408: "Suggest to colour the different sections differently." **NEEDS EIRIK: same — needs source file edit.**

- [ ] **A2.3: Add CAD drawing to Float-structure section (§2.2.2)** — Comment 152: "Could you add a CAD drawing in this section highlighting this structure?" **NEEDS EIRIK: provide or export a FreeCAD screenshot highlighting the float-structure specifically.**

- [ ] **A2.4: Merge Hinges and Connectors, show connected system** — Comment 306. Nathan already merged in tracked changes. But still wants a connected-system figure. **NEEDS EIRIK: provide/export a FreeCAD image showing two connected units at the hinge.**

- [ ] **A2.5: Consider removing Fig 2-2 (gen1 25kWp layout)** — Comment 106: "rest of the document does not really talk about the mooring, and as this design is for Gen 1 anyways." **NEEDS EIRIK: decision — remove or keep with justification?**

- [ ] **A2.6: Better image for Fig 4-1 (raw sheet vs pressed)** — Comment 482: "Do you have a better picture, or two different ones?" **NEEDS EIRIK: provide replacement image(s).**

- [ ] **A2.7: Remove Fig 4-7 (meshed punch/die)** — Comment 537: "punch and die assembly already discarded for Gen 2." *Claude can do: remove figure and update references.* **NEEDS EIRIK: confirm OK to remove.**

- [ ] **A2.8: Move P3/P4 CAD figures to D6.2** — Comments 451, 452, 457: design evolution belongs in D6.2. Consider moving Figs 3-2, 3-3. **NEEDS EIRIK: decision — move to D6.2 or keep? If moved, §3.5 needs a replacement illustration of the parametric design approach.**

- [ ] **A2.9: Show full Gen 2 concept figure under §2** — Comment 102 + 451: component descriptions need an overview figure. **NEEDS EIRIK: provide or export a comprehensive Gen 2 CAD figure (e.g. annotated P4 model showing all component groups).**

### A3. Terminology and editorial (from tracked changes)

- [ ] **A3.1: Apply Nathan's tracked changes** — 136 changed paragraphs. *Claude can do the text changes in report.md.* Key categories:
  - Abbreviation consistency: "floating photovoltaic" → "FPV", "photovoltaic" → "PV", "polyurethane" → "PU" on subsequent use; expand on first use with "(FPV)", "(PU)" etc.
  - "gen 1" / "gen 2" → "Gen 1" / "Gen 2" throughout
  - "panel" → "PV module" where appropriate
  - "hard requirements" softened to "requirements" (FC definition)
  - Various text tightening and rewording
  - Float-structure interface description rewritten (§2.2.2) — more concise, explains casting-on concept
  - Experimental details (§5.3.2) moved from standalone section into §5.3.3 "Coupling with environmental effects" — reframed as motivation for why testing feeds the model chain
  - "Prototype 4" specified where generic "prototype" was used in structural results
  - **NEEDS EIRIK for figures only:** Nathan added Figure 5-2 (CFD dark vs off-white), Figure 5-3 (UV chamber before/after ~480h), Figure 5-4 (FEM stress P4). These image files need to come from IFE/Nathan. Are they in the docx already?

- [ ] **A3.2: Remove gripper ring discussion and Figs 4-4, 4-5** — Comment 507: "Would remove since not relevant for Gen 2 (unless specific outcome of WP6)." *Claude can do.* **NEEDS EIRIK: confirm gripper ring work was pre-SuRE (i.e. safe to remove without losing a WP6 contribution).**

### A4. Technical questions to resolve

- [ ] **A4.1: r90 vs r0 — which is lowest Lankford coefficient?** — Comments 536, 560: Nathan says "Should be r0?" Checked activities.md: Speira data has r0=0.657 lowest; OsloMet data has r90=0.6410 lowest. Both datasets exist. **NEEDS EIRIK: which calibration is used in the LS-DYNA simulations? If OsloMet, report text is correct (r90 lowest). If Speira, Nathan is right (r0 lowest).**

- [ ] **A4.2: Floater size affects more than LCA** — Comment 492: floater size also affects mechanical strength, walkability, hinge design. **NEEDS EIRIK: is this acknowledged somewhere or should §4.1 add a sentence noting these cross-domain effects? Or is floater size truly fixed by panel choice and only LCA varies?**

- [ ] **A4.3: Was punch-die → hydroforming an outcome of WP6?** — Comment 501. **NEEDS EIRIK: did the switch to hydroforming happen before SuRE (Gen 1 used punch-die, Gen 2 always planned as hydroforming) or was it a WP6 finding?**

- [ ] **A4.4: Al thermal conductivity claim** — Comment 515: Nathan points out polystyrene/air gap limits the thermal bridge effect in practice. **NEEDS EIRIK: is the thermal conductivity claim valid for Gen 2 designs (e.g. where cups contact glass directly without polystyrene)? If not, remove to avoid reviewer questions. If yes, add clarification on which design variants exploit it.**

- [ ] **A4.5: Clarify normalised parameter hash** — Comments 540, 546. *Claude can do: each parameter gets its own 0–1 value; the hash is a SHA-256 of all parameter values combined (checked code: `util.py:hash_numbers`). Will clarify in text.*

- [ ] **A4.6: Explain DEAP fallback** — Comment 556. *Claude can do: DEAP is used as a genetic algorithm for generating candidate parameter sets when iterative search and ML model don't produce valid candidates (checked `fluidiogenetic.py`). Will add brief explanation.*

- [ ] **A4.7: How many more datapoints needed?** — Comment 555. **NEEDS EIRIK: is the dataset considered complete, or is there a target number? And what's the selection strategy from the 1,300 Pareto-front candidates — multi-domain screening (Ch 7) or manual engineering judgement?**

- [ ] **A4.8: Who did the forming tests, under which project?** — Comment 535. **NEEDS EIRIK: were the physical forming validation tests (Gen 1 punch-die at 38.5 mm and 40 mm) done by Sunlit Sea pre-SuRE, or by a partner within SuRE? Which facility?**

- [ ] **A4.9: Nathan left off at Ch 6** — Change 132: "NR: LEFT OFF HERE". Nathan's review covers through §5.5 in detail. Chapters 6–9 have not been reviewed by IFE yet. **NEEDS EIRIK: follow up with Nathan for review of Ch 6–9.**

### A5. Outstanding from earlier task list (D6.1)

- [ ] **A5.1: Build references section** — (old T6). Do NOT include OsloMet/Tveit publications or Speira material card. Formalise existing body references. *Claude can do: scan report.md for all inline citations and build a reference list.* **NEEDS EIRIK: confirm whether to include foundational method references (Aretz 2005 on Yld2003, Voce 1948 on hardening) — these are cited implicitly but not referenced.**

---

## B. D6.2 — Preparation and scoping

### B1. Model chain integration (blocking — core D6.2 deliverable)

*All B1 items are coordination tasks between Eirik, IFE (Nathan) and TNO. Claude can draft interface spec documents once the technical answers exist.*

- [ ] **B1.1: Resolve I-2 TODOs with IFE** — Agree STEP version (AP214 or AP242), confirm geometric simplifications before meshing, confirm material property handover mechanism. Target: automate FreeCAD→STEP→SiSim pipeline. **NEEDS EIRIK: schedule meeting with Nathan to resolve.**

- [ ] **B1.2: Implement I-3 (thickness field transfer)** — Agree format for LS-DYNA thickness distribution → SiSim/PATRAN. Confirm coordinate system convention. Pass as-formed thickness map for at least one design point. **NEEDS EIRIK: schedule meeting with Nathan to resolve.**

- [ ] **B1.3: Resolve I-4 TODOs with IFE** — Confirm whether same STEP file is used for structural and thermal CFD. Confirm full list of material properties needed by CFD. Confirm output format and archiving. **NEEDS EIRIK: schedule meeting with Nathan to resolve.**

- [ ] **B1.4: Formalise I-5 (LCA with TNO)** — Replace email-based exchange with structured versioned template. Confirm functional unit and system boundary. Agree which WP6 outputs are direct LCA inputs. Version-track design iterations. **NEEDS EIRIK: coordinate with TNO contact.**

- [ ] **B1.5: Design 3DFloat→SiSim interface** — Connect IFE's 3DFloat hydrodynamic model to SiSim for realistic wave-load profiles. This is the DoW's "combined FEM and CFD model chain to get mechanical stress profiles." Expected second half 2026. If not ready for D6.2, document the interface spec. **NEEDS EIRIK: what is the current status of 3DFloat→SiSim coupling at IFE? Is the "second half 2026" timeline still on track?**

### B2. New measurements and testing (feeds D6.2 content)

*B2 items are IFE/Sunlit lab work. Claude cannot do these — only track status and write them up once results exist.*

- [ ] **B2.1: Measure off-white PU absorptivity** — Needed for updated thermal CFD. Dark blue was 0.88–0.91; off-white expected ~0.35 but not measured. **NEEDS EIRIK: is this Sunlit's or IFE's task? Has it been requested?**

- [ ] **B2.2: Run thermal CFD for P4 geometry** — With off-white PU properties. Flagged as "plan videre" in WP6 report. **NEEDS EIRIK: has this been requested from IFE? Blocked by B2.1.**

- [ ] **B2.3: Complete white PU UV testing at IFE** — Midpatch samples arrived at IFE. After ~480h already showing significant darkening. Mechanical testing after completion needed. **NEEDS EIRIK: current status? Expected completion date?**

- [ ] **B2.4: Complete adhesion testing on P3 samples** — Shear testing of PU-glass interface (long sides) and tensile testing (loose hinges) after UV exposure. **NEEDS EIRIK: current status? Expected completion date?**

- [ ] **B2.5: Get TNO LCA results** — Expected Q2 2026. **NEEDS EIRIK: has Q2 2026 deadline held? Any preliminary results available?**

### B3. Prototype and design (feeds D6.2 content)

*B3 items are Sunlit engineering work. Claude can help with simulation scripting (B3.2, B3.4) if asked.*

- [ ] **B3.1: Complete P4 prototype** — Casting with improved mold design (heat elements, simplified mechanics, air channels). Lab iteration before production. **NEEDS EIRIK: current status of P4?**

- [ ] **B3.2: Run mechanical simulation rig on P4** — Load cases 1a–1f, measurement points 2a–2f. Reusable framework for comparing prototype revisions. **NEEDS EIRIK: is this IFE (SiSim) work or Sunlit work? Has it started?**

- [ ] **B3.3: Resolve architecture decision** — Cast-on-frame vs separate-and-mount. Depends on primer/adhesion/fatigue results, moisture ingress data, and production consequences. Must be decided before P5. **NEEDS EIRIK: timeline for this decision? What data is still missing?**

- [ ] **B3.4: Multi-domain screening** — Apply manufacturing + structural + thermal + LCA filters to the ~1,300 feasible designs. Demonstrate model chain guiding selection. This is the headline D6.2 result. **NEEDS EIRIK: is this feasible with current tooling or does it require the B1 integration work first?**

### B4. Content that Nathan suggests moving from D6.1 to D6.2

- [ ] **B4.1: Experimental testing details** — Tensile, UV, adhesion results. Currently in D6.1 §5.3.2. Nathan moved these to §5.3.3 "Coupling with environmental effects" — but the underlying suggestion is that full experimental detail belongs in D6.2. *Linked to A1.1 decision.*

- [ ] **B4.2: Prototype design evolution (P3→P4 differences)** — Comments 452, 457: design comparison and rationale for changes should be in D6.2 where optimal designs are discussed. *Linked to A2.8 decision.*

- [ ] **B4.3: Structural modelling with infill** — Current SiSim simulation omits infill. D6.2 should have the full model validated against prototype measurements. **NEEDS EIRIK: has IFE been asked to add infill to the SiSim model?**

### B5. CINEA / reporting risk management

- [ ] **B5.1: D6.2 must deliver on inter-model data-transfer** — This is the debt from D6.1. Josefine flagged: "How we formulate this report will be important in order not to raise any red flags with CINEA." D6.2 cannot defer the model chain promise again. **NEEDS EIRIK: is Josefine involved in D6.2 planning? When is the D6.2 deadline?**

- [ ] **B5.2: D6.2 framing** — Core claim: "We built the model chain described in D6.1, connected the tools, ran it on the evolving prototype design, and here are the design decisions it enabled." The interfaces table from D6.1 must show all "manual / targeted for D6.2" upgraded to "implemented." *Claude can draft the D6.2 report structure once B1 answers and D6.2 deadline are known.*

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
