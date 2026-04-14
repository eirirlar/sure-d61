from math import *

import numpy as np

from hexfloatinput import HexFloatInput
from hexcalc import HexCalc
from normalfloatoutput import cups_n_max
from shouldercalc import ShoulderCalc

#distribution of cups, number of cups, shape of cups
structural_integrity_weights = [5, 3, 1]


def calc_structural_integrity(fi: HexFloatInput, sc: ShoulderCalc, hc: HexCalc) -> float:
    corner_dist = fi.side - sc.edge - hc.cup_max_x
    corner_rad = corner_dist * sqrt(3) / 2
    corner_rad_space = corner_rad - fi.cup_rad
    cup_distribution_fitness = fi.space / corner_rad_space
    cups_n = len(hc.cup_points)
    cups_n_fitness = cups_n / cups_n_max
    structural_integrity_fitness = np.average([cup_distribution_fitness, cups_n_fitness, fi.cup_y_to_x],
                                              weights=structural_integrity_weights)
    return structural_integrity_fitness
