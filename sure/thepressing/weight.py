import hexcalc
import shouldercalc
from areacalc import calc_area_plus_cups_plus_corners, calc_corner_area
from hexfloatinput import HexFloatInput

density = 0.00265  # g/mm3


def calc_weight_init(fi: HexFloatInput) -> float:
    sc = shouldercalc.calc_shoulder(fi)
    hc = hexcalc.calc_hex(fi.side, 2 * fi.cup_rad, sc.edge, fi.space)
    w = calc_weight(fi.side, hc.cup_max_x, fi.alu_thick)
    return w


# grams
def calc_weight(side: float, cup_max_x: float, alu_thick: float):
    inner_area_plus_cups_plus_corners = calc_area_plus_cups_plus_corners(side)
    corner_area = calc_corner_area(side, cup_max_x)
    a = inner_area_plus_cups_plus_corners - 6 * corner_area
    v = a * alu_thick
    w = v * density
    return w
