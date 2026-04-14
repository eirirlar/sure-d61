from typing import List, Optional

import cupcalc
import fluidio
import hexfloatinput
import normalfloatinput
from neural import Neural
from neuralcommon import filename_collect
from press import calc_press_fault


# vs = FluidInputOutput vals normed
def predict_pressure(vs: List[float], neu: Optional[Neural] = None) -> float:
    pressure_input = [vs[fluidio.params_to_index[f]] for f in fluidio.params_order[0]]
    pressure: float
    if neu is None:
        try:
            neu = Neural([*fluidio.params_order, fluidio.output_params], fluidio.params_filters,
                         filename_collect,
                         normalfloatinput.normalizers, True, False)
        except Exception as e:
            print('fluidneural: Could not create Neural object')
    try:
        pressure = neu.predict(0, pressure_input)['pressure']
    except Exception:
        pressure = fluidio.calculate_pressure(vs)
    return pressure


def predict_press_fault(vs: List[float], neu: Optional[Neural] = None) -> float:
    press_fault_input = [vs[fluidio.params_to_index[f]] for f in fluidio.params_acc[1]]
    press_fault: float
    if neu is None:
        try:
            neu = Neural([*fluidio.params_order, fluidio.output_params], fluidio.params_filters,
                         filename_collect,
                         normalfloatinput.normalizers, True, False)
        except Exception as e:
            print('fluidneural: Could not create Neural object')
    try:
        press_fault = neu.predict(1, press_fault_input)['press_fault']
    except Exception:
        fi = hexfloatinput.from_fluid_input(normalfloatinput.denormalize_fluid_input(fluidio.from_values(vs).input))
        cc = cupcalc.calc_cup(fi)
        press_fault = calc_press_fault(fi, cc)
    return press_fault
