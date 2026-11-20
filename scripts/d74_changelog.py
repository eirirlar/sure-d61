"""Print the v2 -> v3 result tables for the D7.4 cost model changelog (Markdown).

Usage:
    python scripts/d74_changelog.py <v2.xlsx> [<v3_recalculated.xlsx>]

Table 1: headline results per base case, v2 (as in the v2 workbook) vs v3.
Table 2: effect of each correction on the 10 MW cases, measured leave-one-out
         (full v3 minus v3 without that correction), so each number is the
         correction's effect with all other corrections applied.
If a recalculated v3 workbook is given, v3 values are read from it and
checked against the Python model.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import d74_cost_model as m  # noqa: E402

FIX_ORDER = ["unused_cost_inputs", "reinstall_in_lcoe", "discounting", "replacement_rings", "end_of_life",
             "freight_key", "pontoon_count_bug", "variant_columns", "irr_undiscounted_full_life"]


def fmt_irr(x):
    return "–" if x in (None, "-") else f"{x * 100:.1f} %"


def fmt_pb(x):
    return "–" if x in (None, "-") else str(x)


def main(v2: str, v3: str | None = None) -> None:
    inp = m.load_inputs(v2)
    cached = m.read_cached_outputs(v2)
    xl = m.read_cached_outputs(v3) if v3 else None
    print("| Case | LCOE v2 | LCOE v3 | NPV v2 (M€) | NPV v3 (M€) | IRR v2 | IRR v3 | Payback v2 | Payback v3 |")
    print("|---|---|---|---|---|---|---|---|---|")
    for case in m.LOCATIONS:
        a = cached[case]
        b = m.v3_outputs(inp, case)
        if xl:
            for k in ("lcoe", "npv"):
                assert abs(xl[case][k] - b[k]) <= 1e-7 * max(1, abs(b[k])), (case, k)
        print(f"| {case} | {a['lcoe']:.4f} | {b['lcoe']:.4f} | {a['npv'] / 1e6:.2f} | {b['npv'] / 1e6:.2f} | "
              f"{fmt_irr(a['irr'])} | {fmt_irr(b['irr'])} | {fmt_pb(a['payback_period'])} | {fmt_pb(b['payback_period'])} |")
    print()
    print("| Correction | " + " | ".join(f"{c}: ΔLCOE (€/kWh) / ΔNPV (M€)" for c in ("m_10", "b_10", "n_10")) + " |")
    print("|---|---|---|---|")
    full = {c: m.v3_outputs(inp, c) for c in ("m_10", "b_10", "n_10")}
    for fx in FIX_ORDER:
        cells = []
        for c in ("m_10", "b_10", "n_10"):
            o = m.v3_outputs(inp, c, fixes=set(m.V3_FIXES) - {fx})
            cells.append(f"{full[c]['lcoe'] - o['lcoe']:+.4f} / {(full[c]['npv'] - o['npv']) / 1e6:+.2f}")
        print(f"| {m.V3_FIXES[fx]} | " + " | ".join(cells) + " |")


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    main(*sys.argv[1:])
