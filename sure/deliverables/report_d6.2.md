# Executive Summary

> **TBD.** Two- to three-paragraph summary, written last. Cover:
> - what D6.2 delivers (the Pareto frontier mapping over the four DoW parameter families plus the identified Gen 2 prototype candidates);
> - that the D6.1 model chain has been put into operation end-to-end on at least one Gen 2 candidate;
> - the headline trade-offs identified (aluminium mass vs. structural margin vs. thermal margin vs. cost vs. LCA);
> - the recommended candidate for the Sunlit P5/P6 prototyping track and the candidates retained as fall-backs.
>
> *Addresses: REQ-11.1, REQ-11.4, REQ-15.1, REQ-15.3.*

---

# 1 Introduction

## 1.1 From D6.1 to D6.2

> **TBD.** One-page bridge from D6.1: D6.1 documented the modelling framework (the four-tool chain, the parameter framework, the data-transfer specifications) and the curated 1,300-point feasibility-boundary dataset for the aluminium pressing process. D6.2 applies that framework. Make the link explicit: the screening of Section 4 here uses the dataset produced under D6.1 §4.4 and §7, and the interfaces tabulated in D6.1 §6.3 are the ones whose status is updated in Section 3 here.
>
> *Addresses: REQ-11.4.*

## 1.2 Objectives of D6.2

> **TBD.** Restate the two DoW anchors:
> - Deliverable: "Pareto Frontier mapping, identification of promising prototype designs" (DoW deliverable table, M24, Lead Sunlit, R/SEN).
> - Objective: O6.2.1 "Optimised selection of new floater generation prototype" (DoW WP6 objectives).
>
> Then state the working interpretation: the trade-offs the Pareto front balances and the selection criteria for prototype candidates.
>
> *Addresses: REQ-11.1, REQ-11.2, REQ-11.3, REQ-12.3.*

## 1.3 Scope

> **TBD.** What's in: parameter-space mapping over the four families, multi-stage screening with structural/thermal/LCA filters applied on top of D6.1's manufacturing filter, prototype candidate identification with rationale. What's out: full prototype manufacturing (→ T6.4 / D6.4), module-level cost and efficiency improvements (→ D6.3 / Metsolar), pilot deployment and field data (→ D6.4).
>
> *Addresses: scope-boundary notes.*

---

# 2 Gen 2 design status

> Short chapter. Most of the architecture description lives in D6.1 §2; this chapter only summarises what has changed since D6.1 was written and which design state the Pareto mapping operates on.

## 2.1 Reference design and prototype iterations

### 2.1.1 P1–P3 recap

> **TBD.** One-paragraph recap of Prototypes 1–3 from D6.1 §3.5 and the WP6 working notes. Cover: P1 cup-air-pocket infill concept, P2/P3 hinge geometry evolution, P3 metal mould (Figs 3-4 and 3-5 of D6.1). Treat as background only — no new analysis here.

### 2.1.2 P4 — current reference for D6.2

> **TBD.** Current state of P4: casting status (cast, lab-tested, or pending — TASKS B3.1), mould architecture, hinge/connector geometry (D6.1 Figs 2-7, 2-8), float-structure casting-on approach (D6.1 §2.2.2), infill concept (cup-air pockets vs. puzzle-fit PU foam, D6.1 §2.2.3). State whether P4 is the geometry on which the D6.2 Pareto mapping operates.

### 2.1.3 Trajectory to P5 and P6

> **TBD.** From the WP6 working notes: P5 architectural choice (cast-on-frame vs. separate-and-mount, dependent on TASKS B3.3), P6 full-scale + pilot-testable hinge system. State which choices D6.2 informs and which are deferred.
>
> *Addresses: REQ-15.2, REQ-15.3.*

## 2.2 Reference design parameters

> **TBD.** Confirm the nine pressing parameters from D6.1 §4.1 and the floater outer envelope (PV-module driven: 2384 × 1303 mm class, or 1770 × 1770 mm Gen 1-class alternative). Note any parameter ranges narrowed since D6.1 (e.g. sheet thickness fixed at 0.8 mm).
>
> *Addresses: REQ-12.2, REQ-15.2.*

## 2.3 Changes since D6.1

> **TBD.** Bulleted change log: e.g. PU colour change from dark blue to off-white (D6.1 §5.2.4 outcome), infill domain still excluded from SiSim model (open item), Prototype 4 cast and lab-tested (or not, depending on B3.1 status from TASKS.md). Any other relevant change-since-D6.1 items.
>
> *Addresses: REQ-11.4 (status update against D6.1).*

---

# 3 Model chain — implementation status at M24

## 3.1 Recap of the D6.1 chain

> **TBD.** Half-page recap of Figure 6-1 (D6.1) — the conceptual chain — and the six interfaces I-1 through I-6 from D6.1 Table 6-1. Refer the reader to D6.1 §6 for the full description; here only summarise.
>
> *Addresses: REQ-11.4.*

## 3.2 Updated interface table

> **TBD.** Reproduce D6.1 Table 6-1 with an additional column **"Status at M24"** showing the change from D6.1 to D6.2. Targeted entries:
>
> | ID | From | To | D6.1 status | D6.2 status |
> |----|------|----|-------------|-------------|
> | I-1 | CAD | Pressing FEM | Implemented and automated | (unchanged) |
> | I-2 | CAD | Structural FEM | Implemented; data transfer manual | TBD — was the FreeCAD→SiSim path automated? |
> | I-3 | Pressing FEM | Structural FEM | Available on demand; not passed | TBD — was a thickness map mapped onto SiSim for at least one design point? |
> | I-4 | CAD + meas. | Thermal CFD | Implemented; data transfer manual | TBD — STEP usage and material-property list confirmed? |
> | I-5 | WP6 | LCA / TNO | Active — P3 baseline delivered | TBD — versioned template in place? |
> | I-6 | Dataset | ML model | Implemented and automated | (unchanged) |
>
> *Addresses: REQ-11.4, REQ-13.1, REQ-13.2, REQ-13.3, REQ-13.4.*

## 3.3 Interface I-2 — parametric CAD → structural FEM

### 3.3.1 Status at D6.1

> **TBD.** Recap from D6.1 §6.3 I-2: STEP transfer implemented and demonstrated (two-module 310 k-element assembly), but data transfer manual and STEP version not formally fixed.

### 3.3.2 Resolved items

> **TBD.** Outcome of the meeting closing TASKS B1.1: STEP version (AP214 vs AP242) selected, geometric simplifications documented (screw holes; fillets; cable routing — confirm full list), material-property handover mechanism agreed.

### 3.3.3 Demonstrated automation

> **TBD.** Describe the FreeCAD → SiSim automation reached at M24 (e.g. scripted STEP export + IFE-side import macro), or document the residual manual steps if full automation is not yet in place.

### 3.3.4 Residual gaps

> **TBD.** Anything not closed by M24 — e.g. outstanding geometric features that require manual cleanup, or a missing material-property file. Carry to D6.2's open-items list.
>
> *Addresses: REQ-13.1.*

## 3.4 Interface I-3 — pressing FEM → structural FEM

### 3.4.1 Status at D6.1

> **TBD.** Recap from D6.1 §6.3 I-3: thickness-distribution field available on demand from LS-DYNA but not systematically passed to SiSim.

### 3.4.2 Demonstration design point

> **TBD.** Identify the Gen 2 candidate cup geometry chosen for the first end-to-end I-3 demonstration. Show the as-formed thickness map (from LS-DYNA element output) and how it was mapped onto the SiSim mesh.

### 3.4.3 Transfer format and coordinate convention

> **TBD.** State the agreed format (e.g. CSV of nodal coordinates and thickness values, or an alternative IFE specifies) and the coordinate-system convention (origin, axis orientation).

### 3.4.4 Impact on structural results

> **TBD.** Compare structural-margin results between the uniform-thickness assumption and the as-formed thickness field. Report the change in peak stress in the aluminium domain and any qualitative shift in failure mode.
>
> *Addresses: REQ-13.2.*

## 3.5 Interface I-4 — parametric CAD + measured properties → thermal CFD

### 3.5.1 Geometry handling

> **TBD.** Whether the same STEP file is used for thermal CFD as for structural, or a simplified geometry is generated. If simplified, describe what is removed/preserved.

### 3.5.2 Material property list

> **TBD.** Full list of material properties consumed by the CFD model (k, c_p, ρ per domain plus surface absorptivity and emissivity). For each, state the source (Sunlit measurement, IFE library, standard database).

### 3.5.3 Boundary conditions

> **TBD.** Restate the worst-case Singapore boundary from D6.1 §5.2.3 (GHI 943 W/m², T_air 28.1 °C, T_water 21.5 °C, wind 0.5 m/s). Confirm whether the same boundary applies for D6.2 candidates, or whether additional sites have been added.

### 3.5.4 Off-white PU absorptivity status

> **TBD.** Report the measured off-white PU absorptivity (TASKS B2.1) if available. Otherwise carry the assumed value (≈ 0.35) and flag the open measurement.

### 3.5.5 Output archiving

> **TBD.** Format and location of CFD outputs delivered by IFE (peak temperature scalar; full temperature field; etc.).
>
> *Addresses: REQ-13.3, REQ-14.3.*

## 3.6 Interface I-5 — WP6 → LCA (TNO)

### 3.6.1 Versioned template

> **TBD.** Show the structured template adopted in place of email exchanges (suggested: spreadsheet keyed by material × project component). If the template is not yet adopted at M24, document the proposal and gap.

### 3.6.2 Functional unit and system boundary

> **TBD.** Confirm functional unit (1 MWh of produced electricity, per Surewave precedent) and system boundary (cradle-to-grave, excluding production equipment per Surewave). Note any deviations adopted for SuRE.

### 3.6.3 WP6 outputs that feed LCA directly

> **TBD.** List which WP6 simulation outputs are consumed by the LCA model (e.g. material mass from the FreeCAD model, post-forming aluminium mass from LS-DYNA, PU mass from cast-prototype weighing).

### 3.6.4 Versioning of design iterations

> **TBD.** Mechanism by which a TNO LCA result can be traced back to a specific design state on the Sunlit side (e.g. design hash, BOM revision number).
>
> *Addresses: REQ-13.4, REQ-17.1.*

## 3.7 Combined FEM and CFD chain (3DFloat → SiSim)

### 3.7.1 IFE 3DFloat → SiSim coupling status at M24

> **TBD.** Per the T6.2 M18 report, the coupling was targeted for the second half of 2026. State the actual status at M24 — operational, in development, or deferred.

### 3.7.2 Demonstration on a Gen 2 candidate (if available)

> **TBD.** If the coupling is operational, present mechanical-stress profiles from the combined chain for at least one Gen 2 candidate under realistic wave conditions.

### 3.7.3 Fallback — interface specification only

> **TBD.** If the coupling is not delivered by M24, document the interface specification (data exchanged, formats, planned implementation timeline) so D6.2 still demonstrates the design intent.
>
> *Addresses: REQ-13.5.*

---

# 4 Pareto-frontier mapping

## 4.1 What "Pareto-optimal" means here

> **TBD.** Explicit statement: a design is Pareto-optimal if no other feasible design is at least as good on every performance axis and strictly better on at least one. Then enumerate the axes used in this work — at minimum:
>
> 1. forming feasibility (proxy: time-to-crack, lip-mean, edge-mean from D6.1 §4.3),
> 2. aluminium mass per unit (driven by sheet thickness × cup geometry × envelope),
> 3. structural margin under reference load (peak von Mises in Al/PU/glass under the 10 mm horizontal elongation case from D6.1 §5.3.3, or the wave-load case if 3DFloat→SiSim is online),
> 4. peak component temperature (PU hinge, from CFD under worst-case Singapore boundary),
> 5. life-cycle environmental impact (LCA from TNO),
> 6. cost (from Sunlit BOM compendium and module-class choice with Metsolar).
>
> *Addresses: REQ-12.3.*

## 4.2 Starting dataset

> **TBD.** Reuse the curated ~1,300-point dataset on the manufacturing feasibility boundary from D6.1 §4.4 / §7. Note any data added since D6.1 cut-off. State whether the dataset is considered complete for D6.2 or has a target size — this is the open question A4.7 in TASKS.md and needs Eirik's input before this section can be closed.
>
> *Addresses: REQ-12.4.*

## 4.3 Multi-stage screening methodology

> Build on D6.1 §7.3 (Stages 1–4). For each stage, report the number of designs entering and surviving and the criteria applied.

### 4.3.1 Stage 1 — geometric and manufacturability pre-screen

> **TBD.** Apply D6.1 §7.3 Stage 1 filters: minimum radii, spacing, cup tip < cup radius, parameter validation rules. Report N₁ in / n₁ out.

### 4.3.2 Stage 2 — manufacturing simulation

> **TBD.** Apply D6.1 LS-DYNA forming model (Ch 4): forming completes without cracking (time-to-crack), minimum thickness after forming, no localised failure indicators. Re-use the curated ≈ 1,300-point dataset from D6.1 §4.4 / §7.3 as the starting point; report any extensions added since the D6.1 cut-off.

### 4.3.3 Stage 3 — structural and thermal performance

> **TBD.** This is the new contribution of D6.2. Apply IFE SiSim under the reference load case (10 mm imposed horizontal elongation, or the wave-load case if 3DFloat → SiSim is online per §3.7) and IFE thermal CFD under the worst-case Singapore boundary. Report n₃ out and the binding constraint per eliminated design.

### 4.3.4 Stage 4 — engineering judgement and selection

> **TBD.** Apply the constraint set from Ch 5 plus engineering judgement. Resolve trade-offs explicitly (e.g. lighter aluminium vs. structural margin) and document the rule used. Report the final candidate set (n₄ ≈ 2–4) feeding Ch 6.
>
> *Addresses: REQ-12.5, REQ-12.4.*

## 4.4 Mapping over the four DoW parameter families

> The DoW T6.3 names four parameter families with co-impact on sustainability, reliability and cost. Each subsection presents the Pareto cuts along that axis.

### 4.4.1 Aluminium thickness and feedstock

> **TBD.** Aluminium thickness is currently fixed at 0.8 mm in the pressing pipeline (D6.1 §4.1 justification). Discuss whether the Pareto front motivates revisiting this; report which thickness × cup-geometry combinations achieve the 50 % aluminium reduction target (SO9). If recycled-aluminium feedstock has been characterised (TASKS A1.5 / DoW 3.3c), include it as a discrete parameter; otherwise note the open item.
>
> *Addresses: REQ-12.2(1), REQ-14.4.*

### 4.4.2 Floater shape

> **TBD.** Discuss cup-eccentricity, cup-depth and cup-spacing trade-offs and how they affect mechanical robustness in higher SSCs (the SSC 5 ambition under DoW SO4) and aluminium consumption. Cross-reference §5.2 here.
>
> *Addresses: REQ-12.2(2), REQ-14.2.*

### 4.4.3 Floater size

> **TBD.** Discuss how PV-module class (2384 × 1303 mm vs. 1770 × 1770 mm Gen 1-class) drives the floater outer envelope and unit cost (cabling, factory operations, module per m²). Note the cross-domain effects flagged in TASKS A4.2 (mechanical strength, walkability, hinge sizing) once Eirik confirms.
>
> *Addresses: REQ-12.2(3).*

### 4.4.4 Cup design

> **TBD.** Discuss cup geometry (radius, depth, tip radius, lip radius, eccentricity, angle, spacing) trade-offs with respect to homogeneous water cooling for improved performance and reliability. Tie back to the IFE thermal CFD findings (D6.1 §5.2): which cup geometries keep the PU below 70 °C under the worst-case Singapore boundary?
>
> *Addresses: REQ-12.2(4), REQ-14.3, REQ-14.5.*

---

# 5 Constraint application — FDS and DoW KPIs

> Reuses the FDS table from D6.1 §3.2. Each subsection reports how the surviving candidates score against the binding constraint.

## 5.1 FDS coverage

### 5.1.1 Principal functions (FP1, FP2)

> **TBD.** Verify FP1 (produces power) and FP2 (is certified). FP1 is satisfied by panel selection; for FP2 link to the targeted certification standard once known (TASKS A1.4).

### 5.1.2 Constraint functions (FC1–FC9)

> **TBD.** Verify each of FC1 (flotation), FC2 (watertight), FC3 (mechanical attachment), FC4 (resistance to submergence under 3 m/s current), FC5 (panel-supplier flexibility), FC6 (resistance to high wind), FC7 (resistance to waves up to 1.5 Hs), FC8 (cost competitiveness), FC9 (electrical grounding) against each candidate. Tabulate pass/fail.

### 5.1.3 Secondary functions (FS1–FS3)

> **TBD.** Verify FS1 (walkability), FS2 (fast production), FS3 (fast installation).

### 5.1.4 Summary table

> **TBD.** One row per candidate × FP/FC/FS, pass/fail with brief reason.
>
> *Addresses: REQ-14.1.*

## 5.2 Hydrodynamic loading — FC4, FC7, SSC 5 ambition

### 5.2.1 FC4 — current resistance up to 3 m/s

> **TBD.** Report behaviour under 3 m/s current loading per candidate; note the role of "head" FPV concept from FDS (a leading unit shielding the string).

### 5.2.2 FC7 — wave resistance up to Hs = 1.5 m

> **TBD.** Report stress and deformation under Hs = 1.5 m wave loading per candidate.

### 5.2.3 SSC 5 ambition (Hs 2.5–4 m, DoW SO4)

> **TBD.** Where 3DFloat → SiSim is online (§3.7), report behaviour at the SSC 5 envelope and discuss residual margin. If the coupling is not online, state how the SSC 5 ambition will be addressed in D6.4.
>
> *Addresses: REQ-14.2, REQ-13.5.*

## 5.3 Thermal stability — PU ≤ 70 °C

### 5.3.1 Reference findings from D6.1

> **TBD.** Recap from D6.1 §5.2: dark blue PU (A ≈ 0.88–0.91, peak ≈ 84 °C, fails 70 °C limit) → off-white PU (A ≈ 0.35, peak ≈ 48 °C, passes).

### 5.3.2 Per-candidate peak PU temperature

> **TBD.** Pull peak PU temperature from the CFD for each candidate; tabulate. Confirm all selected candidates use off-white PU.

### 5.3.3 Sensitivity to off-white absorptivity measurement

> **TBD.** Once the actual off-white PU absorptivity is measured (TASKS B2.1), report the difference vs. the assumed 0.35 and whether any candidate's pass/fail flips.
>
> *Addresses: REQ-14.3, REQ-13.3.*

## 5.4 Aluminium reduction — SO9

### 5.4.1 Per-candidate aluminium mass

> **TBD.** Aluminium mass per unit for each candidate, broken down by component (bottom plate, frame).

### 5.4.2 Reduction vs. Gen 1 reference

> **TBD.** Ratio of candidate Al mass to the Gen 1 reference; whether the 50 % reduction target (DoW SO9 / 3.3c) is reached. If not, identify the parameter changes that would reach it and the trade-off.

### 5.4.3 Recycled-aluminium option

> **TBD.** State whether recycled-aluminium feedstock has been characterised and incorporated as a discrete parameter in the screening (DoW 3.3c). If not, list what is needed to add it.
>
> *Addresses: REQ-14.4.*

## 5.5 Thermal loss reduction — SO3

### 5.5.1 Method

> **TBD.** Combine CFD-predicted peak module temperature with the Faiman model to estimate energy yield change relative to the Gen 1 baseline.

### 5.5.2 Per-candidate result

> **TBD.** Predicted thermal-loss change at module level for each candidate (target ≈ 3 % reduction).
>
> *Addresses: REQ-14.5.*

## 5.6 Polymer UV stability

### 5.6.1 Accelerated weathering programme status

> **TBD.** Summarise the IFE campaign on white PU on Prototype 3 hinges (IEC TS 62788-7-2 condition A1, started after the dark-blue dark-blue 209 h failure described in D6.1 §5.3.2). Report current exposure hours and status.

### 5.6.2 Mechanical strength after exposure

> **TBD.** Once the UV exposure ends, report shear strength of the PU-glass interface (long sides) and tensile strength of the loose hinges. Compare with as-cast (unexposed) baseline.

### 5.6.3 Implication for candidate selection

> **TBD.** State whether the candidate selection is robust to plausible UV-degradation outcomes, or whether selection is provisional pending the UV verdict.
>
> *Addresses: REQ-14.6.*

---

# 6 Selected prototype candidates

## 6.1 Selection methodology

> **TBD.** Restate the selection rule: from the Stage-3 survivors (Section 4.3), apply Stage 4 engineering judgement against the constraints in Section 5 to arrive at 2–4 promising candidates. Explain how trade-offs were resolved (e.g. lighter aluminium vs. larger structural margin).
>
> *Addresses: REQ-15.1.*

## 6.2 Candidate A — [name]

### 6.2.1 Forming parameters

> **TBD.** The nine pressing parameters: cup radius, cup depth, eccentricity, angle, tip radius, lip radius, spacing, sheet thickness, forming pressure. Reference the corresponding row in `collect.csv` (input_hash) for traceability.

### 6.2.2 Floater outer envelope and PV-module class

> **TBD.** Outer envelope dimensions; chosen PV-module class (2384 × 1303 mm or 1770 × 1770 mm); cup count tiled across the floater.

### 6.2.3 Component concept

> **TBD.** Infill concept (cup-air pockets / PU foam puzzle-fit / other), hinge/connector concept (P4 reference geometry or successor), float-structure casting approach (cast-on-frame vs. separate-and-mount per TASKS B3.3).

### 6.2.4 Bill of materials per unit

> **TBD.** Al sheet (mass, alloy, thickness, dimensions), PU (mass), PU foam (mass), silicone (mass), cabling (length × type), panel (model). Mirror the Prototype 3 baseline structure transferred to TNO under I-5 (D6.1 §6.3).

### 6.2.5 Performance scorecard

> **TBD.** Per-axis result against the six Pareto axes from §4.1: forming feasibility (margin to manufacturability boundary), Al mass, structural margin, peak PU temperature, LCA impact (if available from §8), cost. Tabulate.

### 6.2.6 Rationale for inclusion

> **TBD.** Which constraint set drove this choice (e.g. lowest Al mass; largest structural margin; best LCA; best balance). What trade-offs were accepted.
>
> *Addresses: REQ-15.1, REQ-15.2.*

## 6.3 Candidate B — [name]

### 6.3.1 Forming parameters

> **TBD.**

### 6.3.2 Floater outer envelope and PV-module class

> **TBD.**

### 6.3.3 Component concept

> **TBD.**

### 6.3.4 Bill of materials per unit

> **TBD.**

### 6.3.5 Performance scorecard

> **TBD.**

### 6.3.6 Rationale for inclusion

> **TBD.**

## 6.4 Candidate C — [name] (if applicable)

### 6.4.1 Forming parameters

> **TBD.**

### 6.4.2 Floater outer envelope and PV-module class

> **TBD.**

### 6.4.3 Component concept

> **TBD.**

### 6.4.4 Bill of materials per unit

> **TBD.**

### 6.4.5 Performance scorecard

> **TBD.**

### 6.4.6 Rationale for inclusion

> **TBD.**

## 6.5 Recommended hand-off to Task 6.4

> **TBD.** Identify which candidate is recommended for the Sunlit P5/P6 prototyping track and which are retained as fall-backs. State the conditions under which a fall-back would be promoted (e.g. casting yield issues with primary, UV results disqualifying primary).
>
> *Addresses: REQ-15.3.*

## 6.6 Modularity work with Metsolar

> **TBD.** Document how the candidate set spans the PV-module classes considered, and any BOM alternatives surfaced through the Metsolar collaboration and Sunlit's BOM compendium (new optical components, PV cells, prismatic glass).
>
> *Addresses: REQ-15.4.*

---

# 7 Validation plan

## 7.1 Lab-scale forming trials

### 7.1.1 Objective

> **TBD.** Close the process-transfer uncertainty between punch/die-calibrated friction and fracture parameters (D6.1 §4.5) and the hydroforming process actually used.

### 7.1.2 Method

> **TBD.** Hydroforming trials on the candidate cup geometry building on the epoxy-mould proof-of-concept (D6.1 §4.5). State sample preparation, edge sealing, water injection pressure, instrumentation.

### 7.1.3 Owner and timeline

> **TBD.** Sunlit-led activity. Indicative dates and dependency on press-tool vendor.

### 7.1.4 Acceptance criterion

> **TBD.** Successful forming of the chosen candidate(s) without tearing/buckling, with thinning within the simulated envelope.
>
> *Addresses: REQ-16.1.*

## 7.2 Mechanical test rig on cast-PU prototypes

### 7.2.1 Test matrix recap

> **TBD.** Six load cases (XY bending, XZ bending, XY compression, XY stretch, YZ bending, XZ shear) and six measurement points at key interfaces (D6.1 §5.3.3).

### 7.2.2 Sequence — P4 first, then P5

> **TBD.** Run the matrix on P4 once cast, then on the down-selected P5 candidate. State the comparison cadence.

### 7.2.3 Comparison with SiSim

> **TBD.** Compare measured deformations and failure modes against SiSim predictions at the matching load cases. Report deltas and flag any model recalibration needed.

### 7.2.4 Owner and timeline

> **TBD.** Sunlit-led, IFE simulation support.
>
> *Addresses: REQ-16.1.*

## 7.3 UV exposure and adhesion testing

### 7.3.1 Continuation of the IFE programme

> **TBD.** Continuation of the IFE programme on white PU on Prototype 3 hinges (TASKS B2.3, B2.4). State the chamber conditions (IEC TS 62788-7-2 condition A1) and the planned exposure duration.

### 7.3.2 Post-exposure tests

> **TBD.** Shear testing of PU-glass on long sides; tensile testing of the loose hinges. Add gravimetric measurement of moisture ingress.

### 7.3.3 Implication for candidate selection

> **TBD.** Report whether the candidate selection is robust to the UV verdict, or whether the selection is provisional.
>
> *Addresses: REQ-14.6, REQ-16.1.*

## 7.4 100 kW pilot at Singløya Nord

### 7.4.1 Hand-off to Task 6.4

> **TBD.** The recommended candidate becomes the basis for the next-generation press tool (DoW T6.4) and ultimately the ~100 kW pilot at Singløya Nord.

### 7.4.2 Dependencies

> **TBD.** Press-tool vendor readiness; casting vendor confirmation; deployment site permitting; mooring/anchoring scope.

### 7.4.3 Indicative timeline

> **TBD.** From candidate hand-off (M24) to pilot installation (DoW M34, D6.4).
>
> *Addresses: REQ-7.1 (D6.1), REQ-16.1.*

## 7.5 Open validation items

> **TBD.** Bulleted list of the validation items not yet closed at M24, the responsible partner, and the expected date. Cross-reference TASKS B2.x and B3.x.
>
> *Addresses: REQ-16.2.*

---

# 8 Sustainability dimension

## 8.1 LCA inputs delivered to TNO

### 8.1.1 Per-candidate unit-level BOM

> **TBD.** Aluminium bottom plate (mass, alloy, thickness, dimensions), PU, PU foam, silicone, return cable, grounding cable, panel — per candidate. Mirror the Prototype 3 baseline structure transferred to TNO (D6.1 §6.3 I-5).

### 8.1.2 Project-level deployment inputs

> **TBD.** Mooring/anchoring (working assumption: four buoys, ≈ 160 m mooring rope, four anchoring chains, four anchors per 30 × 30 m² block), cabling, inverters (one per ≈ 330 kWp), transformers, ground works, deployment site (Singløya Nord).

### 8.1.3 Versioning

> **TBD.** Map each candidate to a design version traceable in the Sunlit FreeCAD repository / BOM compendium (cf. §3.6.4).
>
> *Addresses: REQ-17.1.*

## 8.2 Preliminary LCA outputs

### 8.2.1 Status at M24

> **TBD.** Whether TNO has delivered preliminary results within the M24 window (expected Q2 2026, TASKS B2.5).

### 8.2.2 Relative contributions to environmental impact

> **TBD.** If results are available: relative contributions of aluminium, PU, PU foam, panel, mooring, transport, etc. to the overall impact. Use as a screening dimension in §4.4 / §5.4.

### 8.2.3 Integration plan if results are not yet available

> **TBD.** If not yet available, state when results are expected and how they will be incorporated into a D6.2 revision or addendum.
>
> *Addresses: REQ-17.2.*

## 8.3 Reference methodology — Surewave D7.1

### 8.3.1 Functional unit

> **TBD.** 1 MWh of produced electricity (Surewave precedent).

### 8.3.2 System boundary

> **TBD.** Cradle-to-grave; production equipment and detailed recycling pathways excluded (per Surewave practice).

### 8.3.3 Deviations adopted for SuRE

> **TBD.** State any deviations from the Surewave pattern adopted in SuRE (e.g. inland Norwegian lake site instead of offshore; different hazards — ice, snow, flora/fauna instead of high salinity / wave loads).
>
> *Addresses: REQ-13.4, REQ-17.2.*

---

# 9 Conclusions

## 9.1 Pareto frontier delivered

> **TBD.** Recap of the screening outcome (numbers per stage), the identified Pareto front, and the most material trade-offs.
>
> *Addresses: REQ-11.1.*

## 9.2 Prototype candidates and rationale

> **TBD.** Recap of the selected candidates and the recommended primary for prototyping.
>
> *Addresses: REQ-15.1, REQ-15.3.*

## 9.3 Hand-off to Task 6.4

> **TBD.** Status of the prototype design hand-off to T6.4 / D6.4.
>
> *Addresses: REQ-15.3.*

## 9.4 Contribution to SuRE objectives

> **TBD.** Tie back to SO3 (thermal-loss reduction), SO4 (SSC 5 validation), SO9 (50 % Al reduction, recycled-Al option), and the LCOE ambition.
>
> *Addresses: REQ-14.2, REQ-14.4, REQ-14.5.*

---

# 10 Open items and deviations from DoW

> **TBD.** Honest accounting of what was delivered against DoW T6.3 / D6.2, which interfaces in REQ-13.1–REQ-13.5 are still not "implemented" at M24, and the planned closure for each. Mirror the structure used in D6.1 §9.

---

# Appendices

## A. Updated interface table (full)

> **TBD.** Full updated version of D6.1 Table 6-1 with M24 status column.

## B. Per-candidate datasheets

> **TBD.** One page per candidate: parameters, BOM, scorecard, rendered geometry, deviation notes.

## C. Material model parameters used in candidate evaluation

> **TBD.** Final calibrated Yld2003 anisotropy coefficients, Voce hardening parameters, friction coefficient and fracture threshold values used in the simulations underlying the Pareto front. Source dataset (Speira vs Oslomet) confirmed per TASKS A4.1.

## D. Glossary and abbreviations

> **TBD.** As in D6.1 (FPV, PV, PU, SSC, FDS, FP/FC/FS, etc.) plus any new D6.2 terms.

---

# Skeleton notes (delete before submission)

- Sections marked **TBD** are placeholders. Each cites the requirements it must satisfy (`REQ-x.y` from `requirements.md`); use those as the acceptance check.
- The skeleton intentionally does not duplicate D6.1 content. Cross-references to D6.1 are used where the underlying material is unchanged (Ch 2, §3.2 FDS, §4.1 design parameters, §6.3 interfaces, §7 screening).
- Open dependencies on Eirik / Nathan / TNO are tracked in `TASKS.md` (Part B). Several sections here cannot be closed until those answers come in — flag the dependency in the section, don't hide it.
- When ready to draft, copy this file to `report_d6.2_v1.md` (or similar) and start filling sections in order: Ch 2 → Ch 3 → Ch 4 → Ch 5 → Ch 6 → Ch 7 → Ch 8 → Ch 9 → Ch 10 → Executive Summary → Appendices.
