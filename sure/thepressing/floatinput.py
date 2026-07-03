from typing import List

from util import param_names
from validation import *

# cup_rad (mm) is the radius of a circle that fits one cup. Note that the cup itself may be elliptical within this circle
cup_rad_default = 25.
cup_rad_min = 10.
cup_rad_max = 40.  # cup_rad_max depends on side and space

# cup_lip (mm) is the radius of the fillet that rounds of each cup. The actual length in cup radial direction depends on cup_rad, cup_depth and cup_y_to_x
cup_lip_default = 1.
cup_lip_min = 1.
# cup_lip_min = 0.5
cup_lip_max = 1.
# cup_lip_max = 4.

# cup_depth (mm) is the depth of each cup
cup_depth_default = 20.
cup_depth_min = 5.
cup_depth_max = 40.

# cup_angle is the steepness of the curve inside the cup. High angle = more flat. Low angle = quickly steepens.
cup_angle_default = 80.
cup_angle_min = 10.
cup_angle_max = 85.

# cup_y_to_x denotes the ratio between y and x of an ellipse describing the cup. Note that the cup will be a circle if cup_y_to_x = 1. This ratio is expected to relate to the stretchability of the aluminium in y vs x direction
cup_y_to_x_default = 0.85
cup_y_to_x_min = 0.7
cup_y_to_x_max = 1.  # no need to go higher as this is achievable by rotating the sheet 90 deg

# cup_tip (mm) is the radius of a circle on the tip of the cup, making it flat. It must be less than cup_rad.
cup_tip_default = 25.
cup_tip_to_rad_min = 0.2
cup_tip_to_rad_max = 0.8
cup_tip_min = cup_rad_min * cup_tip_to_rad_min
cup_tip_max = cup_rad_max * cup_tip_to_rad_max  # cup_tip_max depends on cup_rad_max

# space is the spacing between cups, and the space outside the cups along the shoulder of the float. It is the area that the cups will draw aluminum from when being stretched
space_default = 10.  # probably need some space for gripper ring
space_min = 0.
space_max = 40.

# alu_thick is the thickness of the aluminum sheet. The actual thickness will be determined during the FEM simulation stage, this is only indicative
alu_thick_default = 0.8  # suggestion from Techniche Universitet Munich
alu_thick_min = 0.8
# alu_thick_min = 0.5
alu_thick_max = 0.8  # dictated by shoulder_depth
# alu_thick_max = 1.  # dictated by shoulder_depth

# pressure is the fluid pressure applied in the cup simulations
pressure_default = 6.
pressure_min = 4.
pressure_max = 12.

n_user_params = 9


class FloatInput:

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
                 pressure: float = pressure_default
                 ):
        self.cup_rad = cup_rad
        self.cup_lip = cup_lip
        self.cup_depth = cup_depth
        self.cup_angle = cup_angle
        self.cup_y_to_x = cup_y_to_x
        self.cup_tip = cup_tip
        self.space = space
        self.alu_thick = alu_thick
        self.pressure = pressure

    def validate(self):
        validation_results = empty_validation_results(FloatInput)
        if self.cup_rad < cup_rad_min:
            validation_results['cup_rad'].append(f'must be at least {cup_rad_min}')
        if cup_rad_max < self.cup_rad:
            validation_results['cup_rad'].append('must be at most {cup_rad_max}')

        if self.cup_lip < cup_lip_min:
            validation_results['cup_lip'].append(f'must be at least {cup_lip_min}')
        if cup_lip_max < self.cup_lip:
            validation_results['cup_lip'].append(f'must be at most {cup_lip_max}')

        if self.cup_depth < cup_depth_min:
            validation_results['cup_depth'].append(f'must be at least {cup_depth_min}')
        if cup_depth_max < self.cup_depth:
            validation_results['cup_depth'].append(f'must be at most {cup_depth_max}')

        if self.cup_angle < cup_angle_min:
            validation_results['cup_angle'].append(f'must be at least {cup_angle_min}')
        if cup_angle_max < self.cup_angle:
            validation_results['cup_angle'].append(f'must be at most {cup_angle_max}')

        if self.cup_y_to_x < cup_y_to_x_min:
            validation_results['cup_y_to_x'].append(f'must be at least {cup_y_to_x_min}')
        if cup_y_to_x_max < self.cup_y_to_x:
            validation_results['cup_y_to_x'].append(f'must be at most {cup_y_to_x_max}')

        if self.cup_tip < cup_tip_min:
            validation_results['cup_tip'].append(f'must be at least {cup_tip_min}')
        if cup_tip_max < self.cup_tip:
            validation_results['cup_tip'].append(f'must be at most {cup_tip_max}')
        if self.cup_rad * cup_tip_to_rad_max < self.cup_tip:
            validation_results['cup_tip'].append(f'must be at most {self.cup_rad} * {cup_tip_to_rad_max}')

        if self.space < space_min:
            validation_results['space'].append(f'must be at least {space_min}')
        if space_max < self.space:
            validation_results['space'].append(f'must be at most {space_max}')

        if self.alu_thick < alu_thick_min:
            validation_results['alu_thick'].append(f'must be at least {alu_thick_min}')
        if alu_thick_max < self.alu_thick:
            validation_results['alu_thick'].append(f'must be at most {alu_thick_max}')

        if self.pressure < pressure_min:
            validation_results['pressure'].append(f'must be at least {pressure_min}')
        if pressure_max < self.pressure:
            validation_results['pressure'].append(f'must be at most {pressure_max}')

        if self.cup_rad < self.cup_depth:
            e = 'cup_rad must be greater than cup_depth'
            validation_results['cup_depth'].append(e)
            validation_results['cup_rad'].append(e)

        if self.cup_rad < self.cup_lip:
            e = 'cup_rad must be greater than cup_lip'
            validation_results['cup_lip'].append(e)
            validation_results['cup_rad'].append(e)

        if self.cup_rad < self.space:
            e = 'space must be less than cup_rad'
            validation_results['cup_rad'].append(e)
            validation_results['space'].append(e)

        return validation_results


params: List[str] = param_names(FloatInput)
