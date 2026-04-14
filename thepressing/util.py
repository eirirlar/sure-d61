import hashlib
import inspect
import os
import struct
from itertools import islice
from typing import List, Dict, Union


filename_output = 'output'
filename_genetic = 'genetic'
filename_neural = 'neural'
filename_kerastuner = 'kerastuner'
filename_model = 'model'
filename_simulate = 'simulate'
filename_kfiles = 'kfiles'
filename_current = 'current'

filename_output_simulate = filename_output + os.sep + filename_simulate
filename_output_genetic = filename_output + os.sep + filename_genetic
filename_output_neural = filename_output + os.sep + filename_neural
filename_output_neural_kerastuner = filename_output_neural + os.sep + filename_kerastuner
filename_output_neural_model = filename_output_neural + os.sep + filename_model
filename_output_simulate_current = filename_output_simulate + os.sep + filename_current
filename_output_simulate_kfiles = filename_output_simulate + os.sep + filename_kfiles


def param_names(cls: type, n: int = -1) -> list:
    keys = list(inspect.signature(cls.__init__).parameters.keys())
    if -1 == n:
        n = len(keys) - 1
    return keys[1:n + 1]


def param_indices(input_param_names: []):
    return list(map(lambda pn: input_param_names.index(pn), input_param_names))


def values(value_class) -> List:
    return list(value_class.__dict__.values())


def tail(filename: str, lines: int):
    f = open(filename, 'rb')
    total_lines_wanted = lines

    block_size = 1024
    f.seek(0, 2)
    block_end_byte = f.tell()
    lines_to_go = total_lines_wanted
    block_number = -1
    blocks = []
    while lines_to_go > 0 and block_end_byte > 0:
        if (block_end_byte - block_size > 0):
            f.seek(block_number * block_size, 2)
            blocks.append(f.read(block_size))
        else:
            f.seek(0, 0)
            blocks.append(f.read(block_end_byte))
        lines_found = blocks[-1].count(b'\n')
        lines_to_go -= lines_found
        block_end_byte -= block_size
        block_number -= 1
    all_read_text = b''.join(reversed(blocks))
    return b'\n'.join(all_read_text.splitlines()[-total_lines_wanted:])


def sliding(seq, n=2):
    yield list(islice(iter(seq), n))


def flatten(l):
    return [item for sublist in l for item in sublist]


def param_filters_indices(headers: List[str], param_filters: Dict[str, float]) -> Dict[int, float]:
    return {headers.index(k): v for k, v in param_filters.items()}


def values_larger_than_filter(l: List[float], pfi: Dict[int, float], filter_leniency: float = 0.) -> bool:
    return not any((lambda i, v: l[i] < v * (1. - filter_leniency))(i, v) for i, v in pfi.items())


def create_params_str(ps: List[str]) -> str:
    return ';'.join(map(lambda v: '{: >20}'.format(str(v)), ps)) + '\n'


def recreate_file(filename: str):
    try:
        os.remove(filename)
    except Exception as e:
        print('could not remove file', e)
    try:
        with open(filename, 'w'):
            pass
    except Exception as e:
        print('could not create file', e)


def hash_numbers(ints: List[Union[int, float]]) -> int:
    bytes_representation = b''.join(struct.pack('!d', f) for f in ints)
    sha256_hash = hashlib.sha256(bytes_representation).digest()
    hashed_value_as_integer = int.from_bytes(sha256_hash, byteorder='big') & 0xFFFFFFFF
    return hashed_value_as_integer


def accumulate_list_list(ll: List[List]):
    acc = []
    all = []
    for l in ll:
        acc += l
        all.append(acc.copy())
    return all


def delete_csv_rows(filename: str, rows_to_delete: List[int]):
    with open(filename, 'r+') as f:
        lines = f.readlines()
        for row_to_delete in sorted(rows_to_delete, reverse=True):
            # +1 because we skip header line
            del lines[row_to_delete + 1]
        f.seek(0)
        f.truncate()
        f.writelines(lines)
