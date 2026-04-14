from math import *

import cupcalc
import hexcalc
import shouldercalc
from hexfloatinput import HexFloatInput


def calc_contact_area_init(fi: HexFloatInput) -> float:
    sc = shouldercalc.calc_shoulder(fi)
    hc = hexcalc.calc_hex(fi.side, 2 * fi.cup_rad, sc.edge, fi.space)
    cc = cupcalc.calc_cup(fi)
    a = calc_contact_area(hc.inner_side, hc.cup_max_x, len(hc.cup_points), cc.lip_x.circle_r,
                          cc.lip_y.circle_r)
    return a


def calc_area_init(fi: HexFloatInput) -> float:
    sc = shouldercalc.calc_shoulder(fi)
    hc = hexcalc.calc_hex(fi.side, 2 * fi.cup_rad, sc.edge, fi.space)
    a = calc_area(hc.inner_side, hc.cup_max_x)
    return a


# mm2
def calc_contact_area(inner_side: float, cup_max_x: float, n_cups: float, fillet_rad_x: float, fillet_rad_y: float):
    inner_plate_area = calc_area(inner_side, cup_max_x)
    cup_area = n_cups * cupcalc.calc_area(fillet_rad_x, fillet_rad_y)
    a = inner_plate_area - cup_area
    return a


# mm2
def calc_area(side: float, cup_max_x: float) -> float:
    a0 = calc_area_plus_cups_plus_corners(side)
    a1 = 6 * calc_corner_area(side, cup_max_x)
    a = a0 - a1
    return a


def calc_area_plus_cups_plus_corners(side: float) -> float:
    return side ** 2 * sqrt(3) / 2 * 3


def calc_corner_area(side: float, cup_max_x: float) -> float:
    edge_to_cup = side - cup_max_x
    corner_rad = edge_to_cup * sqrt(3) / 2
    triangle_part = edge_to_cup * corner_rad / 2
    circle_part = corner_rad ** 2 * pi / 6
    corner_area = triangle_part - circle_part
    return corner_area
