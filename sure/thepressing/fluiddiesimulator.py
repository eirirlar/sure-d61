import os

import fluidiogenetic
import hexfloatinput
import hexfloatmodel
import fluidio
from fluidneural import predict_pressure
from neural import Neural

FREECAD_BIN_PATH = 'C:\\dev\\freecad\\bin'
FREECAD_BIN_LIB_SITEPACKAGES_PATH = 'C:\\dev\\freecad\\bin\\Lib\\site-packages'
import sys

sys.path.append(FREECAD_BIN_PATH)
sys.path.append(FREECAD_BIN_LIB_SITEPACKAGES_PATH)

from fluidio import params_order, params_filters, from_values, all_increasable_params, params
from hexfloatinput import validator_fluidio_vals
from normalfloatinput import normalizers, denormalizers
from paretooptimizer import pareto_optimize
from typing import List, Dict, Callable, Tuple, Optional
import re
import shutil
from validation import ValidationError
from util import filename_output_simulate_kfiles, filename_output_simulate_current, filename_output, recreate_file, \
    create_params_str, delete_csv_rows
from neuralcommon import filename_collect, load_norm_csv, retain_filter_csv, filename_collect_full, random_values
import freecadfluidandpunchdie


def fluid_die_simulator(perform_deletions: bool = True):
    print('fluid_die_simulator: Running')
    i = get_collect_size()
    get_collect_size(filename_collect_full)
    neu: Neural = None

    def fallback_generator(validator: Callable[[List[float]], bool]) -> List[float]:
        func_name: str
        func: Callable[[Callable[[List[float]], bool]], List[float]]
        #if i % 2 < 1:
        #    func_name = 'random_values'
        #    func = lambda validator: random_values(fluidio.n_params, validator)
        #else:
            # 2/3 chance
        func_name = 'genetic_float'
        func = fluidiogenetic.fluidio_generator
        print('fluiddiesimulator: pareto_optimize falling back to', func_name)
        return func(validator)

    calculations: Dict[str, Tuple[List[str], Callable[[List[float]], float]]] = {
        'pressure': (fluidio.params_order[0], lambda vs: predict_pressure(vs, neu))
    }

    # float_model_func may recommend deletions of previous tests.
    float_model_func = lambda: pareto_optimize(
        params,
        params_order,
        all_increasable_params,
        params_filters,
        filename_collect,
        fallback_generator,
        normalizers,
        denormalizers,
        validator_fluidio_vals,
        calculations)

    while True:
        try:
            print('fluid_die_simulator: i =', i)

            (fluidio_values, rows_to_delete) = float_model_func()
            fio = from_values(fluidio_values)
            float_model = hexfloatmodel.create(hexfloatinput.from_fluid_input(fio.input))

            # deletions
            if perform_deletions:
                i = handle_deletions(i, rows_to_delete)

            fcm = freecadfluidandpunchdie.FreecadFluidAndPunchDie(float_model)
            fcm.generate_lsrun_failtime(
                fc=False,
                stp=False,
                stl=False,
                img=True,
                lsdyn=True,
                bottom=False,
                stats=True,
                runtime=freecadfluidandpunchdie.runtime_default)

            if not os.path.exists(filename_output_simulate_kfiles):
                os.makedirs(filename_output_simulate_kfiles, exist_ok=True)
            kfiles_subfolder2 = filename_output_simulate_kfiles + os.sep + filename_output + '_' + str(
                int(fio.input_hash))
            if os.path.exists(kfiles_subfolder2):
                shutil.rmtree(kfiles_subfolder2)
            print('fluiddiesimulator: Moving current to ', kfiles_subfolder2)
            shutil.move(filename_output_simulate_current, kfiles_subfolder2)
            if not os.path.exists(kfiles_subfolder2):
                print('fluiddiesimulator: WARN: move failed')

            os.makedirs(filename_output_simulate_current, exist_ok=True)
            i += 1
        except ValidationError as e:
            print(e.args[1])


def handle_deletions(i, rows_to_delete):
    hashes = get_collect_hashes(filename_collect)
    index_to_hash: Dict[int, int] = {i: h for i, h in enumerate(hashes)}
    hashes_to_delete = [index_to_hash[r] for r in rows_to_delete]
    i -= len(rows_to_delete)
    if 0 < len(rows_to_delete):
        print('i =', i, '(updated i after deletions)')
    delete_csv_rows(filename_collect, rows_to_delete)
    for hash_to_delete in hashes_to_delete:
        kfiles_subfolder = filename_output_simulate_kfiles + os.sep + filename_output + '_' + str(
            hash_to_delete)
        if os.path.exists(kfiles_subfolder):
            print('fluiddiesimulator: deleting kfiles_subfolder', kfiles_subfolder)
            shutil.rmtree(kfiles_subfolder)
    return i


def get_collect_size(filename: str = filename_collect, touch: bool = True) -> int:
    try:
        with open(filename, 'r') as collect_file:
            i = len(collect_file.readlines())
            if 0 == i:
                raise Exception('Found collect.csv file without headers')
            return i - 1
    except:
        if touch:
            recreate_file(filename)
            with open(filename, 'w') as collect_file:
                collect_file.write(create_params_str(params))
        return 0


def get_collect_hashes(filename_collect: str) -> List[int]:
    headers, csv = load_norm_csv(filename_collect)
    hashes_list = retain_filter_csv(['input_hash'], [], {}, headers, csv)
    hashes = [int(h[0]) for h in hashes_list]
    return hashes


def ns_below(ns: List[int], n: int) -> int:
    count = 0
    for num in ns:
        if num < n:
            count += 1
    return count


def ns_from_folders():
    ns = []
    for root, dirs, files in os.walk(filename_output_simulate_kfiles):
        for dir_name in dirs:
            match = re.search(r'\d+$', dir_name)
            if match:
                ns.append(int(match.group()))
    ns.sort()
    return ns


if __name__ == '__main__':
    fluid_die_simulator()
#    rows_to_delete = [557, 556, 555, 553, 552, 551]
#    handle_deletions(560, rows_to_delete)
