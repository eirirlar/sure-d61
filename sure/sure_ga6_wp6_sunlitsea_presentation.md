---
title: "SuRE WP6 — Sunlit Sea update"
subtitle: "Third General Assembly"
author: "Eirik Larsen, Sunlit Sea"
---

## Where we are in the Gen2 development cycle

- WP6 frames the work as a **model-supported development cycle**:
  - parametric FreeCAD design →
    - prototype →
      - test →
        - simulation feedback →
          - revised design
- Gen1 → Gen2 transition driven by manufacturability, buoyancy and load-transfer findings
- Prototype track so far: P1 → P2 → P3 → P4 (PU cast onto mock glass + bottom plate + frame)
- P3 is built and under testing; P4 is the next iteration — design closed, mold in FreeCAD, casting trial upcoming

::::: {.columns}
:::: {.column width="50%"}
![P3 parametric CAD model](images/gen2_prototype3_freecad_model.png){width="100%"}
::::
:::: {.column width="50%"}
![P4 parametric CAD model](images/gen2_prototyp4_freecad_model.png){width="100%"}
::::
:::::

## Prototype 4 — design changes

- **Hinge geometry revised** — left/right halves joined by a connecting rod, shifting load transfer toward the centre and away from the PU–glass and PU–aluminium interfaces
- **Buoyant PU foam rods on all four sides** — dual function: unit-to-unit connector *and* added buoyancy (addresses freeboard issue flagged by IFE)
- **Infill concept revised** — puzzle-fit multi-piece PU foam eliminates air cavities around junction boxes; pressed-aluminium bottom as integrated infill also under evaluation
- **Mold redesigned** accordingly — clamp-style connector with snap-fit hooks, screw and spring

::::: {.columns}
:::: {.column width="50%"}
![P4 left hinge geometry](images/gen2_prototyp4_freecad_hinge_left.png){width="100%"}
::::
:::: {.column width="50%"}
![P4 buoyant 4-side connector concept](images/gen2_prototyp4_freecad_connector_buoyant_PUfoam_rods_4sides.png){width="100%"}
::::
:::::

## IFE structural simulations on P3 — what we learned

IFE (Fjær, Noorsumar) built a 3D FEM model of the P3 floater in **SiSim**, driven by a STEP file exported from our parametric FreeCAD model — a working instance of the CAD-to-FEM data flow committed to in WP6.

**Key findings (10 mm imposed horizontal elongation):**

- Largest stresses in the **thin aluminium bottom plate and frame** — aluminium close to yield
- **PU stresses well above yield** in parts of the float-structure
- Significant bending of the aluminium frame → high stresses in frame flange and bottom
- **Glass stresses very sensitive** to how the PV sandwich is attached to the frame (rubber inlay vs. glued)
- **Buoyancy:** prototype sits deep in the water, ~half the bottom plate submerged → **insufficient freeboard**

Note: IFE simulated **without the infill** — strengthening the case that infill is structurally necessary, not just an assembly convenience.

## How the IFE findings feed into P4

| IFE finding | Design response in P4 |
|---|---|
| Al and PU near/above yield — simulated without infill (expected result) | Confirms infill is structurally necessary; next step: select one infill candidate with IFE for detailed FEM — likely PU foam with adhesive bonding to glass and bottom |
| Insufficient freeboard / deep submergence | Adjusting rod dimensions; considering with IFE whether to introduce an angled-through bottom plate shape so the bottom rests toward the water surface rather than protruding above it — increasing infill volume and buoyancy |
| Glass stresses sensitive to panel–frame attachment method | Float-structure and hinge design in P4 revised to route loads away from PU–glass and PU–Al interfaces; glass attachment treated as explicit design variable in next simulation |

This closes a full modelling loop: **CAD → STEP → IFE FEM → findings → revised parametric CAD → next prototype.**

## Mold design and casting — what we are testing next

- Molds designed in FreeCAD; **3D-printed mold → cast onto mock panel → inspect → revise → promote to metal mold**
- **P3 metal mold** already produced and cast — validates the workflow end to end
- **P4 mold** is the next test: clamp/snap-fit connector geometry with internal features not previously cast
- Casting vendor engagement (China visit) supports scale-up path

::::: {.columns}
:::: {.column width="50%"}
![P3 metal mold before casting](images/gen2_prototyp3_casting1.png){width="100%"}

![P3 metal mold after PU casting](images/gen2_prototyp3_casting2.png){width="100%"}
::::
:::: {.column width="50%"}
![P4 mold design in FreeCAD](images/gen2_prototyp4_freecad_mold.png){width="100%"}
::::
:::::

## Parallel testing activities on P3

Feeding back into P4 and subsequent iterations:

- **UV + adhesion on P3 samples (IFE)** — plan B adopted after tempered glass proved uncuttable; one full sample in UV chamber + loose hinges for tensile and shear testing
- **PU tensile + UV degradation** — earlier A3-condition test burned samples at ~95 °C; revised protocol at A1 condition (max ~75 °C on samples) to get clean 1000 h data
- **Thermal CFD (IFE, Lindholm)** drove the **dark blue → off-white PU** decision: worst-case hinge temperature drops from 83.8 °C to 48.3 °C under Singapore boundary conditions (70 °C limit)
- **Aluminium pressing pipeline** — ~3,900 forming simulations, ~1,300 Pareto-filtered points available as input to bottom-plate geometry choices

## Near-term plan and asks

**Next ~3 months**

- Cast and inspect **P4** from 3D-printed mold
- Complete P3 **UV + adhesion + tensile** test campaign (IFE)
- Rerun IFE structural FEM **with infill included** and with P4 geometry once casting is validated
- Feed updated material properties (PU after UV) back into structural and thermal models

**Asks to partners**

- IFE: timeline for the rerun with infill; any additional attachment-method sensitivity sweeps
- All: flag any wave-tank or field data from parallel WPs that can be used as load input for the next structural run

Thank you — questions welcome.
