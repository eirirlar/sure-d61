import shouldercalc
from shouldercalc import *
from hexfloatinput import HexFloatInput

fi = HexFloatInput()
s = calc_shoulder(fi)

print(fi.__dict__)


def test_shoulder_calc_y_small_arc_rot_sq_int():
    g0 = y_small_arc_rot_sq_int(math.pi / 3,
                                math.sin(math.radians(math.fabs(fi.shoulder_angle))) * s.small_arc_radius,
                                s.small_arc_radius,
                                math.radians(math.fabs(fi.shoulder_angle)),
                                0.0)
    assert g0 < shouldercalc.very_small
    g1 = y_small_arc_rot_sq_int(math.pi / 3,
                                math.sin(math.radians(math.fabs(fi.shoulder_angle))) * s.small_arc_radius,
                                s.small_arc_radius,
                                math.radians(math.fabs(fi.shoulder_angle)),
                                0.296472)
    a = 0.0138607  # wolfram alpha
    assert a < g1 and g1 < a + 0.00001


def test_vol_rot_small_arc():
    v0 = vol_rot_small_arc(math.pi / 3, s.small_arc_x, s.small_arc_radius, s.angle_rad_abs, s.small_arc_y)
    a0 = vol_rot_slope(math.pi / 3, s.small_arc_x, s.small_arc_x * 0.52, s.small_arc_y)
    assert a0 < v0 and v0 < a0 + 0.001

    v1 = vol_rot_small_arc(math.pi / 3, 1 + s.small_arc_x, 1 + s.small_arc_radius, s.angle_rad_abs, s.small_arc_y)
    a1 = vol_rot_slope(math.pi / 3, 1 + s.small_arc_x, 1 + s.small_arc_x * 0.55, s.small_arc_y)
    assert a1 < v1 and v1 < a1 + 0.1


def test_shoulder_calc_y_large_arc_sq_int():
    g0 = y_large_arc_rot_sq_int(math.pi / 3, s.large_arc_x, s.large_arc_radius, 0)
    a0 = 1.3728  # wolfram alpha
    assert g0 < a0 and a0 < g0 + 0.0001
    x1 = (1 - math.sin(s.angle_inv_rad)) * s.large_arc_radius
    g1 = y_large_arc_rot_sq_int(math.pi / 3, s.large_arc_x, s.large_arc_radius, x1)
    a1 = 1.4472
    assert a1 < g1 and g1 < a1 + 0.0001


def test_vol_rot_large_arc():
    d = (1 - math.sin(s.angle_inv_rad)) * s.large_arc_radius
    v0 = vol_rot_large_arc(math.pi / 3, s.large_arc_x, s.large_arc_radius, d)
    a0 = vol_rot_slope(math.pi / 3, s.large_arc_x * 0.6, 0, d)
    assert v0 < a0 and a0 < v0 + 0.001
    v1 = vol_rot_large_arc(math.pi / 3, 1 + s.large_arc_x, s.large_arc_radius, d)
    a1 = vol_rot_slope(math.pi / 3, 1 + s.large_arc_x * 0.6, 1, d)
    assert v1 < a1 and a1 < v1 + 0.1


def test_shoulder_calc_vol_rot_slope():
    g0 = vol_rot_slope(2 * math.pi, 3, 2, 7)
    a0 = 139.27727  # wolfram alpha
    assert a0 < g0 and g0 < a0 + 0.0001


def test_shoulder_calc_vol_y0():
    g0 = calc_vol_y0(s, 0)
    a0 = math.pow(s.forth_arc_center_x, 2) * s.large_arc_y * math.pi / 6
    assert g0 < a0 and a0 < g0 + 30


def test_shoulder_calc_vol_y1():
    g0 = calc_vol_y1(s, 10)
    a0 = 5825  # online cut of cone calculator
    assert a0 < g0 and g0 < a0 + 1


def test_shoulder_calc_vol_y2():
    a = (s.long_drop_lower_start_x + s.third_arc_center_x) / 2 + 10
    a0 = a * a * s.small_arc_y * math.pi / 6
    g0 = calc_vol_y2(s, 10)
    assert a0 < g0 and g0 < a0 + 1


def test_shoulder_calc_vol_y3():
    g0 = calc_vol_y3(s, 0)
    # 1.07 approximate weighted average between min and max
    a0 = math.pow(1.07, 2) * s.large_arc_y * math.pi / 6
    assert a0 < g0 and g0 < a0 + 0.01

    g1 = calc_vol_y3(s, 10)
    # 1.07 approximate weighted average between min and max
    a1 = math.pow(11.07, 2) * s.large_arc_y * math.pi / 6
    assert g1 < a1 and a1 < g1 + 1


def test_shoulder_calc_vol_y4():
    g0 = calc_vol_y4(s, 10)
    a0 = s.short_drop_y * math.pow(10 + 0.51, 2) * math.pi / 6
    assert a0 < g0 and g0 < a0 + 1


def test_shoulder_calc_vol_y5():
    a = s.small_arc_x / 1.4 + 10
    a0 = a * a * s.small_arc_y * math.pi / 6
    g0 = calc_vol_y5(s, 10)
    assert a0 < g0 and g0 < a0 + 1


def test_shoulder_calc_vol():
    g0 = calc_vol_corner_and_cup_and_float(s, 0)
    a0 = vol_rot_slope(math.pi / 3, 0, 27, 20)
    assert g0 < a0 and a0 < g0 + 150

    g1 = calc_vol_corner_and_cup_and_float(s, 10)
    a1 = vol_rot_slope(math.pi / 3, 10, 37, 20)
    assert a1 < g1 and g1 < a1 + 50


def test_shoulder_calc_edge_cup_without_shoulder_vol():
    g0 = calc_vol_corner_cup_and_float_only(20, 10)
    a0 = 1047  # just math
    assert a0 < g0 and g0 < a0 + 1


def test_shoulder_calc_vol_without_cup():
    g0 = calc_vol_corner(s, 20, 10)
    a0 = 5400
    assert g0 < a0 and a0 < g0 + 10


if __name__ == '__main__':
    test_shoulder_calc_y_small_arc_rot_sq_int()
    test_vol_rot_small_arc()
    test_shoulder_calc_y_large_arc_sq_int()
    test_vol_rot_large_arc()
    test_shoulder_calc_vol_rot_slope()
    test_shoulder_calc_vol_y0()
    test_shoulder_calc_vol_y1()
    test_shoulder_calc_vol_y2()
    test_shoulder_calc_vol_y3()
    test_shoulder_calc_vol_y4()
    test_shoulder_calc_vol_y5()
    test_shoulder_calc_vol()
    test_shoulder_calc_edge_cup_without_shoulder_vol()
    test_shoulder_calc_vol_without_cup()
