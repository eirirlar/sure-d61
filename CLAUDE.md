# D6.1 Report — Working Tracker

## Files in /home/claude/
- `report.txt` — current working version with all edits applied
- `activities.md` — collected evidence and testing activities
- `code/` — code repository for aluminium pressing simulation pipeline
- `TASKS.md` — tasks we are working on. Shall be kept updated.

## Notes
- User wants Mermaid scripts inline (not rendered), will create figures later
- Figures appear near first reference, numbered relative to chapter
- **ALWAYS when delivering docx:** ensure mermaid diagrams are in fenced code blocks with proper line breaks, AND export each diagram as a standalone .mmd file to outputs

## Background Images (`images/` folder)

### Material & Product
- `cup_shape.png` — Sample cup shape showing the target geometry produced by the pressing process
- `alu_sheet_vs_pressed.jpg` — Before/after comparison of raw aluminium sheet vs. the pressed final product
- `chemical_composition_alu5083h111.png` — Composition breakdown of 5083-H111 aluminium alloy (the material used)

### Gen1 FPV System
- `fpv_gen1_assembly.png` — Assembly diagram showing all gen1 components: glass/PET solar panels, polystyrene cup infill, butyl/silicone edge sealant, 2-component silicone potting, two pressed aluminium parts bonded together as a float with air inside (forming the bottom plate, part of infill, and floatsystem), and brackets on the float lip for the connect system
- `fpv_gen1_float.png` — The actual gen1 product as built
- `fpv_matrix_and_mooring_system_for_25kwp.png` — Layout showing how different form factors affect the matrix arrangement and mooring system for a 25kW peak capacity installation

### Heat Transfer
- `gen1_cooling_of_pv_from_heat_transfer_to_water.png` — Shows the natural heat dissipation paths through the infill and the pressed aluminium bottom plate in gen1; not an active cooling system but passive heat flow visualization

### Pressing Equipment & Simulation
- `punch_and_die.png` — Step file image showing the punch and die setup; represents an early iteration of the pressing FEM simulation setup showing iterative development toward the final simulation
- `meshed_punchdie.png` — Finite element mesh visualization of the punch and die components for FEM analysis
- `punch_die_mesh_with_gripper.png` — Meshed punch/die setup with gripper ring; tests flow control and metal thinning reduction
- `punch_die_mesh_without_gripper.png` — Meshed punch/die setup without gripper; baseline for comparison; gripper approach was later abandoned in favor of fluid forming

### CAD Export Process
- `freecad_to_step_1.png` — FreeCAD interface showing design properties and parameters that control the geometry
- `freecad_to_step_2.png` — Step file rendered from one angle
- `freecad_to_step_3.png` — Step file rendered from a second angle
- `freecad_to_step_4.png` — Step file rendered from a third angle

### Tool Failure Analysis
- `punchdie_rip1.png` — Tool damage/failure scenario 1 showing tearing or ripping under pressing loads
- `punchdie_rip2.png` — Tool damage/failure scenario 2 showing tearing or ripping under pressing loads
