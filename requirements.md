# Requirements for D6.1 — Sunlit Model Chain

Derived from: SuRE Technical Description (Annex 1) and D1.1 Monitoring Concepts (28.02.2025).
These requirements are written as if the deliverable does not yet exist.

---

## 1. Scope and purpose

**REQ-1.1** D6.1 shall provide data-format and inter-model data-transfer specifications for the Sunlit modelling chain, as stated in the Description of Work deliverable table.
*Source: DoW deliverable table, D6.1 description.*

**REQ-1.2** D6.1 shall document the outcomes of Task 6.1 (FEM model development for aluminium pressing) and Task 6.2 (model harmonisation and interfacing for digital product development), as these are the two tasks feeding into D6.1.
*Source: DoW T6.1 and T6.2 descriptions.*

**REQ-1.3** D6.1 shall address Objective O6.1.1: developing a digital product development cycle for Sunlit's aluminium floater.
*Source: DoW WP6 objectives.*

**REQ-1.4** D6.1 shall provide a foundation for Objective O6.2.1: optimised selection of a next-generation floater prototype, to be completed in D6.2.
*Source: DoW WP6 objectives.*

---

## 2. The aluminium pressing model (T6.1)

**REQ-2.1** D6.1 shall describe a finite element model for simulation of the aluminium float pressing (hydroforming) process.
*Source: DoW T6.1 — "FEM model development for pressing of aluminum, central to Sunlit manufacturing."*

**REQ-2.2** The FEM model shall handle large plastic deformations occurring during sheet metal forming.
*Source: DoW T6.1 — "numerically challenging large metal deformations."*

**REQ-2.3** The FEM model shall support an anisotropic yield stress model to account for the grain direction in rolled aluminium sheet.
*Source: DoW T6.1 — "anisotropic yield stress model."*

**REQ-2.4** The FEM model shall provide outputs usable as inputs to downstream models in T6.2 (structural, thermal, LCA).
*Source: DoW T6.1 — "Results are used in Tasks 6.2 and further in 6.3-4."*

**REQ-2.5** D6.1 shall report results from the aluminium pressing model sufficient to characterise the feasible design space for the float cup geometry.
*Source: DoW T6.3 — parameter space exploration depends on T6.1/T6.2 outputs; key parameters include aluminium thickness, floater shape, floater size, cup design.*

---

## 3. Model harmonisation and inter-model interfaces (T6.2)

**REQ-3.1** D6.1 shall define interfaces between the following four modelling tools:
- (i) Combined FEM and CFD mechanical stress model for the float under a given design case (developed in WP2, Task 2.3, IFE)
- (ii) CFD model of fluid and heat flows (developed in WP3, Task 3.2, IFE)
- (iii) FEM model of aluminium pressing (developed in T6.1, IFE)
- (iv) LCA model (developed in WP1, Task 1.3, TNO)

*Source: DoW T6.2 — explicit list of four tools to be interfaced.*

**REQ-3.2** For each interface, D6.1 shall specify the data that is transferred: which parameters are outputs of the upstream model and inputs to the downstream model, and in what format.
*Source: DoW T6.2 — "harmonizing input and output data from the different models."*

**REQ-3.3** The inter-model data transfer specifications shall enable automated mapping of the parameter space and rapid iteration.
*Source: DoW T6.2 — "enable automated mapping of the parameter space and rapid iteration turnover."*

**REQ-3.4** D6.1 shall describe how the model chain supports screening of the design parameter space at multiple accuracy levels, trading off computational cost against fidelity.
*Source: DoW T6.2 — "modelling capabilities at different accuracy-levels will be used actively to quickly screen the parameter space and converge to promising design candidates."*

---

## 4. Key design parameters to be covered

**REQ-4.1** The modelling framework documented in D6.1 shall cover the following design parameters as the primary variables for optimisation:
- Aluminium sheet thickness (and potential use of recycled aluminium feedstock)
- Floater shape (for mechanical robustness and/or reduced aluminium consumption)
- Floater size (effect on unit costs)
- Cup design (homogeneous cooling, structural performance, manufacturing feasibility)

*Source: DoW T6.3 — listed as "key design parameters for exploration because of co-impact on sustainability, reliability, and cost."*

**REQ-4.2** The framework shall support evaluation of these parameters with respect to at least three performance dimensions simultaneously: sustainability (aluminium consumption, LCA), reliability (structural performance, durability), and cost efficiency (LCOE drivers).
*Source: DoW T6.3 — "co-impact on sustainability, reliability, and cost."*

---

## 5. Data format and traceability

**REQ-5.1** D6.1 shall define a structured data format for simulation inputs and outputs that enables consistent comparison across design iterations.
*Source: DoW T6.2 — "harmonizing input and output data."*

**REQ-5.2** Each simulated design variant shall be uniquely identifiable, enabling traceability from input parameters through simulation outputs to any derived performance metrics.
*Source: DoW T6.2 — rapid iteration implies traceability of design variants.*

**REQ-5.3** Data formats shall be compatible with the long-format structured data approach recommended by D1.1, with fields for: unique design identifier, parameter name, value, unit, and data source (simulation or test).
*Source: D1.1 Section 5 — recommended data structure for consistent comparison and large-scale analysis.*

**REQ-5.4** Timestamps and version identifiers shall follow ISO 8601 format where applicable.
*Source: D1.1 Table 4 — recommended data format standard.*

---

## 6. Validation

**REQ-6.1** D6.1 shall describe how model predictions are validated against physical test data.
*Source: DoW T6.4 — "Prototype testing in wave-tank with extra sensors will validate simulated results."*

**REQ-6.2** The validation approach shall demonstrate agreement between simulated and observed outcomes for the aluminium pressing model.
*Source: DoW T6.1 — the FEM model must produce results used in subsequent tasks, implying demonstrated reliability.*

**REQ-6.3** Validation data used in D6.1 shall be traceable to physical experiments on Sunlit prototypes or to the ~100 kW pilot installation at Singløya Nord, Norway.
*Source: DoW T6.4 and D1.1 executive summary — "build an approximately 100 kW pilot installation."*

---

## 7. Pilot and deployment context

**REQ-7.1** D6.1 shall be consistent with the planned ~100 kW pilot installation at Singløya Nord, Norway, as this is the reference deployment for which the modelling framework is being developed.
*Source: DoW T6.4 — "Sunlit will build an approximately 100 kW pilot installation by the end of SuRE"; D1.1 executive summary confirms 100 kW scale.*

**REQ-7.2** The modelling framework shall support design for deployment in exposed coastal/marine environments with wave loading up to Hs = 1.5 m (Sea State Class 5, 2.5–4 m) as required for DNV certification.
*Source: DoW SO4 — "Validate Sunlit design up to SSC 5 with respect to structural integrity and moisture ingress."*

---

## 8. Environmental boundary conditions

**REQ-8.1** The thermal modelling component shall use representative environmental boundary conditions including solar irradiance, air temperature, water temperature, and wind speed.
*Source: DoW T6.2 (ii) — "CFD modelling of fluid and heat flows"; D1.1 Tier 1 monitoring parameters — wind and water temperature are mandatory measurement inputs.*

**REQ-8.2** The structural modelling component shall use wave and current loading as boundary conditions, consistent with the hydrodynamic parameters defined as Tier 1 monitoring variables in D1.1.
*Source: D1.1 Table 1 — hydrodynamics (waves, water movement, currents) are Tier 1 mandatory parameters.*

**REQ-8.3** Worst-case environmental scenarios shall be defined and used to evaluate model outputs against material and structural limits.
*Source: DoW SO4 — structural integrity validation requirement; DoW T6.3 — need to identify limits of design space.*

---

## 9. LCA integration

**REQ-9.1** D6.1 shall describe the interface between the engineering models and the LCA model developed by TNO (WP1, Task 1.3), at minimum defining which parameters flow from the design/simulation domain to the LCA domain.
*Source: DoW T6.2 — LCA (TNO WT1.3) is explicitly listed as the fourth modelling tool to be interfaced.*

**REQ-9.2** Material consumption outputs from the aluminium pressing model (e.g. sheet thickness, cup geometry, thinning distribution) shall be made available in a format compatible with LCA input requirements.
*Source: DoW T6.2 — data harmonisation between forming model and LCA model.*

---

## 10. Dissemination and format

**REQ-10.1** D6.1 shall be delivered as a written report (type R) at dissemination level SEN (sensitive/confidential to project partners).
*Source: DoW deliverable table.*

**REQ-10.2** D6.1 was due at Month 20 of the project.
*Source: DoW deliverable table.*

---

## Notes on scope boundaries

The following topics are **not** in scope for D6.1 based on the DoW:
- Pareto frontier mapping and prototype selection (→ D6.2)
- Module cost and efficiency improvements (→ D6.3, Metsolar)
- Pilot installation and field data (→ D6.4)
- Environmental monitoring of the waterbody (→ WP1/D1.x)

D6.1 provides the modelling infrastructure that D6.2 (Pareto mapping) depends on.
