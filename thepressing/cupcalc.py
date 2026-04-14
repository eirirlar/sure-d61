import math
from math import *

import numpy as np
from scipy.integrate import quad
from scipy.special import (ellipe)

from floatinput import FloatInput
from hexfloatinput import HexFloatInput

error = 0.0000001


class LipCalc:

    def __init__(self,
                 tangent_z: float,
                 tangent_r: float,
                 area: float,
                 centroid_r: float,
                 circle_r: float,
                 angle_r: float
                 ):
        self.tangent_z = tangent_z
        self.tangent_r = tangent_r
        self.area = area
        self.centroid_r = centroid_r
        self.circle_r = circle_r
        self.angle_r = angle_r


class CupCalc:
    def __init__(self,
                 cup_angle_r: float,
                 cup_angle_tip: float,
                 cup_ellipsoid_x: float,
                 cup_ellipsoid_y: float,
                 cup_depth_ellipsoid: float,
                 lip_x: LipCalc,
                 lip_y: LipCalc,
                 cup_lip_arc_x: float,
                 cup_lip_arc_y: float
                 ):
        self.cup_angle_r = cup_angle_r
        self.cup_angle_tip = cup_angle_tip
        self.cup_ellipsoid_x = cup_ellipsoid_x
        self.cup_ellipsoid_y = cup_ellipsoid_y
        self.cup_depth_ellipsoid = cup_depth_ellipsoid
        self.lip_x = lip_x
        self.lip_y = lip_y
        self.cup_lip_arc_x = cup_lip_arc_x
        self.cup_lip_arc_y = cup_lip_arc_y


def calc_cup(fi: FloatInput) -> CupCalc:
    #ep = calc_ellipse_parts(fi.cup_tip, fi.cup_rad, fi.cup_depth)
    #print('ep: ', ep)
    cup_angle_r = math.radians(fi.cup_angle)
    # TODO
    cup_angle_tip = -90.
    cup_ellipsoid_x = (fi.cup_rad - fi.cup_lip) / cos(cup_angle_r)
    cup_ellipsoid_y = (fi.cup_rad - fi.cup_lip) / cos(cup_angle_r) * fi.cup_y_to_x
    cup_depth_ellipsoid = fi.cup_depth / (1 - sin(cup_angle_r))
    lip_x = calc_lip(cup_ellipsoid_x, cup_depth_ellipsoid, fi.cup_lip, fi.cup_depth)
    lip_y = calc_lip(cup_ellipsoid_y, cup_depth_ellipsoid, fi.cup_lip, fi.cup_depth)
    cup_lip_arc_x = arclength(cup_angle_r, pi / 2, cup_ellipsoid_x, cup_depth_ellipsoid) + fi.cup_lip * lip_x.angle_r
    cup_lip_arc_y = arclength(cup_angle_r, pi / 2, cup_ellipsoid_y, cup_depth_ellipsoid) + fi.cup_lip * lip_y.angle_r
    return CupCalc(cup_angle_r, cup_angle_tip, cup_ellipsoid_x, cup_ellipsoid_y, cup_depth_ellipsoid, lip_x, lip_y,
                   cup_lip_arc_x, cup_lip_arc_y)


def calc_ellipse_parts(Tx: float, Cx: float, delta_y: float):
    # Cy = Ty + delta_y
    # Cy = b + delta_y
    # We need to solve the following system of equations:
    # (Tx^2 / a^2) + ((Ty - b)^2 / b^2) = 1
    # (Cx^2 / a^2) + ((Ty + delta_y - b)^2 / b^2) = 1

    # First, express Cy and Ty
    Cy = delta_y
    Ty = Cy - delta_y

    # Iterate to find the best b
    b_guess = Cy + delta_y  # initial guess for b
    tolerance = 1e-6
    max_iterations = 1000
    iteration = 0

    while iteration < max_iterations:
        Ty_guess = b_guess - delta_y
        denominator_T = b_guess ** 2 - (Ty_guess - b_guess) ** 2
        if denominator_T <= 0:
            b_guess += 0.1  # Increment b_guess slightly to avoid non-positive denominator
            continue

        a = math.sqrt(Tx ** 2 * b_guess ** 2 / denominator_T)

        ellipse_eq_C = (Cx ** 2 / a ** 2) + ((Cy - b_guess) ** 2 / b_guess ** 2)

        if abs(ellipse_eq_C - 1) < tolerance:
            break

        b_guess += (1 - ellipse_eq_C) * 0.1  # Adjust step size as necessary
        iteration += 1

    if iteration >= max_iterations:
        raise ValueError("Failed to converge to a solution for 'a'")

    b = b_guess
    Ty = b - delta_y

    # Calculate the angle to the point T
    angle_T = math.atan2(Ty - b, Tx)
    # Calculate the angle to the point C
    angle_C = math.atan2(Cy - b, Cx)

    return {
        'b': b,
        'Ty': Ty,
        'a': a,
        'angle_T': angle_T,
        'angle_C': angle_C
    }


def calc_area(fillet_rad_x: float, fillet_rad_y: float) -> float:
    a = pi * fillet_rad_x * fillet_rad_y
    return a


def calc_vol_init(fi: HexFloatInput) -> float:
    cc = calc_cup(fi)
    v = calc_vol(fi.cup_depth, cc)
    return v


# volume of one cup
def calc_vol(cup_depth: float, cc: CupCalc) -> float:
    vol_cap = calc_vol_cap(cc.cup_ellipsoid_x, cc.cup_ellipsoid_y, cc.cup_depth_ellipsoid, cup_depth)
    vol_lip = calc_vol_lip(cc.lip_x, cc.lip_y)
    vol = vol_cap + vol_lip
    return vol


def calc_vol_cap(a: float, b: float, c: float, h: float) -> float:
    v = pi * a * b / 3 / c / c * h * h * (3 * c - h)
    return v


def calc_vol_lip(lip_x: LipCalc,
                 lip_y: LipCalc) -> float:
    (tangent_z_x, tangent_r_x, area_x, centroid_x, _, _) = lip_x.__dict__.values()
    (tangent_z_y, tangent_r_y, area_y, centroid_y, _, _) = lip_y.__dict__.values()
    z_diff = abs(tangent_z_x - tangent_z_y)
    arc_length = arclength_pi_half(centroid_x, centroid_y)
    amplitude = pi * z_diff / 2 / arc_length
    stretch_factor = 2 * (amplitude ** 2 + 1) ** (1 / 2) * ellipe(amplitude ** 2 / (amplitude ** 2 + 1)) / pi
    area_avg = (area_x + area_y) / 2
    v = 4 * area_avg * arc_length * stretch_factor
    return v


# got new ellipsis for arc length path calc by mrx, mry


# We call this 'r' in the returned params because in the return we view it as the r,z plane.
# Internally in this method we view it as the x,y plane.
# Returns:
# - z-coord of tangent point between fillet circle and cup ellipse
# - area between ellipse, fillet circle and cup_height line
# - estimated r-coord of centroid of area above (r is x or y dependent on if this method is called with major or minor ellipse axis). This may be a bad estimate, not fully QAd.
# - r-coord of fillet circle center, and thus the point where the fillet meets the top line
def calc_lip(a: float, b: float, r: float, h: float, n=17) -> LipCalc:
    theta0 = 0.
    ex0 = a * (1 - ((h - b) / b) ** 2) ** .5

    def phi(theta):
        s = sin(theta)
        c = cos(theta)
        p1 = b ** 2 - (b ** 2 - a ** 2) * s ** 2
        p2 = a * r / sqrt(p1) + b
        p3 = s * p2 + b - h + r
        p4 = c * p2 - a * r * (a ** 2 - b ** 2) * s ** 2 * c / sqrt(p1) ** 3
        return theta - p3 / p4

    for k in range(n):
        theta1 = phi(theta0)
        if abs(theta1 - theta0) < error:
            c = cos(theta1)
            s = sin(theta1)
            cx = a * c + r * c * b / sqrt(a ** 2 * s ** 2 + b ** 2 * c ** 2)
            cy = h - r
            # this should be the same (sanity check):
            # cy0 = b + s * (b + a * r / sqrt(a ** 2 * s ** 2 + b ** 2 * c ** 2))
            theta_n = atan(a / b * tan(theta1))
            ex1 = cx - r * cos(theta_n)
            ey1 = cy - r * sin(theta_n)
            cx0 = cx - ex1
            # center of mass is a great simplification
            centroid = ex1 + (ex0 - ex1) / 2 + cx0 / 4
            ey10 = h - ey1
            ac = area_under_circle_part(ey10, cx0, r)
            ae = area_under_ellipse_part(ey10, a, b, h, ex1)
            area = ac - ae
            return LipCalc(ey1, ex1, area, centroid, cx, pi / 2 + theta_n)
        theta0 = theta1
    raise Exception(f"No solution found for input a={a},b={b},r={r},h={h}")


def area_under_circle_part(ey10: float, cx0: float, r: float) -> float:
    px = cx0 * ey10
    bb = r ** (5 / 2) * ey10 ** (1 / 2) * (-(ey10 - 2 * r) / r) ** (
            1 / 2) * asin((ey10 / (2 * r)) ** (1 / 2)) / (ey10 * (2 * r - ey10)) ** (1 / 2)
    gg = (r - ey10) / 2 * sqrt(ey10 * (2 * r - ey10))
    ac = px - bb + gg
    return ac


def area_under_ellipse_part(ey10: float, a: float, b: float, h: float, ex1: float):
    start = area_under_ellipse_integral(0, a, b, h, ex1)
    end = area_under_ellipse_integral(ey10, a, b, h, ex1)
    i = end - start
    return i


def area_under_ellipse_integral(x: float, a: float, b: float, h: float, ex1: float):
    f = b - h
    fx = f + x
    cfx = (b ** 2 - fx ** 2) ** (1 / 2)
    ar = 1 / 2 * (a * fx * cfx / b + b * a * atan(fx / cfx) - 2 * ex1 * x)
    return ar


def e_2(a: float, b: float) -> float:
    return 1. - (b / a) ** 2


def arclength_pi_half(a: float, b: float) -> float:
    e_sq = e_2(a, b)
    al = a * ellipe(e_sq)
    return al


def arclength(T0, T1, a, b) -> float:
    f = lambda t: (a ** 2 * sin(t) ** 2 + b ** 2 * cos(t) ** 2) ** 0.5
    return quad(f, T0, T1)[0]


# only works when c < a and c < b. Ongoing request on reddit to get answer.
# https://www.reddit.com/r/askmath/comments/s656n3/need_help_calculating_the_surface_area_of_an/
def surface(a: float, b: float, c: float, hc: float) -> float:
    h = 1 - hc / c

    def B_t(t):
        result = 1 - (1 - a ** 2 / b ** 2) * t ** 2
        return result

    def F_t(t):
        result = a ** 2 / c ** 2 / B_t(t) - 1
        return result

    def G_t(t):
        result = np.emath.sqrt(h ** 2 + (1 - h ** 2) * c ** 2 / a ** 2 * B_t(t))
        return result

    def f_t(t):
        f_t = F_t(t)
        if f_t == 0:
            result = 2 * (1 - h)
        else:
            # if f_t < 0:
            #    f_t = 0.0000000000000000001
            b_t = B_t(t)
            g_t = G_t(t)
            sq1 = np.emath.sqrt(b_t / f_t)
            sq2 = np.emath.sqrt(f_t / b_t)
            ap = a / c * sq2 * (g_t - h)
            ash = np.arcsinh(ap)
            # ash = np.emath.log(ap + np.emath.sqrt(ap ** 2 + 1))
            res = 1 - h * g_t + c / a * sq1 * ash
            result = res
        return result

    def Integration(n):
        # do sum loop i=1..n
        wi = np.pi / n
        Si = 0.0
        for i in range(1, n + 1):
            xi = np.cos((2 * i - 1) / (2 * n) * np.pi)
            fx = f_t(xi)
            wfx = wi * fx
            Si = Si + wfx
        result = a * b * Si
        return result

    return Integration(10)


def heron(a: float, b: float, c: float) -> float:
    s = (a + b + c) / 2
    c_ = s * (s - a) * (s - b) * (s - c)
    a = math.sqrt(c_)
    return a


def surface3(ea: float, eb: float, ec: float, ha: float, hb: float, hc: float, cup_angle_r: float) -> float:
    ac = arclength(cup_angle_r, pi / 2, ea, ec)
    bc = arclength(cup_angle_r, pi / 2, eb, ec)
    ab = arclength_pi_half(ha, hb)
    a = 4 * heron(ac, bc, ab)


def inside_ellipse(a: float, b: float, x: float, y: float) -> bool:
    p = (x / a) ** 2 + (y / b) ** 2
    return p <= 1


def between_ellipses(a0: float, b0: float, a1: float, b1: float, x: float, y: float) -> bool:
    if inside_ellipse(a0, b0, x, y):
        return False
    elif inside_ellipse(a1, b1, x, y):
        return True
    else:
        return False


def lip_height_mean(tangent_x: float, circle_x: float, tangent_y: float, circle_y: float, cup_depth: float,
                    cup_lip: float):
    lhm_x = lip_height_mean_r(tangent_x, circle_x, cup_depth, cup_lip)
    lhm_y = lip_height_mean_r(tangent_y, circle_y, cup_depth, cup_lip)
    return (lhm_x + lhm_y) / 2.


# height of the lip from the bottom of the cup, along one axis
def lip_height_mean_r(tangent_r: float, circle_r: float, cup_depth: float, cup_lip: float):
    return cup_depth - cup_lip + (cup_lip ** 2. - ((tangent_r + circle_r) / 2. - circle_r) ** 2.) ** (1 / 2.)
