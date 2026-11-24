"""Sunlit Sea KER1 financial plan model (Horizon Results Booster, T158).

Five-year (2027-2031) projection of the income statement, cash flow and
balance sheet for Sunlit Sea AS, plus a worked unit-economics example for a
3.2 MWp Norwegian plant, a quarterly cash view for 2027-2028, scenario and
sensitivity tables, an indicative outlook to 2035 and an indicative cap
table. All amounts in EUR thousand (kEUR) unless the name says otherwise.
Annual periods, nominal.

This module is the single source of the assumptions (INPUTS, YEARLY, UNIT)
and an independent Python implementation of the model (compute). The Excel
workbook built by build_hrb_financial_workbook.py implements the same annual
model with formulas; test_hrb_financial_model.py checks that both agree for
every scenario and that the three statements tie.

Usage:
    python scripts/hrb_financial_model.py                                  # summary, all scenarios
    PYTHONIOENCODING=utf-8 python scripts/hrb_financial_model.py --md      # Markdown tables for the plan
    PYTHONIOENCODING=utf-8 python scripts/hrb_financial_model.py --md --scenario base

Python packages: none beyond the standard library (the builder and tests need
openpyxl, xlsxwriter, formulas and pytest).
"""
from __future__ import annotations

import argparse
import math

YEARS = [2027, 2028, 2029, 2030, 2031]
N = len(YEARS)

# ---------------------------------------------------------------------------
# Scalar inputs: name -> (value, unit, note). Notes marked [CONFIRM] are
# estimates made without a primary figure.
# ---------------------------------------------------------------------------
INPUTS: dict[str, tuple[float, str, str]] = {
    # scenario switches
    "sw_sure_ext": (1, "0/1", "SuRE extension (about EUR 470k grant, 70 %) approved by CINEA"),
    "sw_eic": (0, "0/1", "EIC Transition SUREWAVE awarded (Sunlit Sea share about EUR 750k, 100 %)"),
    "sw_eupi": (0, "0/1", "EUPI-PV Gotland applied for and awarded (not yet decided whether to apply; grant-funded work and a 1 MWp kit delivery in 2029)"),
    # general
    "fx_nok_per_eur": (11.7, "NOK/EUR", "Conversion of NOK figures (information only)"),
    "tax_rate": (0.22, "share", "Norwegian corporate income tax"),
    "interest_rate": (0.07, "share", "Interest on existing bank and Innovasjon Norge loans"),
    "warranty_rate": (0.01, "share", "Warranty provision, share of kit and EPC revenue [CONFIRM]"),
    "eng_cost_ratio": (0.30, "share", "External direct cost of engineering services; staff time is in personnel [CONFIRM]"),
    "receivables_ratio": (0.12, "share", "Trade receivables at year end, share of revenue (about 45 days)"),
    "inventory_ratio": (0.08, "share", "Inventory at year end, share of kit and EPC direct cost"),
    "payables_ratio": (0.10, "share", "Trade payables at year end, share of direct and external costs"),
    "epc_advance_ratio": (0.30, "share", "Customer advance on EPC contracts, received the year before delivery [CONFIRM]"),
    "eu_recv_ratio": (0.25, "share", "Share of the year's EU grant income paid the following year (payment after reporting)"),
    "skattefunn_rate": (0.19, "share", "Skattefunn support on eligible R&D cost (SME rate)"),
    # opening balance 31.12.2026 (estimated from the 2025 accounts and the 2026 cash forecast)
    "open_dev_asset": (1923, "kEUR", "Capitalised development (konto 1005): 21.7 MNOK at 31.12.2025 plus about 0.8 MNOK 2026 SuRE capitalisation"),
    "open_deferred_grant": (1655, "kEUR", "Deferred grants (konto 2160): 18.8 MNOK at 31.12.2025 (board's going-concern assessment) plus about 0.56 MNOK 2026 grant share"),
    "open_tooling": (361, "kEUR", "Press tooling (konto 1205): 4.2 MNOK"),
    "open_cash": (80, "kEUR", "Cash at 31.12.2026, after the Skattefunn 2025 refund and the Enova pre-project grant for Gunneklevfjorden paid in 2026 [CONFIRM]"),
    "open_skattefunn_recv": (0, "kEUR", "Skattefunn receivable: already paid out (Eirik, 2026-11-22)"),
    "open_bank_loan": (285, "kEUR", "SpareBank 1 loan, about 3.34 MNOK (3.36 MNOK at 17.09.2026 less principal)"),
    "open_in_loan": (44, "kEUR", "Innovasjon Norge loan, about 0.52 MNOK, repaid by July 2027"),
    "open_shareholder_loan": (65, "kEUR", "Intercompany balance with the largest shareholder (KodeWorks AS), about 0.77 MNOK of its 1.1 MNOK informal bridge financing; converted to equity in round 1 [CONFIRM]"),
    "open_payables": (200, "kEUR", "Trade payables incl. aged debt to KodeWorks AS (0.34 MNOK) and UiO (0.70 MNOK) [CONFIRM]"),
    "open_other_liab": (20, "kEUR", "VAT, withholding tax and employer tax payable at year end [CONFIRM]"),
    "open_tax_loss": (543, "kEUR", "Tax loss carried forward, 6.36 MNOK at 31.12.2025"),
    # depreciation and amortisation
    "dev_asset_life": (5, "years", "Amortisation of capitalised development from first use (2027)"),
    "tooling_life": (5, "years", "Existing press tooling and new moulds"),
    "plant_life": (10, "years", "Own plant at Skien havn (conservative: two-year permit and PPA, extension assumed)"),
    # own plant: Skien havn
    "plant_kwp": (350, "kWp", "Skien havn reference plant; ownership (own, joint venture, or partner first) to be settled [CONFIRM]"),
    "plant_yield": (892, "kWh/kWp", "337 MWh/year for 378 kWp in the Skien havn PPA analysis"),
    "plant_ppa_price": (0.060, "EUR/kWh", "About 0.70 NOK/kWh, inside the 0.60-0.80 NOK/kWh range analysed and below the host's break-even of 0.84 NOK/kWh [CONFIRM]"),
    "plant_opex": (8, "kEUR/year", "O&M, insurance, lease: 2.5 % of capex"),
    "plant_capex": (330, "kEUR", "Estimate; the draft Enova application budgets 2.87 MNOK for about 270 kWp (EUR 0.91/W) [CONFIRM]"),
    "plant_capex_grant": (85, "kEUR", "Enova (application in preparation recommends 1.0-1.2 MNOK), net method; the local development fund (about EUR 150k) is left out because the fund wants the pilot completed first [CONFIRM]"),
    "sure_ext_grant": (435, "kEUR", "SuRE extension grant, 2027, recalculated at actual staff cost (EUR 8.75k/PM instead of the EUR 10k/PM placeholder): 70 % of eligible cost incl. 25 % indirect [CONFIRM]"),
    "sure_ext_fte": (1.5, "FTE", "Additional staff for the SuRE extension in 2027; the rest of the 31.4 PM is existing staff whose cost the grant covers"),
    "sure_ext_external": (115, "kEUR", "SuRE extension external costs outside the plant: equipment rental, travel, other; the EUR 135k marine works and grid tie are inside the Skien havn plant cost"),
    "eupi_kit_mw": (1.0, "MWp", "Gotland kit delivery in 2029 under EUPI-PV; the breakwater there is funded in the project and supplied by Clement Germany, outside Sunlit Sea's accounts (Eirik, 2026-11-23)"),
    "eic_followon_mw": (1.0, "MWp", "EIC scenario: first commercial plant on the demonstrator lake (Hainer See type), kit delivery in 2031, the first full year after the EIC project (the EIC proposal targets the first commercial 1-5 MWp installation immediately after project completion, about 2030); 5 MWp follows about 2032 and about 30 MWp later (outlook). The breakwater is bought by the plant owner from Clement Germany and is outside Sunlit Sea's accounts"),
    "eic_followon_eng": (33, "kEUR/MWp", "Engineering fee on the follow-on plant: 4 % of a EUR 0.83/W plant, as for other kit buyers"),
    # equity
    "valuation_pre_round1": (5000, "kEUR", "Pre-money valuation, about the level of the last share issue (company value about EUR 5M) [CONFIRM]"),
    "valuation_pre_round2": (12000, "kEUR", "Pre-money valuation for round 2 after two reference plants in operation [CONFIRM]"),
    "esop_share": (0.08, "share", "Option pool created before round 2 for the hires [CONFIRM]"),
}

# ---------------------------------------------------------------------------
# Year-by-year inputs (2027..2031): name -> (values, unit, note)
# ---------------------------------------------------------------------------
YEARLY: dict[str, tuple[list[float], str, str]] = {
    # phase 1: project development and delivery (EPC) on Norwegian projects
    "epc_mw": ([0, 3.2, 0, 1.2, 2.0], "MWp", "EPC deliveries: Gunneklevfjorden 2028; Storavatnet phase 1 after rezoning and an investment decision in 2029, in two sections 2030 and 2031"),
    "epc_price": ([0.73, 0.73, 0.72, 0.71, 0.70], "EUR/W", "EPC contract price to the plant company (about 12-14 % margin) [CONFIRM]"),
    "epc_cost": ([0.64, 0.64, 0.63, 0.61, 0.60], "EUR/W", "EPC direct cost incl. EUR 0.03/W contingency: kit incl. panel at cost, electrical, grid, mooring, installation, site management; no breakwater (sheltered sites)"),
    "eng_revenue": ([150, 10, 170, 198, 462], "kEUR", "Development and engineering fees: Gunneklevfjorden 2027, Storavatnet 2029; kit buyers at 4 % of a EUR 0.83/W plant (EUR 33k/MWp)"),
    # phase 2: technology provider (kit sales)
    "kit_mw": ([0, 0.3, 0.6, 6.0, 14.0], "MWp", "Kit sales to plants built by others; 10 MW-class contract signed early 2030, 5 MWp delivered 2030 and 5 MWp 2031"),
    "kit_price": ([0.50, 0.50, 0.49, 0.47, 0.45], "EUR/W", "Kit incl. solar panel (floats, hinges, mooring interfaces, panel), delivered: EUR 500/kWp, falling slowly with volume (Eirik, 2026-11-22) [CONFIRM path]"),
    "kit_cost": ([0.25, 0.25, 0.24, 0.22, 0.21], "EUR/W", "Production cost incl. panel ex works China or Lithuania: EUR 250/kWp today (floating system EUR 140/kWp plus panel), falling with volume [CONFIRM path]"),
    "kit_logistics": ([0.03, 0.03, 0.025, 0.02, 0.02], "EUR/W", "Packing, freight, duty and CBAM on the aluminium plate"),
    # own plant production factor
    "plant_factor": ([0.5, 1, 1, 1, 1], "share", "Skien havn in operation from mid-2027"),
    # organisation
    "fte": ([2.0, 4.5, 5.5, 7.0, 8.0], "FTE", "Annual average excl. SuRE-extension staff: project engineer and project manager from early 2028, sales lead mid-2028, production and quality engineer mid-2029, two application engineers 2030-2031"),
    "cost_per_fte": ([105, 108, 111, 114, 117], "kEUR/FTE", "Fully loaded Norwegian cost incl. employer tax and holiday pay, 3 % a year"),
    "rnd_share": ([0.3, 0.5, 0.4, 0.3, 0.3], "share", "Share of staff time on R&D eligible for Skattefunn; 2027 excludes the staff time charged to the SuRE extension"),
    "capitalise": ([0.5, 0, 0, 0, 0], "share", "Share of development cost capitalised: Gen 2 development before first use at Skien havn (1 July 2027), per the policy adopted in the 2025 accounts; later work is improvement and expensed"),
    "dev_share": ([0.85, 0.5, 0.4, 0.3, 0.3], "share", "Share of staff time on development, incl. existing staff time charged to the SuRE extension in 2027"),
    "amort_factor": ([0.5, 1, 1, 1, 1], "share", "Share of a full year's amortisation of capitalised development: first use 1 July 2027"),
    "bizdev": ([300, 300, 350, 400, 450], "kEUR", "Business development: sales, permitting, promotion (EUR 0.3M in 2027 as in the business plan)"),
    "g_and_a": ([85, 120, 145, 175, 205], "kEUR", "Office, accounting, audit, insurance, IT, bank guarantee fees on EPC contracts"),
    "rnd_external": ([230, 250, 100, 150, 150], "kEUR", "DNV design-basis assessment, fatigue and ageing tests, IP, continued development"),
    # grant-funded projects (switches)
    "eic_cost": ([80, 240, 200, 80, 0], "kEUR", "EIC Transition direct costs, Sunlit Sea share (lump sum includes 25 % indirect)"),
    "eic_grant": ([100, 300, 250, 100, 0], "kEUR", "EIC Transition grant (100 %)"),
    "eupi_cost": ([40, 210, 340, 170, 0], "kEUR", "EUPI-PV direct costs, Sunlit Sea share, excl. the kit delivery [CONFIRM: share not yet set in the consortium]"),
    "eupi_grant": ([50, 250, 400, 200, 0], "kEUR", "EUPI-PV grant, Sunlit Sea share [CONFIRM]"),
    # investment and financing
    "moulds_capex": ([250, 200, 0, 300, 300], "kEUR", "Industrial moulds and kit-packing equipment; second set for series volume"),
    "spv_equity": ([0, 200, 0, 0, 0], "kEUR", "Minority equity in the Gunneklevfjorden plant company [CONFIRM]"),
    "equity_raise": ([3500, 0, 2000, 0, 0], "kEUR", "Round 1 closes Q1 2027 after the EIC decision; round 2 in the second half of 2029, after a year of operation at Gunneklevfjorden"),
    "bank_repayment": ([5, 5, 5, 5, 5], "kEUR", "SpareBank 1 renegotiated plan: about 288k NOK a year incl. interest"),
}

# Scenario definitions: switch values
SCENARIOS = {
    "base": {"sw_sure_ext": 1, "sw_eic": 0, "sw_eupi": 0},
    "eic": {"sw_sure_ext": 1, "sw_eic": 1, "sw_eupi": 0},
    "eu_upside": {"sw_sure_ext": 1, "sw_eic": 1, "sw_eupi": 1},
    "downside": {"sw_sure_ext": 0, "sw_eic": 0, "sw_eupi": 0},
}
SCENARIO_LABELS = {
    "base": "Base: SuRE extension approved, no new EU projects",
    "eic": "EIC: base plus EIC Transition SUREWAVE",
    "eu_upside": "EU upside: EIC plus EUPI-PV Gotland (if applied for)",
    "downside": "Grant downside: no SuRE extension, no new EU projects",
}

# ---------------------------------------------------------------------------
# Unit economics: worked example, 3.2 MWp sheltered plant in southern Norway
# ---------------------------------------------------------------------------
UNIT: dict[str, tuple[float, str, str]] = {
    "ue_kit": (0.17, "EUR/W", "Floating system at cost: EUR 0.14/W ex works plus EUR 0.03/W logistics (kit incl. panel EUR 0.25/W ex works)"),
    "ue_panels": (0.11, "EUR/W", "Glass-glass panels, imported, Europe, October 2026"),
    "ue_electrical": (0.10, "EUR/W", "Inverters, DC and AC cabling, transformer"),
    "ue_grid": (0.04, "EUR/W", "Connection behind the host's meter"),
    "ue_mooring": (0.08, "EUR/W", "Anchors and lines, sheltered basin"),
    "ue_installation": (0.07, "EUR/W", "Assembly at a local quay, launch, towing"),
    "ue_site_mgmt": (0.04, "EUR/W", "Engineering, project management, commissioning"),
    "ue_contingency": (0.03, "EUR/W", "Contingency for a first-of-a-kind delivery (about 4 %)"),
    "ue_epc_margin": (0.12, "share", "Sunlit Sea margin on the EPC price in phase 1"),
    "ue_owner_costs": (0.04, "EUR/W", "Plant company: development, permits, insurance during construction"),
    "ue_opex": (12, "EUR/kWp/year", "O&M, insurance, water-area lease"),
    "ue_yield": (858, "kWh/kWp", "Southern Norway, first year: PVGIS 5.2 at Skien, 2 degree platform tilt, 8 % losses for still water (yield rule, Eirik 2026-11-23); was 900"),
    "ue_degradation": (0.004, "1/year", "Glass-glass panels"),
    "ue_life": (25, "years", "Economic life"),
    "ue_wacc": (0.06, "share", "Nominal discount rate of the plant company"),
    "ue_opex_escalation": (0.02, "1/year", "Nominal escalation of O&M costs"),
    "ue_inverter": (0.04, "EUR/W", "Inverter replacement"),
    "ue_inverter_year": (13, "year", "Year of inverter replacement"),
    "ue_host_value": (0.072, "EUR/kWh", "Host's break-even price at Skien havn: 0.84 NOK/kWh ex VAT, from avoided energy purchase, export income and a small grid-tariff saving, at 2026 spot prices of about 0.97 NOK/kWh"),
    "ue_support": (0.25, "share", "Investment support as a share of capex in the supported case (Enova typically 30-50 % of the innovation cost) [CONFIRM]"),
    "ue_kit_price_p2": (0.47, "EUR/W", "Phase 2 kit price incl. panel (2030)"),
    "ue_kit_cost_p2": (0.24, "EUR/W", "Phase 2 kit cost incl. panel and logistics (2030)"),
    "ue_eng_share_p2": (0.04, "share", "Phase 2 engineering fee, share of plant capex"),
    "ue_capex_p2": (0.83, "EUR/W", "Phase 2 plant capex for a kit buyer: kit EUR 0.47/W plus electrical, grid, mooring, installation, engineering and owner costs [CONFIRM]"),
}

UE_COST_ITEMS = ("ue_kit", "ue_panels", "ue_electrical", "ue_grid", "ue_mooring", "ue_installation",
                 "ue_site_mgmt", "ue_contingency")


def inputs_for(scenario: str = "base", overrides: dict | None = None):
    s = {k: v[0] for k, v in INPUTS.items()}
    s.update(SCENARIOS[scenario])
    y = {k: list(v[0]) for k, v in YEARLY.items()}
    u = {k: v[0] for k, v in UNIT.items()}
    for k, v in (overrides or {}).items():
        if k in s:
            s[k] = v
        elif k in y:
            y[k] = list(v)
        elif k in u:
            u[k] = v
        else:
            raise KeyError(k)
    return s, y, u


def compute(scenario: str = "base", overrides: dict | None = None) -> dict:
    """Independent Python implementation. Returns {line: [values 2027..2031]}."""
    s, y, u = inputs_for(scenario, overrides)
    r: dict[str, list[float]] = {}
    sw_s, sw_e, sw_u = s["sw_sure_ext"], s["sw_eic"], s["sw_eupi"]
    rng = range(N)

    kit_mw = [y["kit_mw"][t] + (sw_u * s["eupi_kit_mw"] if YEARS[t] == 2029 else 0)
              + (sw_e * s["eic_followon_mw"] if YEARS[t] == 2031 else 0) for t in rng]
    r["kit_mw_total"] = kit_mw
    r["rev_epc"] = [y["epc_mw"][t] * y["epc_price"][t] * 1000 for t in rng]
    r["rev_kit"] = [kit_mw[t] * y["kit_price"][t] * 1000 for t in rng]
    r["rev_eng"] = [y["eng_revenue"][t] + (sw_e * s["eic_followon_mw"] * s["eic_followon_eng"] if YEARS[t] == 2031 else 0)
                    for t in rng]
    r["rev_power"] = [s["plant_kwp"] * s["plant_yield"] * y["plant_factor"][t] * s["plant_ppa_price"] / 1000 for t in rng]
    r["revenue"] = [r["rev_epc"][t] + r["rev_kit"][t] + r["rev_eng"][t] + r["rev_power"][t] for t in rng]

    r["cogs_epc"] = [y["epc_mw"][t] * y["epc_cost"][t] * 1000 for t in rng]
    r["cogs_kit"] = [kit_mw[t] * (y["kit_cost"][t] + y["kit_logistics"][t]) * 1000 for t in rng]
    r["cogs_eng"] = [r["rev_eng"][t] * s["eng_cost_ratio"] for t in rng]
    r["cogs_power"] = [s["plant_opex"] * y["plant_factor"][t] for t in rng]
    r["warranty"] = [s["warranty_rate"] * (r["rev_epc"][t] + r["rev_kit"][t]) for t in rng]
    r["cogs"] = [r["cogs_epc"][t] + r["cogs_kit"][t] + r["cogs_eng"][t] + r["cogs_power"][t] + r["warranty"][t] for t in rng]
    r["gross_profit"] = [r["revenue"][t] - r["cogs"][t] for t in rng]
    r["gross_margin"] = [r["gross_profit"][t] / r["revenue"][t] if r["revenue"][t] else 0 for t in rng]

    fte_ext = [s["sure_ext_fte"] * sw_s if YEARS[t] == 2027 else 0 for t in rng]
    r["fte_total"] = [y["fte"][t] + fte_ext[t] for t in rng]
    r["personnel"] = [r["fte_total"][t] * y["cost_per_fte"][t] for t in rng]
    r["bizdev"] = list(y["bizdev"])
    r["g_and_a"] = list(y["g_and_a"])
    sure_ext_ext = [s["sure_ext_external"] * sw_s if YEARS[t] == 2027 else 0 for t in rng]
    r["rnd_external"] = [y["rnd_external"][t] + sure_ext_ext[t] + sw_e * y["eic_cost"][t] + sw_u * y["eupi_cost"][t]
                         for t in rng]
    r["opex"] = [r["personnel"][t] + r["bizdev"][t] + r["g_and_a"][t] + r["rnd_external"][t] for t in rng]

    sure_grant = [s["sure_ext_grant"] * sw_s if YEARS[t] == 2027 else 0 for t in rng]
    r["grants_eu"] = [sure_grant[t] + sw_e * y["eic_grant"][t] + sw_u * y["eupi_grant"][t] for t in rng]
    # Skattefunn on own R&D staff (excluding EU-funded staff) and own external R&D
    r["skattefunn"] = [s["skattefunn_rate"] * (y["fte"][t] * y["cost_per_fte"][t] * y["rnd_share"][t] + y["rnd_external"][t])
                       for t in rng]
    r["grant_income"] = [r["grants_eu"][t] + r["skattefunn"][t] for t in rng]
    r["dev_cost"] = [r["rnd_external"][t] + y["fte"][t] * y["cost_per_fte"][t] * y["dev_share"][t]
                     + fte_ext[t] * y["cost_per_fte"][t] for t in rng]
    r["dev_capitalised"] = [y["capitalise"][t] * r["dev_cost"][t] for t in rng]
    r["grants_deferred"] = [y["capitalise"][t] * r["grant_income"][t] for t in rng]
    r["ebitda"] = [r["gross_profit"][t] + r["grant_income"][t] - r["grants_deferred"][t] - r["opex"][t]
                   + r["dev_capitalised"][t] for t in rng]

    r["amort_dev"] = [(s["open_dev_asset"] + sum(r["dev_capitalised"][:t + 1])) / s["dev_asset_life"] * y["amort_factor"][t]
                      for t in rng]
    r["depr_tooling"] = [s["open_tooling"] / s["tooling_life"] for t in rng]
    cum = 0.0
    r["depr_moulds"] = []
    for t in rng:
        cum += y["moulds_capex"][t]
        r["depr_moulds"].append(cum / s["tooling_life"])  # valid: horizon <= life
    plant_net = s["plant_capex"] - s["plant_capex_grant"]
    r["depr_plant"] = [plant_net / s["plant_life"] * y["plant_factor"][t] for t in rng]
    r["dna"] = [r["amort_dev"][t] + r["depr_tooling"][t] + r["depr_moulds"][t] + r["depr_plant"][t] for t in rng]
    r["grant_release"] = [(s["open_deferred_grant"] + sum(r["grants_deferred"][:t + 1])) / s["dev_asset_life"]
                          * y["amort_factor"][t] for t in rng]
    r["ebit"] = [r["ebitda"][t] - r["dna"][t] + r["grant_release"][t] for t in rng]

    # loans
    bank, inl = [], []
    b, i_ = s["open_bank_loan"], s["open_in_loan"]
    r["interest"] = []
    r["bank_repay"], r["in_repay"] = [], []
    for t in rng:
        r["interest"].append(s["interest_rate"] * (b + i_))
        rep_b = min(y["bank_repayment"][t], b)
        rep_i = i_  # IN loan repaid in 2027
        b -= rep_b
        i_ -= rep_i
        r["bank_repay"].append(rep_b)
        r["in_repay"].append(rep_i)
        bank.append(b)
        inl.append(i_)
    r["ebt"] = [r["ebit"][t] - r["interest"][t] for t in rng]

    pool = s["open_tax_loss"]
    r["tax"], r["tax_loss_pool"] = [], []
    for t in rng:
        base = r["ebt"][t]
        if base > 0:
            taxable = max(0.0, base - pool)
            pool = max(0.0, pool - base)
        else:
            taxable = 0.0
            pool = pool - base
        r["tax"].append(s["tax_rate"] * taxable)
        r["tax_loss_pool"].append(pool)
    r["net_income"] = [r["ebt"][t] - r["tax"][t] for t in rng]

    # balance sheet stock items
    def prev(line, t, open_value):
        return open_value if t == 0 else r[line][t - 1]

    r["dev_asset"] = [s["open_dev_asset"] + sum(r["dev_capitalised"][:t + 1]) - sum(r["amort_dev"][:t + 1]) for t in rng]
    r["tooling"] = [s["open_tooling"] - r["depr_tooling"][0] * (t + 1) for t in rng]
    cumc, cumd = 0.0, 0.0
    r["moulds"] = []
    for t in rng:
        cumc += y["moulds_capex"][t]
        cumd += r["depr_moulds"][t]
        r["moulds"].append(cumc - cumd)
    cumd = 0.0
    r["plant"] = []
    for t in rng:
        cumd += r["depr_plant"][t]
        r["plant"].append(plant_net - cumd)
    c_spv = 0.0
    r["spv_investment"] = []
    for t in rng:
        c_spv += y["spv_equity"][t]
        r["spv_investment"].append(c_spv)
    r["receivables"] = [s["receivables_ratio"] * r["revenue"][t] for t in rng]
    r["inventory"] = [s["inventory_ratio"] * (r["cogs_epc"][t] + r["cogs_kit"][t]) for t in rng]
    r["skattefunn_recv"] = list(r["skattefunn"])
    r["grants_recv"] = [s["eu_recv_ratio"] * r["grants_eu"][t] for t in rng]
    r["payables"] = [s["payables_ratio"] * (r["cogs"][t] + r["bizdev"][t] + r["g_and_a"][t] + r["rnd_external"][t])
                     for t in rng]
    nxt_epc = [r["rev_epc"][t + 1] if t + 1 < N else 0 for t in rng]
    r["epc_advances"] = [s["epc_advance_ratio"] * nxt_epc[t] for t in rng]
    r["deferred_grant"] = [s["open_deferred_grant"] + sum(r["grants_deferred"][:t + 1]) - sum(r["grant_release"][:t + 1])
                           for t in rng]
    r["other_liab"] = [s["open_other_liab"] for t in rng]
    r["bank_loan"] = bank
    r["in_loan"] = inl
    r["shareholder_loan"] = [0.0 for t in rng]

    # cash flow
    r["d_wc"] = []
    for t in rng:
        d_recv = r["receivables"][t] - prev("receivables", t, 0.0)
        d_inv = r["inventory"][t] - prev("inventory", t, 0.0)
        d_sf = r["skattefunn_recv"][t] - prev("skattefunn_recv", t, s["open_skattefunn_recv"])
        d_gr = r["grants_recv"][t] - prev("grants_recv", t, 0.0)
        d_pay = r["payables"][t] - prev("payables", t, s["open_payables"])
        d_adv = r["epc_advances"][t] - prev("epc_advances", t, 0.0)
        r["d_wc"].append(-d_recv - d_inv - d_sf - d_gr + d_pay + d_adv)
    r["cfo"] = [r["net_income"][t] + r["dna"][t] - r["grant_release"][t] + r["d_wc"][t] for t in rng]
    r["capex"] = [y["moulds_capex"][t] + y["spv_equity"][t] + (s["plant_capex"] if t == 0 else 0) for t in rng]
    r["capex_grants"] = [s["plant_capex_grant"] if t == 0 else 0 for t in rng]
    r["cfi"] = [-r["capex"][t] + r["capex_grants"][t] - r["dev_capitalised"][t] + r["grants_deferred"][t] for t in rng]
    r["equity_raise"] = list(y["equity_raise"])
    r["cff"] = [r["equity_raise"][t] - r["bank_repay"][t] - r["in_repay"][t] for t in rng]
    r["net_cash_flow"] = [r["cfo"][t] + r["cfi"][t] + r["cff"][t] for t in rng]
    c = s["open_cash"]
    r["cash"] = []
    for t in rng:
        c += r["net_cash_flow"][t]
        r["cash"].append(c)
    r["cash_ex_advances"] = [r["cash"][t] - r["epc_advances"][t] for t in rng]

    r["total_assets"] = [r["dev_asset"][t] + r["tooling"][t] + r["moulds"][t] + r["plant"][t] + r["spv_investment"][t]
                         + r["receivables"][t] + r["inventory"][t] + r["skattefunn_recv"][t] + r["grants_recv"][t]
                         + r["cash"][t] for t in rng]
    open_assets = (s["open_dev_asset"] + s["open_tooling"] + s["open_skattefunn_recv"] + s["open_cash"])
    open_liab = (s["open_deferred_grant"] + s["open_bank_loan"] + s["open_in_loan"] + s["open_shareholder_loan"]
                 + s["open_payables"] + s["open_other_liab"])
    r["open_equity"] = [open_assets - open_liab] * N
    conv = s["open_shareholder_loan"]
    eq = open_assets - open_liab
    r["equity"] = []
    for t in rng:
        eq += r["net_income"][t] + r["equity_raise"][t] + (conv if t == 0 else 0)
        r["equity"].append(eq)
    r["total_liabilities"] = [r["deferred_grant"][t] + r["bank_loan"][t] + r["in_loan"][t] + r["shareholder_loan"][t]
                              + r["payables"][t] + r["epc_advances"][t] + r["other_liab"][t] for t in rng]
    r["balance_check"] = [r["total_assets"][t] - r["total_liabilities"][t] - r["equity"][t] for t in rng]
    r["mw_cum"] = []
    m = 0.0
    for t in rng:
        m += y["epc_mw"][t] + kit_mw[t] + (s["plant_kwp"] / 1000 if t == 0 else 0)
        r["mw_cum"].append(m)
    return r


def unit_economics(overrides: dict | None = None) -> dict:
    _, _, u = inputs_for("base", overrides)
    cost = sum(u[k] for k in UE_COST_ITEMS)
    price = cost / (1 - u["ue_epc_margin"])
    capex = price + u["ue_owner_costs"]
    out = {"epc_cost": cost, "epc_price": price, "sunlit_gp_per_w": price - cost, "plant_capex": capex}
    pv_e = sum(u["ue_yield"] * (1 - u["ue_degradation"]) ** (k - 1) / (1 + u["ue_wacc"]) ** k
               for k in range(1, int(u["ue_life"]) + 1))
    pv_o = sum(u["ue_opex"] * (1 + u["ue_opex_escalation"]) ** (k - 1) / (1 + u["ue_wacc"]) ** k
               for k in range(1, int(u["ue_life"]) + 1))
    pv_o += u["ue_inverter"] * 1000 / (1 + u["ue_wacc"]) ** u["ue_inverter_year"]
    out["pv_energy"] = pv_e
    out["pv_opex"] = pv_o
    out["lcoe"] = (capex * 1000 + pv_o) / pv_e
    out["lcoe_supported"] = (capex * 1000 * (1 - u["ue_support"]) + pv_o) / pv_e
    out["host_value"] = u["ue_host_value"]
    # capex at which the unsupported plant matches the host's value
    out["capex_at_host_value"] = (u["ue_host_value"] * pv_e - pv_o) / 1000
    out["support_needed"] = 1 - out["capex_at_host_value"] / capex
    out["lcoe_p2"] = (u["ue_capex_p2"] * 1000 + pv_o) / pv_e
    out["p2_kit_gp_per_w"] = u["ue_kit_price_p2"] - u["ue_kit_cost_p2"]
    out["p2_eng_rev_per_w"] = u["ue_eng_share_p2"] * u["ue_capex_p2"]
    out["p2_gp_per_mw"] = (out["p2_kit_gp_per_w"] + out["p2_eng_rev_per_w"] * (1 - INPUTS["eng_cost_ratio"][0])) * 1000
    out["p2_kit_margin"] = out["p2_kit_gp_per_w"] / u["ue_kit_price_p2"]
    # Kit (incl. panel) margin at today's delivered cost for a range of prices
    kit_now = u["ue_kit"] + u["ue_panels"]
    out["kit_margin_045"] = (0.45 - kit_now) / 0.45
    out["kit_margin_050"] = (0.50 - kit_now) / 0.50
    out["kit_margin_055"] = (0.55 - kit_now) / 0.55
    return out


# Worked example 2: plant with a breakwater at an inland lake with wind waves (Hainer See type)
BW_EXAMPLE = {
    "yield": (960, "kWh/kWp", "PVGIS 5.2 at 51.17 N, 12.45 E (lake south of Leipzig), 2 degree tilt as on the "
                               "platform, 8 % system losses for still water (Eirik, 2026-11-23): 959 kWh/kWp"),
    "sector_deg": (45, "degrees", "Wind waves from south to southeast (Eirik, SUREWAVE fetch estimate)"),
    "host_share": (0.5, "share", "Share of the breakwater cost carried by the site owner's other uses (dual use)"),
    "grid_award": (0.0484, "EUR/kWh", "German solar tender, first segment, 1 July 2025: volume-weighted average award "
                                      "4.84 ct/kWh (Bundesnetzagentur, press release 14 Aug 2025)"),
    "grid_ceiling": (0.068, "EUR/kWh", "Ceiling value of the same tender, 6.80 ct/kWh"),
}


def breakwater_example(sizes_kwp=(1000, 5000)) -> list[dict]:
    """LCOE of a kit-buyer plant (ue_capex_p2) with a light breakwater over the exposed sector, with and
    without half of the breakwater cost carried by other uses; opex and finance as in the worked example."""
    import breakwater_classes as bw     # scripts/breakwater_classes.py
    _, _, u = inputs_for("base")
    yld = BW_EXAMPLE["yield"][0]
    pv_e = sum(yld * (1 - u["ue_degradation"]) ** (k - 1) / (1 + u["ue_wacc"]) ** k
               for k in range(1, int(u["ue_life"]) + 1))
    pv_o = sum(u["ue_opex"] * (1 + u["ue_opex_escalation"]) ** (k - 1) / (1 + u["ue_wacc"]) ** k
               for k in range(1, int(u["ue_life"]) + 1)) + u["ue_inverter"] * 1000 / (1 + u["ue_wacc"]) ** u["ue_inverter_year"]
    rows = []
    for kwp in sizes_kwp:
        full = bw.coverage(kwp, BW_EXAMPLE["sector_deg"][0], "light")["cost_per_kwp"] / 1000
        shared = bw.coverage(kwp, BW_EXAMPLE["sector_deg"][0], "light",
                             host_share=BW_EXAMPLE["host_share"][0])["cost_fpv_per_kwp"] / 1000
        for label, b in (("no breakwater", 0.0), ("breakwater, half carried by other uses", shared),
                         ("breakwater, no other uses", full)):
            capex = u["ue_capex_p2"] + b
            rows.append({"kwp": kwp, "case": label, "breakwater_w": b, "capex_w": capex,
                         "lcoe": (capex * 1000 + pv_o) / pv_e})
    return rows


def breakwater_example_md() -> str:
    rows = ["| Plant | Case | Breakwater (EUR/W) | Plant capex (EUR/W) | LCOE (EUR/kWh) |", "|---|---|---:|---:|---:|"]
    for x in breakwater_example():
        rows.append(f"| {x['kwp'] / 1000:.0f} MWp | {x['case']} | {x['breakwater_w']:.3f} | {x['capex_w']:.2f} | {x['lcoe']:.3f} |")
    return "\n".join(rows)


def kpis(r: dict, scenario: str = "base", overrides: dict | None = None) -> dict:
    """Headline indicators."""
    def first_year(series):
        for t in range(N):
            if all(series[k] >= 0 for k in range(t, N)):
                return YEARS[t]
        return None
    cum = 0.0
    cum_list = []
    for t in range(N):
        cum += r["cfo"][t] + r["cfi"][t]
        cum_list.append(cum)
    return {
        "ebitda_breakeven": first_year(r["ebitda"]),
        "net_breakeven": first_year(r["net_income"]),
        "min_cash": min(r["cash"]),
        "min_cash_year": YEARS[r["cash"].index(min(r["cash"]))],
        "equity_raised": sum(r["equity_raise"]),
        "peak_funding_need": -min(min(cum_list), 0.0),
        "revenue_2031": r["revenue"][-1],
        "cum_mw_2031": r["mw_cum"][-1],
        "breakeven_kit_mw_2031": breakeven_kit_mw(r, scenario=scenario, overrides=overrides),
        "breakeven_kit_mw_net_no_epc": breakeven_kit_mw(r, scenario=scenario, overrides=overrides, exclude_epc=True),
        "breakeven_kit_mw_ebitda_no_epc": breakeven_kit_mw(r, scenario=scenario, overrides=overrides, measure="ebitda",
                                                           exclude_epc=True),
    }


def breakeven_kit_mw(r: dict, t: int = N - 1, scenario: str = "base", overrides: dict | None = None,
                     measure: str = "ebt", exclude_epc: bool = False) -> float:
    """Kit volume (MWp) in year t at which the result before tax is zero,
    other lines unchanged. Gross profit per MWp of kit, net of warranty, plus
    engineering at the phase-2 rate per MWp; the year's engineering revenue
    is replaced by that per-MWp engineering."""
    s, y, _ = inputs_for(scenario, overrides)
    ue = unit_economics(overrides)
    gp_kit = ((y["kit_price"][t] - y["kit_cost"][t] - y["kit_logistics"][t]) * 1000
              - s["warranty_rate"] * y["kit_price"][t] * 1000)
    gp_eng = ue["p2_eng_rev_per_w"] * 1000 * (1 - s["eng_cost_ratio"])
    kit_gp_now = r["kit_mw_total"][t] * gp_kit
    eng_gp_now = r["rev_eng"][t] * (1 - s["eng_cost_ratio"])
    other = r[measure][t] - kit_gp_now - eng_gp_now
    if exclude_epc:
        other -= r["rev_epc"][t] - r["cogs_epc"][t] - s["warranty_rate"] * r["rev_epc"][t]
    return -other / (gp_kit + gp_eng) if (gp_kit + gp_eng) > 0 else math.inf


def funding_gap(r: dict, buffer: float = 200.0) -> float:
    """Extra equity needed to keep year-end cash at or above `buffer`."""
    return max(0.0, buffer - min(r["cash"]))


# ---------------------------------------------------------------------------
# Quarterly cash view 2027-2028 (allocation of the annual flows)
# ---------------------------------------------------------------------------
def quarterly_cash(scenario: str = "base", overrides: dict | None = None) -> list[tuple[str, float, float]]:
    """Allocate the annual net cash flow of 2027 and 2028 to quarters.

    Timing assumptions: round 1 in Q1 2027; Skien havn paid in Q2 2027 and its
    investment grants in Q4 2027; EPC advance received in Q4 of the year before
    delivery; EPC supplier payments 20/40/40/0 % over Q1-Q4 of the delivery
    year and the balance of the EPC price received 0/30/40/30 %; the SPV
    equity in Q2 2028; no grant pre-financing; everything else spread evenly. Quarterly flows add up to the
    annual net cash flow exactly.
    Returns [(label, net flow, cash at quarter end)].
    """
    s, y, _ = inputs_for(scenario, overrides)
    r = compute(scenario, overrides)
    out = []
    cash = s["open_cash"]
    for t in (0, 1):
        q = [0.0, 0.0, 0.0, 0.0]
        specific = 0.0
        eq = r["equity_raise"][t]
        q[0] += eq
        specific += eq
        if t == 0:
            q[1] -= s["plant_capex"]
            q[3] += s["plant_capex_grant"]
            specific += -s["plant_capex"] + s["plant_capex_grant"]
            # no pre-financing assumed for the SuRE extension (conservative)
        adv_in = r["epc_advances"][t]
        q[3] += adv_in
        specific += adv_in
        prev_adv = r["epc_advances"][t - 1] if t > 0 else 0.0
        bal = r["rev_epc"][t] - prev_adv
        for i, f in enumerate((0, 0.3, 0.4, 0.3)):
            q[i] += bal * f
        for i, f in enumerate((0.2, 0.4, 0.4, 0)):
            q[i] -= r["cogs_epc"][t] * f
        specific += bal - r["cogs_epc"][t]
        spv = y["spv_equity"][t]
        q[1] -= spv
        specific -= spv
        rest = r["net_cash_flow"][t] - specific
        for i in range(4):
            q[i] += rest / 4
            cash += q[i]
            out.append((f"Q{i + 1} {YEARS[t]}", q[i], cash))
    return out


# ---------------------------------------------------------------------------
# Indicative outlook 2032-2035 and cap table
# ---------------------------------------------------------------------------
OUTLOOK = {
    "years": [2032, 2033, 2034, 2035],
    "kit_mw": [18, 25, 35, 45],
    "kit_price": [0.44, 0.43, 0.42, 0.41],
    "kit_cost_delivered": [0.225, 0.22, 0.215, 0.21],
    "fixed_cost_growth": 0.08,
}


def outlook(r: dict | None = None) -> list[dict]:
    """Indicative EBITDA beyond the model horizon: kit and engineering only,
    fixed costs growing 8 % a year from 2031 operating costs less grants."""
    r = r or compute("base")
    ue = unit_economics()
    fixed = r["opex"][-1] - r["grant_income"][-1]
    rows = []
    for i, yr in enumerate(OUTLOOK["years"]):
        fixed *= 1 + OUTLOOK["fixed_cost_growth"]
        mw = OUTLOOK["kit_mw"][i]
        rev_kit = mw * OUTLOOK["kit_price"][i] * 1000
        rev_eng = mw * ue["p2_eng_rev_per_w"] * 1000
        gp = (mw * (OUTLOOK["kit_price"][i] - OUTLOOK["kit_cost_delivered"][i]) * 1000
              - INPUTS["warranty_rate"][0] * rev_kit + rev_eng * (1 - INPUTS["eng_cost_ratio"][0]))
        rows.append({"year": yr, "mw": mw, "revenue": rev_kit + rev_eng, "gross_profit": gp,
                     "fixed": fixed, "ebitda": gp - fixed})
    return rows


def leverage_table() -> str:
    """EBITDA at different annual kit volumes, 2031 prices, costs and fixed cost base."""
    r = compute("base")
    _, y, _ = inputs_for("base")
    ue = unit_economics()
    t = N - 1
    gp_kit = (y["kit_price"][t] - y["kit_cost"][t] - y["kit_logistics"][t]
              - INPUTS["warranty_rate"][0] * y["kit_price"][t]) * 1000
    gp_eng = ue["p2_eng_rev_per_w"] * 1000 * (1 - INPUTS["eng_cost_ratio"][0])
    fixed = r["opex"][t] - r["grant_income"][t] - r["rev_power"][t] + r["cogs_power"][t]
    rows = ["| Kit sales a year (MWp) | Revenue (kEUR) | Gross profit (kEUR) | EBITDA (kEUR) | EBITDA margin |",
            "|---:|---:|---:|---:|---:|"]
    for mw in (10, 16, 25, 40):
        rev = mw * (y["kit_price"][t] + ue["p2_eng_rev_per_w"]) * 1000
        gp = mw * (gp_kit + gp_eng)
        e = gp - fixed
        rows.append(f"| {mw} | {fmt(rev)} | {fmt(gp)} | {fmt(e)} | {fmt(e / rev * 100)} % |")
    return "\n".join(rows)


def cap_table() -> list[tuple[str, float, float, float]]:
    """Indicative ownership after each round: (holder, after round 1, after ESOP, after round 2)."""
    s, y, _ = inputs_for("base")
    r1 = y["equity_raise"][0]
    r2 = y["equity_raise"][2]
    pre1, pre2, esop = s["valuation_pre_round1"], s["valuation_pre_round2"], s["esop_share"]
    a1 = {"Existing shareholders": pre1 / (pre1 + r1), "Round 1 investors": r1 / (pre1 + r1)}
    a2 = {k: v * (1 - esop) for k, v in a1.items()}
    a2["Option pool"] = esop
    f2 = pre2 / (pre2 + r2)
    a3 = {k: v * f2 for k, v in a2.items()}
    a3["Round 2 investors"] = r2 / (pre2 + r2)
    rows = []
    for k in ("Existing shareholders", "Round 1 investors", "Option pool", "Round 2 investors"):
        rows.append((k, a1.get(k, 0.0), a2.get(k, 0.0), a3.get(k, 0.0)))
    return rows


# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------
PNL_ROWS = [("Revenue: EPC delivery", "rev_epc"), ("Revenue: kit sales", "rev_kit"),
            ("Revenue: engineering", "rev_eng"), ("Revenue: power sales", "rev_power"),
            ("Total revenue", "revenue"), ("Direct costs", "cogs"), ("Gross profit", "gross_profit"),
            ("Grants and Skattefunn", "grant_income"), ("Grants deferred (capitalised development)", "grants_deferred"),
            ("Personnel", "personnel"),
            ("Business development", "bizdev"), ("General and administration", "g_and_a"),
            ("External R&D", "rnd_external"), ("Development cost capitalised", "dev_capitalised"),
            ("EBITDA", "ebitda"),
            ("Depreciation and amortisation", "dna"), ("Release of deferred grants", "grant_release"),
            ("EBIT", "ebit"), ("Interest", "interest"), ("Tax", "tax"), ("Net result", "net_income")]
CF_ROWS = [("Net result", "net_income"), ("Depreciation and amortisation", "dna"),
           ("Release of deferred grants (non-cash)", "grant_release"), ("Change in working capital", "d_wc"),
           ("Cash flow from operations", "cfo"), ("Investments incl. plant-company equity", "capex"),
           ("Investment grants", "capex_grants"), ("Development capitalised", "dev_capitalised"),
           ("Grants on capitalised development", "grants_deferred"),
           ("Cash flow from investing", "cfi"), ("Equity raised", "equity_raise"),
           ("Loan repayments", "loan_repay"), ("Cash flow from financing", "cff"),
           ("Net cash flow", "net_cash_flow"), ("Cash at year end", "cash"),
           ("Cash at year end less customer advances", "cash_ex_advances")]
BS_ROWS = [("Capitalised development", "dev_asset"), ("Tooling and moulds", "tooling_moulds"),
           ("Own plant and plant-company equity", "plant_spv"),
           ("Receivables, inventory, grants receivable", "current_ex_cash"), ("Cash", "cash"),
           ("Total assets", "total_assets"), ("Equity", "equity"), ("Deferred grants", "deferred_grant"),
           ("Loans", "loans"), ("Payables, customer advances, other", "pay_adv"),
           ("Total equity and liabilities", "tot_eq_liab")]
NEG = {"grants_deferred", "cogs", "personnel", "bizdev", "g_and_a", "rnd_external", "dna", "interest", "tax", "capex", "loan_repay"}
CF_NEG = {"grant_release", "capex", "loan_repay", "dev_capitalised"}


def derived(r: dict) -> dict:
    d = dict(r)
    d["loan_repay"] = [r["bank_repay"][t] + r["in_repay"][t] for t in range(N)]
    d["tooling_moulds"] = [r["tooling"][t] + r["moulds"][t] for t in range(N)]
    d["plant_spv"] = [r["plant"][t] + r["spv_investment"][t] for t in range(N)]
    d["current_ex_cash"] = [r["receivables"][t] + r["inventory"][t] + r["skattefunn_recv"][t] + r["grants_recv"][t]
                            for t in range(N)]
    d["loans"] = [r["bank_loan"][t] + r["in_loan"][t] + r["shareholder_loan"][t] for t in range(N)]
    d["pay_adv"] = [r["payables"][t] + r["epc_advances"][t] + r["other_liab"][t] for t in range(N)]
    d["tot_eq_liab"] = [r["equity"][t] + r["total_liabilities"][t] for t in range(N)]
    return d


def fmt(v: float) -> str:
    s = f"{abs(v):,.0f}".replace(",", " ")
    if round(v) < 0:
        return "−" + s
    return s


def md_table(r: dict, rows, title: str) -> str:
    d = derived(r)
    neg = CF_NEG if rows is CF_ROWS else NEG
    out = [f"| {title} (kEUR) | " + " | ".join(str(y) for y in YEARS) + " |",
           "|---|" + "---:|" * N]
    for label, key in rows:
        sign = -1 if key in neg else 1
        out.append(f"| {label} | " + " | ".join(fmt(sign * v) for v in d[key]) + " |")
    return "\n".join(out)


def _shift(vals, d):
    return [v + d for v in vals]


def _later(vals):
    """Shift a yearly series one year later (the last year drops out of the horizon)."""
    return [0] + list(vals[:-1])


KIT_LATER = _later(YEARLY["kit_mw"][0])
# Breakwater on one side at a mild site (light class, 20 degree sector, straight layout), EUR/W, from
# scripts/breakwater_classes.py (T163): Gunneklevfjorden 3.2 MWp (2028), Storavatnet 1.2 MWp (2030) and 2.0 MWp (2031)
BW_ONE_SIDE = {2028: 0.117, 2030: 0.217, 2031: 0.153}
COMMERCIAL_DOWNSIDE = {
    "epc_mw": _later(YEARLY["epc_mw"][0]),
    "epc_price": _later(YEARLY["epc_price"][0]),
    "epc_cost": _later(YEARLY["epc_cost"][0]),
    "eng_revenue": [0, 150, 10, 170, 198],
    "kit_mw": [v * 0.7 for v in KIT_LATER],
    "kit_cost": [0.25, 0.25, 0.24, 0.24, 0.24],
    "equity_raise": [3500, 0, 0, 2000, 0],
}
EQUITY_LATER = [3500, 0, 0, 2000, 0]

SENSITIVITIES = [
    ("Kit production cost EUR 0.03/W higher", {"kit_cost": _shift(YEARLY["kit_cost"][0], 0.03)}),
    ("Kit price EUR 0.03/W lower", {"kit_price": _shift(YEARLY["kit_price"][0], -0.03)}),
    ("Kit volume 30 % lower in 2030–2031",
     {"kit_mw": [v * (0.7 if i >= 3 else 1) for i, v in enumerate(YEARLY["kit_mw"][0])]}),
    ("Norwegian EPC projects and kit sales one year later (round 2 in 2030)",
     {"epc_mw": _later(YEARLY["epc_mw"][0]), "epc_price": _later(YEARLY["epc_price"][0]),
      "epc_cost": _later(YEARLY["epc_cost"][0]), "eng_revenue": [0, 150, 10, 170, 198], "kit_mw": KIT_LATER,
      "spv_equity": [0, 0, 200, 0, 0], "equity_raise": EQUITY_LATER}),
    ("Gunneklevfjorden not built (no-go at the investment decision)",
     {"epc_mw": [0, 0, 0, 1.2, 2.0], "spv_equity": [0, 0, 0, 0, 0]}),
    ("10 MW-class contract not won",
     {"kit_mw": [0, 0.3, 0.6, 1.0, 9.0], "eng_revenue": [150, 10, 170, 33, 297]}),
    ("Float defect at Gunneklevfjorden: 20 % of the floats resupplied",
     {"epc_cost": [0.64, 0.64 + 0.2 * 0.17, 0.63, 0.61, 0.60]}),
    ("Breakwater (light class, one side) needed at Gunneklevfjorden and Storavatnet, not priced in",
     {"epc_cost": [0.64, 0.64 + BW_ONE_SIDE[2028], 0.63, 0.61 + BW_ONE_SIDE[2030], 0.60 + BW_ONE_SIDE[2031]]}),
    ("Small wavebreakers at Skien havn, about EUR 0.1M, not in the plant cost (estimate; cost to be quoted)",
     {"plant_capex": INPUTS["plant_capex"][0] + 100}),
    ("Cash collateral of EUR 0.3M for EPC guarantees, 2027–2031", {"open_cash": INPUTS["open_cash"][0] - 300}),
    ("EPC direct cost EUR 0.05/W higher (overrun beyond contingency)", {"epc_cost": _shift(YEARLY["epc_cost"][0], 0.05)}),
    ("One more FTE from 2028", {"fte": [v + (1 if i >= 1 else 0) for i, v in enumerate(YEARLY["fte"][0])]}),
    ("Combined commercial downside: one year later (round 2 in 2030), kit volume 30 % lower, kit cost stays at EUR 0.24/W",
     COMMERCIAL_DOWNSIDE),
]


def sensitivity_table() -> str:
    rows = ["| Case | Net result 2027–2031 | EBITDA 2031 | Lowest year-end cash | Extra equity for a €0.2M buffer |",
            "|---|---:|---:|---:|---:|"]

    def line(label, r):
        return (f"| {label} | {fmt(sum(r['net_income']))} | {fmt(r['ebitda'][-1])} | {fmt(min(r['cash']))} | "
                f"{fmt(funding_gap(r))} |")
    rows.append(line("Base case", compute("base")))
    for label, ov in SENSITIVITIES:
        rows.append(line(label, compute("base", ov)))
    return "\n".join(rows)


def scenario_table() -> str:
    rows = ["| Scenario | Revenue 2031 | EBITDA 2031 | Net result 2027–2031 | Lowest cash (year) | Cash end 2031 |",
            "|---|---:|---:|---:|---:|---:|"]
    for sc in SCENARIOS:
        r = compute(sc)
        k = kpis(r, sc)
        rows.append(f"| {SCENARIO_LABELS[sc]} | {fmt(r['revenue'][-1])} | {fmt(r['ebitda'][-1])} | "
                    f"{fmt(sum(r['net_income']))} | {fmt(k['min_cash'])} ({k['min_cash_year']}) | {fmt(r['cash'][-1])} |")
    return "\n".join(rows)


def quarterly_table() -> str:
    q = quarterly_cash()
    rows = ["| Quarter | " + " | ".join(lbl for lbl, _, _ in q) + " |", "|---|" + "---:|" * len(q),
            "| Net cash flow (kEUR) | " + " | ".join(fmt(f) for _, f, _ in q) + " |",
            "| Cash at quarter end (kEUR) | " + " | ".join(fmt(c) for _, _, c in q) + " |"]
    return "\n".join(rows)


def outlook_table() -> str:
    rows = ["| Indicative (kEUR) | " + " | ".join(str(o["year"]) for o in outlook()) + " |",
            "|---|" + "---:|" * len(OUTLOOK["years"])]
    o = outlook()
    for label, key in (("Kit sales, MWp", "mw"), ("Revenue", "revenue"), ("Gross profit", "gross_profit"),
                       ("Operating costs less grants", "fixed"), ("EBITDA", "ebitda")):
        rows.append(f"| {label} | " + " | ".join(fmt(x[key]) for x in o) + " |")
    return "\n".join(rows)


def cap_table_md() -> str:
    rows = ["| Holder | After round 1 (2027) | After option pool | After round 2 (2029) |", "|---|---:|---:|---:|"]
    for k, a, b, c in cap_table():
        rows.append(f"| {k} | {a * 100:.0f} % | {b * 100:.0f} % | {c * 100:.0f} % |")
    return "\n".join(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", action="store_true")
    ap.add_argument("--scenario", default=None)
    a = ap.parse_args()
    names = [a.scenario] if a.scenario else list(SCENARIOS)
    for sc in names:
        r = compute(sc)
        k = kpis(r, sc)
        print(f"## {SCENARIO_LABELS[sc]}\n")
        if a.md:
            print(md_table(r, PNL_ROWS, "Income statement"), "\n")
            print(md_table(r, CF_ROWS, "Cash flow"), "\n")
            print(md_table(r, BS_ROWS, "Balance sheet 31 Dec"), "\n")
        else:
            for key in ("revenue", "gross_profit", "ebitda", "net_income", "cash", "equity"):
                print(f"{key:14s}", " ".join(f"{v:8.0f}" for v in r[key]))
        print("KPIs:", {kk: (round(v) if isinstance(v, float) else v) for kk, v in k.items()})
        print("balance check max abs:", max(abs(x) for x in r["balance_check"]), "\n")
    if a.md:
        print(scenario_table(), "\n")
        print(sensitivity_table(), "\n")
        print(quarterly_table(), "\n")
        print(outlook_table(), "\n")
        print(leverage_table(), "\n")
        print(cap_table_md(), "\n")
        print(breakwater_example_md(), "\n")
    ue = unit_economics()
    print("Unit economics:", {k: round(v, 4) for k, v in ue.items()})


if __name__ == "__main__":
    main()
