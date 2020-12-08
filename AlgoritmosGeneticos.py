import random
import numpy
import math

from deap import base
from deap import creator
from deap import tools
from deap import algorithms

class AlgoritmosGeneticos:
    def config_1(self, typeRandom, varMinimo, varMaximo, evaluate):
        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMin)

        toolbox = base.Toolbox()
        # Attribute generator
        toolbox.register("attr", typeRandom, varMinimo, varMaximo)
        # Structure initializers
        toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr, 10)
        toolbox.register("population", tools.initRepeat, list, toolbox.individual)

        toolbox.register("evaluate", evaluate)

        toolbox.register("mate", tools.cxTwoPoint)  # OnePoint, TwoPoint, Uniform
        # toolbox.register("mutate", tools.mutFlipBit, indpb=0.1)
        toolbox.register("mutate", tools.mutFlipBit, indpb=0.1)
        toolbox.register("select", tools.selTournament, tournsize=3)

        return toolbox

    def start(self, toolbox, population, hallOfFame):
        random.seed(64)

        pop = toolbox.population(n=population)
        hof = tools.HallOfFame(hallOfFame)
        stats = tools.Statistics(lambda ind: ind.fitness.values)
        stats.register("avg", numpy.mean)
        stats.register("std", numpy.std)
        stats.register("min", numpy.min)
        stats.register("max", numpy.max)

        pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=3000,
                                       stats=stats, halloffame=hof, verbose=True)

        return pop, log, hof