# TASKS

## Completed
- [x] Gen 2 parametric design / prototyping work elaborated — new paragraph added to Section 3.5 describing FreeCAD mould workflow, 3D-print-to-metal-mould progression, P1–P4+ series, and vendor visit
- [x] Executive summary rewritten — now describes D6.1 content (simulation pipeline, thermal/structural modelling, experimental work, model chain); SuRE project framing removed
- [x] "3.2 MWp pilot" claim removed from executive summary — size of pilot installation no longer stated

## Outstanding issues

### From gap analysis against requirements (requirements.md)
- [x] **T1: Anisotropic yield stress model and material characterization (REQ-2.3, also strengthens REQ-6.1/6.2)** — Done. Section 4.2 expanded from one "elasto-plastic" sentence to six paragraphs covering the material (AA5083-H111), the constitutive model (Yld2003 / *MAT_WTM_STM with Voce hardening), the calibration basis (ISO 10113/16808/12004-2), the measured r-values and their implications, and the *PERTURBATION/Karhunen–Loève necking trigger with critical thickness strain fracture criterion. Section 4.5 strengthened with calibration against the known Gen 1 forming envelope (38.5 mm / 40 mm) and the two-parameter cup-depth-vs-drawbead study as methodological precursor. Section 4.1 cup eccentricity rationale rewritten to cite the measured anisotropy pattern explicitly. No external parties named and no formal citations added (Yld2003 and Voce are named by their standard technical labels only).
  - [x] **T1a: Constitutive model description (Section 4.2)** — Done. New paragraphs describe Yld2003 as a non-quadratic anisotropic yield function implemented in LS-DYNA as *MAT_WTM_STM with eight anisotropy coefficients, paired with a Voce hardening law, and cite the measured r-values (r0 ≈ 0.66, r45 ≈ 0.84, r90 ≈ 0.71, r_biaxial ≈ 1.09) and their directional implications.
  - [x] **T1b: Material and characterization paragraph (Section 4.2)** — Done. New paragraph introduces AA5083-H111 (marine-grade, corrosion resistance, high thermal conductivity used as thermal bridge), sheet thicknesses (1.5 mm historical / 0.8 mm current target), and the ISO 10113:2020 / ISO 16808:2014 / ISO 12004-2:2009 calibration basis. Presented as Sunlit Sea activity with no external attribution.
  - [x] **T1c: Necking trigger, fracture criterion and calibration against Gen 1 envelope (Sections 4.2 and 4.5)** — Done. Section 4.2 documents *PERTURBATION with Karhunen–Loève spectral decomposition, characteristic length and amplitude, Marciniak–Kuczyński interpretation, and critical thickness strain fracture criterion. Section 4.5 now explicitly describes calibration against 38.5 mm / 40 mm Gen 1 envelope with the specific parameter values (μ ≈ 0.085, εt,cr ≈ −0.45), and mentions the ~30-simulation two-parameter study of cup depth vs drawbead distance as the methodological precursor to the nine-parameter iterative boundary search.
  - [x] **T1d: Link cup eccentricity (cup_y_to_x) to measured anisotropy (Section 4.1)** — Done. Cup eccentricity bullet rewritten to explicitly cite the orthotropic plastic behaviour and the directional r-value pattern (thinning prone along transverse, most formable along diagonal), framing cup_y_to_x as a physically motivated parameter that allows the forming process to exploit favourable strain-ratio directions for deeper cups and greater buoyancy per unit material.
- [x] **T2: LCA interface (REQ-3.1, 9.1, 9.2)** — Resolved together with T3d. Section 5.4.2 expanded with SUREWAVE methodology precedent, cradle-to-grave scope, 1 MWh functional unit reference, and baseline inventory delivery to TNO. Detailed interface description written as I-5 in Section 6.3.
- [x] **T3: Formal data-format / interface specifications (REQ-1.1, 3.2)** — Ch 6 describes the model chain conceptually but does not provide actual format specs. Core mandate of D6.1 per DoW. Add a structured section (table per interface) to Ch 6.3 covering the four DoW-required interfaces plus the internal pressing→ML interface. Subtasks:
  - [x] **T3a: I-2: CAD → Structural FEM (SiSim/IFE)** — PARTIAL, operational but unspecified. Document: STEP format, which geometric simplifications IFE applies before import (screw holes etc.), how material properties (E, ν, ρ) are communicated alongside the geometry.
  - [x] **T3b: I-3: Pressing FEM (as-formed) → Structural FEM** — MISSING, not implemented. Document the conceptual spec: thickness distribution field from LS-DYNA output, how it maps to the structural mesh, acknowledge as not yet implemented and flag for D6.2.
  - [x] **T3c: I-4: CAD + surface properties → Thermal CFD (IFE)** — PARTIAL, inputs named but format unspecified. Document: how geometry reaches the CFD model (STEP assumed), how surface property values (A=0.88–0.91, ε=0.85) are communicated, what the CFD model returns as output.
  - [x] **T3d: I-5: WP6 models → LCA (TNO)** — Done. Section 6.3 expanded with I-5 prose: SUREWAVE methodology precedent, per-unit bill of materials (aluminium bottom plate spec, 12 kg PU, 2 kg PU foam, 0.2 kg silicone, cabling), project-level components (mooring, anchoring, inverters, transformers, ground works), inland Norwegian lake site hazards (ice, snow, ice cast), baseline delivery to TNO based on Prototype 3 of Gen 2, iterative update path. TODOs for TNO on template, functional unit, versioning. Also updated I-5 row in Table 6-1. Resolves T2.
  - [x] **T3e: I-6: Pressing FEM CSV → ML model** — Done. Section 4.3 now documents the CSV schema: input_hash key, nine input fields (cup_rad, cup_lip, cup_depth, cup_angle, cup_y_to_x, cup_tip, space, alu_thick, pressure), three output fields (time_to_crack, lip_mean, edge_mean), and the collect.csv / collect_full.csv split.
- [x] **T4: Singapore worst-case scenario not named in report body (REQ-8.3)** — Done. Sec 5.2.3 now names Singapore (1.25°N, 104°E), the 5-year ERA5 source, and the full worst-case values (GHI 943 W/m², T_air 28.1°C, T_water 21.5°C, wind 0.5 m/s), plus the Faiman-model module temperature range (60.2–61.3°C). Section 6.3 I-4 block trimmed to reference 5.2.3 instead of repeating values.
- [x] **T5: Floater size as design variable (REQ-4.1)** — Done. Section 4.1 now explains that floater size is architecturally out of scope for the pressing simulation (each run represents one cup), is determined at the system level by PV panel choice (Section 2.2.1), and is systematically addressed in the LCA work (Section 5.4.2 / I-5) where it drives material totals, production effort and plant layout.

### Pre-existing
- [x] **T8: Clarify punch/die vs hydroforming process transition (Sections 4.2 and 4.5)** — Done. Section 4.2 now explains that Gen 1 used a conventional punch/die press and Gen 2 targets hydroforming, with the reason (tooling flexibility and cost). Section 4.5 calibration paragraph split into three paragraphs: (1) material constants are process-independent and transfer directly; (2) friction/fracture calibration was done against Gen 1 punch/die data; (3) explicit process-transfer caveat — contact mechanics differ between punch/die and hydroforming, recalibration against hydroforming trials is needed when production tooling becomes available.
  - [x] **T8a: Section 4.2** — Done.
  - [x] **T8b: Section 4.5** — Done.
- [ ] **T6: No references section** — build a references section for the report. **Constraint:** do NOT include the OsloMet/Tveit ESAFORM/ECCOMAS/thesis publications or the Speira material card. Existing body references (e.g. Roosloot, Selj, Otnes, IEEE J. Photovoltaics 2024 on edge sealant durability) should be formalised. Decide with the user whether to include foundational method references (Aretz 2005 on Yld2003, Voce 1948 on hardening) if T1 cites them.
- [ ] **T7: Mermaid flowcharts embedded as raw code** — user will render later

## Chapter mapping (final)
- Ch 1: Introduction
- Ch 2: System Architecture
- Ch 3: Product Development Framework and Design Domains (merged old 3+4)
- Ch 4: FEM Model Development for Aluminium Float Pressing (was 5)
- Ch 5: Thermal, Mechanical and Economic Modelling (was 6, renamed)
- Ch 6: Model Harmonisation and Digital Product Development (was 7)
- Ch 7: Screening of the Design Parameter Space (was 8)
- Ch 8: Conclusions (was 9)
- Ch 9: Deviation from Description of Work (was 10, condensed)

