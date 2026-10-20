# Image asset catalogue

Catalogue of image assets used in Sunlit Sea / SUREWAVE deliverables, with provenance tags. Use this before writing image guidance in any deliverable — see [`docs/rules/image-guidance.md`](rules/image-guidance.md).

Provenance tags:

- **Photo** — real photograph.
- **CAD render** — rendered output from a FreeCAD / CAD model of the actual Sunlit Sea product.
- **FEM output** — screenshot or render of a finite-element simulation (ANSYS, LS-DYNA, FLOW-3D HYDRO, etc.) with the actual simulation data.
- **AI concept render** — AI-generated photorealistic image. Not a photograph; a prompt-driven synthetic image.
- **AI vector illustration** — AI-generated flat-vector / technical-illustration-style image. Not a hand-drawn diagram.
- **Infographic** — flat-vector infographic generated from a prompt or hand-authored.

---

## `sure/images/` — SuRE project images (D6.1 / D6.2 and related)

### Material & product

- `cup_shape.png` — Sample cup shape showing the target geometry produced by the pressing process. **CAD render.**
- `alu_sheet.jpg` — Raw aluminium sheet before pressing. **Photo.**
- `alu_pressed.jpg` — The pressed final product on the same sheet. **Photo.**
- `chemical_composition_alu5083h111.png` — Composition breakdown of 5083-H111 aluminium alloy (the material used). **Infographic.**

### Gen 1 FPV system

- `fpv_gen1_assembly.png` — Assembly diagram showing all Gen 1 components: glass/PET solar panels, polystyrene cup infill, butyl/silicone edge sealant, 2-component silicone potting, two pressed aluminium parts bonded as a float with air inside, and brackets on the float lip for the connect system. **CAD render.**
- `fpv_gen1_float.png` — The actual Gen 1 product as built. **Photo.**
- `groundings.png` — Grounding / electrical bonding scheme for the Gen 1 float. **CAD render / diagram.** (Content not confirmed from file inspection — read the file before citing details.)

### Gen 1 heat transfer

- `gen1_cooling_of_pv_from_heat_transfer_to_water.png` — Natural heat-dissipation paths through infill and pressed aluminium bottom plate; passive heat flow visualisation. **Diagram.**
- `gen1_eval_flow_submerge_effect_in_real_conditions.png` — Flow evaluation of submergence effects. **CAD render / diagram.** (Content not confirmed — read the file.)

### Panel and FPV float views (standalone)

- `solar_panel_top.png` — Top view of a single Sunlit Sea solar panel. **CAD render.**
- `solar_panel_bottom.png` — Bottom view of the same. **CAD render.**
- `fpv_top.png` — Top view of a single Sunlit Sea FPV float (panel + housing). **CAD render.**
- `fpv_side.png` — Side view. **CAD render.**
- `fpv_bottom.png` — Bottom view. **CAD render.**

### Float system and matrix layout

- `float_system_left_top.png` — Float system shown from one angle. **CAD render.**
- `float_system_top_top.png` — Float system shown from another angle. **CAD render.**
- `float_p3_matrix.png` — P3 prototype matrix layout showing how connected floats form an array. **CAD render.**

### Gen 2 product development

- `gen2_freecad_bottom_flat.png` — Gen 2 flat-bottom float, FreeCAD view. **CAD render.**
- `gen2_freecad_bottom_pressed.png` — Gen 2 pressed-bottom float, FreeCAD view. **CAD render.**
- `gen2_freecad_infill_split_PUfoam.png` — Gen 2 float with PU foam infill, split view. **CAD render.**
- `gen2_matrix_installed_rendered_still_water.png` — Rendered Gen 2 matrix in still water. **CAD render.**
- `gen2_prototype1_freecad_fpv_without_glass.png` — Prototype 1 FPV with glass omitted. **CAD render.**
- `gen2_prototype3_freecad_model.png` — Prototype 3 complete model. **CAD render.**
- `gen2_prototyp3_casting1.png`, `gen2_prototyp3_casting2.png` — Prototype 3 casting trials. **Photos.**
- `gen2_prototyp4_freecad_model.png` — Prototype 4 complete model. **CAD render.**
- `gen2_prototyp4_freecad_mold.png` — Prototype 4 mould design. **CAD render.**
- `gen2_prototyp4_freecad_hinge_left.png`, `gen2_prototyp4_freecad_hinge_right.png` — Prototype 4 hinge views. **CAD render.**
- `gen2_prototyp4_freecad_connector_buoyant_PUfoam_rods_4sides.png` — Prototype 4 buoyant PU-foam connector with rods on four sides. **CAD render.**

### Pressing equipment & simulation

- `punch_and_die.png` — STEP file image of the punch and die setup; early iteration of the pressing FEM simulation. **CAD render.**
- `meshed_fluid_die.png` — Finite-element mesh of the fluid-forming die. **FEM output.**
- `punch_die_mesh_with_gripper.png` — Meshed punch/die with gripper ring. **FEM output.**
- `punch_die_mesh_without_gripper.png` — Baseline (gripper later abandoned in favour of fluid forming). **FEM output.**

### CAD export process

- `freecad_to_step_1.png` through `freecad_to_step_4.png` — FreeCAD interface showing design parameters, and STEP file rendered from three different angles. **CAD renders / UI screenshots.**

### Tool failure analysis

- `punchdie_rip1.png`, `punchdie_rip2.png` — Tool damage / tearing scenarios under pressing loads. **FEM output.**

### Pressing simulation reference

Pressing pipeline code and `.k.hbs` LS-DYNA templates live in `../thepressing/` (separate neighbour repo). See CLAUDE.md "Neighbour projects" for scope and read-only access rule.

---

## `gen2/images/renders/` — Blender renders of the Gen 2 matrix in a lake-and-terrain scene

Five Blender stills dated 2025-05-08, derived from the Gen 2 FreeCAD model (CAD imported, materials and water added in Blender, lake / shoreline terrain built around it). Photorealistic rendering quality; dusk / golden-hour lighting. Show the Gen 2 FPV matrix as a flat grid of dark-blue panels at the water surface, with red/orange mooring buoys and rock-and-grass shoreline. **CAD render (Blender, from real CAD model).** Not AI-generated.

- `Still 2025-05-08 231304_1.1.1.png` — oblique close perspective of the matrix corner at low angle; panels fill the upper two thirds, water with reflections below.
- `Still 2025-05-08 231304_1.2.1.png` — perspective view from the water surface.
- `Still 2025-05-08 231304_1.3.1.png` — wide view with the shoreline and terrain prominent on the right; matrix on the left in water.
- `Still 2025-05-08 231304_1.4.1.png` — mid-distance perspective.
- `Still 2025-05-08 231304_1.5.1.png` — high-oblique / near-overhead view of the matrix corner, water on three sides, shoreline bottom-right.

Attribution: *Image: Sunlit Sea AS (Blender render from Gen 2 CAD model).*

These are the best available visual of the actual product in a realistic water-and-terrain scene. They do not show the SUREWAVE breakwater (only the FPV matrix and moorings), so they are safe for nearshore deliverables where no specific breakwater configuration should be implied.

A `renders.bak` folder sits alongside `renders/`; treat as backup, do not cite from it.

---

## Repo root — Sunlit Sea deployment / assets

- `asset-solar-floating.jpg` — Sunlit Sea's close-up of actual FPV modules in real sea conditions. Panels sit nearly flush with the water (approximately 6 cm freeboard at the lowest edge, 2° tilt for drainage; see `gen2/norsmaterials_brief.md` line 44). Dark Baltic-like water, water droplets on the panel surface. **Photo.** Also duplicated at `surewave/images/2026-09-29_sunlit_sea_webpage/`.
- `asset-solar-panels-multiple.jpg` — Deployed array on water with a figure in a yellow drysuit visible on the left. **Photo.** Crop the drysuit figure out when the deliverable is for an audience that does not need the person. Also duplicated at `surewave/images/2026-09-29_sunlit_sea_webpage/`.
- `d8.3_frontpage_preview.png` — Preview of the SUREWAVE D8.3 Technical Brochure front page. **Derived from the brochure PDF cover; the cover image itself is AI-generated (see fig01 below).**
- `haugaland1.png` — Haugaland deployment reference image. **Photo.** (Content not confirmed from file inspection — read before citing details.)

---

## `surewave/images/2026-09-28_surewave_d8.3_technical_brochure_lowres/` — D8.3 brochure figures

All brochure figures (fig01 through fig24) have their generation prompts and provenance recorded in `surewave/deliverables/2026-09-28_surewave_d8.3_figures.md`. Summary provenance:

- `fig01.png` — Cover hero image, full-ring open-sea installation. **AI concept render.** Not a photograph.
- `fig02.png` — Market opportunity bar chart. **Infographic.**
- `fig03.png` — Integrated SUREWAVE system, isometric cutaway with labelled subsystems. **AI vector illustration.** Full-ring reference plant.
- `fig04.png` — Reference plant plan view, 346 m circular. **CAD / vector drawing.** Full-ring reference plant.
- `fig05.png` — Three reference site classes (Baltic / Mediterranean / North Sea). **Infographic.**
- `fig06.png` — Floating breakwater dimensioned three-view engineering drawing. **CAD / vector drawing.**
- `fig07.png` — FPV module and hinge architecture, exploded isometric. **CAD / vector drawing.**
- `fig08.png` — Catenary mooring configurations across three sites. **CAD / vector drawing.**
- `fig09.png` — Circular concrete composition breakdown. **Infographic.**
- `fig10.png` through `fig12.png` — Section 4 materials and manufacturing figures. **Mixed — see figures spec.**
- `fig13.png` — Mooring eye stress distribution. **FEM output** (real Ceit FE output, 11-event bipolar colour scale; see T120 solution notes).
- `fig14.png` through `fig16.png` — Section 5 modelling / testing figures. **Mixed — see figures spec.**
- `fig17.png` — SHMS load-history / rainflow spectrum. **FEM / software output** (Ceit MATLAB build).
- `fig18.png` through `fig20.png` — Section 6 operational / lifecycle figures. **Mixed — see figures spec.**
- `fig21.png` — Mediterranean 10 MW CAPEX composition. **Infographic.**
- `fig22.png` through `fig24.png` — Consortium / partner figures. **Mixed — see figures spec.**

**Important for deliverables:** fig01, fig03 and fig04 all show the full-ring open-sea reference plant. They do not represent nearshore configurations (Gotland, Hainer See). Do not use these to illustrate a nearshore demonstrator — see [`docs/surewave_configurations.md`](surewave_configurations.md).

---

## `surewave/images/` — other SUREWAVE deliverable images

Each SUREWAVE deliverable has its own image folder, named by the deliverable date and slug. Content varies by deliverable; most contain CAD drawings, FEM outputs, chart screenshots and extracted DOCX images from the original Word deliverable. Read the specific deliverable's figures section for provenance when citing images from these folders.

Notable:

- `surewave/images/2023-08-08_surewave_d3.2_floating_breakwater_design/` — Clement Germany's floating breakwater design deliverable, 60+ images. Mix of **CAD renders** (breakwater pontoon isometrics and cross-sections, Clement's own design output), **CFD / FEM outputs** (FLOW-3D Hydro simulations), and **engineering drawings**. Authoritative source for breakwater geometry — use these as ChatGPT reference uploads instead of writing geometry from scratch. Specifically useful:
  - `image9.png` — isometric of the conventional-materials breakwater pontoon interior (Figure 7 in D3.2). Shows transverse walls, chamfered polystyrene core, concrete shell.
  - `image12.png` — isometric of the breakwater pontoon with new circular materials and bottom slab (Figure 10). Grey-rendered, shows the double-keel geometry clearly through semi-transparent walls. Most representative single-image CAD of the SUREWAVE breakwater unit.
  - `image13.png`, `image14.jpeg` — longitudinal and cross sections of the same unit (Figures 11, 12). Useful alongside the isometric for a ChatGPT upload if proportions matter.
- `surewave/images/2024-11-07_surewave_d5.3_structural_integrity_assessment/` — D5.3 structural integrity figures. Mix of CAD renders, FEM outputs, and extracted DOCX images.
- `surewave/images/wavebreaker_mooring.svg` — Sunlit Sea schematic sketch (SVG) of the mooring architecture for a nearshore SUREWAVE deployment: shows the connection between the Clement breakwater pontoon, the PVC-pipe transition system and the FPV matrix. Used as "Image C" reference upload in the ChatGPT prompt for the Olle leave-of-absence deck slide 2 and other nearshore composite visualisations. **Hand-authored schematic.**
- `surewave/images/eu_flag.png`, `eu_flag.svg` — European Union flag emblem (official).

---

## See also

- [`docs/surewave_configurations.md`](surewave_configurations.md) — reference plant vs nearshore configurations; which imagery applies to which deliverable context.
- [`docs/rules/image-guidance.md`](rules/image-guidance.md) — rule for writing image guidance in deliverables.
- `surewave/deliverables/2026-09-28_surewave_d8.3_figures.md` — authoritative figures spec for D8.3 (prompts, provenance, revision notes).
