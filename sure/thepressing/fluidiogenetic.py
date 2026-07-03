import random
from itertools import repeat
from typing import Sequence, Dict, List

import numpy as np
from deap import base, creator, tools

import hexfloatinput
import hexfloatmodel
import floatoutput
from floatoutput import FloatOutput
import fluidio
import normalfloatinput
import normalfloatoutput
from neural import Neural
from neuralcommon import filename_collect, eval_press_fault_pred, random_values
from util import values_larger_than_filter, param_filters_indices
from validation import ValidationError

fitness_weights_default = floatoutput.FloatOutput(
    area=2.,
    weight=2.,
    volume=2.,
    thermal_conductivity=1.,
    connector_stress=1.,
    structural_integrity=1.,
    press_fault=10.
)
params = fluidio.params_acc[1]
index_to_params: Dict[int, str] = dict((i, h) for i, h in enumerate(params))
params_to_index: Dict[str, int] = dict((h, i) for i, h in enumerate(params))
n_params = len(params)
pfi = param_filters_indices(fluidio.params, fluidio.params_filters[1])


# The input headers is params_acculmulated[1]
def genetic_fluidio(
        population_size: int = 50,
        generations: int = 20,
        fitness_weights: FloatOutput = fitness_weights_default,
        verbose: bool = False
) -> fluidio.FluidInput:
    print('fluidiogenetic: Start')
    fitness_weights_vals = list(fitness_weights.__dict__.values())

    neu: Neural = None
    try:
        neu = Neural([*fluidio.params_order, fluidio.output_params], fluidio.params_filters,
                     filename_collect,
                     normalfloatinput.normalizers, True, False)
    except Exception as e:
        print('fluidiogenetic: Could not create Neural object, reverting to calculated fitness for press_fault')

    def eval_individual(individual):
        try:
            nfio = param_vals_to_fio(individual)
            nfi = normalfloatinput.from_fluid_input(nfio.input)
            nfo = normalfloatoutput.create(hexfloatmodel.create(nfi.denorm()).calc_fitness(nfi))
            if neu:
                press_fault_pred = neu.predict(1, individual)
                nfo.press_fault = eval_press_fault_pred(press_fault_pred)
            nfo.weight = 1. - nfo.weight
            # fs = tuple(nfo.__dict__.values())
            # return fs
            fs = list(nfo.__dict__.values())
            f = np.average(fs, weights=fitness_weights_vals)
            return (f,)
        except ValidationError:
            # return tuple(0 for _ in range(len(floatoutput.params)))
            return (0.,)

    def random_float_vals():
        n_to_fail = 2000
        n_to_fallback = int(n_to_fail / 2)
        filter_dev = 0.05
        filter_dev_max = 0.5
        filter_dev_inc = 0.01
        inc_filter_every = 20
        i = 0
        while i < n_to_fail:
            if 0 != i and 0 == i % inc_filter_every and filter_dev < filter_dev_max:
                filter_dev += filter_dev_inc
            individual = random_values(n_params, validator)
            if neu:
                pressure_input = individual[:-1]
                individual[-1] = neu.predict(0, pressure_input)['pressure']
            else:
                individual[-1] = fluidio.calculate_pressure(param_vals_to_fio(individual).values())
            if neu and i < n_to_fallback:
                press_fault_pred = neu.predict(1, individual)
                nfio = param_vals_to_fio(individual)
                nfio.output = fluidio.FluidOutput(**press_fault_pred)
                if values_larger_than_filter(nfio.values(), pfi, filter_dev):
                    return individual
            else:
                nfio = param_vals_to_fio(individual)
                nfio.input.alu_thick = 1.
                nfio.input.cup_lip = 1.
                nfi = normalfloatinput.from_fluid_input(nfio.input)
                nfo = normalfloatoutput.create(hexfloatmodel.create(nfi.denorm()).calc_fitness(nfi))
                if 1. - filter_dev < nfo.press_fault:
                    return individual
            i += 1
        raise Exception('fluidiogenetic: Could not obtain random vals that validate')

    # Define the problem as a maximization problem
    # creator.create("FitnessMax", base.Fitness, weights=tuple(fitness_weights_vals))
    creator.create("FitnessMax", base.Fitness, weights=(1.,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    # Define genetic operators
    toolbox = base.Toolbox()
    toolbox.register("individual", tools.initIterate, creator.Individual, random_float_vals)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", eval_individual)
    toolbox.register("mate", tools.cxSimulatedBinaryBounded, eta=1., low=0., up=1.)
    toolbox.register("mutate", mutGaussian, mu=0, sigma=0.01, indpb=0.2)
    toolbox.register("select", tools.selNSGA2)

    population = toolbox.population(n=population_size)
    crossover_prob, mutation_prob = 0.2, 0.65

    # Evaluate the entire population
    fitnesses = list(map(toolbox.evaluate, population))
    for ind, fit in zip(population, fitnesses):
        ind.fitness.values = fit

    if verbose: print("  Evaluated %i individuals" % len(population))

    for gen in range(generations):
        if verbose: print("-- Generation %i --" % gen)

        # Select the next generation individuals
        offspring = toolbox.select(population, len(population))

        # Clone the selected individuals
        offspring = list(map(toolbox.clone, offspring))

        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if random.random() < crossover_prob:
                toolbox.mate(child1, child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random() < mutation_prob:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        # Evaluate offspring individuals
        fitnesses = list(map(toolbox.evaluate, offspring))
        for ind, fit in zip(offspring, fitnesses):
            ind.fitness.values = fit

        # Replace the old population by the offspring
        population[:] = offspring

        # Gather all the fitnesses in one list and print the stats
        fits = [ind.fitness.values[-1] for ind in population]

        length = len(population)
        mean = sum(fits) / length
        sum2 = sum(x * x for x in fits)
        std = abs(sum2 / length - mean ** 2) ** 0.5

        if verbose:
            print("  Min %s" % min(fits))
            print("  Max %s" % max(fits))
            print("  Avg %s" % mean)
            print("  Std %s" % std)

    best_ind = tools.selBest(population, 1)[0]
    print('fluidiogenetic: Done with fitness', best_ind.fitness.values)
    return param_vals_to_fio(list(best_ind)).input


def mutGaussian(individual, mu, sigma, indpb):
    """Copied from deap.tools.mutation, modified."""
    size = len(individual)
    if not isinstance(mu, Sequence):
        mu = repeat(mu, size)
    elif len(mu) < size:
        raise IndexError("mu must be at least the size of individual: %d < %d" % (len(mu), size))
    if not isinstance(sigma, Sequence):
        sigma = repeat(sigma, size)
    elif len(sigma) < size:
        raise IndexError("sigma must be at least the size of individual: %d < %d" % (len(sigma), size))

    for i, m, s in zip(range(size), mu, sigma):
        if random.random() < indpb:
            # force it between 0 and 1
            j = 0
            ig = individual[i] + random.gauss(m, s)
            while (ig < 0. or 1. < ig) and j < 10:
                ig = individual[i] + random.gauss(m, s)
                j += 1
            individual[i] = ig
            if individual[i] < 0.:
                individual[i] = 0.
            elif 1. < individual[i]:
                individual[i] = 1.
    return individual,


def param_vals_to_fio(vs: List[float]) -> fluidio.FluidInputOutput:
    fio_vals = []
    for p in fluidio.params:
        v: float
        if p in params:
            v = vs[params_to_index[p]]
        else:
            v = 0.
        fio_vals.append(v)
    return fluidio.from_values(fio_vals)


def validator(vs: List[float]) -> bool:
    return normalfloatinput.validator_fluidio_vals(param_vals_to_fio(vs).values())


def fluidio_generator(*args) -> List[float]:
    return fluidio.FluidInputOutput(genetic_fluidio()).values()


if __name__ == "__main__":
    fw = floatoutput.FloatOutput(
        area=2.,
        weight=2.,
        volume=2.,
        thermal_conductivity=1.,
        connector_stress=1.,
        structural_integrity=1.,
        press_fault=10.
    )
    best_ind = genetic_fluidio(50, verbose=True, fitness_weights=fw)
    fi = hexfloatinput.from_fluid_input(normalfloatinput.denormalize_fluid_input(best_ind))
    print('fluidiogenetic: best float:', fi.__dict__)
