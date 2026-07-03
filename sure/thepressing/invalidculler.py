import fluidio
import hexfloatinput
from neuralcommon import load_norm_csv, filename_collect
from hexfloatinput import *
from util import delete_csv_rows


def cull_invalids():
    params, csv = load_norm_csv(filename_collect)
    rows_to_delete = []
    for (i, row) in enumerate(csv):
        if not valid(hexfloatinput.from_fluid_input(fluidio.from_values(row).input).validate()):
            rows_to_delete.append(i)
    print('deleting rows:', rows_to_delete)
    delete_csv_rows(filename_collect, rows_to_delete)


if __name__ == '__main__':
    cull_invalids()
