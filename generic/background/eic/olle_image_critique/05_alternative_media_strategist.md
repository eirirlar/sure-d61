---
persona: Alternative-media strategist
focus: challenging whether ChatGPT is the right tool per slide; identifying existing photography, diagrams, satellite imagery and other sources
---

# Image critique: Olle Roman leave-request deck

Reviewer posture: ChatGPT image generation is a last resort, not a default. The question for each slide is what the image needs to *do* for a Swedish military HR reader — and whether a real photograph or an existing technical figure does that job better than a synthetic render.

---

## Slide 1 — Projektet i korthet (isometric FPV overview)

### What the image needs to do

Establish immediately that this is a credible, engineered system — not a concept sketch. The slide title says "the project in brief", so the image anchors the system visually before any bullet text is read. A Forsvarsmakten HR reader who has never seen offshore FPV needs to believe, within two seconds, that the technology exists and is deployed. An AI-generated isometric illustration does the opposite: it signals "we drew what we wish existed."

### Alternative-media options

**Option A — SUREWAVE D8.3 technical brochure, fig01.png**
The SUREWAVE brochure opens with a professional aerial drone photograph of the actual Skiftestjørna installation: a circular grid of dark-blue panels on open sea, surrounded by a concrete breakwater ring with yellow mooring buoys, anchor chains descending into clear water, islands visible on the horizon. This is a real photograph of the actual SUREWAVE technology. It is publicly released in a Horizon Europe deliverable (D8.3), which means it is available for consortium use. Cost: zero. Effort: copy the file, crop to 16:9. Licensing: consortium public deliverable; Sunlit Sea is a SUREWAVE beneficiary and the operator of the Skiftestjørna installation — they own or co-own the photo rights. Communicative suitability: excellent. The photograph is more persuasive than any render because it shows the system exists. Cons: the installation is circular, not rectangular as specified in the prompt description, but that mismatch is irrelevant to the slide's actual purpose.

**Option B — Sunlit Sea press pack / sunlitsea.com press images**
Sunlit Sea maintains a press-release image set used in media appearances and investor materials. The two web images already in this repo (`asset-solar-panels-multiple.jpg` and `asset-solar-floating.jpg`) show: (1) a man in yellow waders standing on a large deployed FPV array on a calm lake, panels extending to the horizon; (2) a close-up of FPV panels at water level in rough sea. Both are professional photography. The lake installation photo (asset-solar-panels-multiple.jpg) is striking and immediately credible. Cost: zero — already in repo. Licensing: Sunlit Sea press imagery. Suitability: high for "this is a real system" framing. Cons: the lake setting reads more as inland freshwater than Baltic Sea; the man in yellow waders might invite a "whose project is this?" read, but could also be removed via light crop.

**Option C — SUREWAVE D8.3, fig03.png (system diagram with labels)**
Fig03 is a rendered three-quarter ground-level view of the full system showing a concrete breakwater barge, transition elements, PV array, and catenary mooring — with component labels. It is a technical render produced for a Horizon Europe deliverable. More diagrammatic than photographic, but carries the authority of a consortium technical document. Cost: zero, already in repo. Effort: screenshot/extract at full resolution. Suitability: good as a secondary technical figure, slightly better for a "how it works" slide than an overview.

**Option D — SUREWAVE D8.3, fig04.png (top-down plan drawing)**
Fig04 is the 340 m diameter reference plant layout — a clean engineering plan view showing the circular array of FPV modules, breakwater perimeter, mooring lines, and a north arrow. This is an engineering drawing, not a photograph. For a slide titled "the project in brief" it is usable as a supplementary technical inset. Cost: zero. Suitability: lower than fig01 as the lead image since it reads as engineering documentation rather than a "here is the technology" opener.

### Recommendation

Use fig01.png from the SUREWAVE D8.3 brochure as the slide's lead image. Confidence: **high**. It is a real aerial photograph of the exact technology Olle will be coordinating. A Forsvarsmakten HR reader looking at a real installation photograph reads "this is a funded, operating European consortium project." An AI isometric illustration reads "someone made a nice picture."

Fallback: `asset-solar-panels-multiple.jpg` (the Sunlit Sea press photo of the deployed array on water). Slightly different setting (lake, not sea) but still a real deployed installation.

### If ChatGPT is still used

Drop the isometric/cutaway instruction entirely. Request a straight overhead drone photograph style — not an illustration. The isometric cutaway aesthetic is the most AI-generation-legible style there is; a Forsvarsmakten reader who has seen drone footage knows instantly it is synthetic. If generation is used, request: "Overhead drone photograph, photorealistic, of a rectangular grid of offshore floating solar panels on calm open sea, surrounded by a grey concrete breakwater ring, no people, no vessels, clear Nordic sky, 16:9." Remove all "illustration", "flat shading", "muted palette" language — those are tells that you are asking for an illustration, not a photograph.

---

## Slide 2 — Platsen på Gotland (aerial coastline)

### What the image needs to do

Locate the project geographically and anchor it to a real, identifiable place. For an HR reader who will be approving a leave request, "the location is real and specific" is the key message. An AI-generated coastline does the opposite: it is demonstrably not Storugns. Worse, a reader with any map familiarity will notice the coastline is generic and invented. Geographic slides should show the actual geography.

### Alternative-media options

**Option A — Google Earth / Google Maps satellite screenshot**
Coordinate: 57.844 N, 18.797 E. In Google Earth Pro (free for personal use) you can orbit to an oblique view, looking southwest over the Storugns coastal area, showing the limestone quarry, Nordkalk terminal, the small pier, and the pale Baltic water. A screenshot at 1920×1080 takes five minutes to produce. The image is immediately identifiable as the actual site. Cost: zero. Effort: five minutes. Licensing: Google Earth imagery for presentation use is generally permitted under Google's terms; add a small "Source: Google Earth" attribution in the slide notes or footer. Communicative suitability: extremely high — nothing tells a reader "this is real" faster than a Google Earth view they can cross-reference in Maps themselves.

**Option B — Nordkalk Storugns press photography**
Nordkalk is a major limestone producer operating at Storugns. Their press pack and website (nordkalk.com) include professional aerial and ground-level photography of the Storugns site showing the quarry, coastal terminal, and Baltic water. Their YouTube channel ("Nordkalk Storugns 2024") contains at minimum one aerial video from which stills can be extracted. Cost: low (contact press@nordkalk.com; for a Horizon Europe project they will almost certainly provide images gratis with attribution). Effort: one email, 24–48 hours. Licensing: request permission for non-commercial academic/project use; Nordkalk's participation in the local economy makes them likely supporters of EU visibility. Suitability: high — real site, professional production, shows the industrial coexistence context.

**Option C — Visit Gotland / Gotlands Media press imagery**
Visit Gotland maintains a press archive (visitgotland.com/press) with professional photography of the northern Gotland coast — limestone cliffs, junipers, Baltic light. Gotlands Media (local newspaper) has aerial photography of the Fårö/northern Gotland area. Cost: low (free for non-commercial use with attribution, or very low stock licensing fee). Effort: 30 minutes to browse and download. Suitability: moderate — great for capturing the Nordic coastal character but unlikely to show the Storugns industrial area specifically.

**Option D — Lantmäteriet / Swedish Geodata Portal**
Sweden's Lantmäteriet (lantmateriet.se) provides free high-resolution aerial photography of the entire country through its Geodataportalen. Northern Gotland coverage is excellent. This is official Swedish government imagery with clear licensing for educational and research use. Cost: zero. Effort: 20 minutes to navigate the portal and export a tile. Suitability: high for accurate representation of the actual site; the imagery may be 2–3 years old but the site changes slowly.

### Recommendation

Google Earth oblique screenshot of 57.844 N, 18.797 E. Confidence: **high**. A five-minute task that produces a geographically accurate, instantly recognisable image of the actual location. Forsvarsmakten HR readers can pull out their own phone and confirm the location. An AI-generated coastline cannot compete with this level of specificity and credibility.

Fallback: Nordkalk press imagery (contact nordkalk.com press) or Lantmäteriet aerial photography from the Geodataportalen.

### If ChatGPT is still used

Do not use ChatGPT for this slide. The prompt describes a generic Nordic limestone coastline that will produce something indistinguishable from Gotland, Öland, the Norwegian coast, or a Finnish island — it has no identifying features. The HR reader will see "generic Nordic coastline" and understand the presenter does not know the actual site. If for some reason none of the real imagery is obtainable, replace the image with a map inset (OpenStreetMap iframe exported as PNG showing northern Gotland with a location pin at Storugns) — this conveys "specific real place" far better than AI generation.

---

## Slide 3 — Hur tekniken fungerar (ground-level sea view with FPV)

### What the image needs to do

Convey the physical scale relationship between the installation and the water surface, so a reader who has never seen offshore FPV can intuit how it sits on the sea. This is a technical education slide. Authenticity is the dominant need: the reader needs to believe the panels actually float on the sea and are not conceptual.

### Alternative-media options

**Option A — SUREWAVE D8.3, fig15.png (sea-level photo of deployed prototype)**
Fig15 in the SUREWAVE brochure is a real photograph at sea level: a prototype SUREWAVE module being wave-tested in open water (looks like the Mediterranean deployment trial), with a concrete breakwater barge visible and waves breaking around the edges. This is a real system on real water. The image is slightly rough/grainy (video still quality) but it is exactly what the slide description asks for: ground-level, FPV on sea, breakwater perimeter visible. Cost: zero, in repo. Licensing: SUREWAVE consortium public deliverable. Suitability: excellent — it is the actual system, showing real sea conditions.

**Option B — SUREWAVE D8.3, fig03.png (three-quarter rendered system view)**
As noted above, fig03 shows the full system architecture — breakwater barge, transition elements, PV array — at a low oblique angle with component labels. For a "how the technology works" slide, the labelled render may be more useful than a photograph alone because it names the parts. Cost: zero. Effort: extract at full resolution. Suitability: high as a companion or overlay to a text explanation; lower than a photograph as a standalone background image.

**Option C — Sunlit Sea `asset-solar-floating.jpg`**
The close-up wet-conditions photograph of FPV panels at water level (already in repo) shows panels riding on choppy water. The aesthetic is moody and slightly dark but authentic — this is what the system looks like in real Baltic-type conditions, not a calm Mediterranean lagoon. Cost: zero. Licensing: Sunlit Sea press. Suitability: high for "the system sits on the water" message; the rough sea conditions may actually be more relevant for a Baltic presentation than a calm-water shot.

**Option D — Composite: fig03 PNG overlay on `asset-solar-floating.jpg` background**
A simple Canva or PowerPoint composite: the Sunlit Sea close-up photograph as a full-bleed background with the fig03 schematic as a semi-transparent technical inset in the upper right. This communicates both "it is real" (photograph) and "here is how it is structured" (diagram) in one image. Cost: 20 minutes in Canva. Effort: low. Suitability: potentially the highest-impact option for a "how it works" slide.

### Recommendation

SUREWAVE D8.3 fig15.png as the primary image, potentially combined in a composite with fig03 as a small inset. Confidence: **high** for the standalone fig15 option; **medium-high** for the composite (depends on execution). The raw photograph of the prototype in real sea conditions is more persuasive than any AI render of calm turquoise water — the slightly rough/authentic look signals "real engineering test" not "marketing material."

Fallback: `asset-solar-floating.jpg` as a full-bleed background — the moody, close-up wet panels are immediately credible and the dark palette works well as a slide background.

### If ChatGPT is still used

The original prompt is too serene. The description asks for "glassy and reflective" water with "warm golden horizontal light" — this produces a marketing render. A Forsvarsmakten reader looking at a golden-light glassy Baltic will read "promotional material." If generation is unavoidable, request documentary style with slightly overcast light, textured water surface, and a grittier palette. Remove all references to "late-afternoon" and "golden" light — those are advertising photography triggers. Add: "photojournalistic documentary style, slight grain, muted palette, no golden hour."

---

## Slide 4 — Olles roll (civilian coordinator on jetty)

### What the image needs to do

Establish Olle as a credible, professionally active coordinator — not as a tourist or a generic stock-photo stand-in. This is the most sensitive image in the deck: the audience is Olle's own military line management, approving his absence. The image must not read as AI-generated, must not look like a stock photo, and must not look promotional. A competent HR reader will notice immediately if the "Olle" in the photo does not look like someone who exists.

### Alternative-media options

**Option A — Drop the image entirely; use a plain text slide**
This is the most defensible recommendation for this slide. Olle's role can be conveyed in a clean text block: his title, reporting line, deliverables, time commitment. A text slide is more credible to an HR reader than a synthetic photograph of a person who does not exist. The risk of AI-generation detection is highest on human portrait photographs — the hands, the reflection in the phone screen, the way the jacket drapes. These are exactly the tells an experienced HR reader will notice. Cost: zero. Effort: zero. Communicative suitability: high — the content is what the HR reader needs, not a photograph of a man on a jetty.

**Option B — A real photograph of Olle Roman**
If Olle has a suitable photograph of himself on a coastal site — from a field visit, a site inspection, a previous project — this is unambiguously the right image. It does not need to be taken on Gotland. A photograph of Olle looking at a coastline, holding a notebook, dressed in civilian clothes, is impossible to confuse with AI generation. Cost: zero. Effort: Olle searches his phone. Suitability: the highest possible.

**Option C — A real photograph of someone in a comparable role at a comparable project**
If the SUREWAVE consortium has published press images from site coordination activities — an engineer or project manager visiting a marine site — those images exist as real photographs with real people. Cost: low (check SUREWAVE.eu press). Suitability: moderate; the person is not Olle and a sharp HR reader may ask "who is that."

**Option D — Unsplash / Pexels stock photography**
Search: "man coastal site survey notebook" or "engineer site visit harbour". Unsplash and Pexels have thousands of professional documentary-style photographs of people in civilian outdoor clothing in coastal environments. These are real photographs of real people. Cost: zero (Unsplash free licence; Pexels free licence). Effort: 15 minutes. Licensing: free for commercial and personal use. Suitability: moderate. The risk is that a stock photo looks like a stock photo — but that is still better than an AI-generated photograph. Key criterion: the person must be clearly middle-aged, dressed plainly, doing something purposeful, with no high-visibility or safety elements.

### Recommendation

Drop the image. Use a plain text slide or a simple info-box layout listing Olle's proposed role, scope, and time commitment. Confidence: **high**. The communicative purpose of this slide is to make the HR reader confident in Olle's preparation and seriousness. A wall of text with specifics ("weekly coordination calls with SUREWAVE consortium; on-site presence during installation week; reporting to project manager per Horizon Europe D8.x schedule") is more persuasive than any photograph. The AI-generation risk on human photographs is unacceptable for this audience.

Fallback: a real photograph of Olle himself on any coastal or industrial site. If that photograph exists, it belongs in the deck. If it does not exist, text is correct.

### If ChatGPT is still used

Do not use ChatGPT for this slide under any circumstances. A photorealistic AI-generated photograph of a person, described with such specificity (softshell jacket, notebook, mobile phone, three-quarter rear view, coastal pines lower left), will show artefacts that a 50-year-old HR officer will recognise immediately as synthetic. The specific risk is the hands holding the phone — AI still struggles with hand anatomy in this framing. The secondary risk is the jacket material and the coastline vegetation. This slide has the highest "AI leakage risk" in the deck and the lowest justification for AI generation — do not proceed.

---

## Overall strategy for the deck's imagery

**Use SUREWAVE brochure fig01.png for slide 1. Use Google Earth for slide 2. Use SUREWAVE fig15.png or the Sunlit Sea close-up for slide 3. Abandon slide 4's photograph entirely and replace with a text block.**

Abandon ChatGPT image generation for this deck entirely.

The reasoning:

1. The audience is a military HR reader evaluating a leave request. Credibility and sobriety matter more than visual polish. Real photographs from a Horizon Europe deliverable carry institutional weight that AI renders cannot. They also signal that the project is real, funded, and documented — not assembled from a chatbot.

2. All four image needs can be served without AI generation. The SUREWAVE brochure (publicly released, consortium-usable, already in this repo) provides excellent coverage for slides 1 and 3. Google Earth covers slide 2 at higher geographic specificity than any AI generation could. Slide 4 does not benefit from a photograph at all.

3. The iterative cost argument is self-defeating. The user flags that ChatGPT image generation is expensive to iterate. That cost is incurred precisely because AI renders rarely nail the brief on the first attempt. Real photographs either fit or they do not — and if they fit, the iteration cost is zero.

---

## Tactical steps

1. **Slide 1:** Open `surewave/images/2026-09-28_surewave_d8.3_technical_brochure_lowres/fig01.png` in any image editor (even Paint). Crop to 16:9 (approximately 1920×1080 px centering the circular array). Export as JPEG at 80% quality. Insert into the slide as full-bleed background. Add a small attribution footnote: "Photo: SUREWAVE consortium / Sunlit Sea AS. Horizon Europe Grant 101083342." Total time: 5 minutes.

2. **Slide 2:** Open Google Earth Pro (free download from earth.google.com). Enter coordinates 57°50'39"N 18°47'49"E in the search bar. Switch to 3D view and tilt to approximately 30–35 degrees, looking southwest so the Nordkalk terminal and sea are both visible. Zoom to ~2 km eye altitude. Take a screenshot at full screen resolution. Crop to 16:9. Add attribution: "Source: Google Earth." Total time: 10 minutes.

3. **Slide 3:** Use `surewave/images/2026-09-28_surewave_d8.3_technical_brochure_lowres/fig15.png` as the primary option. If the image quality (video-still grain) is unacceptable at full size, fall back to `asset-solar-floating.jpg` from the root or `surewave/images/2026-09-29_sunlit_sea_webpage/asset-solar-floating.jpg`. The close-up Sunlit Sea photograph has a slightly darker, rougher aesthetic that suits a slide titled "hur tekniken fungerar" — it shows the technology handling real sea conditions. Insert as full-bleed and place any explanatory text boxes on the left third of the slide where the image is less busy. Attribution for fig15: as above. Attribution for Sunlit Sea photograph: "Photo: Sunlit Sea AS."

4. **Slide 4:** Delete the image placeholder. Replace with a clean two-column text layout: left column — "Olles uppdrag" with three to four bullet points (specific deliverables and coordination tasks); right column — "Tidsomfattning" with a simple table showing weeks on-site, weeks remote, total hours. No photography. If a visual anchor is needed, a small SUREWAVE consortium logo or the Horizon Europe flag-and-text emblem signals EU-project legitimacy without requiring a person photograph.

5. **ChatGPT image generation budget:** Zero. Redirect the budget to the 20 minutes needed for steps 1–4.
