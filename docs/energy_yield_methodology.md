# Energy-yield methodology

Reference note for `scripts/estimate_yield.py` and the `estimate-yield` skill. Explains inputs, defaults, data sources, the yield computation, loss decomposition, scenario sensitivity, FPV cooling bonus, and what the estimator does *not* do.

## What the estimator produces

A preliminary estimate of annual AC energy yield for a floating-PV site, formatted as a six-section Markdown report in the Sunlit Sea *Simuleringsrapport* style (headline KPI row + Panelkonfigurasjon og areal + Solinnstråling og POA-analyse + Tapsbudsjett / PR-dekomponering + Energiproduksjon + Sensitivitetsanalyse + Nøkkelantakelser og begrensninger). YAML frontmatter `sunlit_template: report` routes the file through `md_to_sunlit_report.py` for PDF rendering in the Sunlit Sea visual profile.

Reference artefact for the target format: [`../generic/background/2026-09-17_simuleringsrapport_blekinge_mulighetsstudie.pdf`](../generic/background/2026-09-17_simuleringsrapport_blekinge_mulighetsstudie.pdf).

Intended use:

- RFP and tender responses where a plausible annual production figure with a defensible assumption chain must be stated.
- Investor and board material where an order-of-magnitude yield with scenario range is needed.
- Internal commercial-pipeline sizing.

*Not* a bankable P50/P75/P90 yield. Projects that need bankable numbers go through site-measured solar resource, a validated PV model (PVsyst or equivalent), and third-party review.

## Inputs

Minimum (must be supplied):

- Latitude and longitude in WGS84 decimal degrees.
- Either installed DC capacity (`--kwp`) **or** available water surface area (`--area` in m²). When area is supplied, the panel count and installed capacity are derived from the panel geometry defaults; when capacity is supplied directly, panel count is back-calculated from the panel-power default and the panel-configuration section is marked as not-from-area.

Optional overrides (defaults apply if omitted):

| Parameter | Default | Notes |
|---|---|---|
| Panel width × height | 2384 × 1303 mm | Matches the CONNECT product class. |
| Panel nominal power | 740 Wp | Middle of the 710–740 Wp class. The reference Simuleringsrapport used 750 Wp. |
| Inter-panel gap | 100 mm | Matches the reference. |
| Tilt | 2° | CONNECT architectural tilt. |
| Azimuth (compass) | 180° | 0 = N, 90 = E, 180 = S, 270 = W. Converted internally to PVGIS aspect. |
| Loss components (9 of them, each independently adjustable) | See below | Sum defaults to 10 % → PR = 90 %. Matches the reference. |
| FPV cooling bonus | 2 % | DC-yield uplift vs land reference. Conservative; see *FPV cooling bonus* below. |
| Reference year | PVGIS TMY | Override with a specific year when the user needs an actual-weather estimate. |

### Default loss decomposition (sum = 10 %)

| Component | Default (%) |
|---|---|
| Temperature coefficient | 3.0 |
| Inverter | 2.0 |
| DC cable | 1.0 |
| AC cable | 0.5 |
| Mismatch | 0.5 |
| Soiling | 0.5 |
| LID (light-induced degradation) | 0.5 |
| Availability | 1.0 |
| Transformer | 1.0 |

Each component is an independent `--loss-<name>` flag. Users adjust individual values when a site-specific or project-specific number is defensible (e.g. dropping soiling to 0.2 % for a protected fjord site, or raising temperature to 4 % for a tropical deployment). PR is computed as `100 − Σ losses`.

## Data sources

### PVGIS 5.2 (primary)

The estimator calls the European Commission Joint Research Centre's PVGIS 5.2 web service with two endpoints:

- `PVcalc` with `loss=0` — returns the plane-of-array irradiation (POA, `H(i)_y` and `H(i)_m`) at the specified tilt and azimuth, and PVGIS's own AC yield estimate using the crystSi model with internal temperature and spectral derating. The POA is used as the physical irradiation input. The AC yield is retained as a cross-check only.
- `MRcalc` with `horirrad=1` — returns the monthly horizontal irradiation (GHI, `H(h)_m`) over the standard PVGIS reference period (2005–2020). Annual GHI is summed and averaged across years.

GHI and POA are shown side by side in the report so the reader sees the tilt gain explicitly (`+N %` vs horizontal).

### Yield formula

The authoritative yield figure is:

```
E = POA × kWp × PR × (1 + fpv_cooling_bonus)
```

where:

- `POA` is the PVGIS plane-of-array annual irradiation in kWh/m²/year.
- `kWp` is the installed DC capacity.
- `PR` is the Performance Ratio from the user-supplied loss decomposition (`PR = 100 − Σ losses`, in decimal form).
- `fpv_cooling_bonus` is the DC-yield uplift vs land reference (default 2 %).

PVGIS's own AC yield (crystSi model at `loss=0`, before the external PR) is shown in section 3 as a cross-check. When the two estimates diverge by more than ~1 pp in PR, the report notes it: if the user's PR is higher than PVGIS's implied PR, the component list is likely optimistic; if lower, conservative.

This decoupled computation is what lets the user's loss decomposition remain meaningful. A naïve approach that hands the total loss to PVGIS and reports back the AC yield double-counts temperature (PVGIS has its own temperature model) and makes the component values uninterpretable. The reference Simuleringsrapport uses the same decoupled approach.

### Over-sea handling

PVGIS refuses lat/lng that fall over open water (HTTP 400 "Location over the sea"). For nearshore floating PV this is the normal case. The estimator catches the error on either endpoint and auto-nudges to the nearest land grid cell in an expanding 500 m-step search out to ~5 km. The nudged coordinate is printed in the assumption audit (Section 6) when nudging happened. A site genuinely far from any coast falls outside the search and errors out.

### NASA POWER fallback

Not yet wired. PVGIS being down is rare; adding POWER as a fallback is a future enhancement.

## FPV cooling bonus

Floating PV modules cool faster than land-mounted modules because the water below acts as a heat sink and the air layer between module and water is more convective than a ground boundary layer. Published FPV field studies report DC-yield uplifts in the range 2–10 % vs matched land-based references, with the higher end from shallow-tropical lake studies and the lower end from temperate / cold-water sites.

The estimator defaults to **2 %** — the conservative end of the range. That default reflects:

- The lack of a validated site-measured cooling bonus for any Sunlit Sea deployment today.
- The CONNECT architecture, where the module sits on a cast PU structure above the water surface (not touching the water), which reduces cooling-bonus magnitude compared with raft-on-water designs.
- A deliberate under-promise.

Override to a measured value when it becomes available from SuRE / Gen 2 thermal work. The default should drop in the estimator once that measurement lands.

The bonus is a simple multiplier on the annual and monthly yield. A temperature-weighted monthly bonus (larger in summer than winter) is a future enhancement.

## Scenario sensitivity

Three scenarios are reported as a Low / Base / High table:

- **Base** — the computed yield.
- **Low** — GHI reduced by 5 %, PR reduced by 3 pp. Approximates a pessimistic-but-plausible combination of a low-irradiation year and a slightly higher real-world loss budget.
- **High** — GHI increased by 5 %, PR increased by 2 pp. Approximates an optimistic-but-plausible combination.

The scenario range is implemented as `E × (1 ± ΔGHI) × ((PR ± ΔPR) / PR)`. The absolute scenario spread (Low → High) is typically ±7–8 % around the base, which matches the reference Simuleringsrapport.

This replaces the per-parameter sensitivity table (tilt ±5°, azimuth ±30°, cooling bonus endpoints) used in the earlier estimator version. The scenario table is what procurement and investor audiences expect; parameter-level sensitivity remains useful internally but is not shown by default.

## What the estimator explicitly does not do

- No coupled float thermal model. The FPV cooling bonus is a flat multiplier, not a modelled heat balance between module, float, air and water.
- No wind-driven tilt variation. CONNECT tilt is architecturally fixed.
- No bathymetry-dependent albedo. Shallow / reflective bottoms (sandy lagoons) can raise effective albedo and bifacial gain; the estimator does not model this.
- No site-specific shading from local obstructions. PVGIS handles horizon masking (mountains, hills) when `usehorizon=1` but not nearby buildings, cranes, other arrays. The estimator trusts PVGIS on horizon and assumes no local shading.
- No bifacial gain model. Monofacial only in this version.
- No LCOE / NPV / cashflow. That is a commercial model, kept separate.
- Not a design optimiser. One run, one number out. Design optimisation (optimal tilt, string sizing, inverter sizing, DC/AC ratio) belongs in PVsyst or the SuRE D6.2 design-screening pipeline (T20).
- No pvlib dependency. PVGIS is the backend; adding pvlib would require per-component Perez / temperature / module / inverter models that duplicate what PVGIS already does.

## When to upgrade from the estimator to a validated tool

- When a project needs a bankable yield for financing.
- When the site's solar resource differs materially from the regional PVGIS cell (microclimate, specific horizon features).
- When the system design requires string- and inverter-specific yield rather than a nameplate yield.
- When a legal, regulatory or grant-reporting commitment requires a specific tool (PVGIS is accepted by many EU funding streams; private lenders typically want PVsyst with site measurement).

In all other cases — RFPs, pipeline sizing, investor and board material, exploratory site screening — the estimator is the right tool.
