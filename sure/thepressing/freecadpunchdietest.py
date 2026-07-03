import normalfloatoutput
FREECAD_BIN_PATH = 'C:\\dev\\freecad\\bin'
FREECAD_BIN_LIB_SITEPACKAGES_PATH = 'C:\\dev\\freecad\\bin\\Lib\\site-packages'
import sys

sys.path.append(FREECAD_BIN_PATH)
sys.path.append(FREECAD_BIN_LIB_SITEPACKAGES_PATH)
from hexfloatinput import HexFloatInput
import freecadpunchdie


def freecad_punch_die_test():
    print("freecad_punch_die_test")
    normalfloatoutput.strict = False

    fcm = freecadpunchdie.create(HexFloatInput(
        cup_rad=53.86699549370134,
        cup_lip=4.788286291110409,
        cup_depth=77.19128428360575,
        cup_angle=69.1409249873599,
        cup_y_to_x=0.8030531449534937,
        cup_tip=0.8*53.86699549370134,
        space=97.64803882228355,
        alu_thick=0.30558618222098144,
        shoulder_angle=-33.577456771779914
    ))

    fcm.generate(True, False, False, False)


if __name__ == '__main__':
    freecad_punch_die_test()
