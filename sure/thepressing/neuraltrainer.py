import time

from fluidio import params_order, output_params, params_filters
from neural import Neural
from neuralcommon import filename_collect
from normalfloatinput import normalizers
from datetime import datetime

def train_neural(sleep_seconds: int = 6, alive_print_interval_seconds=60):
    print('neuraltrainer: running')
    t0 = time.time()
    while True:
        secs_passed_capped = (time.time() - t0) % alive_print_interval_seconds
        if alive_print_interval_seconds - sleep_seconds < secs_passed_capped:
            print('neuraltrainer: still running at', datetime.now())
        Neural([*params_order, output_params], params_filters, filename_collect, normalizers, True)
        time.sleep(sleep_seconds)


if __name__ == '__main__':
    train_neural()
