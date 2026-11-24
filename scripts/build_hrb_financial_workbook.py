"""Build the Sunlit Sea KER1 financial plan workbook (Horizon Results Booster, T158).

The workbook implements the model in hrb_financial_model.py with Excel
formulas, so the reader can change any input and see the three statements
update. Sheets:

- README        purpose, conventions, scenario switches
- inputs        scalar inputs (scenario switches, opening balance, rates)
- yearly        year-by-year inputs 2027-2031
- model         income statement, cash flow and balance sheet, with a balance check
- unit          worked unit economics for a 3.2 MWp Norwegian plant

Usage:
    python scripts/build_hrb_financial_workbook.py <out.xlsx>        # ~20 s

Pipeline as for the D7.4 workbook: openpyxl assembles the workbook, the
`formulas` library evaluates every formula, and xlsxwriter writes the file
with each result stored next to its formula (Excel recalculates on open).
scripts/test_hrb_financial_model.py compares every model cell with the
independent Python implementation, for all scenarios.

Python packages: openpyxl, xlsxwriter, formulas (numpy).
"""
from __future__ import annotations

import sys
from pathlib import Path

import openpyxl
from openpyxl.styles import Font, PatternFill
from openpyxl.utils import get_column_letter as col

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hrb_financial_model as m  # noqa: E402
from build_d74_workbook import evaluate, write_with_results  # noqa: E402

YC = [col(4 + t) for t in range(m.N)]   # model year columns D..H
OPEN = "C"                              # model opening column (31.12.2026)
YYC = [col(3 + t) for t in range(m.N)]  # yearly-sheet year columns C..G
INPUT_FILL = PatternFill("solid", fgColor="FFF2CC")
HEAD = Font(bold=True)

# Model lines in display order: (key, label, kind, formula builder, opening builder)
# kind: 'h' heading, 'f' flow, 's' stock. Builders receive a context object.


class Ctx:
    def __init__(self):
        self.s_row: dict[str, int] = {}
        self.y_row: dict[str, int] = {}
        self.m_row: dict[str, int] = {}
        self.u_row: dict[str, int] = {}

    def S(self, name):
        return f"inputs!$B${self.s_row[name]}"

    def Y(self, name, t):
        return f"yearly!{YYC[t]}{self.y_row[name]}"

    def M(self, key, t):
        return f"{YC[t]}{self.m_row[key]}"

    def P(self, key, t):
        return f"{OPEN if t == 0 else YC[t - 1]}{self.m_row[key]}"

    def U(self, name):
        return f"unit!$B${self.u_row[name]}"


def lines():
    """Return list of (key, label, kind, f(c, t) -> formula, open(c) -> formula|None)."""
    L = []

    def h(label):
        L.append((None, label, "h", None, None))

    def f(key, label, fn, op=None, kind="f"):
        L.append((key, label, kind, fn, op))

    def sumf(keys, sign=None):
        def fn(c, t):
            parts = []
            for i, k in enumerate(keys):
                sg = "-" if sign and sign[i] < 0 else "+"
                parts.append(f"{sg}{c.M(k, t)}")
            s = "".join(parts)
            return "=" + (s[1:] if s.startswith("+") else s)
        return fn

    h("Volumes")
    f("kit_mw_total", "Kit sales, MWp",
      lambda c, t: f"={c.Y('kit_mw', t)}" + (f"+{c.S('sw_eupi')}*{c.S('eupi_kit_mw')}" if m.YEARS[t] == 2029 else "")
      + (f"+{c.S('sw_eic')}*{c.S('eic_followon_mw')}" if m.YEARS[t] == 2031 else ""))
    f("mw_cum", "MWp delivered, cumulative",
      lambda c, t: f"={c.P('mw_cum', t)}+{c.Y('epc_mw', t)}+{c.M('kit_mw_total', t)}"
      + (f"+{c.S('plant_kwp')}/1000" if t == 0 else ""), lambda c: "=0", "s")
    f("fte_total", "Staff, FTE",
      lambda c, t: f"={c.Y('fte', t)}" + (f"+{c.S('sure_ext_fte')}*{c.S('sw_sure_ext')}" if t == 0 else ""))

    h("Income statement")
    f("rev_epc", "Revenue: EPC delivery", lambda c, t: f"={c.Y('epc_mw', t)}*{c.Y('epc_price', t)}*1000")
    f("rev_kit", "Revenue: kit sales", lambda c, t: f"={c.M('kit_mw_total', t)}*{c.Y('kit_price', t)}*1000")
    f("rev_eng", "Revenue: engineering", lambda c, t: f"={c.Y('eng_revenue', t)}"
      + (f"+{c.S('sw_eic')}*{c.S('eic_followon_mw')}*{c.S('eic_followon_eng')}" if m.YEARS[t] == 2031 else ""))
    f("rev_power", "Revenue: power sales",
      lambda c, t: f"={c.S('plant_kwp')}*{c.S('plant_yield')}*{c.Y('plant_factor', t)}*{c.S('plant_ppa_price')}/1000")
    f("revenue", "Total revenue", sumf(["rev_epc", "rev_kit", "rev_eng", "rev_power"]))
    f("cogs_epc", "Direct cost: EPC", lambda c, t: f"={c.Y('epc_mw', t)}*{c.Y('epc_cost', t)}*1000")
    f("cogs_kit", "Direct cost: kits",
      lambda c, t: f"={c.M('kit_mw_total', t)}*({c.Y('kit_cost', t)}+{c.Y('kit_logistics', t)})*1000")
    f("cogs_eng", "Direct cost: engineering", lambda c, t: f"={c.M('rev_eng', t)}*{c.S('eng_cost_ratio')}")
    f("cogs_power", "Direct cost: own plant", lambda c, t: f"={c.S('plant_opex')}*{c.Y('plant_factor', t)}")
    f("warranty", "Warranty provision",
      lambda c, t: f"={c.S('warranty_rate')}*({c.M('rev_epc', t)}+{c.M('rev_kit', t)})")
    f("cogs", "Direct costs", sumf(["cogs_epc", "cogs_kit", "cogs_eng", "cogs_power", "warranty"]))
    f("gross_profit", "Gross profit", sumf(["revenue", "cogs"], [1, -1]))
    f("gross_margin", "Gross margin",
      lambda c, t: f"=IF({c.M('revenue', t)}=0,0,{c.M('gross_profit', t)}/{c.M('revenue', t)})")
    f("grants_eu", "EU grants",
      lambda c, t: "=" + (f"{c.S('sure_ext_grant')}*{c.S('sw_sure_ext')}+" if t == 0 else "")
      + f"{c.S('sw_eic')}*{c.Y('eic_grant', t)}+{c.S('sw_eupi')}*{c.Y('eupi_grant', t)}")
    f("skattefunn", "Skattefunn",
      lambda c, t: f"={c.S('skattefunn_rate')}*({c.Y('fte', t)}*{c.Y('cost_per_fte', t)}*{c.Y('rnd_share', t)}"
      f"+{c.Y('rnd_external', t)})")
    f("grant_income", "Grants and Skattefunn", sumf(["grants_eu", "skattefunn"]))
    f("personnel", "Personnel", lambda c, t: f"={c.M('fte_total', t)}*{c.Y('cost_per_fte', t)}")
    f("bizdev", "Business development", lambda c, t: f"={c.Y('bizdev', t)}")
    f("g_and_a", "General and administration", lambda c, t: f"={c.Y('g_and_a', t)}")
    f("rnd_external", "External R&D",
      lambda c, t: f"={c.Y('rnd_external', t)}"
      + (f"+{c.S('sure_ext_external')}*{c.S('sw_sure_ext')}" if t == 0 else "")
      + f"+{c.S('sw_eic')}*{c.Y('eic_cost', t)}+{c.S('sw_eupi')}*{c.Y('eupi_cost', t)}")
    f("opex", "Operating costs", sumf(["personnel", "bizdev", "g_and_a", "rnd_external"]))
    f("dev_cost", "Development cost (external R&D and R&D staff)",
      lambda c, t: f"={c.M('rnd_external', t)}+{c.Y('fte', t)}*{c.Y('cost_per_fte', t)}*{c.Y('dev_share', t)}"
      + (f"+{c.S('sure_ext_fte')}*{c.S('sw_sure_ext')}*{c.Y('cost_per_fte', t)}" if t == 0 else ""))
    f("dev_capitalised", "Development cost capitalised", lambda c, t: f"={c.Y('capitalise', t)}*{c.M('dev_cost', t)}")
    f("grants_deferred", "Grants deferred (capitalised development)",
      lambda c, t: f"={c.Y('capitalise', t)}*{c.M('grant_income', t)}")
    f("ebitda", "EBITDA", sumf(["gross_profit", "grant_income", "grants_deferred", "opex", "dev_capitalised"],
                               [1, 1, -1, -1, 1]))

    def prior_sum(key, c, t):
        return f"+SUM({YC[0]}{c.m_row[key]}:{YC[t]}{c.m_row[key]})"

    f("amort_dev", "Amortisation of capitalised development",
      lambda c, t: f"=({c.S('open_dev_asset')}{prior_sum('dev_capitalised', c, t)})/{c.S('dev_asset_life')}"
      f"*{c.Y('amort_factor', t)}")
    f("depr_tooling", "Depreciation of existing tooling",
      lambda c, t: f"={c.S('open_tooling')}/{c.S('tooling_life')}")
    f("depr_moulds", "Depreciation of new moulds",
      lambda c, t: f"=SUM(yearly!$C${c.y_row['moulds_capex']}:{YYC[t]}{c.y_row['moulds_capex']})/{c.S('tooling_life')}")
    f("depr_plant", "Depreciation of own plant",
      lambda c, t: f"=({c.S('plant_capex')}-{c.S('plant_capex_grant')})/{c.S('plant_life')}*{c.Y('plant_factor', t)}")
    f("dna", "Depreciation and amortisation", sumf(["amort_dev", "depr_tooling", "depr_moulds", "depr_plant"]))
    f("grant_release", "Release of deferred grants",
      lambda c, t: f"=({c.S('open_deferred_grant')}{prior_sum('grants_deferred', c, t)})/{c.S('dev_asset_life')}"
      f"*{c.Y('amort_factor', t)}")
    f("ebit", "EBIT", sumf(["ebitda", "dna", "grant_release"], [1, -1, 1]))
    f("interest", "Interest", lambda c, t: f"={c.S('interest_rate')}*({c.P('bank_loan', t)}+{c.P('in_loan', t)})")
    f("ebt", "Result before tax", sumf(["ebit", "interest"], [1, -1]))
    f("tax", "Tax",
      lambda c, t: f"={c.S('tax_rate')}*IF({c.M('ebt', t)}>0,MAX(0,{c.M('ebt', t)}-{c.P('tax_loss_pool', t)}),0)")
    f("net_income", "Net result", sumf(["ebt", "tax"], [1, -1]))
    f("tax_loss_pool", "Tax loss carried forward",
      lambda c, t: f"=IF({c.M('ebt', t)}>0,MAX(0,{c.P('tax_loss_pool', t)}-{c.M('ebt', t)}),"
      f"{c.P('tax_loss_pool', t)}-{c.M('ebt', t)})", lambda c: f"={c.S('open_tax_loss')}", "s")

    h("Cash flow")
    f("d_wc", "Change in working capital",
      lambda c, t: f"=-({c.M('receivables', t)}-{c.P('receivables', t)})-({c.M('inventory', t)}-{c.P('inventory', t)})"
      f"-({c.M('skattefunn_recv', t)}-{c.P('skattefunn_recv', t)})-({c.M('grants_recv', t)}-{c.P('grants_recv', t)})"
      f"+({c.M('payables', t)}-{c.P('payables', t)})"
      f"+({c.M('epc_advances', t)}-{c.P('epc_advances', t)})")
    f("cfo", "Cash flow from operations", sumf(["net_income", "dna", "grant_release", "d_wc"], [1, 1, -1, 1]))
    f("capex", "Investments incl. plant-company equity",
      lambda c, t: f"={c.Y('moulds_capex', t)}+{c.Y('spv_equity', t)}" + (f"+{c.S('plant_capex')}" if t == 0 else ""))
    f("capex_grants", "Investment grants", lambda c, t: f"={c.S('plant_capex_grant')}" if t == 0 else "=0")
    f("cfi", "Cash flow from investing", sumf(["capex", "capex_grants", "dev_capitalised", "grants_deferred"],
                                              [-1, 1, -1, 1]))
    f("equity_raise", "Equity raised", lambda c, t: f"={c.Y('equity_raise', t)}")
    f("bank_repay", "Repayment, bank loan", lambda c, t: f"=MIN({c.Y('bank_repayment', t)},{c.P('bank_loan', t)})")
    f("in_repay", "Repayment, Innovasjon Norge loan", lambda c, t: f"={c.P('in_loan', t)}")
    f("cff", "Cash flow from financing", sumf(["equity_raise", "bank_repay", "in_repay"], [1, -1, -1]))
    f("net_cash_flow", "Net cash flow", sumf(["cfo", "cfi", "cff"]))
    f("shareholder_conversion", "Shareholder loan converted to equity (non-cash)",
      lambda c, t: f"={c.P('shareholder_loan', t)}" if t == 0 else "=0")

    h("Balance sheet 31 December")
    f("dev_asset", "Capitalised development",
      lambda c, t: f"={c.P('dev_asset', t)}+{c.M('dev_capitalised', t)}-{c.M('amort_dev', t)}",
      lambda c: f"={c.S('open_dev_asset')}", "s")
    f("tooling", "Existing tooling", lambda c, t: f"={c.P('tooling', t)}-{c.M('depr_tooling', t)}",
      lambda c: f"={c.S('open_tooling')}", "s")
    f("moulds", "New moulds", lambda c, t: f"={c.P('moulds', t)}+{c.Y('moulds_capex', t)}-{c.M('depr_moulds', t)}",
      lambda c: "=0", "s")
    f("plant", "Own plant",
      lambda c, t: f"={c.P('plant', t)}" + (f"+{c.S('plant_capex')}-{c.S('plant_capex_grant')}" if t == 0 else "")
      + f"-{c.M('depr_plant', t)}", lambda c: "=0", "s")
    f("spv_investment", "Equity in plant companies", lambda c, t: f"={c.P('spv_investment', t)}+{c.Y('spv_equity', t)}",
      lambda c: "=0", "s")
    f("grants_recv", "EU grants receivable", lambda c, t: f"={c.S('eu_recv_ratio')}*{c.M('grants_eu', t)}",
      lambda c: "=0", "s")
    f("receivables", "Trade receivables", lambda c, t: f"={c.S('receivables_ratio')}*{c.M('revenue', t)}",
      lambda c: "=0", "s")
    f("inventory", "Inventory", lambda c, t: f"={c.S('inventory_ratio')}*({c.M('cogs_epc', t)}+{c.M('cogs_kit', t)})",
      lambda c: "=0", "s")
    f("skattefunn_recv", "Skattefunn receivable", lambda c, t: f"={c.M('skattefunn', t)}",
      lambda c: f"={c.S('open_skattefunn_recv')}", "s")
    f("cash", "Cash", lambda c, t: f"={c.P('cash', t)}+{c.M('net_cash_flow', t)}",
      lambda c: f"={c.S('open_cash')}", "s")
    ta = ["dev_asset", "tooling", "moulds", "plant", "spv_investment", "receivables", "inventory", "skattefunn_recv",
          "grants_recv", "cash"]
    f("total_assets", "Total assets", sumf(ta), lambda c: "=" + "+".join(f"{OPEN}{c.m_row[k]}" for k in ta), "s")
    f("deferred_grant", "Deferred grants",
      lambda c, t: f"={c.P('deferred_grant', t)}+{c.M('grants_deferred', t)}-{c.M('grant_release', t)}",
      lambda c: f"={c.S('open_deferred_grant')}", "s")
    f("bank_loan", "Bank loan", lambda c, t: f"={c.P('bank_loan', t)}-{c.M('bank_repay', t)}",
      lambda c: f"={c.S('open_bank_loan')}", "s")
    f("in_loan", "Innovasjon Norge loan", lambda c, t: f"={c.P('in_loan', t)}-{c.M('in_repay', t)}",
      lambda c: f"={c.S('open_in_loan')}", "s")
    f("shareholder_loan", "Shareholder loan",
      lambda c, t: f"={c.P('shareholder_loan', t)}-{c.M('shareholder_conversion', t)}",
      lambda c: f"={c.S('open_shareholder_loan')}", "s")
    f("payables", "Trade payables",
      lambda c, t: f"={c.S('payables_ratio')}*({c.M('cogs', t)}+{c.M('bizdev', t)}+{c.M('g_and_a', t)}"
      f"+{c.M('rnd_external', t)})", lambda c: f"={c.S('open_payables')}", "s")
    f("epc_advances", "Customer advances",
      lambda c, t: (f"={c.S('epc_advance_ratio')}*{YC[t + 1]}{c.m_row['rev_epc']}" if t + 1 < m.N else "=0"),
      lambda c: "=0", "s")
    f("other_liab", "Other short-term liabilities", lambda c, t: f"={c.S('open_other_liab')}",
      lambda c: f"={c.S('open_other_liab')}", "s")
    tl = ["deferred_grant", "bank_loan", "in_loan", "shareholder_loan", "payables", "epc_advances", "other_liab"]
    f("total_liabilities", "Total liabilities", sumf(tl), lambda c: "=" + "+".join(f"{OPEN}{c.m_row[k]}" for k in tl), "s")
    f("equity", "Equity",
      lambda c, t: f"={c.P('equity', t)}+{c.M('net_income', t)}+{c.M('equity_raise', t)}"
      f"+{c.M('shareholder_conversion', t)}",
      lambda c: f"={OPEN}{c.m_row['total_assets']}-{OPEN}{c.m_row['total_liabilities']}", "s")
    f("cash_ex_advances", "Cash less customer advances", sumf(["cash", "epc_advances"], [1, -1]))
    f("balance_check", "Check: assets − liabilities − equity (must be 0)",
      sumf(["total_assets", "total_liabilities", "equity"], [1, -1, -1]),
      lambda c: f"={OPEN}{c.m_row['total_assets']}-{OPEN}{c.m_row['total_liabilities']}-{OPEN}{c.m_row['equity']}", "s")
    return L


README = [
    "Sunlit Sea KER1 financial plan model (Horizon Results Booster)",
    "",
    "Confidential. Contains Sunlit Sea's cost, price and pipeline assumptions.",
    "All amounts in EUR thousand (kEUR) unless the unit column says otherwise. Annual periods 2027-2031, nominal.",
    "Yellow cells are inputs. Change the scenario switches on the inputs sheet (1 = on, 0 = off):",
    "  sw_sure_ext  SuRE extension approved;  sw_eic  EIC Transition SUREWAVE awarded;  sw_eupi  EUPI-PV Gotland awarded.",
    "Scenarios in the plan: base (1,0,0), EIC (1,1,0), EU upside (1,1,1), downside (0,0,0). The file is saved in base.",
    "",
    "Conventions",
    "- Revenue on EPC contracts is recognised in the year of delivery; customers pay an advance the year before.",
    "- Generation 2 development before first use at Skien havn (1 July 2027) is capitalised with its grants deferred",
    "  (gross method, NRS 4), as in the policy adopted in the 2025 accounts; later development is expensed.",
    "  All capitalised development is amortised over 5 years from first use, and the deferred grants released alongside.",
    "- Investment support for the own plant is deducted from its cost (net method).",
    "- EU grants: a share is paid the year after the cost (grants receivable).",
    "- Skattefunn is recognised in the year of the cost and paid the following year.",
    "- Tax: 22 % on positive results after the tax loss carried forward; no deferred tax asset is recognised.",
    "- Mould depreciation uses cumulative investment / 5 years, which is exact while the horizon is 5 years or less.",
    "- The model sheet ends with a balance check that must be 0 in every column.",
    "",
    "Built by scripts/build_hrb_financial_workbook.py from scripts/hrb_financial_model.py;",
    "tested by scripts/test_hrb_financial_model.py.",
]


def build() -> tuple[openpyxl.Workbook, Ctx]:
    c = Ctx()
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "README"
    for i, line in enumerate(README, 1):
        ws.cell(i, 1, line)
    ws["A1"].font = HEAD
    ws.column_dimensions["A"].width = 110

    # inputs sheet
    wi = wb.create_sheet("inputs")
    wi.append(["Name", "Value", "Unit", "Note"])
    for cell in wi[1]:
        cell.font = HEAD
    for name, (v, unit, note) in m.INPUTS.items():
        wi.append([name, v, unit, note])
        c.s_row[name] = wi.max_row
        wi.cell(wi.max_row, 2).fill = INPUT_FILL
    for k, w in zip("ABCD", (24, 12, 12, 100)):
        wi.column_dimensions[k].width = w
    wi.freeze_panes = "B2"

    # yearly sheet
    wy = wb.create_sheet("yearly")
    wy.append(["Name", "Unit"] + m.YEARS + ["Note"])
    for cell in wy[1]:
        cell.font = HEAD
    for name, (vals, unit, note) in m.YEARLY.items():
        wy.append([name, unit] + list(vals) + [note])
        c.y_row[name] = wy.max_row
        for t in range(m.N):
            wy.cell(wy.max_row, 3 + t).fill = INPUT_FILL
    for k, w in zip("ABCDEFGH", (18, 10, 9, 9, 9, 9, 9, 100)):
        wy.column_dimensions[k].width = w
    wy.freeze_panes = "C2"

    # model sheet: first pass assigns rows
    L = lines()
    wm = wb.create_sheet("model")
    wm.append(["Line", "Key", "31.12.2026"] + m.YEARS)
    for cell in wm[1]:
        cell.font = HEAD
    r = 2
    for key, label, kind, fn, op in L:
        if key:
            c.m_row[key] = r
        r += 1
    r = 2
    for key, label, kind, fn, op in L:
        wm.cell(r, 1, label)
        if kind == "h":
            wm.cell(r, 1).font = HEAD
        else:
            wm.cell(r, 2, key)
            if op is not None:
                wm.cell(r, 3, op(c))
                wm.cell(r, 3).number_format = "#,##0;-#,##0"
            for t in range(m.N):
                wm.cell(r, 4 + t, fn(c, t))
                wm.cell(r, 4 + t).number_format = "0.0%" if key == "gross_margin" else (
                    "#,##0.0" if key in ("kit_mw_total", "mw_cum", "fte_total") else "#,##0;-#,##0")
        r += 1
    for k, w in zip("ABCDEFGH", (48, 22, 12, 10, 10, 10, 10, 10)):
        wm.column_dimensions[k].width = w
    wm.freeze_panes = "D2"

    # unit economics sheet
    wu = wb.create_sheet("unit")
    wu.append(["Name", "Value", "Unit", "Note"])
    for cell in wu[1]:
        cell.font = HEAD
    for name, (v, unit, note) in m.UNIT.items():
        wu.append([name, v, unit, note])
        c.u_row[name] = wu.max_row
        wu.cell(wu.max_row, 2).fill = INPUT_FILL
    wu.append([])
    wu.append(["Results"])
    wu.cell(wu.max_row, 1).font = HEAD
    U = c.U

    def res(name, formula, unit, note=""):
        wu.append([name, formula, unit, note])
        c.u_row[name] = wu.max_row
        wu.cell(wu.max_row, 2).number_format = "0.0000"

    res("epc_cost", "=" + "+".join(U(k) for k in m.UE_COST_ITEMS), "EUR/W", "EPC direct cost incl. contingency")
    res("epc_price", f"={U('epc_cost')}/(1-{U('ue_epc_margin')})", "EUR/W", "EPC price at the phase-1 margin")
    res("sunlit_gp_per_w", f"={U('epc_price')}-{U('epc_cost')}", "EUR/W", "Sunlit Sea gross profit per watt, phase 1")
    res("plant_capex", f"={U('epc_price')}+{U('ue_owner_costs')}", "EUR/W", "Plant company's total investment")
    # discounting table
    start = wu.max_row + 3
    wu.cell(start - 1, 1, "Year")
    wu.cell(start - 1, 2, "Energy, kWh/kWp")
    wu.cell(start - 1, 3, "Discount factor")
    wu.cell(start - 1, 4, "Discounted O&M, EUR/kWp")
    for k in range(1, int(m.UNIT["ue_life"][0]) + 1):
        rr = start + k - 1
        wu.cell(rr, 1, k)
        wu.cell(rr, 2, f"={U('ue_yield')}*(1-{U('ue_degradation')})^(A{rr}-1)")
        wu.cell(rr, 3, f"=1/(1+{U('ue_wacc')})^A{rr}")
        wu.cell(rr, 4, f"={U('ue_opex')}*(1+{U('ue_opex_escalation')})^(A{rr}-1)*C{rr}")
    end = start + int(m.UNIT["ue_life"][0]) - 1
    res_rows_at = wu.max_row  # results continue after the table
    # place remaining results below the table
    wu_row = end + 2

    def res2(name, formula, unit, note=""):
        nonlocal wu_row
        wu.cell(wu_row, 1, name)
        wu.cell(wu_row, 2, formula)
        wu.cell(wu_row, 3, unit)
        wu.cell(wu_row, 4, note)
        wu.cell(wu_row, 2).number_format = "0.0000"
        c.u_row[name] = wu_row
        wu_row += 1

    res2("pv_energy", f"=SUMPRODUCT(B{start}:B{end},C{start}:C{end})", "kWh/kWp", "Discounted lifetime energy")
    res2("pv_opex", f"=SUM(D{start}:D{end})+{U('ue_inverter')}*1000/(1+{U('ue_wacc')})^{U('ue_inverter_year')}",
         "EUR/kWp", "Discounted lifetime O&M and inverter replacement")
    res2("lcoe", f"=({U('plant_capex')}*1000+{U('pv_opex')})/{U('pv_energy')}", "EUR/kWh", "Without investment support")
    res2("lcoe_supported", f"=({U('plant_capex')}*1000*(1-{U('ue_support')})+{U('pv_opex')})/{U('pv_energy')}",
         "EUR/kWh", "With investment support")
    res2("host_value", f"={U('ue_host_value')}", "EUR/kWh", "Host's value of behind-the-meter power")
    res2("capex_at_host_value", f"=({U('ue_host_value')}*{U('pv_energy')}-{U('pv_opex')})/1000", "EUR/W",
         "Plant cost at which the unsupported plant matches the host's value")
    res2("support_needed", f"=1-{U('capex_at_host_value')}/{U('plant_capex')}", "share",
         "Investment support needed to match the host's value")
    res2("lcoe_p2", f"=({U('ue_capex_p2')}*1000+{U('pv_opex')})/{U('pv_energy')}", "EUR/kWh",
         "Phase 2 plant for a kit buyer, without support")
    res2("p2_kit_gp_per_w", f"={U('ue_kit_price_p2')}-{U('ue_kit_cost_p2')}", "EUR/W", "Phase 2 kit gross profit")
    res2("p2_eng_rev_per_w", f"={U('ue_eng_share_p2')}*{U('ue_capex_p2')}", "EUR/W", "Phase 2 engineering revenue")
    res2("p2_gp_per_mw", f"=({U('p2_kit_gp_per_w')}+{U('p2_eng_rev_per_w')}*(1-inputs!$B${c.s_row['eng_cost_ratio']}))*1000",
         "kEUR/MWp", "Phase 2 gross profit per MWp sold")
    res2("p2_kit_margin", f"={U('p2_kit_gp_per_w')}/{U('ue_kit_price_p2')}", "share", "Phase 2 kit gross margin")
    for price in ("045", "050", "055"):
        pr = int(price) / 100
        res2(f"kit_margin_{price}", f"=({pr}-{U('ue_kit')}-{U('ue_panels')})/{pr}", "share",
             f"Kit margin incl. panel at EUR {pr:.2f}/W and today's cost")
    for k, w in zip("ABCD", (20, 14, 14, 100)):
        wu.column_dimensions[k].width = w
    del res_rows_at
    return wb, c


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    out = Path(sys.argv[1])
    wb, _ = build()
    tmp = out.with_suffix(".tmp.xlsx")
    wb.save(tmp)
    results, _ = evaluate(tmp)
    tmp.unlink()
    write_with_results(wb, results, out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
