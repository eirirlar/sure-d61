# Image guidance in deliverables

Rule: before writing image recommendations or image-generation prompts in a deliverable, inventory the catalogued visual assets, verify provenance (real photo vs AI-generated vs vector illustration vs CAD render vs model output), and verify the specific product configuration applies to the use case.

## Why

Precedent — 2026-10-19, `generic/deliverable/2026-10-19_olle_leave_of_absence_presentation.md`. The first draft of this presentation contained three stacked errors in a single pass:

1. **Provenance error.** The SUREWAVE D8.3 cover image (`surewave/images/.../fig01.png`) was recommended as "the aerial hero image from the published SUREWAVE Technical Brochure — a real published photograph from the consortium's own deliverable [that] carries institutional authority that a synthetic render cannot." fig01 is an AI-generated concept render; the generation prompt is published in `surewave/deliverables/2026-09-28_surewave_d8.3_figures.md` (Fig 1, "Type: photorealistic concept render"). Calling it a photograph was wrong.
2. **Configuration error.** The ChatGPT fallback prompt for the project-overview slide described "a ring of pale grey concrete floating barges" — the SUREWAVE full-ring breakwater perimeter from the open-sea reference plant. The deliverable is for a nearshore Gotland demonstrator. The nearshore configuration uses directional breakwater placement against the critical wave direction(s), not a full ring. See [`docs/surewave_configurations.md`](../surewave_configurations.md).
3. **Generic-prompt error.** The ChatGPT prompt also described "flat solar panels floating on open sea" — a generic description that would produce tilted-panel-on-pontoon imagery from a model trained predominantly on inland FPV. Sunlit Sea's product has a specific design (panel sits nearly flush with the water — approximately 6 cm above the waterline at the lowest edge, 2° tilt for drainage; integrated with the aluminium float; polyurethane hinges between panels — see `gen2/norsmaterials_brief.md`) with real deployment photos and CAD renders already in the repo. Writing a generic prompt wastes effort when design-accurate assets are a filepath away.

Each individual error was fixable. Together they signalled image guidance was written before preparation work. The user framed it: *"You cannot create the olle presentations based on sloppy preparation work."*

## How to apply

Before writing any image guidance, prompt, or recommendation in a deliverable:

1. **Inventory existing assets.** Open [`docs/sure_images.md`](../sure_images.md) and read the full catalogue. Note the provenance tag for each candidate (real photo, Sunlit Sea CAD render, SUREWAVE AI concept render, SUREWAVE AI vector illustration, finite-element output, satellite imagery).
2. **Verify the configuration applies.** Check [`docs/surewave_configurations.md`](../surewave_configurations.md) when SUREWAVE imagery is in play. The ring layout is reference-plant / open-sea; the directional breakwater is nearshore. Confirm which case your deliverable is for and pick imagery that does not misrepresent.
3. **Prefer, in order:**
   - Real photographs of the actual product (`asset-solar-floating.jpg`, `asset-solar-panels-multiple.jpg`, `sure/images/fpv_gen1_float.png`).
   - CAD renders / isometrics of the actual product (`sure/images/solar_panel_*.png`, `sure/images/fpv_*.png`, `sure/images/gen2_*.png`).
   - Real-site satellite or map imagery for site slides (Google Earth, OpenStreetMap, published press images).
   - SUREWAVE brochure figures only when a reference-plant / open-sea claim is appropriate, and only with the provenance tag made explicit in the deliverable.
4. **Ask the user for a CAD snapshot** for angles not already rendered. The Gen 2 FreeCAD model is live and the user can take isometric or perspective snapshots on request. This beats inventing a ChatGPT prompt.
5. **ChatGPT prompts anchor on uploaded reference images, not on text descriptions.** The native pattern: specify one or more existing repo images for the user to upload alongside the prompt, and write the prompt as *"using attachment N as the exact geometry / material / scene element, re-render in <new setting>"*. This beats text-only prompts because the model gets the actual product geometry rather than reconstructing it from training data. Pattern:
   - Name the specific files to upload (full repo path).
   - State what each attachment is for (geometry reference, material reference, scene reference, breakwater geometry).
   - Write the prompt as a transformation of the attached reference(s) into a new setting, not as an open-ended description.
   - Include an explicit "do not include" list for words that would push the model into wrong directions (e.g. "lake", "ring", "military", "golden hour", "cliff").
   - If no existing reference image is appropriate (angle not rendered, product not photographed), ask the user for a CAD snapshot before writing the prompt — do not fall back to a text-only generic prompt.

## Pre-send checks

Before marking the deliverable ready for conversion:

- No image described as "real photograph" is actually an AI-generated render. Cross-check against the provenance tags in [`docs/sure_images.md`](../sure_images.md) and the generation prompts in `surewave/deliverables/2026-09-28_surewave_d8.3_figures.md`.
- No ring-breakwater imagery sits on a slide that describes a nearshore configuration (or vice versa).
- Where SUREWAVE brochure figures are included, their provenance (AI concept render / AI vector illustration) is called out in the deliverable itself so a downstream reader does not re-use them under false assumptions.
