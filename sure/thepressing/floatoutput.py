from util import param_names


class FloatOutput:

    def __init__(self,
                 area: float,
                 weight: float,
                 volume: float,
                 thermal_conductivity: float,
                 connector_stress: float,
                 structural_integrity: float,
                 press_fault: float
                 ):
        self.area = area
        self.weight = weight
        self.volume = volume
        self.thermal_conductivity = thermal_conductivity
        self.connector_stress = connector_stress
        self.structural_integrity = structural_integrity
        self.press_fault = press_fault

params = param_names(FloatOutput)