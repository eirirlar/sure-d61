---
persona: Nordic documentary photographer / photo editor (Swedish Baltic coast, Gotland specifically)
focus: scene authenticity for northern Gotland + Storugns, Nordic lighting physics, documentary photo conventions
---

# Image critique: four ChatGPT / DALL-E 3 descriptions for the Olle Forsvarsmakten leave-request deck

Reviewed: 2026-10-19

---

## Image 1 — Projektet i korthet (isometric FPV overview)

### 1. Scene authenticity assessment

This is an illustration rather than a photograph, so Baltic-coast authenticity is not directly at stake — the FPV technology render is the primary concern. The description is largely competent for a technical isometric illustration. The main risk is the water colour: "turquoise water" is what DALL-E 3 will render, and it will look like a Mediterranean or Caribbean scene. For the Baltic coastal context this deck lives in, that is a small but real dissonance — the reviewers at Forsvarsmakten on Gotland will unconsciously register it as "not here". Concrete anchor units are described reasonably; the model has enough training mass on FPV concepts to land this illustration well. The "flat shading, no outlines" instruction fights the model's tendency toward hard outlines in isometric illustration — this may require iteration to enforce.

### 2. Lighting physics assessment

"Bright Nordic midday" on an isometric illustration is largely inert — there is no environmental sky to get wrong. The sky in the upper third is described as "soft blue sky with a few scattered cumulus clouds", which is unproblematic for an illustration. The "no shadows" instruction is well-placed to keep this flat and technical.

### 3. Specific authenticity fixes

- Replace "calm turquoise water" with "calm water in grey-blue to steel-grey tones, pale over the shallows, deeper grey-blue offshore — Baltic Sea colouring, not tropical turquoise".
- Replace "bright Nordic midday" with "neutral overcast Nordic light" or simply drop the lighting description — it is irrelevant to a flat technical illustration and "Nordic midday" risks pushing the sky toward a Mediterranean blue.
- Add "the water colour palette is muted Baltic grey-blue, not tropical; overall palette is cool-toned Nordic industrial".
- The breakwater units are described as "pale grey concrete" — correct. Reinforce: "roughened concrete surface, not glossy; industrial not decorative".

### 4. Documentary-style anchor recommendation

This is an illustration, not a photograph, so a documentary photographer reference does not apply. For the illustrative style, anchor on "technical illustration from a Horizon Europe project deliverable: clean isometric line art, muted palette, industrial precision — not infographic pop-art or product-marketing render". If colour treatment risks becoming tropical, add "Scandinavian industrial palette: cool grey, dark slate, muted stone, off-white; no warm highlights, no saturated blues".

---

## Image 2 — Platsen på Gotland (aerial coastline)

### 1. Scene authenticity assessment

This description will produce an aerial view that looks almost nothing like northern Gotland at Storugns / Lärbro. Three failure modes will occur, with high confidence:

**Cliff rendering.** The phrase "pale, slightly weathered grey-white cliffs" combined with "limestone coast" will cause the model to render Dover-style white chalk cliffs or, at best, Møn-style white cliff coast — dramatic vertical faces 20–40 metres above the sea. Northern Gotland at Storugns is the opposite: a very low, flat limestone pavement coast, essentially at sea level, backed by pine and juniper scrub. There are no cliffs here. The model has essentially no training coverage of this specific landscape type; "limestone cliff" is a dominant override.

**Water colour.** "Translucent pale blue over the limestone seabed" is reasonable in principle, but the model will push toward turquoise or azure Mediterranean shallows given "pale blue" and "limestone seabed" together. Baltic near-shore water over a limestone bottom at Storugns is whitish-grey to pale greenish-grey — milky limestone suspension often dominates rather than clear turquoise. In the Nordkalk working basin (a former quarry pocket) the water is specifically white-grey from limestone particulate.

**Industrial facility.** "Cluster of low, pale industrial buildings, a limestone handling terminal with conveyor belts and a small cargo pier where a bulk vessel is moored" is directionally correct for Storugns, but the model will render a generic Scandinavian industrial waterfront — probably red wooden warehouses with a dock, or a grey steel shed complex. The distinctive Storugns features — cylindrical limestone silos in pale grey concrete, a long elevated conveyor belt structure extending to the sea, a deep-water bulk cargo berth with prominent bollards — will not appear. The actual industrial footprint of Storugns is compact and reads from the air as a cluster of grey concrete cylinders (silos) next to a conveyor arm reaching the quay, with a stockpile of crushed limestone visible as a white-grey pile.

**Vegetation.** "Pine-and-juniper vegetation" is correct for Gotland and reasonably likely to land correctly if stated explicitly. Drop "in the foreground" and specify it more precisely as "low sparse pine and juniper scrub growing from flat limestone pavement, no undergrowth, trees wind-sculpted, characteristic Gotland alvar vegetation at the coast" — this gives the model a better prior than generic Scandinavian forest.

**Seabirds.** Plausible — northern Gotland coast does have gulls and terns. Acceptable.

### 2. Lighting physics assessment

"Clear, high-sun Nordic daylight with soft shadows" — "high-sun" is the critical error. At 57.84°N in summer, the maximum solar elevation at solar noon is approximately 55–57°. "High-sun" will cause the model to render a sun angle that looks Southern European — near-vertical shadows suggesting 70–80° solar altitude. The actual result is always longer shadows, more angled light, a distinct "golden horizontal" quality even at noon, and a sky that is lighter blue than a Mediterranean noon sky (the solar disc is lower, scattered path is longer). The result will look Mediterranean-lit, not Gotland-lit. Replace with: "clear Nordic summer daylight, sun roughly south-southwest, shadows noticeably long for summer (low solar elevation), light warm-cool, not harsh".

### 3. Specific authenticity fixes

Replace the current description of the coastal topography entirely:

> _Current:_ "the limestone coast — pale, slightly weathered grey-white cliffs and low pine-and-juniper vegetation"

> _Replace with:_ "the northern Gotland limestone coast near Storugns — very low flat limestone pavement at or barely above sea level, no cliffs; low sparse pine and juniper scrub growing directly from bare grey limestone, trees wind-contorted, coastal alvar character; the land-sea boundary is an almost imperceptible low limestone edge, not a cliff"

Replace the water description:

> _Current:_ "translucent pale blue over the limestone seabed, transitioning to deeper blue further out"

> _Replace with:_ "Baltic Sea near-shore water in milky pale grey-green tones close in — limestone particulate from the Nordkalk operation — transitioning to grey-blue further offshore; no turquoise, no tropical clarity"

Add specificity to the industrial facility:

> _Add:_ "the Nordkalk Storugns terminal is identified by concrete cylindrical limestone silos, a long elevated belt conveyor extending from the silos to the quay, a bulk-cargo berth with heavy mooring bollards; the overall industrial footprint is compact, the colour is pale concrete grey and off-white limestone dust; no red wooden buildings, no steel-clad modern sheds"

Replace the lighting descriptor:

> _Current:_ "clear, high-sun Nordic daylight with soft shadows"

> _Replace with:_ "clear Nordic summer light, sun low in the southern sky even at midday, shadows longer than typical summer sun, light warm-cool white rather than harsh, no harsh overhead shadows"

Remove "cinematic drone photography" — this cues an over-saturated HDR grade. Replace with: "aerial documentary photography, naturalistic colour palette, slightly desaturated, cool Nordic tones".

### 4. Documentary-style anchor recommendation

For photographic style, anchor on Scandinavian industrial landscape documentary rather than drone cinematography. The closest reliably anchored aesthetic in current models: "aerial photograph in the style of a Swedish environmental agency survey, flat naturalistic colour, no dramatic grade". For a named photographer anchor, **Ismo Hölttä** (Finnish industrial documentary) and **Anders Petersen** (Swedish, though known for social not landscape) are recognisable to image models, but neither is reliable for this specific combination. A safer approach: "aerial photograph in the style of Vattenfall annual report environmental documentation: factual, naturalistic, non-promotional, Scandinavian grey-blue-green palette, industrial infrastructure at human scale".

---

## Image 3 — Hur tekniken fungerar (ground-level sea view with FPV)

### 1. Scene authenticity assessment

The FPV installation description is solid and specific. The most serious failure mode here is again water colour: "glassy and reflective" is fine, but the Baltic near Gotland is grey-blue to grey-green, not the model's default reflective-sea colour which tends toward silver-blue in calm conditions. The "Nordic late-afternoon" golden light is a plausible moment to depict and has good authenticity potential if the sun angle is correctly described — late afternoon in summer on Gotland means a very low sun in the northwest, warm raking light at a very low angle, long shadows across the water.

The horizon description — "the coastline is just visible as a thin pale strip on the far horizon" — is good and accurate. Northern Gotland has a low flat coast; from water level it would appear as a very thin line.

The breakwater units as "rounded, barge-shaped" is acceptable as a visual description for generic concrete breakwater units. Specifically: Wave dampening units used in FPV context are often Helsvik or similar rectangular concrete pontoons; "barge-shaped" is close enough and better than "rounded".

The main risk: "No people, no vessels, no infrastructure visible on land, no military elements" — this set of negations is exactly what forces the model to fill the frame with something, and what it fills it with is unpredictable. Expect the model to introduce a coastline in the background that looks Norwegian fjord or Swedish west coast rather than flat Gotland. Explicit "flat low coastline, indistinct on the horizon" is better than absence.

### 2. Lighting physics assessment

"Nordic late-afternoon sky" with "warm golden horizontal light" is actually accurate and achievable. Late afternoon in summer on Gotland: sun in the northwest, very low angle, light distinctly golden-orange, long horizontal shadows on the water surface. The model has strong priors for this "golden hour" aesthetic. The risk is over-rendition — the model will tend toward a dramatic Instagram golden hour rather than the more restrained warm-diffuse quality of actual Baltic late afternoon. The Baltic haze factor also deserves mention: summer haze on the Baltic often softens golden hour into a warm diffuse glow rather than a sharp golden disc.

Replace "warm golden horizontal light" with "warm, slightly hazy late-afternoon light, sun low in the northwest, diffuse gold rather than sharp sunset, Baltic summer haze softening the light". This is both more accurate and resists the over-dramatic interpretation.

### 3. Specific authenticity fixes

- Replace "glassy and reflective, mirroring the panels and the Nordic late-afternoon sky above" with "glassy calm, slight swell, surface in grey-blue Baltic tones reflecting the pale sky; no turquoise, sea-surface colour muted grey-silver in the shaded sections, warm-diffuse gold where the late sun catches"
- Add to water colour: "Baltic Sea in calm conditions, near-shore water colour grey-blue, not tropical blue or turquoise"
- Replace "warm golden horizontal light" as above
- Replace "Natural, understated photographic style — documentary rather than promotional, muted colour palette" with: "documentary photographic style, Scandinavian muted palette, ISO 400 film texture rather than digital hyperreal, slightly understated exposure — not promotional drone cinematography grade"
- Consider adding "overcast sky alternative: the installation reads equally well under a pale overcast — flat white sky, silver water, blue-grey panels — which is more characteristically Baltic than golden hour and is safer for model rendering"

### 4. Documentary-style anchor recommendation

For actual named photographer anchoring: **Terje Abusdal** (Norwegian, known for subdued environmental/landscape documentary) is a reliable anchor in current models. "In the style of Scandinavian maritime environmental documentary photography — muted, slightly desaturated, authentic light, not promotional" is a safer phrase-level anchor. For the golden light version: "late afternoon Baltic light, in the muted realist tradition of Swedish nature photography" outperforms "cinematic golden hour".

---

## Image 4 — Olles roll (civilian coordinator on jetty)

### 1. Scene authenticity assessment

This description faces the strongest model-prior risk of the four. "A middle-aged man on a stone jetty looking out to sea" is one of the most over-represented visual tropes in Northern European image generation training data — the "contemplative Scandinavian man" shot. The model's prior here is essentially: heavily backlit or side-lit, moody blue-grey water, man standing still and looking heroic/contemplative. The notebook and mobile phone are useful specificity markers that fight this prior, but they need to be more foregrounded.

The three-quarter-from-behind composition is clever and appropriate, but note that "from behind the man's left shoulder" is a fairly classical interpretive angle that will land well. However, "three-quarter view from behind" combined with "looking out across calm water" is textbook contemplative Scandinavian man composition. The notebook and phone are the main factors that re-anchor this as workday liaison — but they risk being rendered as props rather than active tools. Make the active use of these objects explicit: he should be consulting the notebook and looking between it and the installation, not simply "holding" them.

Clothing description is good and specific: "dark softshell jacket, grey trousers, sturdy walking boots" is realistic for a Swedish field coordinator. The absence of high-visibility and uniform is correct and worth keeping. The negative list ("no uniform, no high-visibility vest, no safety helmet, no military element whatsoever") is important and should stay — DALL-E 3 will otherwise insert safety equipment or military-adjacent clothing given any ambiguity.

The FPV installation as "barely visible as a thin dark line on the sea surface" is accurate and honest — from a stone jetty on shore, a mid-distance FPV installation would be at or near the horizon threshold.

The "a touch of warm pine green in the lower-left corner where a few coastal pines appear" is authentic for northern Gotland and a good compositional anchor that pushes the scene away from a bare Norwegian rock-and-sea cliché.

### 2. Lighting physics assessment

"Bright, slightly overcast day" is probably the most defensible lighting choice for this image. Nordic diffuse overcast is a highly authentic Baltic daylight condition — grey-white flat sky, even shadows, muted colours, the water taking a grey-green tone. The model will tend to make it more dramatic or more cheerful than this, but "slightly overcast" is a reasonable prior to invoke. The instruction "diffuse, soft Baltic daylight, muted blue-grey palette" reinforces this well. "Muted blue-grey palette with a touch of warm pine green" is both authentic and fights the tendency toward cold monochrome that overcast renders sometimes land on.

No significant change needed here — this is the strongest lighting physics section of the four descriptions.

### 3. Specific authenticity fixes

The main fixes are compositional and behavioural:

- Replace "holding a notebook and a mobile phone, looking out across calm water" with "holding an open notebook and checking between it and the distant installation, mobile phone tucked into his jacket pocket, body language active and purposeful — a field check, not a contemplative stance". This fights the contemplative-man prior directly.
- Add an active element: "he has just looked up from the notebook to check a specific feature of the installation, slight squint — professional assessment, not a posed moment".
- The coastal pines "in the lower-left corner" risk not being rendered if the model does not understand the composition. Specify: "a few wind-shaped coastal pines and juniper visible in the lower-left foreground — low flat coastline vegetation characteristic of northern Gotland, not tall forest".
- Replace "smooth stone jetty" (if the description implies height) with "low flat stone jetty barely above water level" — on the Gotland limestone coast, the 'jetty' or quay at a small fishing harbour is often literally limestone pavement at 30–50 cm above sea level.
- The FPV installation in the background as "a pale breakwater perimeter around it" is good — it makes the installation look like a legitimate industrial installation rather than a solar-farm-in-a-lake.

### 4. Documentary-style anchor recommendation

For documentary style: "photograph in the style of a Swedish government environmental agency field report" or "photograph in the style of a Vattenfall project site-visit documentation". For a named photographer with authentic prior in image models and the right Nordic documentary aesthetic: **Jonas Bendiksen** (Magnum, Norwegian, known for matter-of-fact field documentation) is a reliable and often well-anchored reference in DALL-E 3. "Documentary photograph in the Jonas Bendiksen style — matter-of-fact, field-honest, low drama" is a credible anchor. Alternatively: "in the style of a Svenska Kraftnät or Energimyndigheten internal documentation photograph — no styling, natural work light, authentic gear, non-promotional".

---

## "Use real photography instead" assessment

### Image 1 (isometric FPV illustration)

This is an illustration, not a photograph. No stock photography alternative applies directly. However, consider using Sunlit Sea's own rendered technical diagrams of the FPV system — any existing isometric or 3D model render would be more accurate to the actual product than a DALL-E 3 illustration. If the Sunlit Sea FPV brochure or D6.2 deliverable contains a system diagram, extract it.

### Image 2 (aerial coastline with Storugns)

Real photography is almost certainly better and achievable from at least two sources:

- **Nordkalk's own press images**: Nordkalk has a media archive (nordkalk.com/press) with aerial and ground-level photos of the Storugns terminal. These would be authentic to the actual location and feature the correct silos, conveyor and berth. Permission would be needed, but for an internal Forsvarsmakten pitch, a clearly credited image from Nordkalk's press archive is likely acceptable.
- **Gotland tourism board / Region Gotland image archive**: Region Gotland and Gotlands Turistförening have image archives (gotland.com/media) including aerial and coastal photographs of northern Gotland. The coastline character will be accurate.
- **Swedish Maritime Administration (Sjöfartsverket) or Trafikverket aerial survey images**: Swedish government agencies have aerial imagery of the entire Swedish coast. Some of this is accessible through Lantmäteriet's image portal.
- A ChatGPT render of northern Gotland at Storugns will be significantly less authentic than any of the above.

### Image 3 (ground-level Baltic FPV view)

Plausible real-photography sources:

- **Oceans of Energy (Netherlands)**: Has produced extensive documentation photography of their North Sea floating solar installation, including ground-level and low-altitude photographs. The visual character — grey-green water, dark FPV panels, concrete breakwater — is very close to what would exist at a Baltic site. Their press images are accessible and likely available for non-commercial use with credit. These are the best available analogue for "what a real FPV installation looks like from the coast".
- **Sunlit Sea project photos from Skiftestjørna (Norway)**: If Sunlit Sea has ground-level photos of their own operating installation at Skiftestjørna in Norway, these would be ideal — the technology is the same even if the water is fjord rather than Baltic. Check the Sunlit Sea image library.
- A DALL-E 3 render of an FPV installation on the Baltic is actually relatively plausible for this image — the specific location is not shown, the FPV technology is the anchor. This is the one image where AI generation may be competitive with stock photography because no specific location accuracy is required and FPV imagery is scarce in stock archives.

### Image 4 (civilian coordinator on jetty)

This is the image most at risk from both the contemplative-man trope and from model hallucination of non-authentic details. Real photography options:

- **Sunlit Sea's own people photography**: If Sunlit Sea has any candid project-site photography from Norwegian or other locations showing staff (or contracted personnel) doing field coordination work — even on a Norwegian fjord rather than Gotland — this would be far more authentic than a DALL-E 3 render and would not carry the contemplative-man prior.
- **Swedish regional development / EU Cohesion Fund project documentation images**: Swedish EU co-funded project reports often contain exactly this type of image — a civilian coordinator at an industrial or coastal site. These are typically Creative Commons licensed. Search "Interreg Baltic Sea" or "Länsstyrelsen Gotland" image archives.
- **Editorial or press images from previous Gotland coastal industrial projects**: Swedish local newspaper archives (Gotlandsbladet, Gotlands Allehanda) occasionally have archival images of civilian coordinators at industrial coastal sites on Gotland. Rights would need to be cleared.
- Of the four images, this is the one where DALL-E 3 is most likely to fail — the contemplative-man prior is very strong and the specificity of the Gotland coastal setting is very hard to enforce. Strongly recommend finding a real photograph for this image rather than relying on DALL-E 3.
