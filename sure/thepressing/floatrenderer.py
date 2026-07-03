FREECAD_BIN_PATH = 'C:\\dev\\freecad\\bin'
FREECAD_BIN_LIB_SITEPACKAGES_PATH = 'C:\\dev\\freecad\\bin\\Lib\\site-packages'
import sys

sys.path.append(FREECAD_BIN_PATH)
sys.path.append(FREECAD_BIN_LIB_SITEPACKAGES_PATH)

import json
import time
from typing import Union

import hexfreecadmodel
from hexfloatinput import HexFloatInput
import os
from util import filename_output_genetic


input_file = filename_output_genetic + os.sep + 'best_input.json'
check_seconds_default = 2


def write_float_input(fi: HexFloatInput):
    try:
        os.makedirs(os.path.dirname(input_file), exist_ok=True)
        with open(input_file, 'w') as wf:
            json.dump(fi.__dict__, wf)
    except Exception as e:
        print('Could not dump floatinput')
        print(e)


def file_input() -> Union[HexFloatInput, None]:
    try:
        with open(input_file, 'r') as wf:
            fws = HexFloatInput(**json.load(wf))
            return fws
    except Exception:
        print('Could not load weights')
        return None


class Renderer:
    def __init__(self,
                 check_seconds=check_seconds_default
                 ):
        self.check_seconds = check_seconds

    def run(self):
        current_float = HexFloatInput()
        while True:
            fi = file_input()
            if current_float.__dict__ != fi.__dict__:
                current_float = fi
                fm = hexfreecadmodel.create(fi)
                fm.generate(fc=False, stp=False, stl=False, img=True)
                print(fi.__dict__)
            time.sleep(self.check_seconds)


if __name__ == '__main__':
    Renderer().run()
