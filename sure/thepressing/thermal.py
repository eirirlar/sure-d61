import numpy as np
from normalfloatinput import NormalFloatInput

thermal_weights = [5, 4, 3, 2, 1]


# This is just a big hack. We look at what input params seem relevant, weight them, average them by weights and return that number.
def calc_thermal(fi: NormalFloatInput, area_normalized: float) -> float:
    input = [
        area_normalized,
        1. - fi.cup_depth,
        fi.alu_thick,
        fi.cup_angle,
        1. - fi.shoulder_angle
    ]
    t = np.average(input, weights=thermal_weights)
    return t