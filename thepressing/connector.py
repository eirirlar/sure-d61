import numpy as np

import cupcalc
from cupcalc import CupCalc
from hexfloatinput import HexFloatInput
from normalfloatinput import normalize_val
from normalfloatoutput import weight_div_volume_min, weight_div_volume_max, cup_vol_max, cup_vol_min

connector_stress_weights = [10, 4, 1]


def calc_connector_stress(fi: HexFloatInput, shoulder_angle_normalized: float, weight: float, volume: float,
                          cc:CupCalc) -> float:
    weight_div_volume = weight / volume
    weight_div_volume_fitness = 1. - normalize_val(weight_div_volume, weight_div_volume_min, weight_div_volume_max)
    shoulder_angle_fitness = shoulder_angle_normalized
    cup_vol = cupcalc.calc_vol(fi.cup_depth, cc)
    cup_vol_normalized = normalize_val(cup_vol, cup_vol_min, cup_vol_max)
    cup_vol_fitness = 1. - cup_vol_normalized

    connector_stress_fitness = np.average([weight_div_volume_fitness, shoulder_angle_fitness, cup_vol_fitness],
                                          weights=connector_stress_weights)
    # todo corner roundedness
    return connector_stress_fitness
