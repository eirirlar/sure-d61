Subject: Re: D7.4 rejected – revised version

Hi Balram,

Attached is the revised D7.4 for upload, with a response to the Project Officer below that you can paste into the portal. Also attached is the updated cost workbook (version 3). Please upload it to Zenodo as a new version of the existing D7.4 dataset record (10.5281/zenodo.17534609) before submitting, since the report and the response refer to it.

To include the end-of-life costs, I extended the cost model and reviewed it for completeness at the same time. The model now also includes maintenance of the floating structure, inverters and transformers, the SCADA system and the PV replacement cost in the LCOE, and it uses the standard discounting and IRR conventions. The headline figures change accordingly:

| 10 MW case | LCOE (€/kWh) | NPV | IRR |
|---|---|---|---|
| Mediterranean | 0.062 → 0.076 | €8.9M → €7.3M | 10.7% → 15.6% |
| Baltic | 0.096 → 0.120 | €2.1M → €0.0M (break-even) | 2.2% → 8.5% |
| North Sea | 0.139 → 0.173 | negative | negative → 3.4% |

The IRR is now calculated on undiscounted cash flows, the standard definition, so the old and new IRR values are not directly comparable. Like for like, the return falls with the NPV, from 21.1% to 15.6% for the Mediterranean.

The conclusions hold: the Mediterranean 10 MW configuration is clearly viable and the North Sea is not. The Baltic moves from marginally viable to break-even at the 8.5% discount rate.

Since the revision goes beyond the end-of-life text, you may want to mention the updated figures to the Project Officer before the upload. Let me know how you prefer to handle it.

These figures are also used in the preprint, D7.6, D8.3, D8.4 and the final technical report, so those will need the same update. I will send you corrected text for the preprint and the final report, and I will contact IFEU about D7.6.

Best regards,
Eirik

---

Response to the request for revision of D7.4 (Ref. Ares(2026)9755377)

The revised deliverable (version 2.0) addresses the request as follows.

1. A new Section 2.4, Scope and System Boundary, defines the cradle-to-grave scope. A table lists what the economic model includes, what is covered as a sensitivity only (submarine export cable, discount rate, breakwater design), and what lies outside the assessment as a scope limitation: the offshore substation and grid connection, the electrical losses and onshore works of an export cable, development and permitting, seabed lease, insurance, financing costs, contingency, environmental monitoring, curtailment, and the residual value of recovered materials. The base case connects to an existing or shared offshore substation, so the substation is not part of the cost model.

2. Section 4.4, Disassembly and End-of-Life Considerations, describes end of life as it is now modelled: replacement of the PV modules in year 25, and decommissioning of the structure and the second PV generation in year 50 at a cost equal to their installation cost. Removed PV modules are assumed to be taken back at no net cost, and no residual value is credited for concrete, steel or mooring components. The scenario follows the end-of-life scenario of the environmental assessment (D7.3), which also covers recycling routes and their environmental effects.

3. To include these costs, the cost model was extended and reviewed for completeness (model version 3, published on Zenodo). It now also covers maintenance of the floating structure, inverters and transformers, the SCADA system and the PV replacement cost in the LCOE, and applies standard discounting, with the IRR calculated on undiscounted cash flows. All results in the report are updated: Mediterranean 10 MW LCOE €0.076/kWh, NPV €7.3 million, IRR 15.6%; Baltic 10 MW at break-even; North Sea 10 MW not viable. The conclusions and deployment recommendations are unchanged, except that Baltic deployments are now described as viable at a lower cost of capital.
