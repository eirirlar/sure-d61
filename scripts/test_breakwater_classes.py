"""Tests for scripts/breakwater_classes.py (T162, T163).

Run:  python -m pytest -p no:cacheprovider scripts/test_breakwater_classes.py     (~1 min)
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import breakwater_classes as b  # noqa: E402


@pytest.fixture(scope="module")
def classes():
    return {c["class"]: c for c in b.class_table()}


def test_macagno_reproduces_d32_for_surewave_unit():
    # D3.2: critical periods 1-3 s reduced to at least 40 % by the chosen unit
    for t in (1.0, 2.0, 3.0):
        assert b.macagno_ct(t, 5.0, 2.03, 38.0) <= 0.40


def test_macagno_no_overflow_in_deep_water_short_waves():
    assert 0 <= b.macagno_ct(0.5, 5.0, 2.03, 200.0) < 1e-3


def test_transmission_falls_with_width_and_rises_with_period():
    assert b.macagno_ct(3.0, 4.0, 1.5, 12) < b.macagno_ct(3.0, 2.5, 1.0, 12)
    assert b.macagno_ct(4.0, 4.0, 1.5, 12) > b.macagno_ct(3.0, 4.0, 1.5, 12)


def test_dispersion_deep_water_limit():
    t = 3.0
    assert math.isclose(b.wavelength(t, 200.0), b.G * t * t / (2 * math.pi), rel_tol=1e-6)


def test_growth_curve_inverse():
    ua = b.adjusted_wind(22.0)
    f = b.fetch_for_hs(1.0, ua)
    assert math.isclose(1.6e-3 * (b.G * f / ua ** 2) ** 0.5 * ua ** 2 / b.G, 1.0, rel_tol=1e-9)


def test_spectrum_without_breakwater_returns_hs():
    sh = b.spectral_heights(1.0, 3.0, None, None, 20.0)
    assert math.isclose(sh["hs_transmitted"], 1.0, rel_tol=0.02)


def test_every_class_meets_both_criteria(classes):
    for c in classes.values():
        assert c["meets"], c["class"]


def test_chosen_classes_not_lighter_than_search(classes):
    for name, c in classes.items():
        s = b.search_section(c["wave_class"])
        assert s is not None
        assert c["width_m"] * c["draft_m"] >= s["section_m2"] - 1e-9, name


def test_class_costs_ordered_and_below_open_sea_reference(classes):
    assert classes["light"]["installed_per_m"] < classes["medium"]["installed_per_m"] < classes["heavy"]["installed_per_m"]
    assert classes["heavy"]["installed_per_m"] < b.reference_open_sea_per_metre()


def test_heavy_material_equals_d74_per_metre(classes):
    assert math.isclose(classes["heavy"]["material_per_m"], b.REF["ring_material_eur"] / 1120, rel_tol=1e-9)


def test_ring_geometry_close_to_d74():
    assert 0.9 < b.ring_check()["ratio"] < 1.1


def test_coverage_monotonic_and_capped():
    l20 = b.coverage(3200, 20, "medium")["length_m"]
    l60 = b.coverage(3200, 60, "medium")["length_m"]
    l180 = b.coverage(3200, 180, "medium")["length_m"]
    ring = b.coverage(3200, 360, "medium")["length_m"]
    assert l20 < l60 < l180 <= ring + 1e-9
    assert math.isclose(ring, 2 * math.pi * (b.plant_radius(3200) + b.ASSUMPTIONS["standoff_m"]))


def test_cost_per_kwp_falls_with_plant_size():
    assert b.coverage(10000, 60, "medium")["cost_per_kwp"] < b.coverage(1000, 60, "medium")["cost_per_kwp"]


def test_host_share():
    r = b.coverage(3200, 60, "medium", host_share=0.5)
    assert math.isclose(r["cost_fpv_eur"], 0.5 * r["cost_eur"])
