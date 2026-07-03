import math
from typing import Callable
import numpy as np

view_size = 200.
overlap = 20.


class RectCalc:
    def __init__(self,
                 inner_width: float,
                 inner_length: float,
                 cup_points: [(float, float)],
                 inner_rect_corner_upper_left_x: float,
                 inner_rect_corner_upper_left_y: float,
                 inner_rect_corner_lower_right_x: float,
                 inner_rect_corner_lower_right_y: float,
                 cup_max_x: float,
                 cup_max_y: float,
                 view_centers: [((int, int), (float, float))],
                 view_chunks_x: int,
                 view_chunks_y: int,
                 view_width: float,
                 view_length: float
                 ):
        self.inner_width = inner_width
        self.inner_length = inner_length
        self.cup_points = cup_points
        self.inner_rect_corner_upper_left_x = inner_rect_corner_upper_left_x
        self.inner_rect_corner_upper_left_y = inner_rect_corner_upper_left_y
        self.inner_rect_corner_lower_right_x = inner_rect_corner_lower_right_x
        self.inner_rect_corner_lower_right_y = inner_rect_corner_lower_right_y
        self.cup_max_x = cup_max_x
        self.cup_max_y = cup_max_y
        self.view_centers = view_centers
        self.view_chunks_x = view_chunks_x
        self.view_chunks_y = view_chunks_y
        self.view_width = view_width
        self.view_length = view_length


def calc_rect(
        width: float = 1303.,
        length: float = 2384.,
        cup_diam: float = 40.,
        edge: float = 30.,
        space: float = 30.,
        view_edge: float = 5.,
        offset_x: float = 0.,
        offset_y: float = 0.
):
    inner_width = width - edge * 2.
    inner_length = length - edge * 2.
    inner_rect_corner_upper_left_x = -inner_width / 2.
    inner_rect_corner_upper_left_y = inner_length / 2.
    inner_rect_corner_lower_right_x = inner_width / 2.
    inner_rect_corner_lower_right_y = -inner_length / 2.

    cup_points = generate_circle_positions(width, length, cup_diam / 2., space, edge)
    alt_cup_points = generate_circle_positions(length, width, cup_diam / 2., space, edge)
    if len(cup_points) < len(alt_cup_points):
        cup_points = rotate_positions(alt_cup_points)

    cup_max_x, cup_max_y = find_largest_coordinates(cup_points)

    (view_centers, view_chunks_x, view_chunks_y, view_width, view_length) = calculate_views(width + 2. * view_edge,
                                                                                            length + 2. * view_edge,
                                                                                            view_size, offset_x,
                                                                                            offset_y)

    return RectCalc(inner_width, inner_length, cup_points, inner_rect_corner_upper_left_x,
                    inner_rect_corner_upper_left_y, inner_rect_corner_lower_right_x, inner_rect_corner_lower_right_y,
                    cup_max_x, cup_max_y, view_centers, view_chunks_x, view_chunks_y, view_width, view_length)


def generate_circle_positions(width: float, length: float, cup_rad: float, space: float, edge: float) -> (
        [(float, float)]):
    # TODO if we want hex puzzle: since we start with high ones we must take 2 and 2 cols increases, and we increase to 2 if it is above 1 col
    # n_edge_cups_width = (1. + int(edge / (cup_rad + space))) * math.sqrt(3.)
    # n_edge_cups_length = (1. + int(edge / (cup_rad + space)))
    # big_width = width + 2. * (cup_rad + space) * n_edge_cups_width
    # big_length = length + 2. * (cup_rad + space) * n_edge_cups

    # Effective radius with spacing
    effective_r = cup_rad + space / 2
    # Calculate the distance between circle centers in the x and y directions
    x_dist = 2 * effective_r * np.cos(np.pi / 6)
    y_dist = 2 * effective_r

    # Calculate the number of circles that can fit in width and height
    n_cols = int((width - 2 * edge) / x_dist)
    n_rows = int((length - 2 * edge) / y_dist)

    # Calculate the total used width and length
    used_width = (n_cols - 1) * x_dist + 2 * effective_r
    used_length = (n_rows - 1) * y_dist + 2 * effective_r

    # Calculate offsets to center the grid within the rectangle
    centering_x = (width - used_width) / 2
    centering_y = (length - used_length) / 2

    positions = []
    for i in range(n_rows):
        for j in range(n_cols):
            x = -width / 2 + centering_x + effective_r + j * x_dist
            y = -length / 2 + centering_y + effective_r + i * y_dist
            if j % 2 == 1:
                proposed_y = y + y_dist / 2
                max_y = length / 2 - centering_y - cup_rad
                if proposed_y <= max_y:
                    y = proposed_y
                else:
                    continue
            positions.append((x, y))

    # outside, inside = split_tuples_based_on_function(positions, partial(is_point_outside_rectangle, width=width, length=length))

    return positions


def is_point_outside_rectangle(x: float, y: float, width: float, length: float) -> bool:
    # Calculate the rectangle boundaries
    left_bound = -width / 2
    right_bound = width / 2
    top_bound = length / 2
    bottom_bound = -length / 2

    # Check if the point is outside the rectangle
    return x < left_bound or x > right_bound or y < bottom_bound or y > top_bound


def rotate_positions(positions):
    # Rotate positions 90 degrees
    rotated_positions = [(-y, x) for x, y in positions]
    return rotated_positions


def find_largest_coordinates(coordinates):
    # Initialize the largest x and y values
    largest_x = float('-inf')
    largest_y = float('-inf')

    # Iterate through each coordinate tuple in the array
    for x, y in coordinates:
        if x > largest_x:
            largest_x = x
        if y > largest_y:
            largest_y = y

    return largest_x, largest_y


def split_tuples_based_on_function(tuples: [(float, float)], boolean_function: Callable[[float, float], bool]) -> (
        [(float, float)], [(float, float)]):
    array_true = []
    array_false = []

    for a, b in tuples:
        if boolean_function(a, b):
            array_true.append((a, b))
        else:
            array_false.append((a, b))

    return array_true, array_false


# offset is extra width left/down (if negative) or right/up (if positive)
def calculate_views(width: float, length: float, view_size: float, offset_x: float, offset_y: float) -> (
        [((int, int), (float, float))], int, int, float, float):
    offset_width = width + math.fabs(offset_x)
    offset_length = length + math.fabs(offset_y)
    chunks_x = math.ceil(offset_width / view_size)
    chunks_y = math.ceil(offset_length / view_size)
    view_width = offset_width / chunks_x
    view_length = offset_length / chunks_y
    view_centers = []

    for i in range(int(chunks_x)):
        for j in range(int(chunks_y)):
            x_center = (view_width - offset_width) / 2. + i * view_width + offset_x / 2.
            y_center = (view_length - offset_length) / 2. + j * view_length + offset_y / 2.
            view_centers.append(((i, j), (x_center, y_center)))

    return view_centers, chunks_x, chunks_y, view_width, view_length


if __name__ == "__main__":
    print(calc_rect().__dict__)
