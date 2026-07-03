import math
from math import (pow, sqrt, radians, asin, atan, sin, cos, pi)
from hexfloatinput import HexFloatInput

very_small = 0.00000001


class ShoulderCalc:
    def __init__(self,
                 angle_rad_abs: float,
                 angle_inv_rad: float,
                 angle_3q_rad: float,
                 large_arc_radius: float,
                 large_arc_y: float,
                 large_arc_x: float,
                 small_arc_radius: float,
                 small_arc_y: float,
                 small_arc_x: float,
                 short_drop_y: float,
                 short_drop_x: float,
                 second_lower_arc_end_y: float,
                 long_drop_y: float,
                 long_drop_x: float,
                 edge: float,
                 first_lower_arc_end_x: float,
                 first_lower_arc_end_y: float,
                 first_drop_end_x: float,
                 first_drop_end_y: float,
                 second_arc_center_x: float,
                 second_arc_center_y: float,
                 second_upper_arc_end_y: float,
                 third_arc_center_x: float,
                 third_arc_center_y: float,
                 long_drop_upper_start_x: float,
                 long_drop_upper_start_y: float,
                 long_drop_upper_end_x: float,
                 long_drop_upper_end_y: float,
                 long_drop_lower_start_x: float,
                 long_drop_lower_start_y: float,
                 long_drop_lower_end_x: float,
                 forth_arc_center_x: float,
                 float_lip_end_x: float
                 ):
        self.angle_rad_abs = angle_rad_abs
        self.angle_inv_rad = angle_inv_rad
        self.angle_3q_rad = angle_3q_rad
        self.large_arc_radius = large_arc_radius
        self.large_arc_y = large_arc_y
        self.large_arc_x = large_arc_x
        self.small_arc_radius = small_arc_radius
        self.small_arc_y = small_arc_y
        self.small_arc_x = small_arc_x
        self.short_drop_y = short_drop_y
        self.short_drop_x = short_drop_x
        self.second_lower_arc_end_y = second_lower_arc_end_y
        self.long_drop_y = long_drop_y
        self.long_drop_x = long_drop_x
        self.edge = edge
        self.first_lower_arc_end_x = first_lower_arc_end_x
        self.first_lower_arc_end_y = first_lower_arc_end_y
        self.short_drop_end_x = first_drop_end_x
        self.short_drop_end_y = first_drop_end_y
        self.second_arc_center_x = second_arc_center_x
        self.second_arc_center_y = second_arc_center_y
        self.second_upper_arc_end_y = second_upper_arc_end_y
        self.third_arc_center_x = third_arc_center_x
        self.third_arc_center_y = third_arc_center_y
        self.long_drop_upper_start_x = long_drop_upper_start_x
        self.long_drop_upper_start_y = long_drop_upper_start_y
        self.long_drop_upper_end_x = long_drop_upper_end_x
        self.long_drop_upper_end_y = long_drop_upper_end_y
        self.long_drop_lower_start_x = long_drop_lower_start_x
        self.long_drop_lower_start_y = long_drop_lower_start_y
        self.long_drop_lower_end_x = long_drop_lower_end_x
        self.forth_arc_center_x = forth_arc_center_x
        self.float_lip_end_x = float_lip_end_x

    def calc_area(self, f: HexFloatInput) -> float:
        angle_r_abs = radians(math.fabs(f.shoulder_angle))
        area_within_small_arc_upper = pow(self.small_arc_radius, 2) * angle_r_abs / 2
        area_within_small_arc_lower = self.small_arc_x * (self.small_arc_radius - self.small_arc_y) / 2
        area_within_small_arc = area_within_small_arc_upper + area_within_small_arc_lower
        area_under_first_arc = (f.cup_depth - self.small_arc_radius) * self.small_arc_x + area_within_small_arc
        area_within_short_drop = self.short_drop_x * self.short_drop_y / 2
        area_under_first_drop = self.short_drop_end_y * self.short_drop_x + area_within_short_drop
        area_within_large_arc_lower = pow(self.large_arc_radius, 2) * angle_r_abs / 2
        area_within_large_arc_upper = self.large_arc_x * (self.large_arc_radius - self.large_arc_y) / 2
        area_within_large_arc = area_within_large_arc_upper + area_within_large_arc_lower
        area_under_second_arc = self.second_arc_center_y * self.large_arc_x - area_within_large_arc
        area_under_first_flat = self.second_lower_arc_end_y * (self.third_arc_center_x - self.second_arc_center_x)
        area_under_third_arc = self.third_arc_center_y * self.small_arc_x + area_within_small_arc
        area_under_long_drop = self.long_drop_x * (self.long_drop_lower_start_y + self.large_arc_y) / 2
        area_under_forth_arc = self.large_arc_x * self.large_arc_radius - area_within_large_arc
        area_under = area_under_first_arc + area_under_first_drop + area_under_second_arc + area_under_first_flat + area_under_third_arc + area_under_long_drop + area_under_forth_arc
        return area_under

    # The following are graphs defining the horizontal slices of the shoulder, from bottom to top
    # The curve's squared integrated version with rotation (volume) is described for small_arc, large_arc and slope
    # All the slices have been translated so that they start at global z=0. This is to make integration more computationally effective and less complex.

    def shoulder_vol(self, cup_depth, f: HexFloatInput, hex_calc) -> float:
        shoulder_vol_corner = self.calc_vol_corner(cup_depth,
                                                   (hex_calc.inner_side - hex_calc.cup_max_x) * sqrt(3) / 2)
        area_under_shoulder = self.calc_area(f)
        shoulder_vol_side = area_under_shoulder * hex_calc.cup_max_x
        v = 6 * (shoulder_vol_corner + shoulder_vol_side)
        return v

    # h is radius of cup + edge out to where the shoulder starts
    # d is height of cup
    def calc_vol_corner(self, d: float, h: float) -> float:
        v0 = calc_vol_corner_cup_and_float_only(d, h)
        v1 = self.calc_vol_corner_and_cup_and_float(h)
        v = v1 - v0
        return v

    def calc_vol_corner_and_cup_and_float(self, h: float) -> float:
        v0 = self.calc_vol_y0(h)
        v1 = self.calc_vol_y1(h)
        v2 = self.calc_vol_y2(h)
        v3 = self.calc_vol_y3(h)
        v4 = self.calc_vol_y4(h)
        v5 = self.calc_vol_y5(h)
        v = v0 + v1 + v2 + v3 + v4 + v5
        return v

    def calc_vol_y0(self, h: float) -> float:
        v = vol_rot_large_arc(pi / 3, h + self.forth_arc_center_x, self.large_arc_radius, self.large_arc_y)
        return v

    def calc_vol_y1(self, h: float) -> float:
        v = vol_rot_slope(pi / 3, h + self.long_drop_lower_end_x, h + self.long_drop_lower_start_x, self.long_drop_y)
        return v

    def calc_vol_y2(self, h: float) -> float:
        v = vol_rot_small_arc(pi / 3, h + self.long_drop_lower_start_x, self.small_arc_radius, self.angle_rad_abs,
                              self.small_arc_y)
        return v

    def calc_vol_y3(self, h: float) -> float:
        v = vol_rot_large_arc(pi / 3, h + self.second_arc_center_x, self.large_arc_radius, self.large_arc_y)
        return v

    def calc_vol_y4(self, h: float) -> float:
        v = vol_rot_slope(pi / 3, h + self.short_drop_end_x, h + self.first_lower_arc_end_x, self.short_drop_y)
        return v

    def calc_vol_y5(self, h: float) -> float:
        v = vol_rot_small_arc(pi / 3, h + self.small_arc_x, self.small_arc_radius, self.angle_rad_abs, self.small_arc_y)
        return v


def calc_shoulder(
        f: HexFloatInput
) -> ShoulderCalc:
    angle_rad_abs = radians(abs(f.shoulder_angle))
    angle_inv_rad = math.pi / 2 - angle_rad_abs
    angle_3q_rad = math.pi * 3 / 2 - angle_rad_abs
    small_arc_radius = f.alu_thick / 2
    large_arc_radius = small_arc_radius * 3
    large_arc_y = large_arc_radius * (1 - math.sin(angle_inv_rad))
    large_arc_x = large_arc_radius * math.cos(angle_inv_rad)
    small_arc_y = large_arc_y / 3
    small_arc_x = large_arc_x / 3
    short_drop_y = f.shoulder_depth - large_arc_y - small_arc_y
    short_drop_x = sqrt(
        short_drop_y * short_drop_y * (
                1 / pow(math.cos(angle_inv_rad), 2) - 1))
    second_lower_arc_end_y = f.cup_depth - f.shoulder_depth
    long_drop_y = second_lower_arc_end_y - large_arc_y - small_arc_y
    long_drop_x = sqrt(
        long_drop_y * long_drop_y * (
                1 / pow(math.cos(angle_inv_rad), 2) - 1))
    edge = 2 * large_arc_x + short_drop_x + small_arc_x + f.shoulder_width + long_drop_x + f.float_lip
    first_lower_arc_end_x = small_arc_radius * math.cos(angle_inv_rad)
    first_lower_arc_end_y = f.cup_depth - small_arc_y
    short_drop_end_x = small_arc_x + short_drop_x
    short_drop_end_y = second_lower_arc_end_y + large_arc_y
    second_arc_center_x = large_arc_x + short_drop_x + small_arc_x
    second_arc_center_y = second_lower_arc_end_y + large_arc_radius
    second_upper_arc_end_y = second_lower_arc_end_y + f.alu_thick
    third_arc_center_x = second_arc_center_x + f.shoulder_width - small_arc_x
    third_arc_center_y = second_lower_arc_end_y - small_arc_radius
    long_drop_upper_start_x = third_arc_center_x + large_arc_x
    long_drop_upper_start_y = second_upper_arc_end_y - large_arc_y
    long_drop_upper_end_x = long_drop_upper_start_x + long_drop_x
    long_drop_upper_end_y = f.alu_thick + small_arc_y
    long_drop_lower_start_x = third_arc_center_x + small_arc_x
    long_drop_lower_start_y = second_lower_arc_end_y - small_arc_y
    long_drop_lower_end_x = long_drop_lower_start_x + long_drop_x
    forth_arc_center_x = long_drop_upper_end_x + small_arc_x
    float_lip_end_x = forth_arc_center_x + f.float_lip

    return ShoulderCalc(
        angle_rad_abs,
        angle_inv_rad,
        angle_3q_rad,
        large_arc_radius,
        large_arc_y,
        large_arc_x,
        small_arc_radius,
        small_arc_y,
        small_arc_x,
        short_drop_y,
        short_drop_x,
        second_lower_arc_end_y,
        long_drop_y,
        long_drop_x,
        edge,
        first_lower_arc_end_x,
        first_lower_arc_end_y,
        short_drop_end_x,
        short_drop_end_y,
        second_arc_center_x,
        second_arc_center_y,
        second_upper_arc_end_y,
        third_arc_center_x,
        third_arc_center_y,
        long_drop_upper_start_x,
        long_drop_upper_start_y,
        long_drop_upper_end_x,
        long_drop_upper_end_y,
        long_drop_lower_start_x,
        long_drop_lower_start_y,
        long_drop_lower_end_x,
        forth_arc_center_x,
        float_lip_end_x
    )


def calc_vol_corner_cup_and_float_only(d: float, h: float) -> float:
    v = h * h * pi / 6 * d
    return v


# d is always s.small_arc_y
def vol_rot_small_arc(rot: float, h: float, rad: float, angle: float, d: float):
    y0 = y_small_arc_rot_sq_int(rot, h, rad, angle, 0)
    y1 = y_small_arc_rot_sq_int(rot, h, rad, angle, d)
    y = y1 - y0
    return y


def y_small_arc_rot_sq_int(rot: float, h: float, r: float, b: float, x: float) -> float:
    cb = cos(b)
    if x <= 0:
        x = very_small
    elif r - x < r * cb:
        x = r - r * cb - very_small
    r2 = pow(r, 2)
    sb = sin(b)
    x2 = pow(x, 2)
    hrsb = h - r * sb
    a = x * (-2 * h * r * sb - r2 * cos(2 * b) + pow(h, 2) + r2)
    sq = -(2 * x * cb) / r + pow(sb, 2) - x2 / r2
    if sq < 0:
        sq = 0
    c = r * hrsb * (r * cb + x) * sqrt(sq)
    x_r = max(min(cb + x / r, 1), -1)
    d = r2 * hrsb * asin(x_r)
    e = -r * x2 * cb
    f = -pow(x, 3) / 3
    y = rot / 2 * (a + c + d + e + f)
    return y


def vol_rot_large_arc(rot: float, h: float, r: float, d: float):
    y0 = y_large_arc_rot_sq_int(rot, h, r, 0)
    y1 = y_large_arc_rot_sq_int(rot, h, r, d)
    y = y1 - y0
    return y


def y_large_arc_rot_sq_int(rot: float, h: float, r: float, x: float) -> float:
    if 0 == x:
        x = very_small
    a = pow(h, 2) * x
    f = sqrt(x * (2 * r - x))
    b = h * pow(r, 2) * atan((r - x) / f)
    c = h * f * (r - x)
    d = r * pow(x, 2)
    e = -pow(x, 3) / 3
    y = rot / 2 * (a + b + c + d + e)
    return y


def vol_rot_slope(rot: float, h0: float, h1: float, d: float) -> float:
    v = rot / 6 * d * (pow(h0, 2) + h0 * h1 + pow(h1, 2))
    return v
