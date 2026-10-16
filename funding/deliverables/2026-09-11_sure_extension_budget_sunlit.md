# SuRE extension — Sunlit Sea additional-resources budget (draft)

Working draft of the numbers and justifications to be entered into the IFE template `funding/background/nye/Sunlit_Additional_resources.xlsx`, which IFE will bundle into the change-notification to CINEA reallocating the freed BayWa r.e. budget (and the effectively vacated Laketricity dependency) to Sunlit Sea's WP6 scope.

Target: additional grant of about 470 000 EUR at the standard SuRE funding intensity of 70 %, per Mario Silva (IFE) on 2026-09-11: *"We can ask for about 470 000 € more for Sunlit's expanded activities … Only fill in information in the cells highlighted in yellow until the point where the column 'additional Grant' reaches about 470 000 €."* This is the O8 target (the grant column), not the M8 total-cost column.

Yellow input cells to fill (from the sheet inspection):

- G11 — number of person-months
- G12 — PM rate (EUR/month)
- H8 — subcontracting (EUR)
- I8 — travel (EUR)
- J8 — equipment (EUR)
- K8 — other g/w/s (EUR)
- H9, I9, J9, K9 — one-line justifications for each of H8–K8

Green cells (G8 personnel formula, L8 indirect, M8 total, N8 funding rate, O8 grant) are computed and must not be touched.

## Summary line (row 8 of the sheet)

| Col | Cost category | EUR | Notes |
|---|---|---:|---|
| G | Personnel costs | 314 000.00 | Computed: G11 × G12 = 31.4 × 10 000 |
| H | Subcontracting costs | 135 000.00 | Marine works, electrical grid tie, monitoring supplier |
| I | Travel and subsistence | 10 000.00 | Site visits and consortium meetings |
| J | Equipment | 75 000.00 | Rental of monitoring instrumentation for the project period |
| K | Other goods, works and services | 30 000.00 | Permits, insurance delta, lab analyses, dissemination |
| L | Indirect costs (auto) | 107 250.00 | 25 % × (G + I + J + K); H excluded per Horizon rules |
| M | Total costs | 671 250.00 | Sum of G–L |
| N | Funding rate | 70 % | Locked |
| O | Additional grant | 469 875.00 | Target: about 470 000.00 EUR (per Mario, 2026-09-11) |

Arithmetic note. Landing at 469 875.00 EUR is 125 EUR under the 470 000 EUR target — well inside "about 470 000" and on the correct side of Mario's phrasing "until the point where … reaches about 470 000.00 €". If a tighter hit is wanted, G11 can be set to 31.4143 for O8 = 470 000.13 (13 cents over). When IFE confirms the actual on-file PM rate for Sunlit Sea (see *Open items*), G11 will be re-tuned to keep O8 close to 470 000 — the PM count is the flex variable, not the other cost lines.

Design principle for this row: Sunlit Sea does the monitoring work in-house (extra Sunlit PM) with rented instrumentation, rather than buying kit that would sit idle after the project or subcontracting a monitoring service that would need to be named and approved by CINEA. This keeps the change notification scoped to a pure budget increase with no new partners or subcontractors to justify.

## Personnel (G) — 314 000 EUR

Enter G11 = 31.4 (person-months) and G12 = 10 000 (EUR/PM). G8 will compute to 314 000. Fractional PM is standard in Horizon Europe budgeting — the sheet accepts it and the project officer expects it.

Thirty-one-point-four person-months over the remaining project period (approximately M24–M36 relative to project start October 2024), split across four roles so the effort is visibly distributed rather than concentrated on one individual:

| Role | PM | Activity |
|---|---:|---|
| CEO / project lead | 4 | Consortium interface, change-notification management, permit and stakeholder coordination (Miljødirektoratet, Herøya Industripark, Herøya Nett, municipality), CINEA reporting delta |
| CTO / lead engineer | 12 | Demonstrator engineering (mooring on capped seabed, float configuration for site conditions), monitoring-instrumentation specification, integration with WP2 mechanical and WP3 performance models |
| Site and commissioning engineer | 8 | Install supervision with Prosolar, commissioning, hand-over to operations |
| Monitoring and data lead | 7.4 | Rental-instrumentation configuration, monitoring-campaign operation, data curation and delivery into the SuRE monitoring framework (WP1) and the WP2/WP3 model chains |

Total 31.4 PM at an assumed PM rate of 10 000 EUR/month. Roughly 2.6 FTE over ~12 remaining project months for an install-and-operate demonstrator phase, with a distinct monitoring/data role added because Sunlit Sea runs the monitoring in-house (rather than subcontracting it to a named service provider that would need to be listed in the change notification). This is a factor 2.6× on the 12 PM Sunlit Sea originally carries in SuRE, reflecting that the extension turns a small paper-modelling scope into a real physical demonstrator plus a full monitoring campaign. The rate must match the one already recorded for Sunlit Sea in the original SuRE grant — do not introduce a new rate here.

## Subcontracting (H) — 135 000 EUR

Enter H8 = 135 000. Not subject to the 25 % indirect uplift, so it is a "clean" euro-for-euro line. Three sub-items:

| Sub-item | EUR | Rationale |
|---|---:|---|
| Marine works: mooring installation, install vessel, diver time | 60 000 | Gunneklevfjorden mooring must sit on the capped contaminated seabed left after Hydro's environmental remediation; installation is more constrained than on a normal seabed and requires a vessel with a competent marine crew. |
| Grid tie and low-voltage electrical works | 50 000 | Executed by local partner Prosolar, who already provides engineering and later O&M for the site. |
| Monitoring instrumentation supply and calibration | 25 000 | Supplier of met-station, load sensors, DAQ hardware and calibration services. |

The Miljødirektoratet reference in the mooring line is deliberate: it signals to the CINEA officer that Sunlit Sea has already worked through the permitting geometry of the site, not that mooring is a novel risk.

## Travel and subsistence (I) — 10 000 EUR

Enter I8 = 10 000. Deliberately modest. Site visits to Herøya (Porsgrunn) from Oslo, plus consortium review meetings tied to the change. A larger travel line would attract scrutiny disproportionate to the amount.

## Equipment (J) — 75 000 EUR (rental)

Enter J8 = 75 000.

This line is the *rental cost* of monitoring instrumentation for the demonstrator period, not a purchase. Under the Horizon Europe rules for Equipment, rental / operational-lease costs are eligible at 100 % for the rental term — no depreciation haircut, no residual asset on Sunlit Sea's balance sheet, and no obligation to justify why we would want to keep 3 more years of use out of a 4-year-life monitoring kit that only serves this project. The €75 000 covers a 12-month rental of a research-grade monitoring package covering:

- Meteorological station (irradiance, wind, wave proxy, water temperature)
- Structural and mooring load sensors (feeding WP2 mechanical-load models)
- Additional string-level electrical monitoring beyond standard plant instrumentation (feeding WP3 performance-loss quantification)
- Data-acquisition hardware, edge storage, and cellular/wired connectivity
- Installation, calibration, and removal at end of project

Not included in this line and not funded by CINEA: the PV modules, aluminium floats, mounting hardware, mooring, inverters and grid-tie hardware that make up the commercial plant itself. Those become a revenue-earning asset after the project and are funded through Enova, the PPA with Aaltvedt, and Sunlit Sea equity — not through the SuRE budget. This split matches the standard Horizon Europe treatment of commercial-plant hardware in demonstrator projects.

Rental price is subject to the standard cap that it must not exceed what depreciation would have cost — commercial vendor rates for the instrumentation classes above are comfortably within that cap.

## Other goods, works and services (K) — 30 000 EUR

Enter K8 = 30 000.

- Permit and application fees (municipality, Miljødirektoratet, grid connection).
- Incremental insurance premium attributable to the demonstrator during construction and operation within the project period.
- Environmental-monitoring lab analyses (water samples, sediment interaction with the mooring footprint).
- Dissemination items directly attributable to the demonstrator: site signage, factsheet, one open-day event.

## Indirect costs (L) — 107 250.00 EUR (auto)

Computed by the sheet as 25 % × (G + I + J + K) = 25 % × 429 000 = 107 250. Subcontracting is correctly excluded from the base.

## Justification texts — final wording for the sheet

The four "Explain costs in this cell" placeholders (H9, I9, J9, K9) are the only free-text areas in the sheet. There is no personnel-cost justification cell — personnel is self-documented by G11 (PM count) and G12 (rate). Suggested final wording, one sentence each, calibrated to fit a narrow spreadsheet cell:

- H9 (subcontracting): Marine works and install-vessel hire for mooring on the capped seabed (subject to Miljødirektoratet approval), low-voltage grid tie by local partner Prosolar, and supply and calibration of monitoring instrumentation, for the Gunneklevfjorden demonstrator at Herøya Industripark (Norway).
- I9 (travel and subsistence): Site visits to Herøya (Porsgrunn) and consortium review meetings tied to the demonstrator.
- J9 (equipment): Rental of a research-grade monitoring package for the demonstrator period — meteorological station, structural and mooring load sensors, additional string-level electrical monitoring, data acquisition and connectivity, including installation, calibration and removal — feeding data into the WP1 monitoring framework and the WP2 mechanical-load and WP3 performance-loss model chains.
- K9 (other g/w/s): Permit and application fees, incremental insurance for the demonstrator during the project period, environmental-monitoring lab analyses and direct dissemination.

## Framing points for IFE's cover message (not entered in the sheet)

Three points to plant with the CINEA project officer via IFE's cover text, kept short and forward-looking:

1. The reallocation restores a *physical demonstration site* to SuRE. BayWa r.e.'s exit removed one deployment site (Netherlands, Laketricity-integrated); the Gunneklevfjorden work puts a comparable Norwegian demonstrator back in.
2. The site is de-risked well beyond a paper proposal. Enova has funded the pre-project (1 MNOK), Herøya Nett has confirmed grid capacity, Miljødirektoratet has confirmed jurisdiction and accepted subsurface mooring, the municipal planning service is positive to processing an application, and Prosolar is engaged for engineering and O&M.
3. Data from the demonstrator flows back into the consortium — into WP1 monitoring, WP2 mechanical load and wear, and WP3 performance-loss quantification — so the extension delivers value to the whole project, not only to Sunlit Sea.

Do not reopen the reasons for BayWa r.e.'s exit, the effect on Laketricity, or the CINEA processing time.

## Open items — confirm with IFE before returning the sheet

1. PM rate on file for Sunlit Sea in the original SuRE grant — this budget assumes 10 000 EUR/PM as a placeholder. The final rate must match the grant record exactly; if the on-file rate differs, adjust G11 so the O8 cell still lands close to 470 000 EUR (higher rate → fewer PM, lower rate → more PM). Personnel is the flex variable; the other cost lines stay as drafted.
2. Whether the change notification wants any additional attachments beyond the completed sheet (short activity description, updated Gantt for Sunlit Sea tasks, list of amended deliverables). Ask Mario before submitting so a follow-up round is avoided.
