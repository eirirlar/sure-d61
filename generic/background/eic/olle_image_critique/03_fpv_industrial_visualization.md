---
persona: Industrial visualisation specialist (FPV, marine infrastructure, offshore energy)
focus: technical plausibility of ChatGPT renders vs the actual SUREWAVE architecture; use of existing brochure illustrations
---

> **⚠ CORRECTION (T135, 2026-10-19) — DO NOT CITE AS SOURCE.** This subagent critique asserts that the Sunlit Sea FPV sits *"~0.4–0.5 m above sea level"* with *"zero tilt angle"* (lines 19, 40, 87). Both claims are false. The authoritative Gen 2 spec (`gen2/norsmaterials_brief.md` line 44) gives *"Distance PV → water: 6 cm at the lowest edge — the panel sits at a 2° tilt"*, and the FDS (`sure/background/2024-08-27_fds_nextgen_product.md` line 212) confirms the drainage angle intent. The order-of-magnitude error (6 cm vs 400–500 mm) and the tilt error (2° vs zero) are kept in the body text below for historical record only — do not propagate from this file into any deliverable, doc or image prompt. See `docs/rules/subagent-outputs.md` for the general rule derived from this incident.

# Image prompt critique — SUREWAVE FPV slide deck for Forsvarsmakten

Four descriptions reviewed against ChatGPT / DALL-E 3 failure modes specific to offshore FPV and concrete floating breakwater architecture.

---

## Image 1 — Projektet i korthet (isometric FPV overview)

### Technical plausibility assessment

The prompt asks for "isometric cutaway illustration" with "rectangular grid of dark-blue solar panels ... floating flat on calm turquoise water" and "a ring of pale grey concrete floating breakwater units." In practice, DALL-E 3 will do the following:

- Render the solar array as a set of large, vertically-tilted photovoltaic panels — the kind you see on a rooftop or ground mount, 30–40° tilt angle — floating improbably on pontoon rafts with walkways between rows. Its dominant prior for "floating solar at sea" is the Dutch lake FPV aesthetic (Lingen, Zwolle, BayWa r.e. Dutch projects), where modules are visibly tilted and mounted on white HDPE floats with prominent walkway channels between rows.
- Miss the SUREWAVE low-profile flat-plate geometry entirely. The ~0.4–0.5 m above sea-level silhouette is the defining visual characteristic of the technology, and it is not what the model associates with "solar panels."
- Render the breakwater as a crenellated concrete sea wall — a fixed, land-anchored structure running across one edge — rather than discrete, elongated floating barrel-shaped units forming a closed ring. The phrase "ring of pale grey concrete floating breakwater units" is almost certainly out-of-distribution. The model does not have meaningful training coverage on floating breakwaters; it will default to a rubble-mound or vertical quay-wall.
- Interpret "isometric cutaway" generously: it may deliver something that looks roughly isometric but will not maintain strict axonometric geometry. The grid lines on the panels will be inconsistent.
- Add wind turbines or container ships in the background with some frequency — its "installation at sea" prior is strongly associated with offshore wind.
- Render "thin anchor chains descend from the breakwater units into the clear water below" as straight vertical lines with no catenary. Physically implausible.

### SUREWAVE-fidelity gap

Very large. The actual SUREWAVE system has three visually distinctive elements the prompt will fail to capture:

1. An almost-flush-with-water array of dark aluminium panels — the array looks like a dark, slightly textured plate at sea level, not a field of angled solar panels.
2. A complete perimeter ring of discrete elongated concrete barge-like units (20 m × 5 m × 2.5 m, circular cross-section, double keels — which are visible below the waterline as two longitudinal fin-shaped keels).
3. Catenary chain mooring from the breakwater corners down at an angle to the seabed — not vertical lines.

What the render will look like: a cheerful lake FPV installation, possibly with pontoons and walkways, surrounded by a vaguely grey wall structure, on turquoise water. That is the wrong technology, the wrong country and the wrong application register for a Forsvarsmakten pitch.

### Specific technical fix recommendations

If generating this image is mandatory, the following prompt rework increases fidelity significantly:

- Replace "isometric cutaway illustration" with "bird's-eye technical illustration, viewed from roughly 60 degrees above horizontal, no strict isometric geometry required." This gives the model more latitude and reduces the chance of it choosing grid-render aesthetics over geometric accuracy.
- Replace "rectangular grid of dark-blue solar panels, roughly 50 by 20 metres" with "a dense, nearly flat dark-blue surface of tightly-packed small photovoltaic panels laying almost flush with the water surface, total footprint roughly 50 by 20 metres, panel edges barely visible from above, zero tilt angle, no walkways between panels, no pontoon floats visible." This directly counters the lake-FPV prior.
- Replace "A ring of pale grey concrete floating breakwater units" with "A closed ring of elongated rectangular pale concrete floating barge units, each approximately 20 metres long and 5 metres wide, with rounded outer hull profiles, placed end-to-end around the solar array perimeter, their tops barely above the waterline, pale grey weathered concrete texture." This replaces the wall prior with a barge-like form.
- Remove "Thin anchor chains descend from the breakwater units into the clear water below" entirely, or replace with "steel anchor chains leaving the breakwater hull at a shallow diagonal angle downward, not vertical."
- Add explicitly: "No wind turbines, no offshore wind structures, no ship walkways, no module tilting frames, no pontoon walkway channels."
- Remove "no outlines" — DALL-E 3 uses outlines heavily in technical illustration style, and fighting that usually produces worse geometry than accepting it.
- The phrase "echoing the visual language of a Horizon Europe technical brochure" is inert. The model does not have a reliable EU brochure style prior. Replace with something concrete: "clean technical illustration style, white background, line-art with flat colour fill, similar to a marine engineering specification drawing."

---

## Image 2 — Platsen på Gotland (aerial coastline)

### Technical plausibility assessment

This prompt is by far the most realistic of the four to render well. It asks for a photographic aerial of a limestone coast with industrial buildings and a cargo pier — no specific technology, no specialised geometry, no physics-demanding elements. DALL-E 3 is competent at photographic landscape and coastal drone shots.

Expected render quality: reasonable. The model will produce a plausible Nordic coastline aerial. The main risks are:

- The "limestone handling terminal with conveyor belts and a small cargo pier where a bulk vessel is moored" is a moderately specific industrial setup. The model may render a generic industrial pier correctly, or may produce something anachronistic (an old-fashioned fishing harbour, or a container port). The conveyor belts are the hardest element — they may appear as generic structures rather than recognisable limestone handling infrastructure.
- "Pine-and-juniper vegetation" is a reasonable description of Gotland's coastal ecology, but the model may default to denser, darker boreal forest. Gotland's coast has a distinctive dry, low scrub character that is not easily prompted.
- The phrase "pale, slightly weathered grey-white cliffs" is good and should produce Gotland-like limestone. The risk is that it drifts toward the more dramatic white chalk-cliff aesthetic (Møns Klint, White Cliffs of Dover) rather than Gotland's flat, pavé-style alvar limestone.
- "No military presence of any kind" — no specific risk here, the model will not spontaneously add military hardware to a landscape shot. This instruction is prudent but unlikely to need to fight against a strong model prior.

### SUREWAVE-fidelity gap

Not applicable — this image does not need to depict the SUREWAVE technology. It is a location-establishing shot. No FPV is present in this image. The fidelity question is purely about geographic plausibility for northern Gotland.

### Specific technical fix recommendations

The description is the strongest of the four and needs only minor adjustment:

- Add "flat alvar limestone pavement, low coastal cliffs no more than 3–5 metres above water level" to anchor the geology against cliff-drift.
- Add "sparse, wind-sculpted Scots pine and juniper, not dense forest" to anchor the vegetation density.
- Replace "conveyor belts" with "a materials-handling terminal with long open sheds, a gravel loading arm over the pier, and a low-hulled bulk carrier moored alongside" — this is more visually specific and more likely to match the Fårösund / Slite limestone terminal aesthetic.
- Remove "A few seabirds in flight" — these are visually distracting at print scale and often render as conspicuous white smears. Delete unless the image will be printed large.
- Consider adding "aerial view from approximately 300 metres altitude, 45-degree oblique looking seaward" to stabilise the camera angle, which the current prompt leaves underspecified.

---

## Image 3 — Hur tekniken fungerar (ground-level sea view with FPV)

### Technical plausibility assessment

This is the highest-risk prompt for SUREWAVE-fidelity. It asks for a "ground-level photographic view" of "a dark-blue grid of about forty rectangular PV panels laid flat on the water, visually similar to a very low floating platform or pontoon dock" with "pale concrete floating breakwater units — rounded, barge-shaped." The failure modes are severe:

- "Forty rectangular PV panels laid flat on the water" will almost certainly render as a pontoon-dock-style array with large, individual panels clearly visible and tilted — possibly at 10–20° — with gaps and walkways between them. The model's training for "PV panels on water" is dominated by tilted arrays with visible mounting frames. A truly flat array at 0° tilt, with panels flush-to-water, is out-of-distribution.
- "Visually similar to a very low floating platform or pontoon dock" is actually counterproductive — a pontoon dock has walkways, bollards, cleats, and other hardware that will bleed into the render. Remove this simile.
- "Pale concrete floating breakwater units — rounded, barge-shaped" is better than Image 1's phrasing, but still risks a rubble-mound or fixed quay interpretation. The model's "breakwater" prior is very strongly biased toward fixed coastal defence structures.
- Ground-level view means the camera is at ~0.5 m above sea level looking across the water at panels that are themselves ~0.4–0.5 m above sea level. This is physically correct and creates the signature silhouette of SUREWAVE — the array appears as a thin dark band at the waterline. The model may try to "help" by raising the panels to make them more visible, producing a dramatically elevated panel array that looks nothing like the real thing.
- "The water is glassy and reflective" is a good constraint — it will produce a specular sea surface. However, the reflection of a flat panel array on a glassy sea will create strong mirror symmetry that the model may handle badly, producing a doubled-array or colour bleed artefact.
- "Golden horizontal light" from a low sun angle plus water reflections plus panels flush to water is a visually complex scene. The model may simplify by elevating the panels or adding atmospheric effects that obscure the installation.

### SUREWAVE-fidelity gap

Very large. The real ground-level view of SUREWAVE at Gotland would show: a dark, almost featureless flat plate barely above the waterline, with a textured surface (the pattern of individual 1–2 m panels is discernible but subtle), bounded by the visible hull profiles of the concrete breakwater units rising maybe 1–1.5 m above the waterline at their highest. The overall impression from sea level is closer to a low dark barge surrounded by grey concrete vessels than to any standard FPV image. This is not in the model's training data.

### Specific technical fix recommendations

Significant rewrite needed:

- Replace "a dark-blue grid of about forty rectangular PV panels laid flat on the water, visually similar to a very low floating platform or pontoon dock" with "a dense flat array of small dark-blue photovoltaic panels arranged in a compact grid, the entire surface nearly flush with the sea surface — the array's top surface is only 40–50 centimetres above the waterline, presenting as a thin, low dark horizontal band from sea level. No tilted panels, no mounting frames visible above the surface, no walkways."
- Replace "Pale concrete floating breakwater units — rounded, barge-shaped — form a loose perimeter around the panels, their white-grey surfaces slightly weathered" with "surrounding the panel array, several large elongated concrete floating units are visible — roughly the size and shape of a 20-metre concrete barge, pale grey weathered concrete, circular hull cross-section, their top deck barely above the waterline, spaced around the perimeter with small gaps between units."
- Add: "The camera perspective is at sea surface level, the viewer's eye is approximately 50 centimetres above the water. The solar array appears as a thin dark horizontal band across the middle distance."
- Remove "visually similar to a very low floating platform or pontoon dock" — the pontoon dock simile will bleed.
- Add: "No tilted solar panels, no mounting frames, no walkways or gangways, no pontoon floats, no visible cable trays."
- Consider whether golden-hour lighting is worth the added render complexity. A flat overcast Nordic light is easier for the model to handle correctly at this geometry and produces a more documentary feel consistent with the slide deck register.

---

## Image 4 — Olles roll (civilian coordinator on jetty)

### Technical plausibility assessment

This is the simplest prompt to render well and the one where the model's general photography training is most useful. "Middle-aged civilian man on a stone jetty, dark softshell jacket, grey trousers, looking at water, holding a notebook and phone" is a very standard lifestyle-documentary photograph. DALL-E 3 handles this well.

The main risks are:

- "Documentary photograph of a middle-aged civilian man" — the model may default to a younger or more photogenic subject. Specifying "middle-aged" is good, but "50–60 years old, weathered Nordic complexion" would anchor it better.
- "Three-quarter view from behind the man's left shoulder" — this compositional instruction is usually well-followed. Risk is low.
- "A small floating photovoltaic installation sits on the water, barely visible as a thin dark line on the sea surface, with a pale breakwater perimeter around it" — in a background element at this scale (it should be tiny, 100–200 pixels wide in the frame) the model will render a generic vague blue shape that could be anything. That is actually fine and arguably correct — the installation should be a minor element in this image.
- "No uniform, no high-visibility vest, no safety helmet, no military element whatsoever" — these are good explicit negative constraints but the model will not spontaneously add a military uniform to a man on a jetty. Low risk.
- "A few coastal pines appear" in the lower-left corner — pine trees in a coastal scene are easy for the model.
- The instruction to show him "holding a notebook and a mobile phone" is fine but may result in him looking at the phone rather than across the water. Add "not looking at his phone — his gaze is directed across the water toward the installation" if the gaze direction matters.

### SUREWAVE-fidelity gap

Low — this image is not primarily about the technology. The installation in the background needs only to be a low, vaguely industrial element on the water. A rough "floating dark platform with grey barge-like elements around it" is sufficient. The human subject carries the communicative weight here.

### Specific technical fix recommendations

This prompt is the closest to ready-to-use. Suggested refinements:

- Add "50–60 years old, short grey hair, calm expression" for the subject to avoid the model defaulting to a younger person.
- Add "his gaze is directed out across the water, not at the phone" to ensure the looking-outward posture is maintained.
- Replace "He is ... looking out across calm water" with "He is standing still, weight on one foot, gaze directed toward the horizon and the installation in the distance" — more specific posture, easier for the model.
- The installation description in the background is adequate — do not over-specify it here. The model will render something vague and that is correct.
- Consider removing "a touch of warm pine green in the lower-left corner where a few coastal pines appear" — colour grading instructions like "touch of warm pine green" are hard for the model to isolate to one corner. Either describe the pines compositionally ("a wind-sculpted pine trunk enters the frame at lower left") or omit.

---

## Use SUREWAVE Technical Brochure images instead

This section assesses each slide's image against the existing published SUREWAVE D8.3 brochure figures. These are consortium-published, publicly releasable illustrations produced by professional technical illustrators with the actual SUREWAVE geometry. They are the single most efficient solution to the accuracy problem identified throughout this critique.

### Slide 1 — Projektet i korthet

**Recommendation: use brochure fig03 and/or fig04 instead of generating.**

Fig03 (integrated SUREWAVE system — isometric cutaway showing four subsystems) is exactly what Image 1 is attempting to generate at considerable risk of failure. It is a professional isometric illustration of the real architecture, with correct panel geometry, correct breakwater unit proportions, and correct spatial relationships. It already exists.

Fig04 (reference plant layout — 346 m diameter circular footprint) shows the full-scale layout from above, which directly communicates scale and configuration to a Forsvarsmakten audience thinking about site footprint.

Using fig03 as the primary visual with fig04 as a secondary inset (or vice versa) would produce a dramatically more accurate and professionally credible slide than any DALL-E 3 render. The risk of the wrong geometry, wrong technology aesthetic and wrong register does not exist if the source is the brochure itself.

If the slide designer insists on a generated image for artistic reasons, use the revised prompt from the fix recommendations above as a starting point — but expect 3–5 iteration rounds before arriving at something acceptable, and still likely inferior to fig03.

### Slide 2 — Platsen på Gotland

**Recommendation: generate the ChatGPT image using the revised prompt.**

There is no brochure figure showing northern Gotland's coastline. The D8.3 brochure is technology-focused; its location content relates to the Gijón pilot (fig15), not Gotland. For a place-establishing shot of a civilian limestone coast with industrial infrastructure, generation is the right tool and this prompt (with the minor revisions above) is likely to succeed in one or two attempts.

The one exception: if the user has access to any actual drone photography of the northern Gotland limestone coast (Fårösund, Slite, Storugns area), real photography would be far more credible in a Forsvarsmakten pitch than a generated image. Real location photography is available via Google Earth Studio or drone operators for a fraction of the cost of iterating ChatGPT renders.

### Slide 3 — Hur tekniken fungerar

**Recommendation: use brochure fig07 and/or fig15 instead of generating. If a sea-level view is essential, generate with the heavily revised prompt.**

Fig07 (FPV module and hinge architecture — exploded isometric) directly explains "how the technology works" at the component level — which is what the slide title says. It shows the aluminium float module, the polyurethane hinges, and the assembly logic. This is more informative for a non-specialist audience than a rendered sea-surface photograph.

Fig15 (reduced-scale breakwater prototype in field monitoring at Port of Gijón) is a real photograph of actual hardware at sea level. It shows the concrete breakwater unit in water with the FPV array behind it. It is the closest thing in existence to what Image 3 is trying to generate, and it is real. The geometry is correct because it is the real object. It may be at reduced scale relative to the full-scale units, but it communicates the visual character of the technology far better than any generated image.

Fig06 (floating breakwater unit — dimensioned three-view engineering drawing) could be used as a supporting element to show the breakwater geometry precisely.

If a generated sea-level view is used (e.g. for aesthetic coherence with slide 2), use the heavily revised prompt from the fix section, but budget 5–8 iteration rounds. The flat-panel-flush-to-water geometry combined with the concrete breakwater hull combined with correct sea-level camera angle is a three-way difficult constraint that will require significant prompting effort.

### Slide 4 — Olles roll

**Recommendation: generate the ChatGPT image using the revised prompt.**

There is no brochure figure of a person on a Gotland jetty. This image is about the human role, not the technology; a generated human-subject image is appropriate. The prompt is the strongest of the four and requires only minor adjustments (age anchor, gaze direction). One or two iterations should produce a usable result.

If the slide designer wants to avoid AI-generated human faces entirely (for realism or consent-related reasons), a stock photograph of a civilian engineer or coordinator on a Baltic coastline would be an appropriate substitute — this is a common subject in Scandinavian engineering and infrastructure stock libraries (Mostphotos, Getty, Unsplash).

---

## Summary table

| Slide | Generate or use brochure | Primary source | Estimated iteration rounds |
|---|---|---|---|
| 1 — Projektet i korthet | Use brochure | fig03 (isometric system) + fig04 (layout) | 0 — already exists |
| 2 — Platsen på Gotland | Generate | Revised Image 2 prompt | 1–2 |
| 3 — Hur tekniken fungerar | Use brochure | fig15 (field photo, Gijón) + fig07 (module architecture) | 0 — already exists |
| 4 — Olles roll | Generate | Revised Image 4 prompt | 1–2 |

The two slides that most need accurate technology representation (slides 1 and 3) are also the two where generation is most likely to fail and where brochure illustrations already provide exactly what is needed. The two slides where generation is recommended (slides 2 and 4) are the ones where the model's general photography training is strongest and where no specialised geometry is required.
