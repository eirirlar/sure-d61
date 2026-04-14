from typing import List

from floatinput import *
from fluidio import FluidInput, from_values
from util import param_names
from validation import *

# these may be overridable params in the future
side_default = 1150.  # an alu sheet comes in max 2000 mm width. 2000/(2*sin(pi/3)) = 2000/sqrt(3) = 1154. A few millis disappears in the pressing.
shoulder_width_default = 12.
shoulder_depth_default = 2.5
float_lip_default = 24.
gripper_default = 0.  # gripper is the part of the press tool that holds the sheet in place

# shoulder_angle is the angle from the top of the float down to the shoulder, and down from the shoulder to the float lip. High angle (-10) = flatter
shoulder_angle_default = -75.
shoulder_angle_min = -90.  # straight down
shoulder_angle_max = -10.  # almost flat


class HexFloatInput(FloatInput):

    def __init__(self,
                 # user params
                 cup_rad: float = cup_rad_default,
                 cup_lip: float = cup_lip_default,
                 cup_depth: float = cup_depth_default,
                 cup_angle: float = cup_angle_default,
                 cup_y_to_x: float = cup_y_to_x_default,
                 cup_tip: float = cup_tip_default,
                 space: float = space_default,
                 alu_thick: float = alu_thick_default,
                 pressure: float = pressure_default,
                 # hardcoded params
                 shoulder_angle: float = shoulder_angle_default,
                 side: float = side_default,
                 shoulder_depth: float = shoulder_depth_default,
                 shoulder_width: float = shoulder_width_default,
                 float_lip: float = float_lip_default,
                 gripper: float = gripper_default
                 ):
        super().__init__(
            cup_rad,
            cup_lip,
            cup_depth,
            cup_angle,
            cup_y_to_x,
            cup_tip,
            space,
            alu_thick,
            pressure
        )
        self.shoulder_angle = shoulder_angle
        self.side = side
        self.shoulder_depth = shoulder_depth
        self.shoulder_width = shoulder_width
        self.float_lip = float_lip
        self.gripper = gripper

    def validate(self):
        super_validation_results = super().validate()
        self_validation_results = empty_validation_results(HexFloatInput)

        if self.side < self.cup_rad:
            e = 'side must be greater than cup_rad'
            self_validation_results['cup_rad'].append(e)
            self_validation_results['side'].append(e)

        if self.shoulder_angle < shoulder_angle_min:
            self_validation_results['shoulder_angle'].append(f'must be at least {shoulder_angle_min}')
        if shoulder_angle_max < self.shoulder_angle:
            self_validation_results['shoulder_angle'].append(f'must be at most {shoulder_angle_max}')

        if self.shoulder_depth < 2 * self.alu_thick:
            e = 'shoulder_depth must be greater than 2 * alu_thick'
            self_validation_results['shoulder_depth'].append(e)
            self_validation_results['alu_thick'].append(e)

        if self.space / 2 < self.gripper:
            e = 'gripper must be less than space / 2'
            self_validation_results['gripper'].append(e)

        validation_results = {**super_validation_results, **self_validation_results}

        # For keys that appear in both dictionaries, combine their lists
        for key in super_validation_results:
            if key in self_validation_results:
                validation_results[key] = super_validation_results[key] + self_validation_results[key]

        return validation_results


def validator_fluidio_vals(vs: List[float]) -> bool:
    validations = from_fluid_input(from_values(vs).input).validate()
    return valid(validations)


def from_fluid_input(fio: FluidInput):
    return HexFloatInput(**fio.__dict__)


params: List[str] = param_names(HexFloatInput)
