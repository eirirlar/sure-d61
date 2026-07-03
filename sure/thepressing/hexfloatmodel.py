from typing import Optional, Tuple, Dict

import fluidio
import hexfloatinput
from floatdata import FloatData
from hexfloatinput import HexFloatInput
from shouldercalc import ShoulderCalc, calc_shoulder
import hexcalc
from hexcalc import HexCalc
from cupcalc import calc_cup, CupCalc
import normalfloatinput
from normalfloatinput import NormalFloatInput
from floatoutput import FloatOutput
from validation import valid, ValidationError
from areacalc import calc_contact_area, calc_area
from weight import calc_weight
from volume import calc_volume, calc_inner_vol_plus_cups
from thermal import calc_thermal
import normalfloatoutput
from connector import calc_connector_stress
from structural import calc_structural_integrity
from press import calc_press_fault


class HexFloatModel:
    def __init__(self,
                 float_input: HexFloatInput,
                 shoulder_calc: ShoulderCalc,
                 hex_calc: HexCalc,
                 cup_calc: CupCalc
                 ):
        validation_results = float_input.validate()
        if not valid(validation_results):
            raise ValidationError(validation_results)
        self.float_input = float_input
        self.shoulder_calc = shoulder_calc
        self.hex_calc = hex_calc
        self.cup_calc = cup_calc

    # returns contact area on top in m2, area on top in m2, weight in kg and volume in dm3 for two float halves.
    # The top half is assumed to have the cups covered, thus the volume of the cups is counted for the top.
    def calc_float_data(self) -> FloatData:
        contact = 1e-6 * calc_contact_area(self.hex_calc.inner_side, self.hex_calc.cup_max_x,
                                           len(self.hex_calc.cup_points),
                                           self.cup_calc.lip_x.circle_r, self.cup_calc.lip_y.circle_r)
        area = 1e-6 * calc_area(self.float_input.side, self.hex_calc.cup_max_x)
        w = calc_weight(self.float_input.side, self.hex_calc.cup_max_x, self.float_input.alu_thick)
        weight = 1e-3 * 2. * w
        volume_with_cups = calc_inner_vol_plus_cups(self.hex_calc.inner_side, self.float_input.cup_depth,
                                                    self.float_input, self.hex_calc, self.shoulder_calc)
        volume_without_cups = calc_volume(self.float_input.cup_depth, self.float_input, self.hex_calc,
                                          self.shoulder_calc,
                                          self.cup_calc)
        volume = 1e-6 * (volume_with_cups + volume_without_cups)
        return FloatData(contact, area, weight, volume)

    def calc_fitness(self, nfi: Optional[NormalFloatInput] = None) -> FloatOutput:
        if nfi is None:
            nfi = normalfloatinput.normalize(self.float_input)

        contact_area = calc_contact_area(self.hex_calc.inner_side, self.hex_calc.cup_max_x,
                                         len(self.hex_calc.cup_points),
                                         self.cup_calc.lip_x.circle_r, self.cup_calc.lip_y.circle_r)
        area = calc_area(self.float_input.side, self.hex_calc.cup_max_x)
        weight = calc_weight(self.float_input.side, self.hex_calc.cup_max_x, self.float_input.alu_thick)
        volume = calc_volume(self.float_input.cup_depth, self.float_input, self.hex_calc, self.shoulder_calc,
                             self.cup_calc)
        thermal_conductivity = calc_thermal(nfi,
                                            normalfloatinput.normalize_val(contact_area,
                                                                           normalfloatoutput.contact_area_min,
                                                                           normalfloatoutput.contact_area_max))
        connector_stress = calc_connector_stress(self.float_input, nfi.shoulder_angle, weight, volume, self.cup_calc)
        structural_integrity = calc_structural_integrity(self.float_input, self.shoulder_calc, self.hex_calc)
        press_fault = calc_press_fault(self.float_input, self.cup_calc)
        return FloatOutput(area, weight, volume, thermal_conductivity, connector_stress, structural_integrity,
                           press_fault)


def create(float_input: HexFloatInput = HexFloatInput()) -> HexFloatModel:
    validation_results = float_input.validate()
    if not valid(validation_results):
        raise ValidationError(float_input.__dict__, validation_results)
    shoulder_calc = calc_shoulder(float_input)
    hex_calc = hexcalc.calc_hex(float_input.side, 2 * float_input.cup_rad, shoulder_calc.edge,
                                float_input.space)
    cup_calc = calc_cup(float_input)
    return HexFloatModel(float_input, shoulder_calc, hex_calc, cup_calc)


if __name__ == '__main__':
    fi = hexfloatinput.from_fluid_input(fluidio.from_values(
        [4127874840.0,
         28.691915445193025,
         1.0,
         16.80575674442374,
         35.217000658372385,
         0.9914753140404857,
         10.91931836767297,
         0.8,
         8.337377548217773,
         1.0,
         0.9183202856333345,
         1.0039464109383192
         ]).input)
    fm = create(fi)
    print(fm.calc_float_data().__dict__)
    # fi = FloatInput(**{'cup_rad': 27.406811955061436, 'cup_lip': 1.0, 'cup_depth': 12.872106784853099,
    #                   'cup_angle': 65.53056108241205, 'cup_y_to_x': 0.7236940512269631, 'space': 1.6554433113257974,
    #                   'alu_thick': 0.8, 'shoulder_angle': -75.0, 'pressure': 6.465301758194844, 'side': 1150.0,
    #                   'shoulder_depth': 2.5, 'shoulder_width': 12.0, 'float_lip': 24.0, 'gripper': 0.0})
    # fm = create(fi)
