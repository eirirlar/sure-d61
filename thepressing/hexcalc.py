import math

import shouldercalc
from hexfloatinput import HexFloatInput
from util import flatten


class HexCalc:
    def __init__(self, inner_side: float, cup_points: [(float, float)], inner_hex_corners: [(float, float)],
                 cup_max_x: float, cup_max_y: float):
        self.inner_side = inner_side
        self.cup_points = cup_points
        self.inner_hex_corners = inner_hex_corners
        self.cup_max_x = cup_max_x
        self.cup_max_y = cup_max_y




def calc_hex(
        side: float = 150,
        cup: float = 40,
        edge: float = 30,
        space: float = 30
):
    sqrt3Div2 = math.sqrt(3) / 2
    cupRad = cup / 2
    cupPlusSpace = cup + space
    cupPlusSpaceDiv2 = cupPlusSpace / 2
    inner_side = side - edge
    inner_sideDiv2 = inner_side / 2
    inner_sideSqrt3Div2 = inner_side * sqrt3Div2
    edgespace = (space + cupRad) / sqrt3Div2 - cupRad
    cupLineHalfLength = inner_side - edgespace - cupRad
    nCups = int(cupLineHalfLength / (cup + space))
    cupLineHalfLengthCropped = int(nCups * (cup + space))

    inner_hex_corners = [
        [inner_side, 0],
        [inner_sideDiv2, inner_sideSqrt3Div2],
        [-inner_sideDiv2, inner_sideSqrt3Div2],
        [-inner_side, 0],
        [-inner_sideDiv2, -inner_sideSqrt3Div2],
        [inner_sideDiv2, -inner_sideSqrt3Div2]
    ]

    # cups

    def treatLine(line: int) -> [(float, float)]:
        cupVerticalOffset = sqrt3Div2 * cupPlusSpace * line
        halfCupLine = cupLineHalfLengthCropped - int(cupPlusSpaceDiv2) * line

        def treatEachCup(x: int) -> [(float, float)]:
            if 0 == line:
                return [[float(x), 0]]
            else:
                return [[float(x), cupVerticalOffset], [float(x), -cupVerticalOffset]]

        return flatten(map(treatEachCup, range(-halfCupLine, halfCupLine + 1, int(cupPlusSpace))))

    cup_points: [(float, float)] = flatten(map(treatLine, range(nCups + 1)))
    return HexCalc(inner_side, cup_points, inner_hex_corners, cupLineHalfLengthCropped,
                   sqrt3Div2 * cupPlusSpace * nCups)


def cups_n(fi: HexFloatInput) -> float:
    sc = shouldercalc.calc_shoulder(fi)
    hc = calc_hex(fi.side, 2 * fi.cup_rad, sc.edge, fi.space)
    cn = len(hc.cup_points)
    return cn
