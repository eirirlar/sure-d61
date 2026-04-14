import math

import cupcalc
from cupcalc import CupCalc
import hexcalc
import shouldercalc
from hexfloatinput import HexFloatInput
from hexcalc import HexCalc
from shouldercalc import ShoulderCalc


def calc_volume_init(fi: HexFloatInput) -> float:
    sc = shouldercalc.calc_shoulder(fi)
    hc = hexcalc.calc_hex(fi.side, 2 * fi.cup_rad, sc.edge, fi.space)
    cc = cupcalc.calc_cup(fi)
    v = calc_volume(fi.cup_depth, fi, hc, sc, cc)
    return v


# mm3
def calc_volume(cup_depth: float, f: HexFloatInput, hex_calc: HexCalc, shoulder_calc: ShoulderCalc,
                cc: CupCalc):
    inner_vol_plus_cups = calc_inner_vol_plus_cups(hex_calc.inner_side, cup_depth, f, hex_calc, shoulder_calc)
    n_cups = len(hex_calc.cup_points)
    cup_vol = cupcalc.calc_vol(cup_depth, cc)
    cup_total_vol = n_cups * cup_vol
    v = inner_vol_plus_cups - cup_total_vol
    return v


def calc_inner_vol_plus_cups(inner_side: float, cup_depth: float, f: HexFloatInput, hex_calc: HexCalc,
                             shoulder_calc: ShoulderCalc) -> float:
    inner_vol_plus_cups_ex_shoulders = calc_inner_vol_plus_cups_ex_shoulders(inner_side, cup_depth)
    shoulder_vol = shoulder_calc.shoulder_vol(cup_depth, f, hex_calc)
    return inner_vol_plus_cups_ex_shoulders + shoulder_vol


def calc_inner_vol_plus_cups_ex_shoulders(inner_side: float, cup_depth: float) -> float:
    return inner_side * inner_side * math.sqrt(3.) / 2. * 3. * cup_depth
