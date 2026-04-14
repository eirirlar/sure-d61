FREECAD_BIN_PATH = 'C:\\dev\\freecad\\bin'
FREECAD_BIN_LIB_SITEPACKAGES_PATH = 'C:\\dev\\freecad\\bin\\Lib\\site-packages'
import sys

sys.path.append(FREECAD_BIN_PATH)
sys.path.append(FREECAD_BIN_LIB_SITEPACKAGES_PATH)
from hexfloatinput import HexFloatInput
from hexfreecadmodel import HexFreecadModel
import hexfloatmodel
import normalfloatinput
import normalfloatoutput


def hex_freecad_model_test():
    print("hex_freecad_model_test")
    normalfloatoutput.strict = False

    fi = HexFloatInput(cup_rad=40, cup_lip=1.0, cup_depth=20,
                       cup_angle=53.078428613046604, cup_y_to_x=0.9977090595645373,
                       cup_tip=0.8*40,
                       space=30,
                       alu_thick=0.8, shoulder_angle=-45.326052275445896, pressure=4.048470044680223)

    fm = hexfloatmodel.create(fi)
    fcm = HexFreecadModel(fm)

    calz = fm.calc_fitness()
    print(normalfloatinput.normalize(fm.float_input).__dict__)
    print(calz.__dict__)
    print(normalfloatoutput.create(calz).__dict__)
    fcm.generate(True, False, False, True)


if __name__ == '__main__':
    hex_freecad_model_test()
