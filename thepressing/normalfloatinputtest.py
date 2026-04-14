FREECAD_BIN_PATH = 'C:\\dev\\freecad\\bin'
FREECAD_BIN_LIB_SITEPACKAGES_PATH = 'C:\\dev\\freecad\\bin\\Lib\\site-packages'
import random
import sys

sys.path.append(FREECAD_BIN_PATH)
sys.path.append(FREECAD_BIN_LIB_SITEPACKAGES_PATH)

from normalfloatinput import NormalFloatInput
import hexfreecadmodel
from validation import valid

def normalFloatInputTest():
    print("normalFloatinputTest")
    i = 0
    invalid_count = 0
    while i < 30:
        fmd = NormalFloatInput(
            random.uniform(0, 1),
            random.uniform(0, 1),
            random.uniform(0, 1),
            random.uniform(0, 1),
            random.uniform(0, 1),
            random.uniform(0, 1),
            random.uniform(0, 1),
            random.uniform(0, 1)
        )
        fm = hexfreecadmodel.create(fmd.denorm())
        if valid(fm.float_model.float_input.validate()):
            print(fm.float_model.float_input.__dict__)
            fm.generate(filename=f'sample_{i}')
            i += 1
        else:
            invalid_count += 1

    print(f'Ditched {invalid_count} invalid random floats')

def othertest():
    nfi = NormalFloatInput(*[0.12122128642897678, 0.09418836030945221, 0.003009648509330387, 0.23187384661524524, 0.7935298227572942, 0.043633163657265106, 0.8813724623775113, 0.7779072525623018])
    fi = nfi.denorm()
    validations = fi.validate()
    v = valid(validations)
    print(fi.__dict__)
    print(v)
    print(validations)

if __name__ == '__main__':
    normalFloatInputTest()
