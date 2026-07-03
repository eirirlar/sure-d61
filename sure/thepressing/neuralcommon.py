from typing import List, Callable, Dict, Tuple

import numpy as np

import fluidio
from util import param_filters_indices, values_larger_than_filter
from validation import ValidationError

filename_collect = 'collect.csv'
filename_collect_full = 'collect_full.csv'

# maybe we want harder focus on time_to_crack?
press_fault_pred_weights_vals = list(fluidio.params_filters[1].values())


# Requires a semicolon separated file with floats as values with us number format. Each column can have a normalizer
# function passed to this function, but if it does not, the values of the column must already be normalized.
def load_norm_csv(filename_csv: str, normalizers: Dict[str, Callable[[float], float]] = {}) -> Tuple[
    List[str], List[List[float]]]:
    try:
        with open(filename_csv, 'r') as csv_file:
            split_lines = csv_file.read().splitlines()
            headers: List[str] = list(map(lambda h: h.strip(), split_lines[0].split(';')))
            tail_lines = split_lines[1:]
            normz = {key: normalizers.get(key, lambda f: f) for key in headers}
            csv: List[List[float]] = list(
                map(lambda l: normalize(list(map(lambda v: float(v), l.split(';'))), headers, normz), tail_lines))
            return headers, csv
    except Exception as e:
        print('Could not open ', filename_collect, ': ', e)
        raise e


def normalize(input: List[float], headers: List[str], normalizers: Dict[str, Callable[[float], float]] = {}) -> List[
    float]:
    normz = {key: normalizers.get(key, lambda f: f) for key in headers}
    return list(map(lambda iv: normz[headers[iv[0]]](iv[1]), enumerate(input)))


def retain_filter_csv(
        params_retained: List[str],
        params_output: List[str],
        param_filters: Dict[str, float],
        headers: List[str],
        csv: List[List[float]]) -> List[List[float]]:
    params_retained_indices = list(map(lambda r: headers.index(r), params_retained + params_output))
    pfi = param_filters_indices(headers, param_filters)
    csv_filtered = list(filter(lambda l: values_larger_than_filter(l, pfi), csv))
    csv_filtered_retained_with_output = list(
        map(lambda l: list(map(lambda g: l[g], params_retained_indices)), csv_filtered))
    return csv_filtered_retained_with_output


def describe_params_output(params_output: List[str]) -> str:
    return '__'.join(params_output)


def random_values(n_params: int, validator: Callable[[List[float]], bool] = lambda x: True) -> List[float]:
    i = 0
    while i < 100:
        vals = list(np.random.rand(n_params))
        if validator(vals):
            return vals
    raise ValidationError('Could not get a valid object')


def eval_press_fault_pred(press_fault_pred: dict) -> float:
    return max(0., min(1., np.average(list(press_fault_pred.values()), weights=press_fault_pred_weights_vals)))
