"""Preliminary annual AC yield estimator for a floating-PV site.

Calls PVGIS 5.2 (EU JRC). Returns a Markdown report structured like the
Sunlit Sea *Simuleringsrapport* (Blekinge/Kronoberg mulighetsstudie, 2026-09):
KPI headline row, panelkonfigurasjon-og-areal, solinnstraling-og-POA,
tapsbudsjett (PR decomposition), energiproduksjon, scenario sensitivity
(Low/Base/High) and antakelser-og-begrensninger. Renders via
``scripts/md_to_sunlit_report.py`` through the YAML frontmatter
``sunlit_template: report``.

Minimum input: ``--lat``, ``--lng``, and either ``--kwp`` (direct capacity)
or ``--area`` (available water surface in m2, panel count derived from the
panel-configuration defaults).

Not a bankable P50/P75/P90 yield; preliminary only. Methodology:
``docs/energy_yield_methodology.md``.
"""
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "requests",
#   "pyyaml",
#   "matplotlib",
# ]
# ///
from __future__ import annotations

import argparse
import datetime as _dt
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path

import requests
import yaml
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

PVGIS_PVCALC = "https://re.jrc.ec.europa.eu/api/v5_2/PVcalc"
PVGIS_MRCALC = "https://re.jrc.ec.europa.eu/api/v5_2/MRcalc"

MONTH_LABELS = {
    "no": ["Jan", "Feb", "Mar", "Apr", "Mai", "Jun",
            "Jul", "Aug", "Sep", "Okt", "Nov", "Des"],
    "en": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
}

# Default loss decomposition in percent. Sum = 10 %, PR = 90 %, matches the
# reference Simuleringsrapport (Blekinge/Kronoberg 2026-09-17). Each item is
# a user-adjustable input, not a fixed value.
DEFAULT_LOSSES = {
    "temperature_coefficient": 3.0,
    "inverter": 2.0,
    "dc_cable": 1.0,
    "ac_cable": 0.5,
    "mismatch": 0.5,
    "soiling": 0.5,
    "lid": 0.5,
    "availability": 1.0,
    "transformer": 1.0,
}

LOSS_LABELS = {
    "no": {
        "temperature_coefficient": "Temperaturkoeffisient",
        "inverter": "Invertervirkningsgrad",
        "dc_cable": "DC-kabeltap",
        "ac_cable": "AC-kabeltap",
        "mismatch": "Mismatch",
        "soiling": "Soiling / smuss",
        "lid": "LID (lysindusert degradering)",
        "availability": "Tilgjengelighet / nedetid",
        "transformer": "Transformatortap",
    },
    "en": {
        "temperature_coefficient": "Temperature coefficient",
        "inverter": "Inverter efficiency",
        "dc_cable": "DC cable loss",
        "ac_cable": "AC cable loss",
        "mismatch": "Mismatch",
        "soiling": "Soiling",
        "lid": "LID (light-induced degradation)",
        "availability": "Availability / downtime",
        "transformer": "Transformer loss",
    },
}

# Localised strings for the report body.
L10N = {
    "no": {
        "title": "Flytende solkraftverk — Mulighetsstudie",
        "tech": "Sunlit Sea-teknologi",
        "prep": "Utarbeidet",
        "prep_by": "Utarbeidet av",
        "status": "Status",
        "status_val": "Innledende estimat",
        "irr_src": "Irradiasjonsdata",
        "data_tmy": "PVGIS 5.2, typisk meteorologisk år",
        "data_year": "PVGIS 5.2, år",
        "headline": "Nøkkeltall",
        "kpi_count": "Antall paneler",
        "kpi_count_unit": "stk",
        "kpi_capacity": "Installert effekt",
        "kpi_poa": "POA-innstråling (tiltet plan)",
        "kpi_pr": "Performance Ratio",
        "kpi_production": "Estimert produksjon",
        "kpi_specific": "Spesifikk yield",
        "sec1": "1 Panelkonfigurasjon og areal",
        "sec1_intro_area": (
            "Sunlit Sea-teknologien monterer panelene med {tilt}° helning mot "
            "sør på pontongkonstruksjoner. Mellomrom på {gap} mm i begge akser "
            "gir drenering og pontongfeste."
        ),
        "sec1_intro_kwp": (
            "Installert kapasitet er oppgitt direkte som {kwp} kWp DC. "
            "Panelkonfigurasjon og arealberegning er ikke utført (ingen "
            "`--area` oppgitt)."
        ),
        "param": "Parameter",
        "value": "Verdi",
        "unit": "Enhet",
        "note": "Merknad",
        "panel_dim": "Panelmål (B × H)",
        "panel_dim_note": "Oppgitt paneldimensjon",
        "gap": "Mellomrom (gap)",
        "gap_note": "Begge akser",
        "slot_dim": "Slot-areal per panel (B × H)",
        "slot_note": "Panel + gap",
        "slot_area": "Slot-areal per panel",
        "panel_wp": "Paneleffekt (nominell)",
        "panel_wp_note": "Per panel, STC",
        "power_density": "Effekttetthet",
        "packing": "Dekkgrad (packing factor)",
        "packing_note": "Panelareal ÷ slot-areal",
        "available_area": "Tilgjengelig vannflate",
        "given": "Oppgitt",
        "panel_count": "Antall paneler",
        "installed_dc": "Installert DC-effekt",
        "assumed_panel_wp": "Antatt paneleffekt",
        "default": "Default",
        "panel_count_derived": "Antall paneler (avledet)",
        "direct": "Oppgitt direkte",
        "sec2": "2 Solinnstråling og POA-analyse",
        "sec2_intro": (
            "Med {tilt}° helning mot sør fanger panelene en noe større andel "
            "innstråling enn et horisontalt plan. POA er hentet fra PVGIS 5.2 "
            "(Perez-modell)."
        ),
        "ghi": "GHI (horisontal referanse)",
        "ghi_note": "PVGIS MRcalc, 2005–2020",
        "poa_at": "POA ved {tilt}° (tiltet plan)",
        "poa_note": "PVGIS PVcalc",
        "tilt_label": "Helningsvinkel",
        "tilt_towards_south": "Mot sør",
        "tilt_towards_az": "Mot azimut {az}°",
        "gain": "Gain vs horisontalt plan",
        "gain_note": "POA ÷ GHI – 1",
        "sec3": "3 Tapsbudsjett — PR-dekomponering",
        "loss_component": "Tapskomponent",
        "loss_pct": "Tap (%)",
        "sum_loss": "Sum tap",
        "pr_result": "Performance Ratio (PR)",
        "pr_formula": "100 − Σ",
        "pvgis_control": (
            "PVGIS kontrollverdi (crystSi-modell med intern temperatur- og "
            "spektralmodell, uten eksterne tap): {pvgis_mwh} MWh/år, implisitt "
            "PR {pvgis_pr:.1f} %. Vår komponentsum er sannsynligvis {verdict} "
            "sammenlignet med PVGIS-modellen."
        ),
        "verdict_optimistic": "optimistisk",
        "verdict_conservative": "konservativ",
        "verdict_consistent": "konsistent",
        "sec4": "4 Energiproduksjon",
        "beregning": "Beregning",
        "p_peak": "Installert DC-effekt (P_peak)",
        "poa_h": "POA-innstråling (H)",
        "pr_dec": "Performance Ratio (PR)",
        "pr_dec_note": "100 − Σ tap (fra tapsbudsjett)",
        "e_production": "Estimert produksjon (E)",
        "e_note": "P × H × PR, pluss {fpv} % FPV-kjøleeffekt",
        "specific": "Spesifikk yield",
        "specific_note": "E ÷ P",
        "op_hours": "Ekvivalente driftstimer",
        "op_hours_note": "= spesifikk yield numerisk",
        "cf_label": "Kapasitetsfaktor",
        "cf_note": "E ÷ (P × 8 760 h)",
        "formula_box": "`E = {kwp} kWp x {poa} kWh/m2/ar x {pr:.2f} x {bonus:.2f} = {e} MWh/ar`",
        "sec5": "5 Sensitivitetsanalyse",
        "scenario": "Scenario",
        "ghi_dev": "GHI-avvik",
        "pr_dev": "PR-avvik",
        "production_mwh": "Produksjon (MWh/år)",
        "low": "Lav",
        "base": "Base",
        "high": "Høy",
        "range_line": (
            "Produksjonsintervall: {low} – {high} MWh/år "
            "(spenn ±{spread:.0f} % rundt basisverdien)."
        ),
        "chart_caption": "Månedlig AC-produksjon",
        "chart_title": "Månedlig AC-produksjon ({kwp} kWp)",
        "chart_ylabel": "AC-energi (kWh)",
        "sec6": "6 Nøkkelantakelser og begrensninger",
        "tema": "Tema",
        "antakelse": "Antakelse / begrensning",
        "next_step": "Anbefalt neste steg",
        "a_irr": "Solinnstråling",
        "a_irr_val": "PVGIS 5.2 (SARAH), regional statistikk. Ingen site-spesifikk måling.",
        "a_irr_next": "Hent lokal pyranometerdata fra nabo-installasjon eller værtjeneste.",
        "a_nudge": "PVGIS lookup-punkt",
        "a_nudge_val": (
            "PVGIS avviste inputkoordinatene som over sjø; nærmeste "
            "land-grid ({lat:.4f}, {lng:.4f}) ble brukt. Irradiasjonsdata "
            "varierer lite på denne avstanden."
        ),
        "a_tilt": "POA / tilt",
        "a_tilt_val": (
            "{tilt}° helning antatt. Faktisk vinkel bekreftes mot Sunlit Seas "
            "designspec ved design freeze."
        ),
        "a_tilt_next": "Bekreft med konstruksjonstegning.",
        "a_area": "Areal",
        "a_area_with": (
            "Hele oppgitt areal ({area} m²) brukt som brutto; typisk netto "
            "80–90 %."
        ),
        "a_area_without": "kWp oppgitt direkte; ingen arealavhengighet.",
        "a_area_next": (
            "Fastsett netto tilgjengelig areal etter gangbaner, ankerfeste og "
            "buffersoner."
        ),
        "a_panel": "Panelspesifikasjon",
        "a_panel_val": "{wp} Wp per panel, {w}×{h} mm.",
        "a_panel_next": "Innhent oppdatert produktspesifikasjon ved tilbudstidspunkt.",
        "a_pr": "Performance Ratio",
        "a_pr_val": (
            "PR = {pr:.1f} % beregnet fra komponentsum. Temperaturleddet "
            "kan være konservativt for flytende anlegg."
        ),
        "a_pr_next": (
            "Mål kjøleeffekt på pilotinstallasjon; juster FPV-kjøleeffekt-"
            "parameter."
        ),
        "a_bonus": "FPV-kjøleeffekt",
        "a_bonus_val": "{bonus} % DC-uplift antatt (literaturbasert, konservativ).",
        "a_bonus_next": (
            "Erstatt med måledata fra Sunlit Sea pilotanlegg når det foreligger."
        ),
        "a_albedo": "Albedo",
        "a_albedo_val": (
            "Vannalbedo (~6 %) ikke eksplisitt modellert; bidrag fra flate "
            "paneler er lite."
        ),
        "a_albedo_next": (
            "Kan inkluderes som sensitivitetsparameter ved bifasiale paneler."
        ),
        "a_grid": "Nett / inverter",
        "a_grid_val": "AC-kapasitet (MWac) ikke fastsatt. DC/AC-ratio ikke definert.",
        "a_grid_next": (
            "Fastsett DC/AC-ratio (typisk 1,10–1,20 for flytende solkraft)."
        ),
        "a_reg": "Regulering",
        "a_reg_val": "Regelverk for flytende solkraft ikke vurdert i denne rapporten.",
        "a_reg_next": "Igangsett regulatorisk screening for konkret lokasjon.",
        "footer_method_label": "Beregningsmetode:",
        "footer_method": (
            "E = P_peak × H × PR × (1 + FPV-kjøleeffekt). Standardmetode iht. "
            "IEC 61724."
        ),
        "footer_irr_label": "Irradiasjonsgrunnlag:",
        "footer_irr": (
            "POA = {poa} kWh/m²/år fra PVGIS 5.2 ({data_source}), tiltet "
            "{tilt}° mot azimut {az}° (kompass)."
        ),
        "footer_disclaimer": (
            "Dette er et innledende estimat. Resultatene bør ikke benyttes "
            "til investeringsbeslutninger uten videre teknisk due diligence."
        ),
    },
    "en": {
        "title": "Floating solar farm — Feasibility study",
        "tech": "Sunlit Sea technology",
        "prep": "Prepared",
        "prep_by": "Prepared by",
        "status": "Status",
        "status_val": "Preliminary estimate",
        "irr_src": "Irradiation data",
        "data_tmy": "PVGIS 5.2, typical meteorological year",
        "data_year": "PVGIS 5.2, year",
        "headline": "Headline figures",
        "kpi_count": "Panel count",
        "kpi_count_unit": "panels",
        "kpi_capacity": "Installed capacity",
        "kpi_poa": "POA irradiation (tilted plane)",
        "kpi_pr": "Performance Ratio",
        "kpi_production": "Estimated production",
        "kpi_specific": "Specific yield",
        "sec1": "1 Panel configuration and area",
        "sec1_intro_area": (
            "Sunlit Sea mounts panels at {tilt}° south-facing tilt on pontoon "
            "structures. A {gap} mm gap on both axes allows surface drainage "
            "and pontoon attachment."
        ),
        "sec1_intro_kwp": (
            "Installed capacity is provided directly as {kwp} kWp DC. Panel "
            "configuration and area derivation are not performed (no `--area` "
            "supplied)."
        ),
        "param": "Parameter",
        "value": "Value",
        "unit": "Unit",
        "note": "Note",
        "panel_dim": "Panel dimensions (W × H)",
        "panel_dim_note": "Supplied panel dimension",
        "gap": "Gap",
        "gap_note": "Both axes",
        "slot_dim": "Slot area per panel (W × H)",
        "slot_note": "Panel + gap",
        "slot_area": "Slot area per panel",
        "panel_wp": "Panel power (nominal)",
        "panel_wp_note": "Per panel, STC",
        "power_density": "Power density",
        "packing": "Packing factor",
        "packing_note": "Panel area ÷ slot area",
        "available_area": "Available water surface",
        "given": "Supplied",
        "panel_count": "Panel count",
        "installed_dc": "Installed DC capacity",
        "assumed_panel_wp": "Assumed panel power",
        "default": "Default",
        "panel_count_derived": "Panel count (derived)",
        "direct": "Supplied directly",
        "sec2": "2 Solar irradiation and POA analysis",
        "sec2_intro": (
            "At {tilt}° south-facing tilt the panels capture slightly more "
            "irradiation than a horizontal plane. POA is taken from PVGIS 5.2 "
            "(Perez model)."
        ),
        "ghi": "GHI (horizontal reference)",
        "ghi_note": "PVGIS MRcalc, 2005–2020",
        "poa_at": "POA at {tilt}° (tilted plane)",
        "poa_note": "PVGIS PVcalc",
        "tilt_label": "Tilt angle",
        "tilt_towards_south": "Facing south",
        "tilt_towards_az": "Facing azimuth {az}°",
        "gain": "Gain vs horizontal plane",
        "gain_note": "POA ÷ GHI – 1",
        "sec3": "3 Loss budget — PR decomposition",
        "loss_component": "Loss component",
        "loss_pct": "Loss (%)",
        "sum_loss": "Total loss",
        "pr_result": "Performance Ratio (PR)",
        "pr_formula": "100 − Σ",
        "pvgis_control": (
            "PVGIS reference value (crystSi model with internal temperature "
            "and spectral derating, no external losses): {pvgis_mwh} MWh/year, "
            "implied PR {pvgis_pr:.1f} %. The component sum is likely "
            "{verdict} compared with the PVGIS model."
        ),
        "verdict_optimistic": "optimistic",
        "verdict_conservative": "conservative",
        "verdict_consistent": "consistent",
        "sec4": "4 Energy production",
        "beregning": "Calculation",
        "p_peak": "Installed DC capacity (P_peak)",
        "poa_h": "POA irradiation (H)",
        "pr_dec": "Performance Ratio (PR)",
        "pr_dec_note": "100 − Σ losses (from loss budget)",
        "e_production": "Estimated production (E)",
        "e_note": "P × H × PR, plus {fpv} % FPV cooling benefit",
        "specific": "Specific yield",
        "specific_note": "E ÷ P",
        "op_hours": "Equivalent operating hours",
        "op_hours_note": "= specific yield numerically",
        "cf_label": "Capacity factor",
        "cf_note": "E ÷ (P × 8 760 h)",
        "formula_box": "`E = {kwp} kWp x {poa} kWh/m2/yr x {pr:.2f} x {bonus:.2f} = {e} MWh/yr`",
        "sec5": "5 Sensitivity analysis",
        "scenario": "Scenario",
        "ghi_dev": "GHI deviation",
        "pr_dev": "PR deviation",
        "production_mwh": "Production (MWh/year)",
        "low": "Low",
        "base": "Base",
        "high": "High",
        "range_line": (
            "Production range: {low} – {high} MWh/year (spread ±{spread:.0f} % "
            "around the base value)."
        ),
        "chart_caption": "Monthly AC production",
        "chart_title": "Monthly AC production ({kwp} kWp)",
        "chart_ylabel": "AC energy (kWh)",
        "sec6": "6 Key assumptions and limitations",
        "tema": "Topic",
        "antakelse": "Assumption / limitation",
        "next_step": "Recommended next step",
        "a_irr": "Solar irradiation",
        "a_irr_val": (
            "PVGIS 5.2 (SARAH), regional statistic. No site-specific "
            "measurement."
        ),
        "a_irr_next": (
            "Obtain local pyranometer data from a nearby installation or "
            "weather service."
        ),
        "a_nudge": "PVGIS lookup point",
        "a_nudge_val": (
            "PVGIS rejected the input coordinates as over-sea; the nearest "
            "land grid cell ({lat:.4f}, {lng:.4f}) was used. Irradiation data "
            "varies little over this distance."
        ),
        "a_tilt": "POA / tilt",
        "a_tilt_val": (
            "{tilt}° tilt assumed. The actual angle is confirmed against the "
            "Sunlit Sea design specification at design freeze."
        ),
        "a_tilt_next": "Confirm against the construction drawing.",
        "a_area": "Area",
        "a_area_with": (
            "Full supplied area ({area} m²) treated as gross; typical net is "
            "80–90 %."
        ),
        "a_area_without": "kWp supplied directly; no area dependency.",
        "a_area_next": (
            "Fix the net available area after walkways, anchor points and "
            "buffer zones."
        ),
        "a_panel": "Panel specification",
        "a_panel_val": "{wp} Wp per panel, {w} × {h} mm.",
        "a_panel_next": "Obtain updated product specification at tender time.",
        "a_pr": "Performance Ratio",
        "a_pr_val": (
            "PR = {pr:.1f} % computed from the component sum. The temperature "
            "term may be conservative for floating installations."
        ),
        "a_pr_next": (
            "Measure the cooling effect at a pilot installation; adjust the "
            "FPV cooling bonus parameter."
        ),
        "a_bonus": "FPV cooling bonus",
        "a_bonus_val": (
            "{bonus} % DC uplift assumed (literature-based, conservative)."
        ),
        "a_bonus_next": (
            "Replace with measurements from a Sunlit Sea pilot installation "
            "when available."
        ),
        "a_albedo": "Albedo",
        "a_albedo_val": (
            "Water albedo (~6 %) not explicitly modelled; the contribution to "
            "flat panels is small."
        ),
        "a_albedo_next": (
            "Can be included as a sensitivity parameter for bifacial panels."
        ),
        "a_grid": "Grid / inverter",
        "a_grid_val": "AC capacity (MWac) not fixed. DC/AC ratio not defined.",
        "a_grid_next": (
            "Fix the DC/AC ratio (typical 1.10–1.20 for floating solar)."
        ),
        "a_reg": "Regulatory",
        "a_reg_val": (
            "Regulatory framework for floating solar not assessed in this "
            "report."
        ),
        "a_reg_next": (
            "Initiate regulatory screening for the specific site."
        ),
        "footer_method_label": "Calculation method:",
        "footer_method": (
            "E = P_peak × H × PR × (1 + FPV cooling bonus). Standard method "
            "per IEC 61724."
        ),
        "footer_irr_label": "Irradiation basis:",
        "footer_irr": (
            "POA = {poa} kWh/m²/year from PVGIS 5.2 ({data_source}), tilted "
            "{tilt}° facing azimuth {az}° (compass)."
        ),
        "footer_disclaimer": (
            "This is a preliminary estimate. The results should not be used "
            "for investment decisions without further technical due diligence."
        ),
    },
}

# Panel defaults match the CONNECT product class and the reference.
DEFAULT_PANEL_WIDTH_MM = 2384
DEFAULT_PANEL_HEIGHT_MM = 1303
DEFAULT_PANEL_WP = 740
DEFAULT_GAP_MM = 100


@dataclass
class Inputs:
    lat: float
    lng: float
    capacity_kwp: float | None = None
    area_m2: float | None = None
    panel_width_mm: int = DEFAULT_PANEL_WIDTH_MM
    panel_height_mm: int = DEFAULT_PANEL_HEIGHT_MM
    panel_wp: int = DEFAULT_PANEL_WP
    gap_mm: int = DEFAULT_GAP_MM
    tilt_deg: float = 2.0
    azimuth_compass_deg: float = 180.0
    losses_pct: dict[str, float] = field(default_factory=lambda: dict(DEFAULT_LOSSES))
    fpv_cooling_bonus_pct: float = 2.0
    year: int | None = None
    use_horizon: bool = True
    location_name: str | None = None


# --- PVGIS -----------------------------------------------------------------

def compass_to_pvgis_aspect(compass_deg: float) -> float:
    """0=N, 90=E, 180=S, 270=W  ->  PVGIS aspect 0=S, -90=E, 90=W."""
    aspect = compass_deg - 180.0
    while aspect >= 180:
        aspect -= 360
    while aspect < -180:
        aspect += 360
    return aspect


class _OverSea(Exception):
    pass


def _pvgis_get(url: str, lat: float, lng: float, params_rest: dict) -> dict:
    params = {"lat": lat, "lon": lng, **params_rest}
    r = requests.get(url, params=params, timeout=30)
    if r.status_code == 400:
        try:
            msg = r.json().get("message", "")
        except ValueError:
            msg = r.text
        if "over the sea" in msg.lower():
            raise _OverSea(msg)
    r.raise_for_status()
    return r.json()


def _nudge_land(lat: float, lng: float, url: str, params_rest: dict) -> tuple[float, float, dict]:
    """Expanding-ring search for the nearest land grid cell. Returns the
    accepted (lat, lng) and the PVGIS response at that point."""
    try:
        return lat, lng, _pvgis_get(url, lat, lng, params_rest)
    except _OverSea:
        pass
    for ring in range(1, 11):
        step = 0.005 * ring
        cand = []
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if di == 0 and dj == 0:
                    continue
                cand.append((lat + di * step, lng + dj * step))
        cand.sort(key=lambda p: (p[0] - lat) ** 2 + (p[1] - lng) ** 2)
        for cl, cg in cand:
            try:
                resp = _pvgis_get(url, cl, cg, params_rest)
                return cl, cg, resp
            except _OverSea:
                continue
    raise RuntimeError(
        f"PVGIS rejected the site at ({lat}, {lng}) and no land point was "
        f"found within a 5 km search radius."
    )


def pvgis_pvcalc(
    inp: Inputs, capacity_kwp: float, *,
    total_loss_pct: float,
    tilt_deg: float | None = None,
    az_compass: float | None = None,
    lookup_point: tuple[float, float] | None = None,
) -> tuple[tuple[float, float], dict]:
    tilt = inp.tilt_deg if tilt_deg is None else tilt_deg
    az = inp.azimuth_compass_deg if az_compass is None else az_compass
    params_rest = {
        "peakpower": capacity_kwp,
        "loss": total_loss_pct,
        "angle": tilt,
        "aspect": compass_to_pvgis_aspect(az),
        "pvtechchoice": "crystSi",
        "mountingplace": "free",
        "usehorizon": 1 if inp.use_horizon else 0,
        "outputformat": "json",
    }
    if inp.year is not None:
        params_rest["startyear"] = inp.year
        params_rest["endyear"] = inp.year
    if lookup_point is not None:
        return lookup_point, _pvgis_get(PVGIS_PVCALC, *lookup_point, params_rest)
    lat_got, lng_got, resp = _nudge_land(inp.lat, inp.lng, PVGIS_PVCALC, params_rest)
    return (lat_got, lng_got), resp


def pvgis_horizontal_ghi(
    lat: float, lng: float,
    year_start: int = 2005, year_end: int = 2020,
) -> float:
    """Annual GHI in kWh/m2/year from PVGIS MRcalc (horizontal irradiation,
    averaged across the given year range)."""
    params_rest = {
        "horirrad": 1,
        "mstartyear": year_start,
        "mendyear": year_end,
        "outputformat": "json",
    }
    resp = _pvgis_get(PVGIS_MRCALC, lat, lng, params_rest)
    rows = resp["outputs"]["monthly"]
    sum_h_h = sum(row["H(h)_m"] for row in rows)
    n_years = year_end - year_start + 1
    return sum_h_h / n_years


def parse_pvcalc(resp: dict) -> dict:
    out = resp["outputs"]
    monthly = out["monthly"]["fixed"]
    totals = out["totals"]["fixed"]
    return {
        "annual_kwh_ac": totals["E_y"],
        "monthly_kwh_ac": [m["E_m"] for m in monthly],
        "annual_poa_kwhm2": totals["H(i)_y"],
        "monthly_poa_kwhm2": [m["H(i)_m"] for m in monthly],
    }


# --- Derivations -----------------------------------------------------------

def derive_panel_count(inp: Inputs) -> tuple[int, float, float, float, float]:
    """From area + panel geometry, derive slot area, packing factor,
    panel count and installed kWp."""
    panel_area_m2 = (inp.panel_width_mm / 1000) * (inp.panel_height_mm / 1000)
    slot_w = (inp.panel_width_mm + inp.gap_mm) / 1000
    slot_h = (inp.panel_height_mm + inp.gap_mm) / 1000
    slot_area_m2 = slot_w * slot_h
    packing_factor_pct = panel_area_m2 / slot_area_m2 * 100
    assert inp.area_m2 is not None
    panel_count = int(inp.area_m2 // slot_area_m2)
    installed_kwp = panel_count * inp.panel_wp / 1000
    return panel_count, slot_area_m2, packing_factor_pct, installed_kwp, panel_area_m2


def apply_fpv_bonus(annual: float, monthly: list[float], bonus_pct: float):
    k = 1.0 + bonus_pct / 100.0
    return annual * k, [m * k for m in monthly]


# --- Rendering -------------------------------------------------------------

def _fmt_num(x: float, decimals: int = 0) -> str:
    """Thousands-separated number with NBSP (U+00A0) to prevent pdf line breaks."""
    if decimals == 0:
        s = f"{int(round(x)):,}"
    else:
        s = f"{x:,.{decimals}f}"
    return s.replace(",", " ")


def write_chart(
    monthly_kwh: list[float], path: Path, title: str, lang: str = "no",
) -> None:
    T = L10N[lang]
    fig, ax = plt.subplots(figsize=(7.5, 3.5))
    ax.bar(MONTH_LABELS[lang], monthly_kwh, color="#2F354F")
    ax.set_ylabel(T["chart_ylabel"])
    ax.set_title(title)
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)


def md_report(
    inp: Inputs, result: dict, chart_rel: str, lang: str = "no",
) -> str:
    T = L10N[lang]
    LOSS = LOSS_LABELS[lang]
    kwp = result["installed_kwp"]
    poa = result["pvgis"]["annual_poa_kwhm2"]
    ghi = result["pvgis"]["annual_ghi_kwhm2"]
    pr_pct = result["pr_pct"]
    e_annual = result["annual_kwh_fpv"]
    specific = e_annual / kwp
    eq_hours = e_annual / kwp
    cf_pct = e_annual / (kwp * 8760) * 100
    panel_count = result["panel_count"]
    tilt_gain_pct = (poa - ghi) / ghi * 100

    loc_title = inp.location_name or f"{inp.lat:.4f}°N / {inp.lng:.4f}°E"
    today = _dt.date.today().isoformat()
    data_source = (
        T["data_tmy"] if inp.year is None
        else f"{T['data_year']} {inp.year}"
    )

    front = {
        "sunlit_template": "report",
        "internal_title": f"{T['title']} — {loc_title}",
    }
    front_yaml = yaml.safe_dump(front, sort_keys=False, allow_unicode=True).strip()

    tilt_towards = (
        T["tilt_towards_south"] if 170 <= inp.azimuth_compass_deg <= 190
        else T["tilt_towards_az"].format(az=f"{inp.azimuth_compass_deg:g}")
    )

    mwp_unit = "MWp DC"
    kwp_unit = "kWp"
    mwh_per_year = "MWh/year" if lang == "en" else "MWh/år"
    kwh_per_kwp_per_year = "kWh/kWp/year" if lang == "en" else "kWh/kWp/år"
    kwh_per_m2_per_year = "kWh/m²/year" if lang == "en" else "kWh/m²/år"
    h_per_year = "h/year" if lang == "en" else "h/år"

    lines = [
        "---",
        front_yaml,
        "---",
        "",
        f"# {T['title']}",
        "",
        f"{loc_title} · {T['tech']}",
        "",
        f"{T['prep']}: {today} · {T['prep_by']}: Sunlit Sea AS · {T['status']}: {T['status_val']}",
        "",
        f"{T['irr_src']}: {data_source}",
        "",
        f"## {T['headline']}",
        "",
        f"| {T['kpi_count']} | {T['kpi_capacity']} | {T['kpi_poa']} |",
        "|---|---|---|",
        f"| **{_fmt_num(panel_count)} {T['kpi_count_unit']}** | **{_fmt_num(kwp / 1000, 3)} {mwp_unit}** | **{_fmt_num(poa)} {kwh_per_m2_per_year}** |",
        "",
        f"| {T['kpi_pr']} | {T['kpi_production']} | {T['kpi_specific']} |",
        "|---|---|---|",
        f"| **{pr_pct:.1f} %** | **{_fmt_num(e_annual / 1000, 1)} {mwh_per_year}** | **{_fmt_num(specific)} {kwh_per_kwp_per_year}** |",
        "",
    ]

    # Section 1
    lines += [
        f"## {T['sec1']}",
        "",
    ]
    if inp.area_m2 is not None:
        lines += [
            T["sec1_intro_area"].format(tilt=f"{inp.tilt_deg:g}", gap=inp.gap_mm),
            "",
            f"| {T['param']} | {T['value']} | {T['unit']} | {T['note']} |",
            "|---|---|---|---|",
            f"| {T['panel_dim']} | {inp.panel_width_mm} × {inp.panel_height_mm} | mm | {T['panel_dim_note']} |",
            f"| {T['gap']} | {inp.gap_mm} | mm | {T['gap_note']} |",
            f"| {T['slot_dim']} | {inp.panel_width_mm + inp.gap_mm} × {inp.panel_height_mm + inp.gap_mm} | mm | {T['slot_note']} |",
            f"| {T['slot_area']} | {result['slot_area_m2']:.3f} | m² | {T['slot_note']} |",
            f"| {T['panel_wp']} | {inp.panel_wp} | Wp | {T['panel_wp_note']} |",
            f"| {T['power_density']} | {inp.panel_wp / result['slot_area_m2']:.1f} | Wp/m² | {inp.panel_wp} ÷ {result['slot_area_m2']:.3f} |",
            f"| {T['packing']} | {result['packing_factor_pct']:.1f} | % | {T['packing_note']} |",
            f"| {T['available_area']} | {_fmt_num(inp.area_m2)} | m² | {T['given']} |",
            f"| **{T['panel_count']}** | **{_fmt_num(panel_count)}** | {T['kpi_count_unit']} | [{_fmt_num(inp.area_m2)} ÷ {result['slot_area_m2']:.3f}] |",
            f"| **{T['installed_dc']}** | **{_fmt_num(kwp)}** | kWp | {_fmt_num(panel_count)} × {inp.panel_wp} W |",
        ]
    else:
        lines += [
            T["sec1_intro_kwp"].format(kwp=_fmt_num(kwp)),
            "",
            f"| {T['param']} | {T['value']} | {T['unit']} | {T['note']} |",
            "|---|---|---|---|",
            f"| {T['installed_dc']} | {_fmt_num(kwp)} | kWp | {T['direct']} |",
            f"| {T['assumed_panel_wp']} | {inp.panel_wp} | Wp | {T['default']} |",
            f"| {T['panel_count_derived']} | ~{_fmt_num(round(kwp * 1000 / inp.panel_wp))} | {T['kpi_count_unit']} | {_fmt_num(kwp)} × 1 000 ÷ {inp.panel_wp} |",
        ]
    lines.append("")

    # Section 2
    lines += [
        f"## {T['sec2']}",
        "",
        T["sec2_intro"].format(tilt=f"{inp.tilt_deg:g}"),
        "",
        f"| {T['param']} | {T['value']} | {T['unit']} | {T['note']} |",
        "|---|---|---|---|",
        f"| {T['ghi']} | {_fmt_num(ghi)} | {kwh_per_m2_per_year} | {T['ghi_note']} |",
        f"| {T['poa_at'].format(tilt=f'{inp.tilt_deg:g}')} | {_fmt_num(poa)} | {kwh_per_m2_per_year} | {T['poa_note']} |",
        f"| {T['tilt_label']} | {inp.tilt_deg:g} | ° | {tilt_towards} |",
        f"| {T['gain']} | {tilt_gain_pct:+.1f} | % | {T['gain_note']} |",
        "",
    ]

    # Section 3
    total_losses = sum(inp.losses_pct.values())
    pvgis_pr = result["pvgis_implied_pr_pct"]
    pvgis_ac = result["pvgis_ac_reference_kwh"]
    verdict = (
        T["verdict_optimistic"] if pr_pct > pvgis_pr + 1
        else T["verdict_conservative"] if pr_pct < pvgis_pr - 1
        else T["verdict_consistent"]
    )
    lines += [
        f"## {T['sec3']}",
        "",
        f"| {T['loss_component']} | {T['loss_pct']} | {T['note']} |",
        "|---|---|---|",
    ]
    for key in LOSS:
        val = inp.losses_pct.get(key, 0.0)
        lines.append(f"| {LOSS[key]} | {val:.1f} | |")
    lines += [
        f"| **{T['sum_loss']}** | **{total_losses:.1f}** | |",
        f"| **{T['pr_result']}** | **{pr_pct:.1f} %** | {T['pr_formula']} |",
        "",
        T["pvgis_control"].format(
            pvgis_mwh=_fmt_num(pvgis_ac / 1000, 1),
            pvgis_pr=pvgis_pr,
            verdict=verdict,
        ),
        "",
    ]

    # Section 4
    lines += [
        f"## {T['sec4']}",
        "",
        f"| {T['param']} | {T['value']} | {T['unit']} | {T['beregning']} |",
        "|---|---|---|---|",
        f"| {T['p_peak']} | {_fmt_num(kwp)} | kWp | |",
        f"| {T['poa_h']} | {_fmt_num(poa)} | {kwh_per_m2_per_year} | |",
        f"| {T['pr_dec']} | {pr_pct / 100:.2f} | — | {T['pr_dec_note']} |",
        f"| **{T['e_production']}** | **{_fmt_num(e_annual / 1000, 1)}** | {mwh_per_year} | {T['e_note'].format(fpv=f'{inp.fpv_cooling_bonus_pct:g}')} |",
        f"| {T['specific']} | {_fmt_num(specific)} | {kwh_per_kwp_per_year} | {T['specific_note']} |",
        f"| {T['op_hours']} | {_fmt_num(eq_hours)} | {h_per_year} | {T['op_hours_note']} |",
        f"| {T['cf_label']} | {cf_pct:.1f} | % | {T['cf_note']} |",
        "",
        T["formula_box"].format(
            kwp=_fmt_num(kwp), poa=_fmt_num(poa),
            pr=pr_pct / 100, bonus=1 + inp.fpv_cooling_bonus_pct / 100,
            e=_fmt_num(e_annual / 1000, 1),
        ),
        "",
    ]

    # Section 5
    scen = result["scenarios"]
    lines += [
        f"## {T['sec5']}",
        "",
        f"| {T['scenario']} | {T['ghi_dev']} | {T['pr_dev']} | {T['production_mwh']} |",
        "|---|---|---|---|",
        f"| {T['low']} | −5 % | −3 pp | {_fmt_num(scen['low_mwh'], 1)} |",
        f"| **{T['base']}** | — | — | **{_fmt_num(scen['base_mwh'], 1)}** |",
        f"| {T['high']} | +5 % | +2 pp | {_fmt_num(scen['high_mwh'], 1)} |",
        "",
        T["range_line"].format(
            low=_fmt_num(scen['low_mwh'], 1),
            high=_fmt_num(scen['high_mwh'], 1),
            spread=scen['spread_pct'],
        ),
        "",
        f"![{T['chart_caption']}]({chart_rel})",
        "",
    ]

    # Section 6
    nudged = result["pvgis_lookup_point"]["nudged_from_input"]
    lines += [
        f"## {T['sec6']}",
        "",
        f"| {T['tema']} | {T['antakelse']} | {T['next_step']} |",
        "|---|---|---|",
        f"| {T['a_irr']} | {T['a_irr_val']} | {T['a_irr_next']} |",
    ]
    if nudged:
        lines.append(
            f"| {T['a_nudge']} | "
            + T["a_nudge_val"].format(
                lat=result['pvgis_lookup_point']['lat'],
                lng=result['pvgis_lookup_point']['lng'],
            ) + " | — |"
        )
    area_val = (
        T["a_area_with"].format(area=_fmt_num(inp.area_m2))
        if inp.area_m2 else T["a_area_without"]
    )
    lines += [
        f"| {T['a_tilt']} | {T['a_tilt_val'].format(tilt=f'{inp.tilt_deg:g}')} | {T['a_tilt_next']} |",
        f"| {T['a_area']} | {area_val} | {T['a_area_next']} |",
        f"| {T['a_panel']} | {T['a_panel_val'].format(wp=inp.panel_wp, w=inp.panel_width_mm, h=inp.panel_height_mm)} | {T['a_panel_next']} |",
        f"| {T['a_pr']} | {T['a_pr_val'].format(pr=pr_pct)} | {T['a_pr_next']} |",
        f"| {T['a_bonus']} | {T['a_bonus_val'].format(bonus=f'{inp.fpv_cooling_bonus_pct:g}')} | {T['a_bonus_next']} |",
        f"| {T['a_albedo']} | {T['a_albedo_val']} | {T['a_albedo_next']} |",
        f"| {T['a_grid']} | {T['a_grid_val']} | {T['a_grid_next']} |",
        f"| {T['a_reg']} | {T['a_reg_val']} | {T['a_reg_next']} |",
        "",
        "---",
        "",
        f"**{T['footer_method_label']}** {T['footer_method']}",
        "",
        f"**{T['footer_irr_label']}** " + T["footer_irr"].format(
            poa=_fmt_num(poa),
            data_source=data_source,
            tilt=f"{inp.tilt_deg:g}",
            az=f"{inp.azimuth_compass_deg:g}",
        ),
        "",
        f"*{T['footer_disclaimer']}*",
    ]

    return "\n".join(lines)


# --- Main ------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--lat", type=float, help="site latitude (decimal degrees)")
    ap.add_argument("--lng", type=float, help="site longitude (decimal degrees)")

    cap = ap.add_mutually_exclusive_group()
    cap.add_argument("--kwp", type=float, help="installed DC capacity in kWp (direct)")
    cap.add_argument("--area", type=float, dest="area_m2",
                      help="available water surface in m2 (capacity derived from panel geometry)")

    ap.add_argument("--panel-width", type=int, dest="panel_width_mm",
                      default=None, help=f"panel width in mm (default {DEFAULT_PANEL_WIDTH_MM})")
    ap.add_argument("--panel-height", type=int, dest="panel_height_mm",
                      default=None, help=f"panel height in mm (default {DEFAULT_PANEL_HEIGHT_MM})")
    ap.add_argument("--panel-wp", type=int, dest="panel_wp",
                      default=None, help=f"panel nominal power in Wp (default {DEFAULT_PANEL_WP})")
    ap.add_argument("--gap-mm", type=int, dest="gap_mm",
                      default=None, help=f"inter-panel gap in mm (default {DEFAULT_GAP_MM})")

    ap.add_argument("--tilt", type=float, help="module tilt in degrees (default 2.0)")
    ap.add_argument("--azimuth", type=float,
                      help="compass azimuth: 0=N, 90=E, 180=S, 270=W (default 180)")

    for lk in DEFAULT_LOSSES:
        ap.add_argument(f"--loss-{lk.replace('_', '-')}", type=float, dest=f"loss_{lk}",
                          help=f"loss component '{lk}' in %% (default {DEFAULT_LOSSES[lk]})")

    ap.add_argument("--fpv-cooling-bonus", type=float, dest="fpv_cooling_bonus",
                      help="FPV cooling bonus in %% vs land reference (default 2.0)")
    ap.add_argument("--year", type=int, help="specific year; default = PVGIS TMY")
    ap.add_argument("--location-name", dest="location_name",
                      help="free-text location string shown on the report (default: lat/lng)")
    ap.add_argument("--lang", choices=["no", "en"], default=None,
                      help="report language: 'no' (default) or 'en'")

    ap.add_argument("--yaml", type=Path, help="read inputs from YAML file (CLI overrides)")
    ap.add_argument("--md-out", type=Path, dest="md_out",
                      help="write Markdown report to this file (with sunlit_template: report frontmatter)")
    ap.add_argument("--chart-out", type=Path, dest="chart_out",
                      help="write chart PNG to this file (defaults to <md-out>.png)")
    ap.add_argument("--json-out", type=Path, dest="json_out",
                      help="write full result JSON to this file")
    ap.add_argument("--quiet", action="store_true",
                      help="suppress stderr progress lines")
    args = ap.parse_args(argv)

    yaml_data = {}
    if args.yaml:
        yaml_data = yaml.safe_load(args.yaml.read_text(encoding="utf-8")) or {}

    def pick(cli_val, yaml_key, default):
        if cli_val is not None:
            return cli_val
        if yaml_key in yaml_data:
            return yaml_data[yaml_key]
        return default

    lat = pick(args.lat, "lat", None)
    lng = pick(args.lng, "lng", None)
    if lat is None or lng is None:
        ap.error("need --lat and --lng (or supply via --yaml)")

    kwp = pick(args.kwp, "capacity_kwp", None)
    area = pick(args.area_m2, "area_m2", None)
    if kwp is None and area is None:
        yaml_losses = yaml_data.get("losses_pct", {})
    else:
        yaml_losses = yaml_data.get("losses_pct", {})

    losses = dict(DEFAULT_LOSSES)
    losses.update(yaml_losses)
    for lk in DEFAULT_LOSSES:
        cli_v = getattr(args, f"loss_{lk}")
        if cli_v is not None:
            losses[lk] = cli_v

    inp = Inputs(
        lat=float(lat),
        lng=float(lng),
        capacity_kwp=float(kwp) if kwp is not None else None,
        area_m2=float(area) if area is not None else None,
        panel_width_mm=int(pick(args.panel_width_mm, "panel_width_mm", DEFAULT_PANEL_WIDTH_MM)),
        panel_height_mm=int(pick(args.panel_height_mm, "panel_height_mm", DEFAULT_PANEL_HEIGHT_MM)),
        panel_wp=int(pick(args.panel_wp, "panel_wp", DEFAULT_PANEL_WP)),
        gap_mm=int(pick(args.gap_mm, "gap_mm", DEFAULT_GAP_MM)),
        tilt_deg=float(pick(args.tilt, "tilt_deg", 2.0)),
        azimuth_compass_deg=float(pick(args.azimuth, "azimuth_compass_deg", 180.0)),
        losses_pct=losses,
        fpv_cooling_bonus_pct=float(pick(args.fpv_cooling_bonus, "fpv_cooling_bonus_pct", 2.0)),
        year=pick(args.year, "year", None),
        location_name=pick(args.location_name, "location_name", None),
    )

    if inp.capacity_kwp is None and inp.area_m2 is None:
        ap.error("need either --kwp or --area")

    def log(msg):
        if not args.quiet:
            print(msg, file=sys.stderr)

    # 1. Derive capacity from area if needed.
    panel_count = None
    slot_area_m2 = None
    packing_factor_pct = None
    if inp.area_m2 is not None:
        panel_count, slot_area_m2, packing_factor_pct, derived_kwp, _ = derive_panel_count(inp)
        if inp.capacity_kwp is None:
            inp.capacity_kwp = derived_kwp
        log(f"Area {inp.area_m2:g} m² -> {panel_count} panels -> {derived_kwp:.1f} kWp")

    assert inp.capacity_kwp is not None
    kwp_used = inp.capacity_kwp
    if panel_count is None:
        panel_count = round(kwp_used * 1000 / inp.panel_wp)

    total_loss_pct = sum(inp.losses_pct.values())

    log(f"Calling PVGIS for lat={inp.lat}, lng={inp.lng}, {kwp_used:.2f} kWp, "
        f"tilt={inp.tilt_deg}°, az_compass={inp.azimuth_compass_deg}°, "
        f"Σloss={total_loss_pct:.1f} %...")

    # Call PVGIS with loss=0 and use it for the POA (plane-of-array irradiation)
    # only. We compute the AC yield ourselves as POA × kWp × PR × (1 + FPV bonus),
    # where PR comes from the user-supplied loss decomposition. PVGIS's own AC
    # output is kept as a reference / cross-check — it uses PVGIS's internal
    # crystSi temperature model which may differ from the user's temperature
    # coefficient.
    try:
        (lat_used, lng_used), pvcalc_resp = pvgis_pvcalc(
            inp, kwp_used, total_loss_pct=0.0,
        )
    except (requests.RequestException, RuntimeError) as e:
        print(f"PVGIS PVcalc failed: {e}", file=sys.stderr)
        return 1

    nudged = (lat_used, lng_used) != (inp.lat, inp.lng)
    if nudged:
        log(f"PVGIS nudged lookup to nearest land ({lat_used:.4f}, {lng_used:.4f}).")

    pvcalc = parse_pvcalc(pvcalc_resp)

    try:
        annual_ghi = pvgis_horizontal_ghi(lat_used, lng_used)
    except requests.RequestException as e:
        print(f"PVGIS MRcalc (GHI) failed: {e}", file=sys.stderr)
        return 1

    # PR from user-supplied components (the authoritative PR for this report).
    pr_pct = 100.0 - total_loss_pct

    # AC yield computed from POA × kWp × PR × FPV bonus.
    poa_annual = pvcalc["annual_poa_kwhm2"]
    poa_monthly = pvcalc["monthly_poa_kwhm2"]
    annual_kwh_pre_bonus = poa_annual * kwp_used * pr_pct / 100.0
    monthly_kwh_pre_bonus = [
        m * kwp_used * pr_pct / 100.0 for m in poa_monthly
    ]
    annual_kwh_fpv, monthly_kwh_fpv = apply_fpv_bonus(
        annual_kwh_pre_bonus, monthly_kwh_pre_bonus,
        inp.fpv_cooling_bonus_pct,
    )

    # PVGIS's own AC estimate at loss=0 — kept as a cross-check reference.
    pvgis_ac_reference_kwh = pvcalc["annual_kwh_ac"]
    pvgis_implied_pr_pct = (
        pvgis_ac_reference_kwh / (kwp_used * poa_annual) * 100
    )

    scen_base = annual_kwh_fpv / 1000
    scen_low = scen_base * 0.95 * (pr_pct - 3.0) / pr_pct
    scen_high = scen_base * 1.05 * (pr_pct + 2.0) / pr_pct
    spread_pct = (scen_high - scen_low) / scen_base * 100 / 2

    result = {
        "inputs": {
            "lat": inp.lat, "lng": inp.lng,
            "capacity_kwp": kwp_used,
            "area_m2": inp.area_m2,
            "panel_width_mm": inp.panel_width_mm,
            "panel_height_mm": inp.panel_height_mm,
            "panel_wp": inp.panel_wp,
            "gap_mm": inp.gap_mm,
            "tilt_deg": inp.tilt_deg,
            "azimuth_compass_deg": inp.azimuth_compass_deg,
            "losses_pct": inp.losses_pct,
            "fpv_cooling_bonus_pct": inp.fpv_cooling_bonus_pct,
            "year": inp.year,
            "location_name": inp.location_name,
        },
        "pvgis_lookup_point": {
            "lat": lat_used, "lng": lng_used, "nudged_from_input": nudged,
        },
        "panel_count": panel_count,
        "slot_area_m2": slot_area_m2,
        "packing_factor_pct": packing_factor_pct,
        "installed_kwp": kwp_used,
        "pvgis": {
            "annual_kwh_ac": pvcalc["annual_kwh_ac"],
            "monthly_kwh_ac": pvcalc["monthly_kwh_ac"],
            "annual_poa_kwhm2": pvcalc["annual_poa_kwhm2"],
            "annual_ghi_kwhm2": annual_ghi,
        },
        "pr_pct": pr_pct,
        "pvgis_implied_pr_pct": pvgis_implied_pr_pct,
        "pvgis_ac_reference_kwh": pvgis_ac_reference_kwh,
        "annual_kwh_pre_bonus": annual_kwh_pre_bonus,
        "annual_kwh_fpv": annual_kwh_fpv,
        "monthly_kwh_fpv": monthly_kwh_fpv,
        "specific_yield_kwh_per_kwp": annual_kwh_fpv / kwp_used,
        "capacity_factor_pct": annual_kwh_fpv / (kwp_used * 8760) * 100,
        "scenarios": {
            "low_mwh": scen_low, "base_mwh": scen_base, "high_mwh": scen_high,
            "spread_pct": spread_pct,
        },
    }

    if args.json_out:
        args.json_out.write_text(json.dumps(result, indent=2), encoding="utf-8")
        log(f"Wrote {args.json_out}")

    lang = pick(args.lang, "lang", "no")
    if lang not in ("no", "en"):
        ap.error("--lang must be 'no' or 'en'")

    if args.md_out:
        chart_path = args.chart_out or args.md_out.with_suffix(".png")
        chart_title = L10N[lang]["chart_title"].format(kwp=_fmt_num(kwp_used))
        write_chart(monthly_kwh_fpv, chart_path, chart_title, lang=lang)
        log(f"Wrote {chart_path}")
        args.md_out.write_text(
            md_report(inp, result, chart_path.name, lang=lang) + "\n",
            encoding="utf-8",
        )
        log(f"Wrote {args.md_out}")

    json.dump(result, sys.stdout, indent=2)
    sys.stdout.write("\n")
    log(
        f"\nProd (FPV): {annual_kwh_fpv / 1000:.1f} MWh/år "
        f"({result['specific_yield_kwh_per_kwp']:.0f} kWh/kWp, "
        f"CF {result['capacity_factor_pct']:.1f} %, PR {pr_pct:.1f} %)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
