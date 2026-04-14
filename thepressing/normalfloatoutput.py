import cupcalc
import floatinput
import hexcalc
import hexfloatinput
import volume
import weight
from areacalc import calc_contact_area_init, calc_area_init
from hexfloatinput import HexFloatInput
from floatoutput import FloatOutput
from normalfloatinput import (denormalize_val, normalize_val, is_normalized)

strict = True

contact_area_min = calc_contact_area_init(
    HexFloatInput(floatinput.cup_rad_max, floatinput.cup_lip_max, floatinput.cup_depth_max,
                  floatinput.cup_angle_default, floatinput.cup_y_to_x_max, floatinput.cup_tip_min, floatinput.space_min,
                  floatinput.alu_thick_default,
                  hexfloatinput.shoulder_angle_max))

contact_area_max = calc_contact_area_init(
    HexFloatInput(floatinput.space_max / 2, floatinput.cup_lip_min, floatinput.cup_depth_min,
                  floatinput.cup_angle_default, floatinput.cup_y_to_x_min, floatinput.cup_tip_max, floatinput.space_max,
                  floatinput.alu_thick_default,
                  hexfloatinput.shoulder_angle_min)) * 1.05
# print('contact_area min max ', contact_area_min, contact_area_max)

area_min = calc_area_init(HexFloatInput(floatinput.cup_rad_max, floatinput.cup_lip_max, floatinput.cup_depth_max,
                                        floatinput.cup_angle_default, floatinput.cup_y_to_x_max,
                                        floatinput.cup_tip_default,
                                        floatinput.space_min,
                                        floatinput.alu_thick_default,
                                        hexfloatinput.shoulder_angle_max))

area_max = calc_area_init(HexFloatInput(floatinput.space_max / 2, floatinput.cup_lip_min, floatinput.cup_depth_min,
                                        floatinput.cup_angle_default, floatinput.cup_y_to_x_min,
                                        floatinput.cup_tip_default, floatinput.space_max,
                                        floatinput.alu_thick_default,
                                        hexfloatinput.shoulder_angle_min)) * 1.1
# print('area min max ', area_min, area_max)

weight_min = weight.calc_weight_init(
    HexFloatInput(floatinput.cup_rad_min, floatinput.cup_lip_min, cup_tip=floatinput.cup_tip_min,
                  space=floatinput.space_min,
                  alu_thick=floatinput.alu_thick_min)) * 0.9

weight_max = weight.calc_weight_init(
    HexFloatInput(floatinput.cup_rad_max, floatinput.cup_lip_max, cup_tip=floatinput.cup_tip_max,
                  space=floatinput.space_max,
                  alu_thick=floatinput.alu_thick_max)) * 1.05
# print('weight min max ', weight_min, weight_max)

volume_min = volume.calc_volume_init(
    HexFloatInput(floatinput.cup_rad_max, floatinput.cup_lip_max, floatinput.cup_depth_min,
                  floatinput.cup_angle_min, floatinput.cup_y_to_x_max, floatinput.cup_tip_default, floatinput.space_min,
                  floatinput.alu_thick_max,
                  hexfloatinput.shoulder_angle_max)) * 0.75

volume_max = volume.calc_volume_init(
    HexFloatInput(min(floatinput.cup_depth_max / 2, floatinput.space_max / 2), floatinput.cup_lip_min,
                  floatinput.cup_depth_max, floatinput.cup_angle_max, floatinput.cup_y_to_x_min,
                  floatinput.cup_tip_default, floatinput.space_max,
                  floatinput.alu_thick_min, hexfloatinput.shoulder_angle_min))
# print('volume min max ', volume_min, volume_max)

thermal_conductivity_min = 0
thermal_conductivity_max = 1

cup_vol_min = cupcalc.calc_vol_init(
    HexFloatInput(floatinput.cup_rad_min, floatinput.cup_lip_min, floatinput.cup_depth_min,
                  floatinput.cup_angle_max, floatinput.cup_y_to_x_min, floatinput.cup_tip_min,
                  floatinput.space_min,
                  floatinput.alu_thick_max,
                  hexfloatinput.shoulder_angle_max))
cup_vol_max = cupcalc.calc_vol_init(
    HexFloatInput(floatinput.cup_rad_max, floatinput.cup_lip_max,
                  floatinput.cup_depth_max, floatinput.cup_angle_min, floatinput.cup_y_to_x_max, floatinput.cup_tip_max,
                  floatinput.space_max,
                  floatinput.alu_thick_min, hexfloatinput.shoulder_angle_min))
# print('cup_vol min max ', cup_vol_min, cup_vol_max)

connector_stress_min = 0
connector_stress_max = 1

weight_div_volume_min = weight_min / volume_max
weight_div_volume_max = weight_max / volume_min

# print('weight_div_volume min max ', weight_div_volume_min, weight_div_volume_max)

cups_n_min = int(max(7.,
                     hexcalc.cups_n(
                         HexFloatInput(floatinput.cup_rad_max, floatinput.cup_lip_default, floatinput.cup_depth_max,
                                       floatinput.cup_angle_default, floatinput.cup_y_to_x_default,
                                       floatinput.cup_tip_default,
                                       floatinput.space_max, floatinput.alu_thick_default,
                                       hexfloatinput.shoulder_angle_max))))
cups_n_max = hexcalc.cups_n(HexFloatInput(floatinput.cup_rad_min, floatinput.cup_lip_default, floatinput.cup_depth_min,
                                          floatinput.cup_angle_default, floatinput.cup_y_to_x_default,
                                          floatinput.cup_tip_default,
                                          floatinput.space_min,
                                          floatinput.alu_thick_default, hexfloatinput.shoulder_angle_min))

# print('cups_n min max ', cups_n_min, cups_n_max)

structural_integrity_min = 0
structural_integrity_max = 1

press_fault_min = 0
press_fault_max = 1


class NormalFloatOutput:

    # takes floats from 0 to 1 and denormalizes them to be within the min max range for each.
    def __init__(self,
                 area: float,
                 weight: float,
                 volume: float,
                 thermal_conductivity: float,
                 connector_stress: float,
                 structural_integrity: float,
                 press_fault: float
                 ):
        params = list(locals().values())[1::]
        if strict and not all(map(is_normalized, params)):
            raise Exception('Some params were not normalized: ', params)
        self.area = area
        self.weight = weight
        self.volume = volume
        self.thermal_conductivity = thermal_conductivity
        self.connector_stress = connector_stress
        self.structural_integrity = structural_integrity
        self.press_fault = press_fault

    def denorm(self):
        return FloatOutput(
            denormalize_val(self.area, area_min, area_max),
            denormalize_val(self.weight, weight_min, weight_max),
            denormalize_val(self.volume, volume_min, volume_max),
            denormalize_val(self.thermal_conductivity, thermal_conductivity_min, thermal_conductivity_max),
            denormalize_val(self.structural_integrity, structural_integrity_min, structural_integrity_max),
            denormalize_val(self.connector_stress, connector_stress_min, connector_stress_max)
        )


def create(fo: FloatOutput) -> NormalFloatOutput:
    return NormalFloatOutput(
        normalize_val(fo.area, area_min, area_max),
        normalize_val(fo.weight, weight_min, weight_max),
        normalize_val(fo.volume, volume_min, volume_max),
        normalize_val(fo.thermal_conductivity, thermal_conductivity_min, thermal_conductivity_max),
        normalize_val(fo.connector_stress, connector_stress_min, connector_stress_max),
        normalize_val(fo.structural_integrity, structural_integrity_min, structural_integrity_max),
        normalize_val(fo.press_fault, press_fault_min, press_fault_max)
    )
