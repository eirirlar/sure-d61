# Requirements for D6.1 and D6.2 — Sunlit model chain and Pareto front

Derived from: SuRE Technical Description (Annex 1, DoW), D1.1 Monitoring Concepts (28.02.2025), Sunlit FDS DES-2024-0003, T6.2 SuRE technical report M18, Sunlit WP6 status notes, Surewave D7.1 (LCA methodology reference), and the Oslomet/Speira material characterisation work.

These requirements are written normatively, as if the deliverables are not yet produced. Each requirement carries a primary source and any binding figure (e.g. KPI, environmental limit) it imposes.

---

# Part A — D6.1 (Sunlit model chain, Lead: IFE, R/SEN, due M20)

## 1. Scope and purpose

**REQ-1.1** D6.1 shall provide data-format and inter-model data-transfer specifications for the Sunlit modelling chain, as stated in the DoW deliverable table.
*Source: DoW deliverable table — D6.1 description.*

**REQ-1.2** D6.1 shall document the outcomes of Task 6.1 (FEM model development for aluminium pressing) and Task 6.2 (model harmonisation and interfacing for digital product development).
*Source: DoW T6.1 and T6.2 descriptions; "Results are used in Tasks 6.2 (and further in 6.3-4)".*

**REQ-1.3** D6.1 shall address Objective O6.1.1: developing a digital product development cycle for Sunlit's aluminium floater.
*Source: DoW WP6 objectives.*

**REQ-1.4** D6.1 shall provide the foundation for Objective O6.2.1 — optimised selection of next-generation floater prototype — to be completed in D6.2.
*Source: DoW WP6 objectives.*

## 2. The aluminium pressing model (T6.1)

**REQ-2.1** D6.1 shall describe a finite element model for simulation of the aluminium float pressing (hydroforming) process.
*Source: DoW T6.1 — "FEM model development for pressing of aluminum, central to Sunlit manufacturing".*

**REQ-2.2** The FEM model shall handle large plastic deformations occurring during sheet-metal forming.
*Source: DoW T6.1 — "numerically challenging large metal deformations".*

**REQ-2.3** The FEM model shall include an anisotropic yield-stress model accounting for the rolling-direction-dependent plasticity of cold-rolled aluminium sheet.
*Source: DoW T6.1 — "anisotropic yield stress model"; calibrated against Oslomet/Speira AA5083-H111 directional data.*

**REQ-2.4** Outputs of the FEM pressing model shall be usable as inputs to the downstream models in T6.2 (structural, thermal, LCA).
*Source: DoW T6.1 — "Results are used in Tasks 6.2 and further in 6.3-4".*

**REQ-2.5** D6.1 shall report results from the aluminium pressing model sufficient to characterise the feasibility boundary of the float cup geometry across the design parameter set used in D6.2.
*Source: DoW T6.3 — Pareto exploration depends on T6.1/T6.2 outputs.*

## 3. Model harmonisation and inter-model interfaces (T6.2)

**REQ-3.1** D6.1 shall define interfaces between the four modelling tools listed in the DoW for Task 6.2:
- (i) Combined FEM and CFD mechanical-stress model for the float under a given design case (WP2/T2.3, IFE),
- (ii) CFD model of fluid and heat flows (WP3/T3.2, IFE),
- (iii) FEM model of aluminium pressing (T6.1, IFE),
- (iv) LCA model (WP1/T1.3, TNO).

*Source: DoW T6.2 — explicit list.*

**REQ-3.2** For every interface, D6.1 shall specify which parameters cross the boundary, in which direction, and in what data format.
*Source: DoW T6.2 — "harmonizing input and output data from the different models".*

**REQ-3.3** The inter-model data-transfer specifications shall be designed to enable automated mapping of the parameter space and rapid iteration turnover.
*Source: DoW T6.2 — verbatim.*

**REQ-3.4** D6.1 shall describe how the model chain supports screening of the design parameter space at multiple accuracy levels, trading computational cost against fidelity.
*Source: DoW T6.2 — "modelling capabilities at different accuracy-levels will be used actively to quickly screen the parameter space".*

## 4. Key design parameters to be covered

**REQ-4.1** The modelling framework documented in D6.1 shall cover the four parameter families identified in DoW T6.3 as having co-impact on sustainability, reliability and cost:
- aluminium sheet thickness (and recycled-aluminium feedstock option),
- floater shape (mechanical robustness vs. material consumption),
- floater size (effect on unit costs),
- cup design (homogeneous water cooling, structural performance, manufacturability).

*Source: DoW T6.3 verbatim list.*

**REQ-4.2** The framework shall support evaluation of these parameters against three performance dimensions simultaneously: sustainability (aluminium consumption, LCA), reliability (structural performance, durability) and cost efficiency (LCOE drivers).
*Source: DoW T6.3 — "co-impact on sustainability, reliability, and cost".*

## 5. Data format and traceability

**REQ-5.1** D6.1 shall define a structured data format for simulation inputs and outputs that enables consistent comparison across design iterations.
*Source: DoW T6.2.*

**REQ-5.2** Each simulated design variant shall be uniquely identifiable, enabling traceability from input parameters through simulation outputs to derived performance metrics.
*Source: DoW T6.2 — rapid iteration implies traceability.*

**REQ-5.3** Data formats shall be compatible with the long-format structured data approach recommended by D1.1 (fields: unique design identifier, parameter name, value, unit, data source).
*Source: D1.1 §5.*

**REQ-5.4** Timestamps and version identifiers shall follow ISO 8601 where applicable.
*Source: D1.1 Table 4.*

## 6. Validation

**REQ-6.1** D6.1 shall describe how model predictions are validated against physical test data.
*Source: DoW T6.4 — "Prototype testing in wave-tank with extra sensors will validate simulated results".*

**REQ-6.2** The validation approach shall demonstrate agreement between simulated and observed outcomes for the aluminium pressing model.
*Source: DoW T6.1.*

**REQ-6.3** Validation data used in D6.1 shall be traceable to physical experiments on Sunlit prototypes or to the ~100 kW pilot installation at Singløya Nord, Norway.
*Source: DoW T6.4; D1.1 executive summary.*

## 7. Pilot and deployment context

**REQ-7.1** D6.1 shall be consistent with the planned ~100 kW Sunlit pilot installation at Singløya Nord, Norway (the project also plans a 105 kW combined verification scope at the same site).
*Source: DoW T6.4; DoW Outcome statement on "105 kW pilot at Singløya".*

**REQ-7.2** The modelling framework shall support design for deployment at SSC 5 (Rough, Hs 2.5–4 m) with respect to structural integrity and moisture ingress, as required for Sunlit's certification scope in SuRE.
*Source: DoW SO4 / 2.1d — "Validate Sunlit design up to SSC 5".*

## 8. Environmental boundary conditions

**REQ-8.1** Thermal modelling shall use representative environmental boundary conditions including solar irradiance, air temperature, water temperature and wind speed.
*Source: DoW T6.2(ii); D1.1 Tier 1 monitoring parameters (wind, water temperature mandatory).*

**REQ-8.2** Structural modelling shall use wave and current loading consistent with hydrodynamic parameters defined as Tier 1 monitoring variables in D1.1.
*Source: D1.1 Table 1.*

**REQ-8.3** Worst-case environmental scenarios shall be defined and used to evaluate model outputs against material and structural limits.
*Source: DoW SO4; DoW T6.3 — need to identify limits of design space.*

## 9. LCA integration

**REQ-9.1** D6.1 shall describe the interface between the engineering models and the TNO LCA model (WP1/T1.3), at minimum defining which parameters flow from the design/simulation domain to the LCA domain.
*Source: DoW T6.2(iv).*

**REQ-9.2** Material consumption outputs from the aluminium pressing model (sheet thickness, cup geometry, post-forming thickness distribution) shall be made available in a format compatible with LCA input requirements.
*Source: DoW T6.2.*

## 10. Dissemination and format

**REQ-10.1** D6.1 shall be delivered as a written report (type R) at dissemination level SEN (sensitive — confidential to project partners).
*Source: DoW deliverable table.*

**REQ-10.2** D6.1 was due at Month 20.
*Source: DoW deliverable table.*

---

# Part B — D6.2 (Sunlit Pareto, Lead: Sunlit, R/SEN, due M24)

D6.2 is the Pareto-frontier deliverable feeding from Task 6.2 (model chain) and Task 6.3 (Pareto mapping & prototype candidate selection, M20–M32). It demonstrates the application of the D6.1 model chain to converge on promising Gen 2 prototype designs.

## 11. Scope and purpose

**REQ-11.1** D6.2 shall deliver a Pareto-frontier mapping of the Sunlit float-design parameter space and identify promising prototype designs.
*Source: DoW deliverable table — "6.2 Sunlit Pareto: Pareto Frontier mapping, identification of promising prototype designs".*

**REQ-11.2** D6.2 shall present the outcomes of Task 6.3 (Pareto frontier mapping & prototype candidate selection, M20–M32, Lead: Sunlit, Participants: IFE, Fraunhofer, Metsolar).
*Source: DoW T6.3.*

**REQ-11.3** D6.2 shall conclude Objective O6.2.1 — optimised selection of new floater-generation prototype.
*Source: DoW WP6 objectives.*

**REQ-11.4** D6.2 shall demonstrate the model chain documented in D6.1 in operation — i.e. show that the data-transfer specifications from D6.1 have been used end-to-end on at least one design iteration. Interfaces tabulated in D6.1 with status "manual" or "targeted for D6.2" shall be reported in D6.2 with their updated implementation status, with the previously deferred ones brought to "implemented" wherever the underlying tooling allows.
*Source: DoW T6.2 → T6.3 chain; CINEA reporting risk noted internally (Josefine).*

## 12. Pareto-frontier mapping

**REQ-12.1** D6.2 shall map the Pareto frontier of the float-design parameter space using the modelling framework from Task 6.2.
*Source: DoW T6.3 verbatim.*

**REQ-12.2** The Pareto-frontier mapping shall cover the four key design parameter families specified in DoW T6.3:
- (1) reduced aluminium thickness and/or aluminium feedstock quality (recycled aluminium),
- (2) modified floater shape for increased mechanical robustness in rougher waters and/or for lower aluminium consumption,
- (3) changed floater size to reduce unit costs (cabling, factory operations, PV cell and module, etc.) per square metre,
- (4) improved cup design for more homogeneous water cooling.

*Source: DoW T6.3.*

**REQ-12.3** D6.2 shall define explicitly what "Pareto-optimal" means in this project — i.e. which performance axes constitute the trade-off (at minimum: forming feasibility, aluminium mass, structural margin, peak component temperature, LCA impact, cost) and what dominance rule is applied.
*Source: implicit in DoW T6.3; expanded in current Sunlit WP6 working notes that already use a feasibility-boundary definition along forming feasibility vs. cup volume vs. structural performance.*

**REQ-12.4** D6.2 shall use the curated dataset of feasible designs produced in D6.1 (≈ 1,300 simulations on the manufacturing feasibility boundary, drawn from ≈ 3,900 total) as the starting set for multi-domain screening.
*Source: D6.1 §4.4 / §7.3 — feasibility-boundary dataset; DoW T6.3 — "use modelling framework from Task 6.2".*

**REQ-12.5** D6.2 shall describe and apply the multi-stage screening methodology outlined in D6.1 §7 (geometric/manufacturability pre-screen → manufacturing simulation → structural and thermal performance → engineering judgement) and report the number of candidate designs surviving each stage.
*Source: DoW T6.2 (multi-accuracy screening); D6.1 §7.3.*

## 13. Inter-model integration to be demonstrated

D6.2 shall report the implementation status, by the M24 cut-off, of each of the inter-model interfaces defined in D6.1, and shall demonstrate end-to-end use of the chain on at least one Gen 2 candidate design.

**REQ-13.1** Interface I-2 (parametric CAD → structural FEM): D6.2 shall confirm STEP version, document the geometric simplifications applied before meshing, and document the agreed material-property handover mechanism. Automated triggering of a structural simulation from a FreeCAD design change is the targeted state.
*Source: D6.1 §6.3 I-2 TODOs; DoW T6.2.*

**REQ-13.2** Interface I-3 (pressing FEM → structural FEM): D6.2 shall include at least one design point for which the as-formed thickness distribution from LS-DYNA has been mapped onto the SiSim/PATRAN structural model and used in the analysis. The transfer format and coordinate-system convention shall be specified.
*Source: D6.1 §6.3 I-3 TODOs; DoW T6.2(i)+(iii).*

**REQ-13.3** Interface I-4 (parametric CAD + measured surface properties → thermal CFD): D6.2 shall document the agreed STEP usage for thermal CFD (full geometry vs. simplified), the full list of material properties consumed by the CFD model, the boundary-condition source (ERA5 worst-case Singapore), and the output archiving format.
*Source: D6.1 §6.3 I-4 TODOs; DoW T6.2(ii); IFE thermal modelling work to date (T6.2 M18 report).*

**REQ-13.4** Interface I-5 (WP6 → LCA / TNO): D6.2 shall replace the email-based bill-of-materials exchange with a structured, versioned template; confirm the functional unit (1 MWh of produced electricity, per Surewave precedent) and the system boundary; agree which WP6 outputs are direct LCA inputs; and version-track design iterations.
*Source: D6.1 §6.3 I-5 TODOs; DoW T6.2(iv); Surewave D7.1 methodology pattern.*

**REQ-13.5** Combined FEM and CFD model chain (DoW T6.2(i)): D6.2 shall report the status of the IFE 3DFloat → SiSim coupling and, for at least one Gen 2 candidate, present mechanical-stress profiles obtained from the combined FEM+CFD chain. If 3DFloat coupling is not delivered by M24, D6.2 shall document the interface specification and the planned closing of the gap.
*Source: T6.2 M18 report — "interface between 3DFloat and SiSim … second half 2026"; DoW T6.2(i).*

## 14. Performance constraints from FDS and DoW KPIs

D6.2 candidate designs shall be screened against the constraint set defined by Sunlit's FDS (DES-2024-0003, rev. 0) and the SuRE WP-level KPIs.

**REQ-14.1** Candidate designs shall satisfy the Functional Design Specification's principal functions (FP1–FP2), constraint functions (FC1–FC3, FC5–FC10 — with the previous FC4 merged into FC1, and FC10 added for environmental ageing) and secondary functions (FS1–FS3), as formulated in D6.1 §3.2 (post-A1.5/A1.6 revision).
*Source: Sunlit FDS DES-2024-0003 with WP6 revisions adopted in the v6 review cycle.*

**REQ-14.2** Candidate designs shall be evaluated for compliance with FC1 (flotation under static and operational loading, including current exposure up to 3 m/s) and FC7 (resistance to waves up to 1.5 Hs), and shall be reported against the SuRE-wide ambition to validate the Sunlit design up to SSC 5 (Hs 2.5–4 m).
*Source: Sunlit FDS FC1/FC7 (post-merge); DoW SO4 / 2.1d.*

**REQ-14.3** Candidate designs shall be screened against the PU thermal stability limit of ≤ 70 °C identified by Sunlit's casting supplier, and against the absorptivity-driven results of the IFE thermal CFD (dark blue PU, A ≈ 0.88–0.91, peak ≈ 84 °C; off-white PU, A ≈ 0.35, peak ≈ 48 °C in worst-case Singapore boundary conditions).
*Source: T6.2 M18 report — supplier 70 °C limit and IFE CFD outputs; D6.1 §5.2.*

**REQ-14.4** Candidate designs shall report, per design point, the aluminium mass per unit and the implied SO9 KPI status: a 50 % reduction in aluminium relative to the Gen 1 reference, and the option to use recycled aluminium feedstock.
*Source: DoW SO9 / 3.3c — "Sunlit: 50 % cut in Al, increase use of recycled Al".*

**REQ-14.5** Candidate designs shall report the expected thermal-loss change at module level relative to the Gen 1 baseline, in support of SO3.
*Source: DoW SO3 — "Sunlit: reduce thermal losses for Sunlit tech of ~3 %".*

**REQ-14.6** Candidate designs shall be evaluated for UV stability of the polymer components (PU hinge / float-structure) drawing on the IFE accelerated-weathering campaign (IEC TS 62788-7-2 condition A1 follow-up, ongoing on white PU samples on Prototype 3).
*Source: DoW 2.1e — "Develop and verify plastics components with satisfactory UV stability"; T6.2 M18 report; Sunlit UV minipatch results 250312.*

## 15. Prototype candidate selection

**REQ-15.1** D6.2 shall identify a small set of promising Gen 2 prototype designs from the Pareto frontier (target order: 2–4 candidates) and document the engineering rationale for the selection.
*Source: DoW deliverable table — "identification of promising prototype designs"; DoW T6.3 — "promising design candidates".*

**REQ-15.2** Each selected candidate shall be characterised by: the nine forming parameters (cup radius, cup depth, eccentricity, angle, tip radius, lip radius, spacing, sheet thickness, forming pressure), the floater outer envelope (driven by PV module choice — 2384 × 1303 mm class or 1770 × 1770 mm Gen 1-class alternative), the infill concept (cup-air pockets, PU foam puzzle-fit, etc.), the hinge/connector concept (P4 reference geometry or successor), and the resulting per-unit bill of materials.
*Source: D6.1 §2.2 component groups; D6.1 §4.1 design parameters.*

**REQ-15.3** D6.2 shall connect the selected candidates to Task 6.4 (prototype production and field deployment) by indicating which candidate is recommended for full-scale prototyping (Sunlit P5/P6 track) and which are retained as fall-backs.
*Source: DoW T6.3 → T6.4 hand-off; Sunlit WP6 prototype roadmap (P4 → P5 → P6).*

**REQ-15.4** D6.2 shall acknowledge the modularity work with Metsolar (matching PV module to float design) and any bill-of-materials alternatives surfaced through Sunlit's BOM compendium and through the examination of new market-available optical components, PV cells and prismatic glass.
*Source: DoW T6.3 — "in concert with Metsolar … harness the modularity of the PV industry"; "Sunlit's bill of materials compendium".*

## 16. Validation hooks for D6.2

**REQ-16.1** D6.2 shall describe the experimental validation plan that will close the loop on the selected candidates, including: lab-scale forming trials, mechanical testing on cast-PU prototypes (Sunlit P3/P4 lab test rig: load cases 1a–1f and measurement points 2a–2f), UV exposure and adhesion testing (IFE, white PU on P3), and the targeted 100 kW pilot at Singløya Nord (DoW T6.4 / D6.4).
*Source: DoW T6.4; D6.1 §5.3 test matrix; T6.2 M18 report.*

**REQ-16.2** Where validation results are not yet available at M24, D6.2 shall list the open validation items, the responsible partner, and the expected date.
*Source: implicit in DoW T6.3 → T6.4 hand-off; pragmatic deliverable hygiene.*

## 17. Sustainability / LCA dimension

**REQ-17.1** D6.2 shall report, per candidate design, the LCA-relevant inputs that have been transferred to TNO under Interface I-5: bill of materials at the unit level, project-level deployment components, production locations and site conditions.
*Source: D6.1 §6.3 I-5; DoW T6.2(iv).*

**REQ-17.2** Where TNO LCA outputs are available within the M24 window (expected Q2 2026), D6.2 shall include the relative contributions of materials and processes to the overall environmental impact and use these as a screening dimension alongside structural, thermal and cost performance. If outputs are not yet available, D6.2 shall describe the integration plan and the latest baseline (Prototype 3 inventory transferred to TNO).
*Source: T6.2 M18 report — TNO LCA underway, expected Q2 2026; DoW T6.2(iv); Surewave D7.1 functional unit and system boundary as reference.*

## 18. Dissemination and format

**REQ-18.1** D6.2 shall be delivered as a written report (type R) at dissemination level SEN.
*Source: DoW deliverable table.*

**REQ-18.2** D6.2 was due at Month 24. (The project is currently at M21–M22 against this deadline and should plan delivery accordingly.)
*Source: DoW deliverable table; current calendar (2026-05-01) vs. project start.*

---

# Part C — Verification of D6.1 requirements after the v6 edits

This section re-checks each D6.1 requirement against the current `report.md` after the edits applied in this session (abbreviation pass, A1.9 forward references, A4.5 hash clarification, A4.6 DEAP fallback explanation, A3.1 partial tracked-changes pass).

| ID | Status | Evidence in report.md (post-edit) |
|----|--------|-----------------------------------|
| REQ-1.1 | met | Executive Summary opening sentence; §1.2; §6.1 |
| REQ-1.2 | met | §1.2 (Tasks 6.1, 6.2 listed); Ch 4 covers T6.1; Ch 6 covers T6.2 |
| REQ-1.3 | met | §1.2 explicitly cites O6.1.1 |
| REQ-1.4 | met | §1.2 cites O6.2.1; §5.4.2 + §6.5 + §9 flag D6.2 follow-on |
| REQ-2.1 | met | §4.1–§4.3 describe LS-DYNA hydroforming model |
| REQ-2.2 | met | §4.2 — large plastic deformation, contact mechanics |
| REQ-2.3 | met | §4.2 — Yld2003 anisotropic yield, Lankford r-values from rolled AA5083-H111 |
| REQ-2.4 | met | §4.6, §6.3 (interfaces I-1, I-3, I-6); §5.3.5 forward references added in this session |
| REQ-2.5 | met | §4.4 + §7 — ≈ 3,900 → ≈ 1,300 curated feasibility-boundary dataset |
| REQ-3.1 | met | Table 6-1 lists I-1 … I-6 covering all four DoW tools (FEM stress, thermal CFD, pressing FEM, LCA); §6.3 narrative |
| REQ-3.2 | met | Table 6-1 (Data transferred / Format columns) and §6.3 prose for I-2, I-3, I-4, I-5 |
| REQ-3.3 | met | §6.5 (level of model integration; automation as next step) and §4.3 (automated pressing pipeline) |
| REQ-3.4 | met | §6.5 + Ch 7 (multi-stage screening with progressively higher-cost models) |
| REQ-4.1 | met | §4.1 (sheet thickness, cup geometry); §2.2.1 (panel/floater size dependency); §5.4.2 (recycled-Al / floater-size LCA hook) |
| REQ-4.2 | met | §3.3 (functional + engineering domains map across sustainability/reliability/cost); Ch 5 (thermal, mechanical, economic) |
| REQ-5.1 | met | §4.3 (CSV schema); §3.6 (parameter framework: design / process / performance) |
| REQ-5.2 | met | §4.3 — input_hash clarified in this session as SHA-256 unique identifier per design |
| REQ-5.3 | partial | Long-format CSV with parameter-name/value/unit per row is described conceptually in §3.6 but the explicit D1.1-style schema with `data source` field is not shown; consider noting the mapping in a future revision |
| REQ-5.4 | partial | Report uses ISO dates in references (e.g. 2024 IEEE J. Photovoltaics) but does not explicitly state ISO 8601 as the timestamp/version convention. Low risk; flag for editorial pass |
| REQ-6.1 | met | §4.5 (calibration vs. punch/die known forming envelope); §5.3 (test matrix); §5.2 (PU optical properties) |
| REQ-6.2 | met | §4.5 — friction and fracture threshold tuned to reproduce 38.5 mm pass / 40 mm fail from physical Gen 1 forming |
| REQ-6.3 | partial | Validation traces to Sunlit Gen 1 forming experience and to IFE PU/UV/CFD work; explicit reference to the 100 kW Singløya pilot is not in §6 — pilot context appears only as future work in §9. Acceptable for D6.1 since the pilot is still being built; flag if reviewers ask |
| REQ-7.1 | partial | §9 mentions deployment context but does not name Singløya Nord. Low-effort fix in next editorial pass |
| REQ-7.2 | met | §3.2 — FC7 wave-resistance (1.5 Hs); §5.2 worst-case scenarios. (SSC 5 ambition is cross-WP and not strictly D6.1 scope — flagged but not blocking) |
| REQ-8.1 | met | §5.2.3 (ERA5, Singapore worst-case: GHI, T_air, T_water, wind speed) |
| REQ-8.2 | met | §5.3.3 (10 mm imposed horizontal elongation as wave/current proxy); §6.3 I-2 |
| REQ-8.3 | met | §5.2.3 + §5.2.4 (worst-case Singapore boundary; PU 70 °C limit) |
| REQ-9.1 | met | §6.3 Interface I-5 — full WP6 → TNO LCA description, including baseline Prototype 3 inventory |
| REQ-9.2 | met | §6.3 I-1, I-3, I-5 — sheet thickness, cup geometry and as-formed thickness distribution available; §5.4.2 makes the LCA path explicit |
| REQ-10.1 | met | Document is markdown report (typesets to Word per `README_MARKDOWN.md`); SEN level is set at delivery time |
| REQ-10.2 | met | M20 due date; report is post-M20 in the v6 review cycle |

**Net result:** all D6.1 requirements remain satisfied after the edits in this session and after the second-round resolution of A1.x and A4.x items (FC10 added, FC4 merged into FC1, §3.4 rewritten to qualitative engineering judgement, §3.7 / §2.5 summaries added, §5.3 restructured per Nathan, gripper-ring and dataset-evolution narratives shortened, MariSol/Accura attribution added, hydroforming switch attributed to WP6, r-values corrected against the calibrated `*MAT_WTM_STM` material card). Four items remain flagged as partial (REQ-5.3, REQ-5.4, REQ-6.3, REQ-7.1) — none of them are regressions caused by the edits; they were partial in the prior version too. Each is a small, targeted editorial fix and is not blocking the deliverable. Recommend bundling them into the next editorial pass once Eirik / IFE return the answers still pending on A2.x (figures), A4.4 (Al thermal conductivity claim), A4.9 (Nathan's Ch 6–9 review) and A5.1 (references list).

---

# Notes on scope boundaries

The following topics are **not** in scope for D6.1 or D6.2 per the DoW:

- Module cost and efficiency improvements for Sunlit's design → D6.3 (Metsolar, M30).
- 100 kW pilot installation and field data → D6.4 (Sunlit, M34).
- Environmental monitoring of the waterbody → WP1 / D1.x.
- ZIM / CTI / BayWa technology streams in WP2–WP5.

D6.1 supplies the modelling infrastructure that D6.2 (Pareto mapping) consumes. D6.2 supplies the prototype designs that Task 6.4 / D6.4 (pilot) builds and tests.
