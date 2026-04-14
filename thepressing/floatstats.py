from floatdata import FloatData
from hexfloatinput import HexFloatInput
from floatoutput import FloatOutput


class FloatStats:
    input: HexFloatInput
    output: FloatOutput
    fd: FloatData

    def __init__(self,
                 input: HexFloatInput,
                 output: FloatOutput,
                 data: FloatData
                 ):
        self.input = input
        self.output = output
        self.data = data

    def dict(self):
        return {k: v.__dict__ for k, v in self.__dict__.items()}
