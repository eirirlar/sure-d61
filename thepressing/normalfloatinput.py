from typing import Dict, List

import floatinput
import fluidio
import hexfloatinput
from fluidio import FluidInput
from hexfloatinput import HexFloatInput
from util import param_names
from validation import valid


def is_normalized(value: float) -> bool:
    return 0. <= value and value <= 1.


def normalize_val(value: float, min: float, max: float) -> float:
    max_min = max - min
    if 0 == max_min:
        return min
    else:
        return (value - min) / max_min


def denormalize_val(value: float, min: float, max: float) -> float:
    return value * (max - min) + min


class NormalFloatInput:

    # takes floats from 0 to 1 and denormalizes them to be within the min max range for each.
    def __init__(self,
                 cup_rad: float = normalize_val(floatinput.cup_rad_default, floatinput.cup_rad_min,
                                                floatinput.cup_rad_max),
                 cup_lip: float = normalize_val(floatinput.cup_lip_default, floatinput.cup_lip_min,
                                                floatinput.cup_lip_max),
                 cup_depth: float = normalize_val(floatinput.cup_depth_default, floatinput.cup_depth_min,
                                                  floatinput.cup_depth_max),
                 cup_angle: float = normalize_val(floatinput.cup_angle_default, floatinput.cup_angle_min,
                                                  floatinput.cup_angle_max),
                 cup_y_to_x: float = normalize_val(floatinput.cup_y_to_x_default, floatinput.cup_y_to_x_min,
                                                   floatinput.cup_y_to_x_max),
                 cup_tip: float = normalize_val(floatinput.cup_tip_default, floatinput.cup_tip_min,
                                                   floatinput.cup_tip_max),
                 space: float = normalize_val(floatinput.space_default, floatinput.space_min, floatinput.space_max),
                 alu_thick: float = normalize_val(floatinput.alu_thick_default, floatinput.alu_thick_min,
                                                  floatinput.alu_thick_max),
                 pressure: float = normalize_val(floatinput.pressure_default, floatinput.pressure_min,
                                                 floatinput.pressure_max),
                 shoulder_angle: float = normalize_val(hexfloatinput.shoulder_angle_default,
                                                       hexfloatinput.shoulder_angle_min,
                                                       hexfloatinput.shoulder_angle_max)
                 ):
        self.cup_rad = cup_rad
        # TODO fix when reverted
        # self.cup_lip = cup_lip
        self.cup_lip = 1.
        self.cup_depth = cup_depth
        self.cup_angle = cup_angle
        self.cup_y_to_x = cup_y_to_x
        self.cup_tip = cup_tip
        self.space = space
        # TODO fix when reverted
        # self.alu_thick = alu_thick
        self.alu_thick = 1.
        self.pressure = pressure
        self.shoulder_angle = shoulder_angle

    def denorm(self) -> HexFloatInput:
        return denormalize(self)


def from_fluid_input(fio: FluidInput):
    return NormalFloatInput(**fio.__dict__)


def normalize(fi: HexFloatInput) -> NormalFloatInput:
    return NormalFloatInput(**dict(map(lambda kv: (kv[0], kv[1](fi.__dict__[kv[0]])), normalizers.items())))


def denormalize(nfi: NormalFloatInput) -> HexFloatInput:
    return HexFloatInput(**dict(map(lambda kv: (kv[0], kv[1](nfi.__dict__[kv[0]])), denormalizers.items())))


def normalize_fluid_input(fioi: FluidInput) -> FluidInput:
    return fluidio.from_float(normalize(hexfloatinput.from_fluid_input(fioi)).__dict__)


def denormalize_fluid_input(fioi: FluidInput) -> FluidInput:
    return fluidio.from_float(denormalize(from_fluid_input(fioi)).__dict__)

def validator_fluidio_vals(vs: List[float]) -> bool:
    validations = from_fluid_input(fluidio.from_values(vs).input).denorm().validate()
    return valid(validations)

normalizers = {
    'cup_rad': lambda v: normalize_val(v, floatinput.cup_rad_min, floatinput.cup_rad_max),
    'cup_lip': lambda v: normalize_val(v, floatinput.cup_lip_min, floatinput.cup_lip_max),
    'cup_depth': lambda v: normalize_val(v, floatinput.cup_depth_min, floatinput.cup_depth_max),
    'cup_angle': lambda v: normalize_val(v, floatinput.cup_angle_min, floatinput.cup_angle_max),
    'cup_y_to_x': lambda v: normalize_val(v, floatinput.cup_y_to_x_min, floatinput.cup_y_to_x_max),
    'space': lambda v: normalize_val(v, floatinput.space_min, floatinput.space_max),
    'alu_thick': lambda v: normalize_val(v, floatinput.alu_thick_min, floatinput.alu_thick_max),
    'pressure': lambda v: normalize_val(v, floatinput.pressure_min, floatinput.pressure_max),
    'shoulder_angle': lambda v: normalize_val(v, hexfloatinput.shoulder_angle_min, hexfloatinput.shoulder_angle_max)
}

denormalizers = {
    'cup_rad': lambda v: denormalize_val(v, floatinput.cup_rad_min, floatinput.cup_rad_max),
    'cup_lip': lambda v: denormalize_val(v, floatinput.cup_lip_min, floatinput.cup_lip_max),
    'cup_depth': lambda v: denormalize_val(v, floatinput.cup_depth_min, floatinput.cup_depth_max),
    'cup_angle': lambda v: denormalize_val(v, floatinput.cup_angle_min, floatinput.cup_angle_max),
    'cup_y_to_x': lambda v: denormalize_val(v, floatinput.cup_y_to_x_min, floatinput.cup_y_to_x_max),
    'cup_tip': lambda v: denormalize_val(v, floatinput.cup_tip_min, floatinput.cup_tip_max),
    'space': lambda v: denormalize_val(v, floatinput.space_min, floatinput.space_max),
    'alu_thick': lambda v: denormalize_val(v, floatinput.alu_thick_min, floatinput.alu_thick_max),
    'pressure': lambda v: denormalize_val(v, floatinput.pressure_min, floatinput.pressure_max),
    'shoulder_angle': lambda v: denormalize_val(v, hexfloatinput.shoulder_angle_min, hexfloatinput.shoulder_angle_max)
}

params = param_names(NormalFloatInput)
params_to_index: Dict[str, int] = dict((p, i) for i, p in enumerate(params))
index_to_params: Dict[int, str] = dict((i, p) for i, p in enumerate(params))
n_params = len(params)
