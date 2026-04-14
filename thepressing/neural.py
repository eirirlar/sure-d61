import os
import random
from datetime import datetime
from typing import List, Callable, Dict, Tuple

import numpy as np
import tensorflow as tf
from keras import Sequential
from keras_tuner.src.engine.hyperparameters.hyperparameters import HyperParameters
from keras_tuner.tuners import Hyperband
from sklearn.model_selection import train_test_split
from tensorflow import keras

import fluidio
import normalfloatinput
from neuralcommon import load_norm_csv, retain_filter_csv, describe_params_output, normalize, filename_collect, \
    random_values
from util import filename_output_neural_kerastuner, hash_numbers, filename_output_neural_model, accumulate_list_list, \
    values_larger_than_filter, param_filters_indices

seed = 69103928
np.random.seed(seed)
random.seed(seed)
tf.random.set_seed(seed)
data_size_min = 10
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
tf.get_logger().setLevel('WARNING')
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)


class Neural:
    models: List[Sequential]
    hashes: List[int]
    filename_models: List[str]
    filename_hashes: List[str]
    params_retained_accumulated: List[List[str]]

    def __init__(self,
                 params_retained_order: List[List[str]],
                 # first filter is irrelevant
                 params_filters: List[Dict[str, float]],
                 filename_csv: str,
                 normalizers: Dict[str, Callable[[float], float]] = {},
                 try_load: bool = True,
                 try_train: bool = True):
        filename_paths = list(
            map(lambda p: filename_output_neural_model + os.sep + describe_params_output(p),
                params_retained_order[1:]))
        for filename_path in filename_paths:
            try:
                os.makedirs(filename_path)
            except Exception:
                pass
        self.filename_models = list(map(lambda p: p + os.sep + 'model.keras', filename_paths))
        self.filename_hashes = list(map(lambda p: p + os.sep + 'hash', filename_paths))
        self.params_retained_order = params_retained_order
        self.normalizers = normalizers
        self.params_retained_accumulated = accumulate_list_list(params_retained_order)

        (headers, csv) = load_norm_csv(filename_csv, normalizers)
        csvs, hashes_new = csvs_hashes(self.params_retained_accumulated, params_retained_order, params_filters, headers,
                                       csv)
        self.hashes = hashes_new
        if try_load:
            try:
                self.models, self.hashes = self.load_models_hashes()
                if try_train:
                    for i, (o, n) in enumerate(zip(self.hashes, hashes_new)):
                        if o != n:
                            print('neural: CSVs changed for model', self.filename_models[i], 'retraining at',
                                  datetime.now())
                            m = train_detailed(self.params_retained_accumulated[i], params_retained_order[i + 1],
                                               csvs[i])
                            self.models[i] = m
                            self.hashes[i] = n
                            save_model_hash(self.filename_hashes[i], self.filename_models[i], n, m)
            except Exception as e:
                print('neural: Could not load models and hashes: ', e)
                if try_train:
                    print('neural: Training instead.')
                    self.models = train(self.params_retained_accumulated, params_retained_order, csvs)
                    self.save_models_hashes()
                else:
                    raise Exception('neural: Configured to load and not train, and could not load. Punting.')
        elif try_train:
            print('neural: Configured not to load, and train, training instead')
            self.models = train(self.params_retained_accumulated, params_retained_order, csvs)
            self.save_models_hashes()
        else:
            raise Exception('neural: Configured to not load and not train, punting')

    def save_models_hashes(self):
        for m, h, fm, fh in zip(self.models, self.hashes, self.filename_models, self.filename_hashes):
            if m is not None:
                save_model_hash(fh, fm, h, m)

    def load_models_hashes(self) -> Tuple[List[Sequential], List[int]]:
        models: List[Sequential] = []
        hashes: List[int] = []
        for f, z in zip(self.filename_models, self.filename_hashes):
            models.append(tf.keras.models.load_model(f))
            hashes.append(load_hash(z))
        return models, hashes

    # length of input must match model_index of params_retained_order.
    # input must be denormalized
    # returns a dict with the estimated params, which correspond to the params on index model_index+1 of params_retained_order
    def predict(self, model_index: int, input: List[float], do_norm: bool = False):
        norm_input = input
        if do_norm:
            headers = []
            for i in range(model_index + 1):
                headers += self.params_retained_order[i]
            norm_input = normalize(input, headers, self.normalizers)
        model = self.models[model_index]
        if model is not None:
            predictions = model.predict(np.asarray([norm_input]), verbose=0)[0]
            predictions_clamped = [min(1., max(0., p)) for p in predictions]
            return dict(zip(self.params_retained_order[model_index + 1], predictions_clamped))
        else:
            m = 'neural: model at index' + str(model_index) + ' is not trained (maybe too few data points?)'
            raise Exception(m)


def csvs_hashes(
        params_retained_accumulated: List[List[str]],
        params_retained_order: List[List[str]],
        params_filters: List[Dict[str, float]],
        headers: List[str],
        csv: List[List[float]]
) -> Tuple[List[List[List[float]]], List[int]]:
    csvs: List[List[List[float]]] = []
    hashes: List[int] = []
    for (param_retained_accumulated, params_output, param_filters) in list(
            zip(params_retained_accumulated, params_retained_order[1:], params_filters[1:] + [{}])):
        filter_csv = retain_filter_csv(param_retained_accumulated, params_output, param_filters, headers, csv)
        csvs.append(filter_csv)
        hashes.append(hash_numbers([hash_numbers(n) for n in filter_csv]))
    return csvs, hashes


def train(
        params_retained_accumulated: List[List[str]],
        params_retained_order: List[List[str]],
        csvs: List[List[List[float]]],
) -> List[Sequential]:
    models: List[Sequential] = []
    for (param_retained_accumulated, params_output, csv) in list(
            zip(params_retained_accumulated, params_retained_order[1:], csvs)):
        model = train_detailed(param_retained_accumulated, params_output, csv)
        models.append(model)
    return models


def train_detailed(
        params_retained: List[str],
        params_output: List[str],
        filter_csv: List[List[float]]
) -> Sequential:
    project_name = describe_params_output(params_output)
    csv_filtered_retained_with_output = np.asarray(
        filter_csv)
    m = len(params_retained)
    if data_size_min > len(csv_filtered_retained_with_output):
        return None
    x = csv_filtered_retained_with_output[:, :m]
    y = csv_filtered_retained_with_output[:, m:]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=seed)

    tuner_epochs = 500
    search_epochs = 5
    fit_epochs = 150
    fit_batch_size = 8

    # TODO comment in to make it run faster when testing
    # tuner_epochs = 5
    # search_epochs = 2
    # fit_epochs = 5
    # fit_batch_size = 2

    def build_model(hp: HyperParameters):
        modelbuilder = tf.keras.Sequential([
            tf.keras.layers.Dense(hp.Int('units_0', min_value=4, max_value=64, step=1), activation='relu',
                                  input_shape=(m,)),
        ])

        # n extra layers except the first is x-2
        for i in range(1, hp.Int('num_layers', 2, 5)):
            modelbuilder.add(tf.keras.layers.Dense(units=hp.Int('units_' + str(i), min_value=4, max_value=64, step=1),
                                                   activation='relu'))
        modelbuilder.add(tf.keras.layers.Dense(len(params_output), activation='linear'))

        modelbuilder.compile(optimizer=keras.optimizers.Adam(
            learning_rate=hp.Float('learning_rate', min_value=0.0001, max_value=0.01, sampling='log')),
            loss='mse')

        return modelbuilder

    tuner = Hyperband(build_model,
                      objective='val_loss',
                      max_epochs=tuner_epochs,
                      factor=3,
                      seed=seed,
                      directory=filename_output_neural_kerastuner,
                      project_name=project_name,
                      overwrite=True
                      )
    stop_early = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=20)
    tuner.search(x_train, y_train, epochs=search_epochs, validation_data=(x_test, y_test), callbacks=[stop_early],
                 verbose=0)
    best_hps = tuner.oracle.get_best_trials(num_trials=1)[0].hyperparameters
    model = tuner.hypermodel.build(best_hps)
    model.fit(x_train, y_train, epochs=fit_epochs, batch_size=fit_batch_size, validation_data=(x_test, y_test),
              verbose=0)
    loss = model.evaluate(x_test, y_test)
    print(f'neural: Hyperparam values: {best_hps.values}')
    print(f'neural: Mean Squared Error on Test Data: {loss}')
    return model


def load_hash(filename_hash: str):
    with open(filename_hash, 'r') as hash_file:
        return int(hash_file.readline().strip())


def save_hash(hash: int, filename_hash: str):
    with open(filename_hash, 'w') as hash_file:
        hash_file.write(str(hash))


def save_model_hash(fh: str, fm: str, h: int, m: Sequential):
    m.save(fm)
    save_hash(h, fh)


if __name__ == '__main__':
    #    n = Neural([*fluidio.params_order, fluidio.output_params], fluidio.params_filters, filename_collect,
    #               normalfloatinput.normalizers, False, True)
    n = Neural([*fluidio.params_order, fluidio.output_params], fluidio.params_filters, filename_collect,
               normalfloatinput.normalizers, True, False)
    pfi = param_filters_indices(fluidio.params, fluidio.params_filters[1])

    acc = []
    num = 300
    for i in range(num):
        vs = random_values(fluidio.n_params, normalfloatinput.validator_fluidio_vals)
        pressure_input = [vs[fluidio.params_to_index[f]] for f in fluidio.params_order[0]]
        press_fault_input = [vs[fluidio.params_to_index[f]] for f in
                             (fluidio.params_order[0] + fluidio.params_order[1])]
        pressure_pred = n.predict(0, pressure_input)['pressure']
        press_fault_input[-1] = pressure_pred
        press_fault_pred = n.predict(1, press_fault_input)
        for p, v in press_fault_pred.items():
            vs[fluidio.params_to_index[p]] = v
        if values_larger_than_filter(vs, pfi, 0.05):
            acc.append(press_fault_pred)
    num_passed = float(len(acc))
    perc_passed = num_passed / num
    print(perc_passed)
