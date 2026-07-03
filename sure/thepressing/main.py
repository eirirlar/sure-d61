import hexfloatinput

FREECAD_BIN_PATH = 'C:\\dev\\freecad\\bin'
FREECAD_BIN_LIB_SITEPACKAGES_PATH = 'C:\\dev\\freecad\\bin\\Lib\\site-packages'
import sys

sys.path.append(FREECAD_BIN_PATH)
sys.path.append(FREECAD_BIN_LIB_SITEPACKAGES_PATH)

import FreeCAD
import Draft
import hexfreecadmodel
from hexfloatinput import HexFloatInput
from validation import valid
import floatinput

import argparse

def main():
    parser = argparse.ArgumentParser(description='Sunlit Sea float generator', argument_default=argparse.SUPPRESS)
    parser.add_argument('-cr', '--cup_rad', type=float, required=False, help=f'Min {floatinput.cup_rad_min}, max {floatinput.cup_rad_max}, default {floatinput.cup_rad_default}. cup_rad (mm) is the radius of a circle that fits one cup. Note that the cup itself may be elliptical within this circle')
    parser.add_argument('-cl', '--cup_lip', type=float, required=False, help=f'Min {floatinput.cup_lip_min}, max {floatinput.cup_lip_max}, default {floatinput.cup_lip_default}. cup_lip (mm) is the radius of the fillet that rounds of each cup. The actual length in cup radial direction depends on cup_rad, cup_depth and cup_y_to_x')
    parser.add_argument('-cd', '--cup_depth', type=float, required=False, help=f'Min {floatinput.cup_depth_min}, max {floatinput.cup_depth_max}, default {floatinput.cup_depth_default}. cup_depth (mm) is the depth of each cup')
    parser.add_argument('-ca', '--cup_angle', type=float, required=False, help=f'Min {floatinput.cup_angle_min}, max {floatinput.cup_angle_max}, default {floatinput.cup_angle_default}. cup_angle (degrees) is the steepness of the curve inside the cup. 90 degrees means the top of the cup, just before the fillet, is horizontal. 0 degrees means there is no cup just a flat space')
    parser.add_argument('-cyx', '--cup_y_to_x', type=float, required=False, help=f'Min {floatinput.cup_y_to_x_min}, max {floatinput.cup_y_to_x_max}, default {floatinput.cup_y_to_x_default}. cup_y_to_x (ratio, mm/mm) denotes the ratio between y and x of an ellipse describing the cup. Note that the cup will be a circle if cup_y_to_x = 1. This ratio is expected to relate to the stretchability of the aluminium in y vs x direction')
    parser.add_argument('-ct', '--cup_tip', type=float, required=False, help=f'Min {floatinput.cup_tip_min}, max {floatinput.cup_tip_max}, default {floatinput.cup_tip_default}. cup_tip (mm) denotes the radius of the tip of the cup. Must be less than 0.8*cup_rad')
    parser.add_argument('-s', '--space', type=float, required=False, help=f'Min {floatinput.space_min}, max {floatinput.space_max}, default {floatinput.space_default}. space (mm) is the spacing between cups, and the space outside the cups along the shoulder of the float. It is the area that the cups will draw aluminum from when being stretched')
    parser.add_argument('-at', '--alu_thick', type=float, required=False, help=f'Min {floatinput.alu_thick_min}, max {floatinput.alu_thick_max}, default {floatinput.alu_thick_default}. alu_thick (mm) is the thickness of the aluminum sheet. The actual thickness will be determined during the FEM simulation stage, this is only indicative')
    parser.add_argument('-sa', '--shoulder_angle', type=float, required=False, help=f'Min {hexfloatinput.shoulder_angle_min}, max {hexfloatinput.shoulder_angle_max}, default {hexfloatinput.shoulder_angle_default}. shoulder_angle (degrees) is the angle from the top of the float down to the shoulder, and down from the shoulder to the float lip')
    fi = HexFloatInput(**vars(parser.parse_args()))
    validation_results = fi.validate()
    if not valid(validation_results):
        print('Validation failed with resuts:')
        print(validation_results)
    else:
        print(fi.__dict__)
        fm = hexfreecadmodel.create(fi)
        fm.generate(True,False,False,False)

if __name__ == '__main__':
    main()
