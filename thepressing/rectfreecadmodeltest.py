FREECAD_BIN_PATH = 'C:\\dev\\freecad\\bin'
FREECAD_BIN_LIB_SITEPACKAGES_PATH = 'C:\\dev\\freecad\\bin\\Lib\\site-packages'
import sys

sys.path.append(FREECAD_BIN_PATH)
sys.path.append(FREECAD_BIN_LIB_SITEPACKAGES_PATH)
from rectfloatinput import RectFloatInput
from rectfreecadmodel import RectFreecadModel
import rectfloatmodel
import normalfloatoutput


def rect_freecad_model_test():
    print("rect_freecad_model_test")
    normalfloatoutput.strict = False

    # fi = FloatInput(cup_rad=27.611066824724553, cup_lip=1.0, cup_depth=22.853018502435127,
    #                         cup_angle=53.078428613046604, cup_y_to_x=0.9977090595645373, space=55.15227006909975,
    #                         alu_thick=0.8, shoulder_angle=-45.326052275445896, pressure=4.048470044680223)

    fid = {
        'cup_rad': 39.37290758,
        'cup_lip': 2.0,
        'cup_depth': 24.4691106,
        'cup_angle': 72.89327465,
        'cup_y_to_x': 0.9967237779,
        'cup_tip': 0.3 * 39.37290758,
        'space': 13.25108274,
        'alu_thick': 0.8,
        'pressure': 7.5,
        'width': 300.,
        'length': 400.
        #'width': 1303.,
        #'length': 2384.
        # width: 506.3
        # length: 636.1
    }

    fi = RectFloatInput(**fid)

    fm = rectfloatmodel.create(fi, False)
    fcm = RectFreecadModel(fm)

    # calz = fm.calc_fitness()
    # print(normalfloatinput.normalize(fm.float_input).__dict__)
    # print(calz.__dict__)
    # print(normalfloatoutput.create(calz).__dict__)
    fcm.generate(True, False, False, False, inverted_die=True)


if __name__ == '__main__':
    rect_freecad_model_test()
