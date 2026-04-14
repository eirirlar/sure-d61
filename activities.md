# Adhesion testing

- To make testing relevant for modelling and promises made in WP6, focus on testing of hinges attached to rest of sample ("Larger samples") rather than individual tensile or lap shear tests
  - Note Hallvard: testing of small samples (e.g. individual tensile or lap shear tests) allows to identify local load bearing capacity and calibrate material properties in the model. Testing on larger samples (as described below) is good for model validation and identification of failure modes, but is limited to one load condition and results are more difficult to interpret.
    - Hallvard suggests mix of testing small and large samples. If only one type, he prefers small one since most likely clearer results.

- Larger samples: cut sample in individual pieces as on right
  - Easier handling and testing than with samples with several hinges on it

- Could fit about 8 samples inside UV
  - UV relevant to address sensitivity of sample design to ageing. Have done UV on different colour PU before, which might have different properties, and test ended prematurely due to too high testing T. Never tested adhesion after UV.
  - 4 samples with only chemical bonding and 4 with chemical and mechanical bonding
    - All with glass side facing up (Al side receives no UV in real life)
  - Can 'repurpose' samples into lap shear tests afterwards if we see the need

- Tensile testing:
  - Find weakest interface (hinge, Al-glass or Al-aluminium) and absolute strength for the two different bonding types
  - Compare strength with and without UV exposure
  - Chance that results not fully relevant for newest design since hinge design different


# Prototype 3 testing — email exchange (Nathan / Eirik / Hallvard)

Context: Testing of prototype 3 of Sunlit Sea's second generation product (the product being developed in SuRE).

## Email 1 — Nathan to Eirik

We tried to cut a sample, but the glass shattered immediately. It thus seems that the glass is tempered, which makes any cutting impossible. Our engineer will try with a glass cutter later this week, and if that works a colleague will start the UV. If not, I think the only possible UV testing would be to cut off all the hinges and fit the remaining 'box', plus a couple of loose hinges, inside the UV. We can then test adhesion between the glass/Al and PU, and tensile strength of the hinges. The adhesion testing between glass and PU requires cutting out strips of PU against the glass, which also has a risk of glass breakage, but can be worth the try.

Do you think it makes sense to go for this plan B if plan A does not work? If so, would you want a sample with or without mechanical bonding to go in the UV? There is only space for one.

I will think of other adhesion testing on full samples when I get back from holidays, but we might be limited by the size of the samples.

P.S. I think I identified the one sample with mechanical bonding. However, the entire cavity seems to be filled with PU rather than just a small area behind the holes (see images). The holes were therefore not clearly visible, but this is the only sample with PU in the cavity.

## Email 2 — Nathan to Eirik and Hallvard (9 March 2026)

We discussed plan B and decided to go for one sample without hinges in the UV (will be with chemical bonding only) plus some loose hinges. We will cut the hinges along the dotted lines in the image below, leaving the inner circle intact for the hinges on the short side. Then we can try to test overall adhesion against the sample by putting a pipe through that hole. The long sides will be available for shear testing with the glass only, and the loose hinges are for tensile testing. We will try cutting the glass on one more sample with the glass cutter, so if that somehow works, we stick to plan A. But think this is a quite good backup.

## Summary of testing approach

- Plan A: Cut samples into individual pieces for UV exposure and subsequent adhesion/tensile testing
- Plan A problem: Glass is tempered and shatters when cut
- Plan B (adopted): Remove hinges from one sample (chemical bonding only), fit remaining box + loose hinges in UV chamber
  - Long sides: shear testing (PU against glass)
  - Short sides: overall adhesion testing via pipe through hole
  - Loose hinges: tensile testing
  - One more attempt with glass cutter before committing to plan B


# Reference: Roosloot, Selj, Otnes (2024) — Edge sealant durability study

Paper: "Evaluating Durability of a Double Edge Sealant in a Floating Photovoltaic Application"
Published in: IEEE Journal of Photovoltaics, 2024
Authors: Nathan Roosloot, Josefine H. Selj, Gaute Otnes (all IFE)
DOI: 10.1109/JPHOTOV.2024.3417420

Context: Work done by IFE on Sunlit Sea generation 1 product. Relevant to generation 2 because the same methodologies (lap shear testing, UV exposure, adhesion evaluation) will be applied to test how PU bonds to glass and aluminium in the new design.

## What they studied
- Double edge sealant design (silicone outer + butyl inner) used in Sunlit Sea's integrated module-float FPV concept (Gen 1)
- Sealant placed between PV module glass and aluminium float
- Aluminium float forms impermeable backsheet; moisture can only enter from the perimeter

## Experimental approach
- Field samples: taken from a single float deployed 15 months in inner Oslofjord (salt water, calm conditions, 2.15 kWp prototype)
- Lab samples: lap shear test samples (glass-sealant-aluminium) mimicking fielded design
- Lab samples tested unexposed, after 1000h damp heat (85°C/85%RH), or after 1000h UV (IEC TS 62788-7-2 condition A3)
- Tested with and without aluminium anodization
- Glass was tempered — could not be cut (same problem encountered in P3 testing)

## Testing method
- Lap shear test (strength of attachment) + visual failure type classification (cohesive vs adhesive)
- Pull rate: 13 mm/min
- Field samples required horizontal pull setup (float too large for vertical tester); horizontal setup yielded ~68% of vertical force
- Statistical significance evaluated by t-test (p=0.05)

## Key findings
- Field samples: mean lap shear strength 4.7-7.1x lower than unexposed lab samples
- Field samples: failure type shifted from mostly cohesive (unexposed) to adhesive at aluminium-sealant interface
- Debonding observed visually along parts of float perimeter
- Damp heat (1000h): no significant loss in lap shear strength
- UV (1000h): significant loss in lap shear strength (factor 1.9-2.9 lower than unexposed for double sealant)
- UV: silicone failure shifted from cohesive to adhesive at glass-sealant interface
- Silicone provides most of the lap shear strength in the double sealant design (11-12x higher than butyl)
- Anodization: no significant effect on lap shear strength or failure type
- UV alone cannot fully explain field degradation — other stressors (salt, liquid water, thermomechanical loads) likely contributed

## Relevance to Gen 2 / SuRE
- Methodology (lap shear testing, UV exposure, adhesion classification) directly applicable to PU-glass and PU-aluminium interfaces in Gen 2
- Tempered glass cutting problem already encountered in Gen 1 — confirms P3 experience
- UV degradation of adhesion is a known risk that must be addressed in Gen 2 PU design
- Supports the need for adhesion testing after UV exposure (as planned in P3 testing campaign)


# IFE Thermal Simulation Presentation (Dag Lindholm, 11 August 2025)

Source: SuRE Presentation 2025-08-15.pptx (text extract; full pptx contains CAD model images of P3 and thermal simulation visualisations)

## Key requirement
- PU hinge temperature must not exceed 70°C

## Material properties measured at IFE
- Emissivity(PU) ~ 0.85 (measured with hand-held IR camera; reference: black tape ~ 0.9)
- Absorptivity(PU) ~ 0.9
- Two absorptivity values used in simulations: 0.35 (light-coloured PU, after colour change from dark blue to off-white) and 0.9 (dark PU)

## Boundary conditions
- Worst-case climate: Singapore (lat 1.25°, long 104°), 5 years ERA5 satellite data
- Worst-case weather instance: GHI = 943 W/m², T(air) = 28.1°C, T(water) = 21.5°C, wind = 0.5 m/s
- Top 5 module temperatures from Faiman model: 60.2–61.3°C

## CFD simulation results (Singapore worst case)

### Low absorptivity (0.35, light-coloured PU)
- Wafer layer: T(average) = 60.0°C, T(max) = 68.3°C
- Hinges: T(max) = 48.3°C → PASSES 70°C requirement

### High absorptivity (0.9, dark PU)
- Wafer layer: T(average) = 60.9°C, T(max) = 68.4°C
- Hinges: T(max) = 83.8°C → FAILS 70°C requirement by 13.8°C

## Design implication
- Colour change from dark blue to off-white PU was implemented based on these results
- Reduces hinge temperature from 83.8°C to 48.3°C under worst-case conditions
- This is a direct example of simulation-driven design decision in the development cycle

## Relevance to D6.1
- Concrete example of thermal modelling informing material selection (Chapter 5/old 6)
- Demonstrates the CFD modelling capability described in the report
- Shows real parameter values (absorptivity, emissivity) and boundary conditions
- Validates the framework: simulation identified a problem → design change implemented → problem resolved


# Code repository: thepressing — aluminium cup pressing simulation pipeline

Source: Sunlit Sea in-house code, uploaded as thepressing.zip. Stored in /home/claude/thepressing/.

## Overview
Sunlit Sea's simulation pipeline for optimising aluminium cup pressing on float structures. This is the actual implementation of the work described in WP6 report draft 2 (Arbeidsspor A) and the D6.1 deliverable Chapter 5.

## Architecture — four layers

### 1. Parametric geometry (FreeCAD + Python)
Core input class: FloatInput (floatinput.py) with 9 parameters:
- cup_rad (10–40 mm): radius of circle fitting one cup
- cup_lip (1 mm): fillet radius rounding off each cup
- cup_depth (5–40 mm): depth of each cup
- cup_angle (10–85 deg): steepness of curve inside cup
- cup_y_to_x (0.7–1.0): ellipse eccentricity ratio (relates to aluminium grain direction from rolling)
- cup_tip: radius of flat area at bottom of cup (0.2–0.8 x cup_rad)
- space (0–40 mm): spacing between cups
- alu_thick (0.8 mm): aluminium sheet thickness
- pressure (4–12): fluid pressure for hydroforming

All parameters have validation logic with min/max ranges and cross-parameter constraints (e.g. cup_rad must be > cup_depth).

Two geometry models:
- hexfloatmodel / hexfreecadmodel (hexagonal cup layout)
- rectfloatmodel / rectfreecadmodel (rectangular cup layout)

FreeCAD models are fully parametric, driven via Python API, export .STEP files.

### 2. LS-DYNA simulation
Handlebars templates (.k.hbs and .cfile.hbs) generate LS-DYNA keyword files for hydroforming simulation (fluid pressure pushing aluminium sheet into cup mould). fluiddiesimulator.py is the main driver — generates geometry, creates LS-DYNA input, runs simulation, collects results.

### 3. Pareto optimisation (paretooptimizer.py)
Custom iterative binary-search algorithm working on normalised parameter values (0–1). Process:
- Pick a parameter at random from current parameter group
- Binary search to find boundary between pass/fail
- If current design passes filters: push parameter toward harder territory
- If current design fails: push toward easier territory
- Track explored parameters; move through parameter groups in order (params_order)
- Data culling: remove redundant interior points, keep only boundary points along Pareto front

This is NOT the NSGA-II from the early pilot project README — the approach evolved into a custom algorithm.

### 4. Machine learning (neural.py)
- TensorFlow/Keras neural network with Hyperband hyperparameter tuning (keras-tuner)
- Trained on filtered dataset
- Predicts output parameters (especially pressure needed for successful forming) from geometric inputs
- Enables ML-guided sampling as third approach to generating candidates
- Genetic algorithm fallback (fluidiogenetic.py using deap library)

## Dataset sizes
- collect.csv: 1,334 rows (culled/filtered dataset along Pareto front)
- collect_full.csv: 3,927 rows (full unfiltered dataset)

## Output parameters tracked per simulation
- input_hash: unique identifier
- 8 input parameters (cup geometry + material + pressure)
- time_to_crack: key manufacturability metric — how far through simulation before fracture
- lip_mean: mean metric at cup lip region
- edge_mean: mean metric at cup edge region

## Supporting modules
- cupcalc.py, shouldercalc.py, hexcalc.py: geometric calculations
- volume.py, weight.py, areacalc.py: physical property calculations
- hinge.py, connector.py, structural.py, thermal.py: stubs for planned integration with other domains

## Relevance to D6.1 report
- Demonstrates a real, functioning simulation-driven design pipeline
- ~4,000 simulations have been run
- Shows the parametric CAD to FEM to analysis to ML loop described in the report framework
- The dataset sizes and parameter definitions provide concrete numbers that are currently missing from the report
- The stub files (structural.py, thermal.py) show planned but not yet implemented cross-domain integration — consistent with the deviation narrative in Chapter 9


# IFE PU UV preliminary results (Nathan Roosloot, 12 March 2025)

Source: Presentation "SuRE WP6: PU UV (preliminary) results"

## Samples tested
- 12 minipatches (PU cast around glass+aluminium, representing the hinge-to-panel interface), three hardnesses:
  - 4x 90A (Serial# 107–110)
  - 4x 80A (Serial# 206–209)
  - 4x 70A (Serial# 307–310)
- 4x PU sheets (20x15x0.2 cm), cut into 10x1.5 cm strips for tensile testing:
  - 2x B 70A
  - 1x B 80-85A
  - 1x C+ 85A (lower quality product)

## Testing plan
- Goals: test PU tensile strength and PU-glass/PU-Al adhesive strength as function of UV exposure; measure moisture ingress in minipatches after humidity exposure
- UV exposure: 1000h at condition A3 (chamber T=65°C, black panel T=90°C, irradiance 0.8 W/m² at 340nm, RH=80% — modified from standard 20% to test moisture ingress)
- 1000h UV dose equivalent to approximately 2 years of field exposure at Sætre, Norway

## Key findings — test stopped after only 209h

### Minipatches (elevated irradiance — 25% higher than tensile samples due to sample height closer to lamp)
- All samples severely darkened, several with burn marks
- UV test stopped completely due to damage observations
- Clear differences between PU hardnesses:
  - 90A: top black, no burn marks, PU still hard to touch, some sides still blue
  - 80A: top black with burn marks, PU deforms on touch (soft), sides also black
  - 70A: top black with most severe burn marks, PU deforms easily (softest), sides black
- Estimated temperature on minipatches: ~95°C (above intended 90°C due to elevated irradiance)
- Gravimetric measurements showed mass increase of 2–8g in UV-exposed samples vs zero in reference samples — possible moisture ingress but inconclusive

### Tensile strips (at correct irradiance level, T up to 90°C)
- Darkening and cracking observed, but no burn marks
- B 80-85A: black with small cracks
- B 70A: black with larger cracks
- C+ 85A: black but no cracks (supposedly lowest quality but visually looked best)
- Tensile testing not yet completed at time of presentation

## Suggested way forward
- New UV test at lower temperature: condition A1 (chamber T=45°C, black panel T=70°C) to avoid burning
- Expected max temperature on minipatches: ~75°C (to be measured before test start)
- Test matrix for minipatches: reference (no UV), 209h at A3, 1000h at A1
- Test matrix for tensile strips per PU type: reference (6 samples), 209h at A3 (6), 1000h at A1 (5), 209h A3 + 1000h A1 (3)

## PU material properties (from manufacturer, 90A)
- Compressive strength: 67.60 MPa
- Density: 1100 kg/m³
- Poisson ratio: 0.49
- Ultimate tensile strength: 75.45 MPa
- Yield strength: 100.00 kPa
- Young's modulus: 41.33 MPa

## Questions for manufacturer
- Thermal stability limits for stress testing
- UV stability information for different PU types
- Test conditions under which published strength values were obtained
- Other material parameters
- Motivation for choosing this material for hinges

## Relevance to D6.1
- Direct input to Chapter 5 (mechanical testing and environmental exposure)
- Demonstrates the simulation-testing cycle: UV test revealed unexpected thermal degradation → design change (dark blue → off-white PU) → need for revised testing protocol
- Material properties feed into structural and thermal modelling
- Confirms that PU absorptivity/emissivity (measured separately, A=0.88-0.91, ε=0.85) drives overheating — links thermal modelling to material durability


# Parametric Gen 2 product design and prototyping (Sunlit Sea, ongoing)

## Parametric FreeCAD design
- Full parametric model of the Gen 2 integrated FPV unit maintained in FreeCAD
- Set of changeable and scaleable properties allowing derivation of many design variants from a single base model
- Design iterations are continuous — the model evolves with each prototype cycle

## PU mould design and casting workflow
- PU cast moulds are designed in FreeCAD as part of the parametric system
- Moulds are 3D printed for rapid prototyping
- Casting is performed onto mock solar panels (glass + bottom plate + frame) — these constitute the prototypes (P1, P2, P3, P4, etc.) referenced in other reports
- 3D-printed moulds that prove viable after inspection and testing are promoted to actual metal moulds for proper production casting
- Significant iteration involved in mould design, print, cast, inspect, revise cycle

## Vendor engagement
- Visited casting vendor in China as part of production scale-up work

## Note
This is a summary placeholder. Substantial additional detail is available on the prototyping iterations, mould design evolution, casting process development, and lessons learned from each prototype generation (P1–P4+). To be elaborated as needed for report content.


# IFE structural FEM simulation of Sunlit Sea prototype floater (Hallvard G. Fjær, Gulshan Noorsumar, 10 April 2026)

Source: Presentation "Simulation of stresses in Sunlit Sea prototype floater" (IFE Internal)

## Overview
IFE has developed a 3D FEM model of the Sunlit Sea prototype floater using their in-house tool SiSim (with MSC PATRAN for pre-processing). The model takes a STEP file exported from Sunlit Sea's parametric FreeCAD model as input, demonstrating a concrete instance of the CAD-to-FEM data flow described in the model chain.

## Model setup
- CAD file received from Sunlit Sea in STEP format
- Minor geometric simplifications (e.g. screw holes removed) before import to MSC PATRAN
- Meshed with TE10 (tetrahedral) and HEX20 (hexahedral) elements
- Different material domains defined with separate properties: polyurethane parts, glass, aluminium parts
- Mechanical interactions between parts defined by interface boundary conditions
- Solution domain: two connected floating modules, 310,000 elements, approximately 2,000,000 degrees of freedom
- One linear analysis step takes approximately 2.5 minutes

## Capabilities demonstrated
- Copy-and-paste of floater components using SiSim to investigate stresses around hinge/rod connections
- Buoyancy boundary condition implemented: computes vertical position from balance of gravity and buoyancy forces, determines how deep floaters sink under self-weight and added loads (e.g. persons walking on floaters)
- Inertial effects: initially unbalanced buoyancy force initiates oscillation; numerical dissipation observed (dampening depends on time step size)
- Response to horizontal forces: simulates wave/current/wind-induced horizontal forces on floater array, computing interface forces and internal stresses

## Key findings from stress analysis (10 mm imposed horizontal elongation)
- Largest XX stresses found in thin aluminium bottom plate and aluminium frame (due to smaller thickness relative to glass)
- Considerable difference between top and bottom surface stresses in both aluminium and glass plates, indicating significant bending
- With distortions magnified x5:
  - Significant bending of upper side of aluminium frame, leading to large stresses in frame flange and bottom plate
  - Aluminium stress close to yield stress level
  - Largest PU stresses well above yield
  - In glass: largest stresses at upper surface near PU ring attachment; dependent on how glass is attached to aluminium frame

## Glass attachment sensitivity
- The way the PV module sandwich is attached to the aluminium frame strongly influences stresses in glass and at PU-glass interface
- If rubber inlay or free movement in slot: low glass stresses, but potentially significant PU-glass interface stresses
- If glued: larger aluminium-glass forces, potentially lower PU-glass interface stresses
- Interface stiffness of 100 MPa/mm displacement applied in simulations (considered rather stiff)

## Important observations (from Sunlit Sea review)
- IFE appear to have simulated without the infill between bottom plate and glass. This is a significant deviation from the current design. The infill (PU foam, aluminium cups, honeycomb, or polystyrene — see Section 2.2.3) provides structural support to the glass, internal load distribution, and sealing. Its absence in the simulation means the stress results likely overestimate stresses in the glass and underestimate the overall stiffness of the system.
- However, the findings remain relevant in two ways: (1) they build a strong case for why the infill is structurally necessary — without it, both aluminium and PU stresses approach or exceed yield under moderate loading; (2) the methodology and data flow are demonstrated regardless of whether infill is included.
- The buoyancy finding — that the prototype sits very deep in the water with half the bottom plate submerged — is an important design input. It suggests the design should be revised to provide more freeboard, either through increased buoyancy volume (deeper cups or larger float area) or reduced system weight.

## Relevance to D6.1
- This is the structural FEM modelling component of the model chain described in Chapter 6 — a concrete implementation of the data flow from CAD (Sunlit) to structural analysis (IFE)
- Demonstrates that the STEP file exchange between Sunlit's parametric FreeCAD model and IFE's FEM tools is operational
- Results directly inform the hinge design principle (absorb loads near centre, away from PU-glass and PU-aluminium interfaces)
- Buoyancy and stress results feed into the system-level trade-offs described in Chapter 7 (screening)
- The finding that aluminium stresses approach yield under 10mm elongation is relevant to FC7 (wave resistance) in the FDS
- Glass attachment sensitivity analysis is relevant to interface I4 (Glass↔Infill), I14 (Frame↔FloatStructure), and I17 (FloatStructure↔Glass) in the interface catalogue
