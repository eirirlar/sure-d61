from hexfloatinput import HexFloatInput
from math import *

# less means you can make it thinner without breaking
max_thinning_x = 0.5
max_thinning_y = 0.5

steep_default = 50


def press_fault_prob(thin: float, cut: float, steep: float = steep_default) -> float:
    return 1 / (1 + exp(-steep * (thin - cut)))


def calc_press_fault(fi: HexFloatInput, cc) -> float:
    thin_x = 1 - cc.lip_x.circle_r / cc.cup_lip_arc_x
    thin_y = 1 - cc.lip_y.circle_r * fi.cup_y_to_x / cc.cup_lip_arc_x
    pf_x = 1 - press_fault_prob(thin_x, max_thinning_x)
    pf_y = 1 - press_fault_prob(thin_y, max_thinning_y)
    pf = (pf_x + pf_y) / 2
    return pf
