FREECAD_BIN_PATH = 'C:\\dev\\freecad\\bin'
FREECAD_BIN_LIB_SITEPACKAGES_PATH = 'C:\\dev\\freecad\\bin\\Lib\\site-packages'
import sys

sys.path.append(FREECAD_BIN_PATH)
sys.path.append(FREECAD_BIN_LIB_SITEPACKAGES_PATH)
from hexfloatinput import HexFloatInput
import freecadfluidandpunchdie
from validation import ValidationError
import normalfloatoutput


def freecad_fluid_and_punch_die_test():
    print('freecad_fluid_and_punch_die_test')
    normalfloatoutput.strict = False

    try:

        fid = {
            'cup_rad': 39.37290758,
            'cup_lip': 1.0,
            'cup_depth': 24.4691106,
            'cup_angle': 72.89327465,
            'cup_y_to_x': 0.9967237779,
            'cup_tip': 0.3 * 39.37290758,
            'space': 13.25108274,
            'alu_thick': 0.8,
            'pressure': 7.5,
        }

        fi = HexFloatInput(**fid)
        fcm = freecadfluidandpunchdie.create(fi)
        # fcm.generate_lsrun_failtime(True, True, False, False, False, runtime=1.)
        fcm.generate(True, False, False, False, False, False, runtime=.5)
    except ValidationError as e:
        print(e.args[1])


if __name__ == '__main__':
    freecad_fluid_and_punch_die_test()
