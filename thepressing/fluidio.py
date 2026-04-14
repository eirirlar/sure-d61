from typing import List, Dict, Tuple, Callable

from util import values, param_names, create_params_str, hash_numbers, accumulate_list_list
from validation import valid

edge_mean_near = 0.05
lip_mean_near_0 = 0.1


# lip_mean_near_1 = 0.05


class FluidInput:
    def __init__(self,
                 cup_rad: float,
                 cup_lip: float,
                 cup_depth: float,
                 cup_angle: float,
                 cup_y_to_x: float,
                 space: float,
                 alu_thick: float,
                 pressure: float
                 ):
        self.cup_rad = cup_rad
        self.cup_lip = cup_lip
        self.cup_depth = cup_depth
        self.cup_angle = cup_angle
        self.cup_y_to_x = cup_y_to_x
        self.space = space
        self.alu_thick = alu_thick
        self.pressure = pressure

    def values(self, params: List[str] = None) -> List[float]:
        if params is None:
            return list(self.__dict__.values())
        else:
            return [value for key, value in self.__dict__.items() if key in params]


class FluidOutput:
    def __init__(self,
                 time_to_crack: float = 0.,
                 lip_mean: float = 0.,
                 edge_mean: float = 0.
                 ):
        self.time_to_crack = time_to_crack
        self.lip_mean = lip_mean
        self.edge_mean = edge_mean


class FluidInputOutput:
    def __init__(self,
                 input: FluidInput,
                 output: FluidOutput = FluidOutput()
                 ):
        i = hash_numbers(input.values())
        # some loss of precision but doesn't matter
        self.input_hash = float(i)
        self.input = input
        self.output = output

    def dict(self):
        return {**self.input.__dict__, **self.output.__dict__}

    def values(self):
        return [self.input_hash] + values(self.input) + values(self.output)

    def to_str(self) -> str:
        return ';'.join(map(lambda v: '{: >20}'.format(str(v)), self.values())) + '\n'


def from_float(fi: dict) -> FluidInput:
    return FluidInput(**{p: v for p, v in fi.items() if p in input_params})


def from_str(s: str) -> FluidInputOutput:
    input_output = list(map(lambda floatstr: float(floatstr), s.split(';')))
    return from_values(input_output)


# values must contain hash, but it will be recalculated
def from_values(vs: List[float]) -> FluidInputOutput:
    return FluidInputOutput(FluidInput(*vs[1:n_inputs + 1]), FluidOutput(*vs[1 + n_inputs:]))


# vs is values of a FluidInputOutput
def calculate_pressure(vs: List[float]) -> float:
    f = from_values(vs).input
    cup_rad = f.cup_rad
    cup_depth = f.cup_depth
    alu_thick = f.alu_thick
    # TODO change if we move away from hardcoded alu_thick
    alu_thick = 1.
    pressure = 1.1 * 0.5 * cup_depth + 0.2 * (1. - cup_rad) + 0.3 * alu_thick
    return min(1., pressure)


# dict of calculatable param that is dependent on the list of strings given, with a function that does the calculation,
# taking an input that is the whole value set n_params long.
calculations: Dict[str, Tuple[List[str], Callable[[List[float]], float]]] = {
    'pressure': (['cup_rad', 'cup_depth', 'alu_thick'], calculate_pressure)
}

input_params = param_names(FluidInput)
input_params_to_index: Dict[str, int] = dict((h, i) for i, h in enumerate(input_params))
index_to_input_params: Dict[int, str] = dict((i, h) for i, h in enumerate(input_params))
n_inputs = len(input_params)

output_params = param_names(FluidOutput)
output_params_to_index: Dict[str, int] = dict((h, i) for i, h in enumerate(output_params))
index_to_output_params: Dict[int, str] = dict((i, h) for i, h in enumerate(output_params))
n_outputs = len(output_params)

params = ['input_hash'] + input_params + output_params
params_to_index: Dict[str, int] = dict((h, i) for i, h in enumerate(params))
index_to_params: Dict[int, str] = dict((i, h) for i, h in enumerate(params))
n_params = len(params)

params_order = [
    ['cup_rad',
     'cup_depth',
     'cup_angle',
     'cup_y_to_x',
     'space',
     # 'alu_thick'
     ],
    ['pressure']
    # ,
    # ['cup_lip']
]
params_acc: List[List[str]] = accumulate_list_list(params_order)
params_filters = [
    {'time_to_crack': 1.},
    {'time_to_crack': 1., 'lip_mean': 1. - lip_mean_near_0, 'edge_mean': 1. - edge_mean_near}
    # ,
    # {'time_to_crack': 1., 'lip_mean': 1. - lip_mean_near_1, 'edge_mean': 1. - edge_mean_near}
]
all_increasable_params = ['cup_rad', 'cup_y_to_x', 'space', 'alu_thick', 'pressure']  # , 'cup_lip']
all_decreasable_params = ['cup_depth', 'cup_angle']

params_str = create_params_str(params)
