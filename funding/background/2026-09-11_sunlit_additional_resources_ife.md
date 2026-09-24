# Additional resources for Sunlit and justifications

IFE-provided template (`Sunlit_Additional_resources.xlsx`, single sheet "Sheet2"), sent to Sunlit Sea 2026-09-11 for input toward the SuRE change-notification to CINEA that reallocates the freed BayWa r.e. budget (and the effectively vacated Laketricity dependency) to Sunlit Sea's WP6 scope. Original xlsx is empty apart from formulas and labels; the values below are those we have to supply.

Sheet name: **Sheet2**. Layout reconstructed:

**Title (row 4, col H):** Additional resources for Sunlit and justifications *(sic — "Adittional" in original)*

## Cost table (rows 7–9)

| # | Column | Header (row 7) | Cell (row 8) | Justification cell (row 9) |
|---|---|---|---|---|
| 1 | G | Personnel costs | `=G11*G12` (PM × PM-rate) | "Justification" (single label spanning the row) |
| 2 | H | Subcontracting costs | *empty — enter EUR directly* | "Explain costs in this cell" |
| 3 | I | Travel and subsistence | *empty — enter EUR directly* | "Explain costs in this cell" |
| 4 | J | Equipment | *empty — enter EUR directly* | "Explain costs in this cell" |
| 5 | K | Other goods, works and services | *empty — enter EUR directly* | "Explain costs in this cell" |
| 6 | L | Indirect costs | `=0.25*SUM(G8,I8:K8)` | — |
| 7 | M | Total costs | `=SUM(G8:L8)` | — |
| 8 | N | Funding Rate 70% | `0.7` (locked) | — |
| 9 | O | Additional Grant | `=N8*M8` | — |

Note the indirect-cost base: `L8 = 0.25 × (G8 + I8 + J8 + K8)` — subcontracting (H8) is deliberately excluded from the 25 % overhead base, in line with standard Horizon Europe rules.

## Personnel-cost inputs (rows 11–12)

| Cell | Label | Input cell |
|---|---|---|
| C11 | Number of Person-months eq (PM) | **G11** (empty) |
| E12 | PM rate (€/month) | **G12** (empty) |

## What the sheet does not contain

- No pre-populated numbers of any kind. Every value cell is empty; the sheet is a fill-in template.
- No dropdowns, no linked lookup tables, no protection on cells.
- No narrative / task-description fields — the four "Explain costs in this cell" placeholders in H9:K9 are the only free-text areas, and they are per cost category (not per task).
- No target amount printed on the sheet. The ~0.4 MEUR figure lives only in prior IFE correspondence.

## Origin and use

- Received from IFE on 2026-09-11 following months of delay at CINEA (CINEA has been occupied with formalising BayWa r.e.'s withdrawal from the consortium).
- IFE's intent: Sunlit Sea fills in the numbers plus one-line justifications per column; IFE bundles it into the change notification submitted to the CINEA project officer.
- This is Sunlit Sea's first substantive written input to CINEA since the BayWa r.e. pull-out — see [`generic/background/loeypemelding/2026-07-16_loeypemelding.md`](../../background/loeypemelding/2026-07-16_loeypemelding.md) §5 for the extension context.
