"""Floating breakwater classes for nearshore sites and a coverage formula (T162, T163).

Defines light, medium and heavy floating breakwater classes for mild, medium
and rough nearshore wave conditions, with indicative installed costs per metre
built up from the SUREWAVE D7.4 (version 2.0, cost model v3) reference ring
and the D3.2 breakwater design, plus stated assumptions for the cost items
D7.4 does not contain (fabrication, couplings and fenders, transport, supplier
margin). Then turns a plant (capacity) and a site (exposure sector, wave
class) into a breakwater length, number of units and cost.

All costs in EUR, indicative, to be checked with Clement Germany.

Usage:
    PYTHONIOENCODING=utf-8 python scripts/breakwater_classes.py --md            # tables for the note
    python scripts/breakwater_classes.py --site 3200 60 medium --host-share 0.5 # one site: kWp, exposure deg, class

Physics:
- Wave transmission by the Macagno formula (rigid box, linear waves), as used
  in D3.2 and D5.1. For the SUREWAVE unit it gives Ct = 0.34 at 3 s, in line
  with D3.2 (critical wave periods of 1-3 s reduced to Ct <= 0.4).
- Design sea states are fetch-limited JONSWAP spectra (SPM 1984 growth
  curves with the adjusted wind U_A = 0.71 U10^1.23; gamma 3.3).
- Two sizing criteria, both on the spectrum transmitted behind the breakwater:
  (1) significant height of the short waves (periods of 3 s and less, the
      critical band for the PV array in D3.2; hinge-load RAOs in D5.1 peak at
      1.2-2 s) at most H_SHORT_ALLOW;
  (2) total transmitted significant height at most the platform's limit for
      the longer waves it rides (sheltered-site platform, or the exposed-site
      platform for rough sites).

Python packages: standard library only.
"""
from __future__ import annotations

import argparse
import math

G = 9.81
RHO = 1025.0

# ---------------------------------------------------------------------------
# Reference: SUREWAVE heavy unit and the D7.4 10 MW ring (Mediterranean case m_10)
# ---------------------------------------------------------------------------
REF = {
    "unit_length_m": 20.0,          # D3.2
    "unit_width_m": 5.0,            # D3.2
    "unit_draft_m": 2.03,           # D3.2
    "unit_height_m": 2.5,           # D3.2
    "unit_mass_t": 123.4,           # D3.2
    "unit_roll_period_s": 3.75,     # D5.1 Section 5 (CFD forced motion): natural roll period of the unit
    "unit_heave_period_s": 3.57,    # D5.1 Section 5: natural heave period of the unit
    "ring_units": 56,               # D3.2 / D5.1 / D7.4 pontoons sheet (10 MW)
    "ring_material_eur": 1_221_594, # D7.4 v2.0 Section 3.2.1, conventional design O0: raw material only (t x EUR/t)
    "pontoon_install_eur": 535_000 + 42_000 + 221_000,  # D7.4 v3 in_loc m_10: equipment, fuel, personnel
    "pontoons_installed": 91,       # D7.4 v3 (56 breakwater + 35 bridge pontoons of similar mass)
    "anchors_eur": 58.41 * 2000,    # D7.4 v3 in_loc m_10 anchor weight (t, total) x EUR/t
    "chains_eur": 30.61 * 3000,     # D7.4 v3 in_loc m_10 chain weight (t, total) x EUR/t
    "anchor_count": 26,             # D7.4 v3 in_loc m_10
    "couplings_fenders_eur": 128_940 + 12_760,  # D7.4 v3 pontoons sheet, 10 MW: structural steel 214.9 t x 600 + rubber 31.9 t x 400 (all 91 pontoons)
    "design_hs_m": 2.0,             # D5.1 Table 6: largest line loads, Mediterranean, Hs 2.0 m, Tp 3.6 s
    "water_depth_m": 38.0,          # D5.1: Mediterranean site depth
    "ring_standoff_m": 30.0,        # D7.4 v3 in_loc m_10: array to PVC pipe 15 m + pipe to breakwater 15 m
}

ASSUMPTIONS = {
    "power_density_kwp_per_m2": 0.150,  # proposal: 150 W/m2 of plant area (D7.4 10 MW ring layout gives about 145 W/m2)
    "standoff_m": 15.0,                 # nearshore: array to breakwater incl. transition element (D7.4 2 MW cases: 7.5 + 7.5 m) [CONFIRM]
    "fabrication_factor": 1.0,          # casting labour, formwork and moulds, yard, curing, QC, as a multiple of the D7.4 material cost (range 0.5-1.5) [CONFIRM]
    "couplings_fabrication_factor": 2.0,  # D7.4 prices steel and rubber per tonne; machining, galvanising and fitting as a multiple [CONFIRM]
    "anchoring_reading": "totals",      # "totals": D7.4 v3 as modelled; "per_anchor": D7.4 glossary (weight per anchor / per chain) [CONFIRM with Clement]
    "transport_per_unit_eur": 4_000,    # yard to site, heavy unit; scaled for lighter units [CONFIRM]
    "fixed_share": 0.20,                # share of per-unit cost items that does not scale with mass [CONFIRM]
    "anchoring_floor": 0.35,            # minimum anchoring per metre, as a share of the reference [CONFIRM]
    "open_arc_anchoring_factor": 1.5,   # an open arc lacks the ring's self-restraint: more lines per metre [CONFIRM]
    "end_anchor_sets": 2,               # extra anchor sets at each open end [CONFIRM]
    "supplier_factor": 1.25,            # supplier's design, project management and margin [CONFIRM]
    "mobilisation_eur": 40_000,         # crane, tug and crew mobilisation per site [CONFIRM]
    "h_short_allow_m": 0.45,            # short waves (<= 3 s) at the array: 0.5 m limit with 10 % margin [CONFIRM]
    "h_total_allow_sheltered_m": 0.60,  # total transmitted Hs, sheltered-site platform [CONFIRM]
    "h_total_allow_exposed_m": 0.80,    # total transmitted Hs, exposed-site platform (EIC Transition) [CONFIRM]
    "t_short_s": 3.0,                   # critical band upper period (D3.2)
    "design_wind_u10_ms": 22.0,         # design wind at 10 m for fetch-limited waves [CONFIRM]
    "spreading_deg": 10.0,              # directional spreading added on each side of the exposure sector [CONFIRM]
    "end_extension_min_m": 10.0,        # minimum extension beyond the geometric shadow line at each end [CONFIRM]
    "min_width_m": 2.5,                 # practical minimum width for stability and access [CONFIRM]
}

WAVE_CLASSES = {
    "mild": {"hs_m": 0.65, "depth_m": 8.0, "platform": "sheltered"},
    "medium": {"hs_m": 1.0, "depth_m": 12.0, "platform": "sheltered"},
    "rough": {"hs_m": 1.3, "depth_m": 20.0, "platform": "exposed"},
}

# Classes as found by search_section() (rounded), with freeboard set per class
BREAKWATER_CLASSES = {
    "light": {"width_m": 2.5, "draft_m": 1.0, "height_m": 1.5, "wave_class": "mild", "anchoring": "weak"},
    "medium": {"width_m": 4.0, "draft_m": 1.5, "height_m": 2.2, "wave_class": "medium", "anchoring": "medium"},
    "heavy": {"width_m": 5.0, "draft_m": 2.03, "height_m": 2.5, "wave_class": "rough", "anchoring": "strong"},
}


# ---------------------------------------------------------------------------
# Wave physics
# ---------------------------------------------------------------------------
def wavenumber(t: float, h: float) -> float:
    k = 4 * math.pi ** 2 / (G * t * t)
    for _ in range(200):
        k = 4 * math.pi ** 2 / (G * t * t) / math.tanh(k * h)
    return k


def wavelength(t: float, h: float) -> float:
    return 2 * math.pi / wavenumber(t, h)


def macagno_ct(t: float, width: float, draft: float, h: float) -> float:
    k = wavenumber(t, h)
    # sinh(kh) / cosh(kh - kd) in an overflow-safe form
    ratio = math.exp(k * draft) * (1 - math.exp(-2 * k * h)) / (1 + math.exp(-2 * k * h + 2 * k * draft))
    x = k * width * ratio / 2
    return 1 / math.sqrt(1 + x * x)


def adjusted_wind(u10: float) -> float:
    return 0.71 * u10 ** 1.23


def fetch_for_hs(hs: float, ua: float) -> float:
    """Fetch (m) giving Hs at adjusted wind ua (SPM 1984: g Hs/ua^2 = 1.6e-3 (g F/ua^2)^0.5)."""
    return (hs * G / ua ** 2 / 1.6e-3) ** 2 * ua ** 2 / G


def tp_for_fetch(f: float, ua: float) -> float:
    """Peak period (s) for fetch f (SPM 1984: g Tp/ua = 0.286 (g F/ua^2)^(1/3))."""
    return 0.286 * ua / G * (G * f / ua ** 2) ** (1 / 3)


def jonswap(f: float, tp: float, gamma: float = 3.3) -> float:
    fp = 1 / tp
    sig = 0.07 if f <= fp else 0.09
    return f ** -5 * math.exp(-1.25 * (fp / f) ** 4) * gamma ** math.exp(-((f - fp) ** 2) / (2 * sig * sig * fp * fp))


def spectral_heights(hs: float, tp: float, width: float | None, draft: float | None, h: float) -> dict:
    """Incident and transmitted Hs, total and for periods <= t_short (no breakwater if width is None)."""
    df = 0.0025
    fs = [0.04 + i * df for i in range(1800)]
    s = [jonswap(f, tp) for f in fs]
    scale = hs ** 2 / 16 / (sum(s) * df)
    f_short = 1 / ASSUMPTIONS["t_short_s"]
    m_short = m_tr = m_tr_short = 0.0
    for f, v in zip(fs, s):
        e = scale * v * df
        ct2 = 1.0 if width is None else macagno_ct(1 / f, width, draft, h) ** 2
        m_tr += e * ct2
        if f >= f_short:
            m_short += e
            m_tr_short += e * ct2
    return {"hs_short_incident": 4 * math.sqrt(m_short), "hs_transmitted": 4 * math.sqrt(m_tr),
            "hs_short_transmitted": 4 * math.sqrt(m_tr_short)}


def wave_class_table() -> list[dict]:
    ua = adjusted_wind(ASSUMPTIONS["design_wind_u10_ms"])
    rows = []
    for name, w in WAVE_CLASSES.items():
        f = fetch_for_hs(w["hs_m"], ua)
        tp = tp_for_fetch(f, ua)
        sh = spectral_heights(w["hs_m"], tp, None, None, w["depth_m"])
        rows.append({"wave_class": name, "hs_m": w["hs_m"], "tp_s": tp, "fetch_km": f / 1000, "depth_m": w["depth_m"],
                     "platform": w["platform"], "hs_short_m": sh["hs_short_incident"]})
    return rows


def total_allow(platform: str) -> float:
    return ASSUMPTIONS["h_total_allow_exposed_m" if platform == "exposed" else "h_total_allow_sheltered_m"]


def meets(width: float, draft: float, w: dict) -> tuple[bool, dict]:
    sh = spectral_heights(w["hs_m"], w["tp_s"], width, draft, w["depth_m"])
    ok = (sh["hs_short_transmitted"] <= ASSUMPTIONS["h_short_allow_m"] + 1e-9
          and sh["hs_transmitted"] <= total_allow(w["platform"]) + 1e-9)
    return ok, sh


def search_section(wave_class: str) -> dict | None:
    """Lightest cross-section (width x draft) meeting both criteria, width >= minimum, width/draft 2-3."""
    w = {r["wave_class"]: r for r in wave_class_table()}[wave_class]
    best = None
    for w10 in range(int(ASSUMPTIONS["min_width_m"] * 10), 81, 5):
        for d10 in range(5, 31):
            width, draft = w10 / 10, d10 / 10
            if not 2.0 <= width / draft <= 3.0:
                continue
            ok, sh = meets(width, draft, w)
            if ok and (best is None or width * draft < best["section_m2"]):
                best = {"width_m": width, "draft_m": draft, "section_m2": width * draft, **sh}
    return best


def natural_periods(width: float) -> tuple[float, float]:
    """Natural roll and heave periods (s), Froude-scaled from the SUREWAVE unit (D5.1) by width."""
    f = math.sqrt(width / REF["unit_width_m"])
    return REF["unit_roll_period_s"] * f, REF["unit_heave_period_s"] * f


# ---------------------------------------------------------------------------
# Breakwater classes: performance and cost per metre
# ---------------------------------------------------------------------------
def ref_per_metre() -> dict:
    length = REF["ring_units"] * REF["unit_length_m"]
    mult = REF["anchor_count"] if ASSUMPTIONS["anchoring_reading"] == "per_anchor" else 1
    return {
        "ring_length_m": length,
        "material_per_m": REF["ring_material_eur"] / length,
        "install_per_m": REF["pontoon_install_eur"] / REF["pontoons_installed"] / REF["unit_length_m"],
        "anchors_per_m": REF["anchors_eur"] * mult / length,
        "chains_per_m": REF["chains_eur"] * mult / length,
        "anchor_set_eur": (REF["anchors_eur"] + REF["chains_eur"]) * mult / REF["anchor_count"],
        "couplings_per_unit": REF["couplings_fenders_eur"] / REF["pontoons_installed"],
        "mass_per_m_t": REF["unit_mass_t"] / REF["unit_length_m"],
    }


def _scaled(x: float, mass_ratio: float) -> float:
    a = ASSUMPTIONS["fixed_share"]
    return x * (a + (1 - a) * mass_ratio)


def class_table() -> list[dict]:
    r = ref_per_metre()
    a = ASSUMPTIONS
    ref_section = REF["unit_width_m"] * REF["unit_draft_m"]
    waves = {w["wave_class"]: w for w in wave_class_table()}
    rows = []
    for name, b in BREAKWATER_CLASSES.items():
        w = waves[b["wave_class"]]
        mass_ratio = b["width_m"] * b["draft_m"] / ref_section
        ok, sh = meets(b["width_m"], b["draft_m"], w)
        material = r["material_per_m"] * mass_ratio
        fabrication = material * a["fabrication_factor"]
        couplings = _scaled(r["couplings_per_unit"] * a["couplings_fabrication_factor"], mass_ratio) / REF["unit_length_m"]
        transport = _scaled(a["transport_per_unit_eur"], mass_ratio) / REF["unit_length_m"]
        install = _scaled(r["install_per_m"], mass_ratio)
        load_ratio = max(a["anchoring_floor"], (w["hs_m"] / REF["design_hs_m"]) ** 2)
        depth_ratio = w["depth_m"] / REF["water_depth_m"]
        anchoring_ring = r["anchors_per_m"] * load_ratio + r["chains_per_m"] * load_ratio * depth_ratio
        anchoring = anchoring_ring * a["open_arc_anchoring_factor"]
        production = material + fabrication + couplings + transport + install + anchoring
        hmax = 1.86 * w["hs_m"]
        rows.append({
            "class": name, "wave_class": b["wave_class"], "anchoring_class": b["anchoring"], "platform": w["platform"],
            "width_m": b["width_m"], "draft_m": b["draft_m"], "height_m": b["height_m"],
            "freeboard_m": b["height_m"] - b["draft_m"], "crest_hmax_m": 0.5 * hmax,
            "unit_mass_t": REF["unit_mass_t"] * mass_ratio, "mass_ratio": mass_ratio,
            "roll_period_s": natural_periods(b["width_m"])[0], "heave_period_s": natural_periods(b["width_m"])[1],
            "meets": ok, **sh, "tp_s": w["tp_s"], "hs_m": w["hs_m"], "depth_m": w["depth_m"],
            "material_per_m": material, "fabrication_per_m": fabrication, "couplings_per_m": couplings,
            "transport_per_m": transport, "install_per_m": install, "anchoring_per_m": anchoring,
            "load_ratio": load_ratio, "production_per_m": production, "anchoring_ring_per_m": anchoring_ring,
            "installed_per_m": production * a["supplier_factor"],
        })
    return rows


def reference_open_sea_per_metre() -> float:
    """Installed cost per metre of the D7.4 ring built the same way (heavy unit, Mediterranean loads, 38 m, closed ring)."""
    r = ref_per_metre()
    a = ASSUMPTIONS
    material = r["material_per_m"]
    prod = (material * (1 + a["fabrication_factor"]) + r["couplings_per_unit"] * a["couplings_fabrication_factor"] / REF["unit_length_m"]
            + a["transport_per_unit_eur"] / REF["unit_length_m"] + r["install_per_m"] + r["anchors_per_m"] + r["chains_per_m"])
    return prod * a["supplier_factor"]


def d74_like_for_like_per_kwp() -> dict:
    """D7.4 breakwater cost for 10 MW on its own basis: material + 56/91 of pontoon installation + anchoring."""
    share = REF["ring_units"] / REF["pontoons_installed"]
    raw = REF["ring_material_eur"] + (REF["pontoon_install_eur"] + REF["couplings_fenders_eur"]) * share \
        + REF["anchors_eur"] + REF["chains_eur"]
    built = reference_open_sea_per_metre() * REF["ring_units"] * REF["unit_length_m"]
    return {"d74_basis_per_kwp": raw / 10_000, "with_supplier_per_kwp": raw * ASSUMPTIONS["supplier_factor"] / 10_000,
            "built_up_per_kwp": built / 10_000}


# ---------------------------------------------------------------------------
# Coverage formula (T163)
# ---------------------------------------------------------------------------
def plant_radius(kwp: float) -> float:
    """Plant taken as a circle of the area set by the power density."""
    return math.sqrt(kwp / ASSUMPTIONS["power_density_kwp_per_m2"] / math.pi)


def end_extension(cls: dict, r_dist: float) -> float:
    """Extension beyond the geometric shadow line at each end (m).

    Semi-infinite breakwater diffraction: Kd is about 0.5 at the shadow line
    and falls as about 0.225/u inside the shadow, with u = y sqrt(2/(lambda r))
    (straight-edge approximation). The target Kd is the allowable short-wave
    height over the incident short-wave height; the far side of the array is
    at distance r_dist from the end.
    """
    # Kd is about 0.5 at the shadow line; for targets at or above 0.5 the minimum extension governs.
    target = ASSUMPTIONS["h_short_allow_m"] / max(cls["hs_short_incident"], 1e-6)
    lam = wavelength(min(cls["tp_s"], ASSUMPTIONS["t_short_s"]), cls["depth_m"])
    if target >= 0.5:
        y = 0.0
    else:
        u = 0.225 / target
        y = u * math.sqrt(lam * r_dist / 2)
    return max(y, ASSUMPTIONS["end_extension_min_m"])


def coverage(kwp: float, exposure_deg: float, bw_class: str, host_share: float = 0.0, standoff: float | None = None) -> dict:
    """Breakwater length and cost to shield a plant over an exposure sector.

    Two layouts, the shorter is used:
    - arc of radius R = r + s around the plant centre: span = sector + spreading + 2 asin(r/R), plus the end extensions;
    - straight breakwater tangent to the stand-off circle, facing the sector's centre: length = 2 (r + s) tan(half
      sector incl. spreading) + 2 r sec(half sector), plus the end extensions; used only for sectors up to 120 degrees.
    A sector of 360 degrees is a closed ring without ends. host_share is the share of the breakwater cost carried by
    another use (berths, platforms).
    """
    a = ASSUMPTIONS
    s = a["standoff_m"] if standoff is None else standoff
    r = plant_radius(kwp)
    big_r = r + s
    cls = {c["class"]: c for c in class_table()}[bw_class]
    if exposure_deg >= 360:
        length, layout, n_ends = 2 * math.pi * big_r, "ring", 0
    else:
        theta = math.radians(min(360.0, exposure_deg + 2 * a["spreading_deg"]))
        e = end_extension(cls, s + 2 * r)
        arc = big_r * (theta + 2 * math.asin(r / big_r)) + 2 * e
        if arc >= 2 * math.pi * big_r:
            length, layout, n_ends = 2 * math.pi * big_r, "ring", 0
        else:
            length, layout, n_ends = arc, "arc", 2
            if exposure_deg <= 120:
                straight = 2 * (r + s) * math.tan(theta / 2) + 2 * r / math.cos(theta / 2) + 2 * e
                if straight < arc:
                    length, layout = straight, "straight"
    units = math.ceil(length / REF["unit_length_m"])
    rp = ref_per_metre()
    end_sets = n_ends * a["end_anchor_sets"] * rp["anchor_set_eur"] * cls["load_ratio"] * a["supplier_factor"]
    per_m = cls["installed_per_m"]
    if layout == "ring":
        per_m -= (cls["anchoring_per_m"] - cls["anchoring_ring_per_m"]) * a["supplier_factor"]
    cost = units * REF["unit_length_m"] * per_m + end_sets + a["mobilisation_eur"]
    return {"kwp": kwp, "exposure_deg": exposure_deg, "class": bw_class, "layout": layout, "plant_radius_m": r,
            "length_m": length, "units": units, "unit_mass_t": cls["unit_mass_t"], "cost_eur": cost,
            "cost_per_kwp": cost / kwp, "host_share": host_share, "cost_fpv_eur": cost * (1 - host_share),
            "cost_fpv_per_kwp": cost * (1 - host_share) / kwp}


STANDARD_SITES = [
    ("A Mild: one exposed side", 3200, 20, "light", 0.0),
    ("B Medium: two exposed sides", 3200, 60, "medium", 0.0),
    ("B' Medium, half paid by dual use", 3200, 60, "medium", 0.5),
    ("C Rough nearshore: three sides", 3200, 180, "heavy", 0.0),
]


def ring_check() -> dict:
    """Calibrate the geometry against the D7.4 10 MW ring (56 units, 1,120 m) with the D7.4 stand-off of 30 m."""
    length = 2 * math.pi * (plant_radius(10_000) + REF["ring_standoff_m"])
    d74 = ref_per_metre()["ring_length_m"]
    return {"model_length_m": length, "d74_length_m": d74, "ratio": length / d74}


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
def fmt(v: float, nd: int = 0) -> str:
    s = f"{abs(v):,.{nd}f}".replace(",", " ")
    return ("−" + s) if round(v, nd) < 0 else s


def md() -> str:
    a = ASSUMPTIONS
    out = ["| Wave class | Design Hs (m) | Peak period (s) | Fetch at U10 22 m/s (km) | Typical depth (m) | Short-wave Hs, ≤ 3 s (m) | Platform |",
           "|---|---:|---:|---:|---:|---:|---|"]
    for w in wave_class_table():
        out.append(f"| {w['wave_class']} | {w['hs_m']:.2f} | {w['tp_s']:.1f} | {w['fetch_km']:.1f} | {w['depth_m']:.0f} | "
                   f"{w['hs_short_m']:.2f} | {w['platform']} |")
    out += ["", "| Wave class | Lightest section meeting both criteria (W × d, m) | Short-wave Hs at array (m) | Total Hs at array (m) |",
            "|---|---|---:|---:|"]
    for wc in WAVE_CLASSES:
        sres = search_section(wc)
        out.append(f"| {wc} | {sres['width_m']:.1f} × {sres['draft_m']:.1f} | {sres['hs_short_transmitted']:.2f} | "
                   f"{sres['hs_transmitted']:.2f} |" if sres else f"| {wc} | none found | – | – |")
    out += ["", "| Breakwater class | For waves | Anchoring | Width × draft × height (m) | Mass per 20 m unit (t) | Short-wave Hs at array (m) | Total Hs at array (m) | Limit total (m) | Freeboard / crest of max wave (m) | Natural roll / heave period (s) |",
            "|---|---|---|---|---:|---:|---:|---:|---|---|"]
    for c in class_table():
        out.append(f"| {c['class']} | {c['wave_class']} | {c['anchoring_class']} | {c['width_m']:.1f} × {c['draft_m']:.2f} × {c['height_m']:.1f} | "
                   f"{fmt(c['unit_mass_t'])} | {c['hs_short_transmitted']:.2f} | {c['hs_transmitted']:.2f} | {total_allow(c['platform']):.2f} | "
                   f"{c['freeboard_m']:.2f} / {c['crest_hmax_m']:.2f} | {c['roll_period_s']:.1f} / {c['heave_period_s']:.1f} |")
    out += ["", "| Breakwater class | Material | Fabrication | Couplings, fenders | Transport | Installation | Anchoring | Production | Installed incl. supplier |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for c in class_table():
        out.append(f"| {c['class']} | {fmt(c['material_per_m'])} | {fmt(c['fabrication_per_m'])} | {fmt(c['couplings_per_m'])} | "
                   f"{fmt(c['transport_per_m'])} | {fmt(c['install_per_m'])} | {fmt(c['anchoring_per_m'])} | {fmt(c['production_per_m'])} | "
                   f"{fmt(c['installed_per_m'])} |")
    out.append(f"| Open-sea reference (D7.4 ring built the same way, closed ring) | | | | | | | | {fmt(reference_open_sea_per_metre())} |")
    out += ["", "| Standard site | Plant (kWp) | Exposure | Class | Layout | Breakwater length (m) | Units | Cost (k€) | €/kWp | €/kWp to the solar plant |",
            "|---|---:|---:|---|---|---:|---:|---:|---:|---:|"]
    for label, kwp, exp, cls, share in STANDARD_SITES:
        r = coverage(kwp, exp, cls, share)
        out.append(f"| {label} | {fmt(kwp)} | {exp:.0f}° | {cls} | {r['layout']} | {fmt(r['length_m'])} | {r['units']} | "
                   f"{fmt(r['cost_eur'] / 1000)} | {fmt(r['cost_per_kwp'])} | {fmt(r['cost_fpv_per_kwp'])} |")
    out += ["", "| Plant size (kWp) | A mild, light, 20° | B medium, medium, 60° | C rough, heavy, 180° | Full ring, heavy |",
            "|---:|---:|---:|---:|---:|"]
    for kwp in (350, 1000, 3200, 10000):
        vals = [coverage(kwp, 20, "light"), coverage(kwp, 60, "medium"), coverage(kwp, 180, "heavy"), coverage(kwp, 360, "heavy")]
        out.append(f"| {fmt(kwp)} | " + " | ".join(fmt(v["cost_per_kwp"]) for v in vals) + " |")
    rc = ring_check()
    lf = d74_like_for_like_per_kwp()
    saved = ASSUMPTIONS["anchoring_reading"]
    ASSUMPTIONS["anchoring_reading"] = "per_anchor"
    hi = {c["class"]: c for c in class_table()}
    hi_sites = [coverage(kwp, exp, cls, share) for _, kwp, exp, cls, share in STANDARD_SITES]
    hi_ref = reference_open_sea_per_metre()
    ASSUMPTIONS["anchoring_reading"] = saved
    out += ["", "Anchoring if D7.4's weights are per anchor and per chain (its glossary) rather than totals (its model):", "",
            "| Breakwater class | Anchoring €/m | Installed €/m incl. supplier |", "|---|---:|---:|"]
    for name in ("light", "medium", "heavy"):
        out.append(f"| {name} | {fmt(hi[name]['anchoring_per_m'])} | {fmt(hi[name]['installed_per_m'])} |")
    out.append(f"| Open-sea reference | | {fmt(hi_ref)} |")
    out += ["", "| Standard site | €/kWp, anchoring per anchor |", "|---|---:|"]
    for (label, *_), r in zip(STANDARD_SITES, hi_sites):
        out.append(f"| {label} | {fmt(r['cost_fpv_per_kwp'])} |")
    ring = coverage(10000, 360, "heavy", standoff=REF["ring_standoff_m"])
    out += ["", f"Ring check: geometry {rc['model_length_m']:.0f} m against D7.4 {rc['d74_length_m']:.0f} m (ratio {rc['ratio']:.2f}). "
            f"D7.4 like-for-like breakwater cost (material, 56/91 of pontoon installation, anchoring): €{lf['d74_basis_per_kwp']:.0f}/kWp, "
            f"€{lf['with_supplier_per_kwp']:.0f}/kWp with the supplier factor; built up as here (open-sea loads, closed ring): "
            f"€{lf['built_up_per_kwp']:.0f}/kWp. Nearshore heavy full ring at 10 MWp with the D7.4 stand-off: €{ring['cost_per_kwp']:.0f}/kWp."]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", action="store_true")
    ap.add_argument("--site", nargs=3, metavar=("KWP", "EXPOSURE_DEG", "CLASS"))
    ap.add_argument("--host-share", type=float, default=0.0)
    a = ap.parse_args()
    if a.site:
        r = coverage(float(a.site[0]), float(a.site[1]), a.site[2], a.host_share)
        for k, v in r.items():
            print(f"{k:18s} {v:.2f}" if isinstance(v, float) else f"{k:18s} {v}")
    else:
        print(md())


if __name__ == "__main__":
    main()
