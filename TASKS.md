# TASKS

## Completed
- [x] Gen 2 parametric design / prototyping work elaborated — new paragraph added to Section 3.5 describing FreeCAD mould workflow, 3D-print-to-metal-mould progression, P1–P4+ series, and vendor visit
- [x] Executive summary rewritten — now describes D6.1 content (simulation pipeline, thermal/structural modelling, experimental work, model chain); SuRE project framing removed
- [x] "3.2 MWp pilot" claim removed from executive summary — size of pilot installation no longer stated

## Outstanding issues

### From gap analysis against requirements (requirements.md)
- [ ] **T1: Anisotropic yield stress model (REQ-2.3)** — FEM section says "elasto-plastic constitutive models" only; DoW T6.1 explicitly required anisotropic yield. Add description of how LS-DYNA handles grain anisotropy, or acknowledge as deviation in Ch 9.
- [x] **T2: LCA interface (REQ-3.1, 9.1, 9.2)** — Resolved together with T3d. Section 5.4.2 expanded with SUREWAVE methodology precedent, cradle-to-grave scope, 1 MWh functional unit reference, and baseline inventory delivery to TNO. Detailed interface description written as I-5 in Section 6.3.
- [x] **T3: Formal data-format / interface specifications (REQ-1.1, 3.2)** — Ch 6 describes the model chain conceptually but does not provide actual format specs. Core mandate of D6.1 per DoW. Add a structured section (table per interface) to Ch 6.3 covering the four DoW-required interfaces plus the internal pressing→ML interface. Subtasks:
  - [x] **T3a: I-2: CAD → Structural FEM (SiSim/IFE)** — PARTIAL, operational but unspecified. Document: STEP format, which geometric simplifications IFE applies before import (screw holes etc.), how material properties (E, ν, ρ) are communicated alongside the geometry.
  - [x] **T3b: I-3: Pressing FEM (as-formed) → Structural FEM** — MISSING, not implemented. Document the conceptual spec: thickness distribution field from LS-DYNA output, how it maps to the structural mesh, acknowledge as not yet implemented and flag for D6.2.
  - [x] **T3c: I-4: CAD + surface properties → Thermal CFD (IFE)** — PARTIAL, inputs named but format unspecified. Document: how geometry reaches the CFD model (STEP assumed), how surface property values (A=0.88–0.91, ε=0.85) are communicated, what the CFD model returns as output.
  - [x] **T3d: I-5: WP6 models → LCA (TNO)** — Done. Section 6.3 expanded with I-5 prose: SUREWAVE methodology precedent, per-unit bill of materials (aluminium bottom plate spec, 12 kg PU, 2 kg PU foam, 0.2 kg silicone, cabling), project-level components (mooring, anchoring, inverters, transformers, ground works), inland Norwegian lake site hazards (ice, snow, ice cast), baseline delivery to TNO based on Prototype 3 of Gen 2, iterative update path. TODOs for TNO on template, functional unit, versioning. Also updated I-5 row in Table 6-1. Resolves T2.
  - [x] **T3e: I-6: Pressing FEM CSV → ML model** — Done. Section 4.3 now documents the CSV schema: input_hash key, nine input fields (cup_rad, cup_lip, cup_depth, cup_angle, cup_y_to_x, cup_tip, space, alu_thick, pressure), three output fields (time_to_crack, lip_mean, edge_mean), and the collect.csv / collect_full.csv split.
- [x] **T4: Singapore worst-case scenario not named in report body (REQ-8.3)** — Done. Sec 5.2.3 now names Singapore (1.25°N, 104°E), the 5-year ERA5 source, and the full worst-case values (GHI 943 W/m², T_air 28.1°C, T_water 21.5°C, wind 0.5 m/s), plus the Faiman-model module temperature range (60.2–61.3°C). Section 6.3 I-4 block trimmed to reference 5.2.3 instead of repeating values.
- [ ] **T5: Floater size as design variable (REQ-4.1)** — not systematically addressed in the parameter framework. At minimum note it as a parameter and why it was not varied in the current study.

### Pre-existing
- [ ] **T6: No references section**
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

