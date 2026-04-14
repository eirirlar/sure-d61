from typing import List

from floatinput import *
from fluidio import FluidInput
from util import param_names
from validation import *

# these may be overridable params in the future
width_default = 1303.
length_default = 2465.


class RectFloatInput(FloatInput):

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
                 width: float = width_default,
                 length: float = length_default
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
        self.width = width
        self.length = length

    def validate(self):
        super_validation_results = super().validate()
        self_validation_results = empty_validation_results(RectFloatInput)

        if self.width < self.cup_rad:
            e = 'width must be greater than cup_rad'
            self_validation_results['cup_rad'].append(e)
            self_validation_results['width'].append(e)
        if self.length < self.cup_rad:
            e = 'length must be greater than cup_rad'
            self_validation_results['cup_rad'].append(e)
            self_validation_results['length'].append(e)
        if self.length < self.width:
            e = 'length must be greater than width'
            self_validation_results['width'].append(e)
            self_validation_results['length'].append(e)

        validation_results = {**super_validation_results, **self_validation_results}

        # For keys that appear in both dictionaries, combine their lists
        for key in super_validation_results:
            if key in self_validation_results:
                validation_results[key] = super_validation_results[key] + self_validation_results[key]

        return validation_results


def from_fluid_input(fio: FluidInput):
    return RectFloatInput(**fio.__dict__)


params: List[str] = param_names(RectFloatInput)
