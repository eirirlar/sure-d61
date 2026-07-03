import math
import random
from typing import List, Dict, Callable, Tuple

import fluidiogenetic
import fluidio
import normalfloatinput
from neural import Neural
from neuralcommon import load_norm_csv
from util import flatten, param_filters_indices, values_larger_than_filter, create_params_str

param_impr = 0.01
param_impr_small = param_impr / 10.
filter_leniency = 0.05


# paretoptimizer does not know anything about floats or fluidio, it is generic
# when used from fluidsimulator, headers are the fluidio headers (not normalfloatinput). The fallback_generator must
# take this into account
def pareto_optimize(
        headers: List[str],
        params_order: List[List[str]],
        params_increasable: List[str],
        params_filters: List[Dict[str, float]],
        filename_csv: str,
        # n_params: int, validator: Callable[[List[float]], bool]] -> param_values:List[float].
        # Must produce normed values that are valid. Validator must validate normed values
        values_generator: Callable[[Callable[[List[float]], bool]], List[float]],
        normalizers: Dict[str, Callable[[float], float]] = {},
        denormalizers: Dict[str, Callable[[float], float]] = {},
        # param_values:List[float] -> bool (True if valid). param_values must be denormed
        validator: Callable[[List[float]], bool] = lambda x: True,
        calculations: Dict[str, Tuple[List[str], Callable[[List[float]], float]]] = {}
):
    if any(not po for po in params_order):
        raise Exception('params order must only have elements which are non-empty lists')
    input_params = flatten(params_order)
    csv_headers: List[str]
    csv: List[List[float]]
    try:
        csv_headers, csv = load_norm_csv(filename_csv, normalizers)
    except Exception as e:
        print('pareto_optimizer: creating file because could not load', filename_collect, e)
        with open(filename_collect, 'w') as collect_file:
            collect_file.write(create_params_str(headers))
            csv = []
            csv_headers = headers
    if headers != csv_headers:
        raise Exception('pareto_optimizer: headers != csv_headers')
    if any(x for x in input_params if x not in headers):
        raise Exception(
            'some params in params_order were not in csv headers\n' + str(input_params) + '\n' + str(headers))
    params_filters_indexed: List[Dict[int, float]] = list(
        map(lambda p: param_filters_indices(headers, p), params_filters))
    index_to_header: Dict[int, str] = dict((i, p) for i, p in enumerate(headers))
    header_to_index: Dict[str, int] = dict((p, i) for i, p in enumerate(headers))
    if not all(c for c in csv if validator(c)):
        raise Exception('invalid objects in ', filename_csv)

    def validator_normed(normed_vals: List[float]) -> bool:
        return validator(denorm_values(normed_vals, index_to_header, denormalizers))

    num_rows = len(csv)
    cur_val_min = 0.
    cur_val_max = 1.
    prev_params: List[str] = []
    cur: List[float] = None
    if 0 < num_rows:
        cur = csv[num_rows - 1]
    cur_param: str = None
    cur_val: float
    cur_index: int = 0
    cur_row_param = None
    cur_row_val = None
    cur_row_val_min = cur_val_min
    cur_row_val_max = cur_val_max
    new_val: float
    # these represent the actual lines in the file, not index in csv (which is one off)
    delete_rows: List[int] = []
    # the index of the params_order of the changing param of the last change
    param_level = 0

    def params_calculator(vs: List[float],
                          calcs: Dict[str, Tuple[List[str], Callable[[List[float]], float]]] = calculations
                          ) -> List[float]:
        calced = vs.copy()
        calc_param: str
        for (calc_param, calc_input_func) in calcs.items():
            calc_input: List[str]
            calc_func: Callable[[List[float]], float]
            calc_input, calc_func = calc_input_func
            # input_vals = [c for i, c in enumerate(calced) if index_to_header[i] in calc_input]
            calced_val = calc_func(calced)
            calced[header_to_index[calc_param]] = calced_val
        return calced

    def set_cur(new_param: str = None):
        nonlocal cur_param
        nonlocal cur_val
        nonlocal cur_row_param
        nonlocal cur_row_val
        nonlocal param_level
        if cur_param is None:
            if new_param is None:
                new_param = random_param(params_order, param_level, prev_params)
            cur_param = new_param
            cur_val = cur[header_to_index[cur_param]]
            param_level = params_order_index(new_param, params_order)
            if cur_row_param is None:
                cur_row_param = cur_param
                cur_row_val = cur_val

    def fallback_return() -> Tuple[List[float], List[int]]:
        return denorm_values(params_calculator(values_generator(validator_normed)), index_to_header,
                             denormalizers), delete_rows

    def add_deleted(deleted: int):
        delete_rows.append(deleted)

    n_params = len(headers)
    if 0 == num_rows:
        print('pareto_optimize: no prev rows, return random_values')
        return fallback_return()
    elif 1 == num_rows:
        set_cur()
    else:
        i = num_rows - 1
        while 0 < i:
            prev = csv[i - 1]
            prevprev = prev
            if 1 < i:
                prevprev = csv[i - 2]
            row = csv[i]
            d: List[str] = diff_without_expecteds(prev, row, index_to_header, calculations, input_params,
                                                  param_impr_small)
            dd: List[str] = diff_without_expecteds(prevprev, prev, index_to_header, calculations, input_params,
                                                   param_impr_small)

            def handle_val_change():
                nonlocal cur_row_val_min
                nonlocal cur_row_val_max
                nonlocal cur_val_min
                nonlocal cur_val_max
                prev_val = prev[header_to_index[cur_row_param]]
                if prev_val < cur_row_val:
                    last_cur_row_val_min = cur_row_val_min
                    if prev_val < cur_row_val_min:
                        if len(d) == 1 and 0. < last_cur_row_val_min and 0 < i:
                            add_deleted(i - 1)
                    else:
                        cur_row_val_min = prev_val
                else:
                    last_cur_row_val_max = cur_row_val_max
                    if cur_row_val_max < prev_val:
                        if len(d) == 1 and last_cur_row_val_max < 1. and 0 < i:
                            add_deleted(i - 1)
                    else:
                        cur_row_val_max = prev_val

                if cur_param == cur_row_param and 0 == cur_index:
                    cur_val_min = cur_row_val_min
                    cur_val_max = cur_row_val_max

            def handle_param_change(row_param: str):
                nonlocal cur_row_param
                nonlocal cur_row_val
                nonlocal cur_row_val_min
                nonlocal cur_row_val_max
                if row_param not in prev_params and \
                        cur_index == 0 and \
                        cur_param != row_param:
                    prev_params.append(row_param)
                cur_row_param = row_param
                cur_row_val = row[header_to_index[row_param]]
                cur_row_val_min = 0.
                cur_row_val_max = 1.

            def search_earlier_branch():
                nonlocal i
                nonlocal prev
                nonlocal delete_rows
                nonlocal d
                new_param = None

                j = i - 2
                maybe_delete_rows = []  # dont include i-1, we want some bad samples right under pareto front
                d2 = []
                while 0 < j:
                    earlier = csv[j]
                    d2 = list(set(d2 + diff_without_expecteds(earlier, row, index_to_header, calculations, input_params,
                                                              param_impr_small)))
                    if 1 == len(d2):
                        new_param = next(iter(d2))
                        d = d2
                        prev = earlier
                        for dr in maybe_delete_rows:
                            add_deleted(dr)
                        i = j + 1
                        print('pareto_optimize: found branching point at index ', j)
                        break
                    maybe_delete_rows.append(j)
                    j -= 1
                return new_param

            if 1 == len(d):
                row_param = next(iter(d))
                set_cur(row_param)
                if row_param != cur_row_param:
                    handle_param_change(row_param)
                    handle_val_change()
                else:
                    handle_val_change()
            elif 2 == len(d):
                new_param = None
                if cur_row_val is not None:
                    diffs_except_cur_row = [p for p in d if p != cur_row_param]
                    if 2 == len(diffs_except_cur_row):
                        hld = highest_level_diffs(diffs_except_cur_row, params_order)
                        new_param = hld[0]
                        if 0 == cur_index:
                            if 1 == len(hld):
                                prev_params.append(next(filter(lambda p: p != new_param, diffs_except_cur_row)))
                            else:
                                prev_params.append(hld[1])
                    else:
                        new_param = diffs_except_cur_row[0]
                else:
                    hld = highest_level_diffs(d, params_order)
                    if 1 == len(hld):
                        new_param = hld[0]
                    else:
                        d_dd_overlap = [x for x in d if x in dd]
                        if 1 == len(d_dd_overlap):
                            new_param = d_dd_overlap[0]
                        elif 2 == len(d_dd_overlap):
                            hld = highest_level_diffs(d, params_order)
                            if 1 == len(hld):
                                new_param = hld[0]
                if new_param is None:
                    if 1 < i:
                        new_param = search_earlier_branch()
                if new_param is None:
                    print('pareto_optimize: chose random new_param')
                    new_param = random.choice(d)
                if cur_row_val is None:
                    row_param = next(filter(lambda param: param != new_param, d))
                    set_cur(row_param)
                handle_val_change()
                handle_param_change(new_param)
            else:
                new_param = search_earlier_branch()
                set_cur(new_param)
                if new_param is None:
                    if 0 == cur_index:
                        cur_index = i - 1
                else:
                    handle_val_change()
                    handle_param_change(new_param)
                cur_row_val_min = 0.
                cur_row_val_max = 1.
                # cur_row_param = None
                # cur_row_val = None
            i -= 1
    print('pareto_optimize: delete_rows:', delete_rows)

    j = 1
    while True:
        params = params_order[param_level]
        cur_params_increasable = [p for p in params if p in params_increasable]
        new_val = improve_param(cur_val, j, cur, cur_param, cur_val_min, cur_val_max, cur_params_increasable,
                                # object_to_dict,
                                params_filters_indexed[param_level])
        val_diff = abs(new_val - cur_val)
        if val_diff < param_impr:
            if cur_param not in prev_params:
                prev_params.append(cur_param)
            param_level_exhausted = all(p in prev_params for p in params)
            param_level_is_last = param_level == len(params_order) - 1
            if param_level_exhausted:
                if param_level_is_last:
                    return fallback_return()
                else:
                    param_level += 1
                    cur_param = random_param(params_order, param_level, prev_params)

                    i = num_rows - 1
                    diff_wo_exp_acc = []
                    while 0 < i:
                        prev = csv[i - 1]
                        row = csv[i]
                        d = diff_without_expecteds(prev, row, index_to_header, calculations, input_params,
                                                   param_impr_small)
                        diff_wo_exp_acc = list(set(d + diff_wo_exp_acc))
                        acceptable_vals = values_larger_than_filter(row, params_filters_indexed[param_level],
                                                                    filter_leniency)
                        acceptable_diff = 1 == len(diff_wo_exp_acc)
                        if acceptable_diff and acceptable_vals:
                            print('pareto_optimizer: Found an earlier row with acceptable diff and vals, replacing cur')
                            cur = row
                            break
                        i -= 1

                    cur_val = cur[header_to_index[cur_param]]
                    cur_val_min = 0.
                    cur_val_max = 1.
                    j = 1
            else:
                cur_param = random_param(params_order, param_level, prev_params)
                cur_val = cur[header_to_index[cur_param]]
                cur_val_min = 0.
                cur_val_max = 1.
                j = 1
        else:
            new_values = cur.copy()
            new_values[header_to_index[cur_param]] = new_val
            calcs_without_cur_or_prevs = {k: v for k, v in calculations.items() if
                                          k != cur_param and k not in prev_params}
            new_values_denormed = denorm_values(params_calculator(new_values, calcs_without_cur_or_prevs),
                                                index_to_header,
                                                denormalizers)
            if validator(new_values_denormed):
                print('pareto_optimize: return object with improved ', cur_param, ', with prev improved params: ',
                      prev_params)
                return (new_values_denormed, delete_rows)
            else:
                print('pareto_optimize: alas, it did not validate')
                j += 1


def random_param(params_order: List[List[str]], params_level: int = 0, prevs: List[str] = []) -> str:
    # return 'cup_angle'
    untaken_params = [x for x in params_order[params_level] if x not in prevs]
    if not untaken_params:
        if params_level == len(params_order) - 1:
            raise Exception('pareto_optimizer: cannot chose random param, all exhausted')
        params_level += 1
        untaken_params = [x for x in params_order[params_level] if x not in prevs]
    return random.choice(untaken_params)


def diff_without_expecteds(fio1: List[float], fio2: List[float],
                           index_to_header: Dict[int, str],
                           calcs: Dict[str, Tuple[List[str], Callable[[List[float]], float]]],
                           params: List[str] = None,
                           abs_tol: float = 0.01) -> List[str]:
    diffs = diff_values(fio1, fio2, index_to_header, params, abs_tol)
    expecteds = expected_diffs(diffs, calcs)
    diff_wo_expecteds = [d for d in diffs if d not in expecteds]
    return diff_wo_expecteds


def diff_values(fio1: List[float], fio2: List[float],
                index_to_header: Dict[int, str],
                params: List[str] = None,
                abs_tol: float = 0.01):
    return [index_to_header[i] for i, z in enumerate(zip(fio1, fio2)) if
            index_to_header[i] in params and not math.isclose(z[0], z[1], abs_tol=abs_tol)]


def expected_diffs(diff: List[str], calcs: Dict[str, Tuple[List[str], Callable[[List[float]], float]]]):
    return [calc_param for calc_param, calc_input_func in calcs.items() if any(i in diff for i in calc_input_func[0])]


def highest_level_diffs(diff: List[str], params_order: List[List[str]]) -> List[str]:
    diff_indexed = list(map(lambda p: (p, params_order_index(p, params_order)), diff))
    highest_param_level = max(diff_indexed, key=lambda x: x[1])[1]
    params_in_highest_level = list(map(lambda x: x[0], filter(lambda x: x[1] == highest_param_level, diff_indexed)))
    return params_in_highest_level


def denorm_values(values: List[float],
                  index_to_header: Dict[int, str],
                  denormalizers: Dict[str, Callable[[float], float]]
                  ) -> List[float]:
    return list(denormalizers.get(index_to_header[i], lambda v: v)(v) for i, v in enumerate(values))


def params_order_index(param: str, params_order: List[List[str]]) -> int:
    try:
        return next(i for i, ps in enumerate(params_order) if param in ps)
    except StopIteration:
        return -1


def improve_param(cur_val: float, step: int, cur: List[float], cur_param: str, cur_val_min: float,
                  cur_val_max: float,
                  increasable_params: List[str],
                  params_filter_indexed: Dict[int, float]):
    frac = 1. / 2. ** step
    cur_val_frac = cur_val * (1. - frac)
    new_val: float

    optimal = values_larger_than_filter(cur, params_filter_indexed)
    if optimal:
        # make runtime worse
        if cur_param in increasable_params:
            new_val = cur_val_min * frac + cur_val_frac
        else:
            new_val = cur_val_max * frac + cur_val_frac
    else:
        # make runtime better
        if cur_param in increasable_params:
            new_val = (cur_val_max * frac + cur_val_frac)
        else:
            new_val = (cur_val_min * frac + cur_val_frac)
    return new_val


if __name__ == '__main__':
    from fluidio import params_order, params_filters,  all_increasable_params, params, \
        calculate_pressure
    from hexfloatinput import validator_fluidio_vals
    from neuralcommon import filename_collect
    from normalfloatinput import normalizers, denormalizers

    n = Neural([*fluidio.params_order, fluidio.output_params], fluidio.params_filters, filename_collect,
               normalfloatinput.normalizers, True, False)


    def calc_pressure(vs: List[float]) -> float:
        pressure_input = [vs[fluidio.params_to_index[f]] for f in fluidio.params_order[0]]
        pressure: float
        try:
            pressure = n.predict(0, pressure_input)['pressure']
        except Exception:
            pressure = calculate_pressure(vs)
        return pressure


    calculations: Dict[str, Tuple[List[str], Callable[[List[float]], float]]] = {
        'pressure': (fluidio.params_order[0], calc_pressure)
    }

    p, d = pareto_optimize(
        params,
        params_order,
        all_increasable_params,
        params_filters,
        filename_collect,
        fluidiogenetic.fluidio_generator,
        normalizers,
        denormalizers,
        validator_fluidio_vals,
        calculations
    )
    vals_str = str(list(map(lambda f: '{: >20}'.format(f), p)))
    print(vals_str[1:len(vals_str) - 1].replace(', ', ';').replace('\'', ''))
