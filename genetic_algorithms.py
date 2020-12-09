import random
import numpy

from deap import base
from deap import creator
from deap import tools
from deap import algorithms

class GeneticAlgorithms:

    def __init__(self):
        self.toolbox = None

    def configFlipBitTournament(self, typeRandom, minValue, maxValue, evaluate, weights, size, mate):
        creator.create("FitnessType", base.Fitness, weights=weights)
        creator.create("Individual", list, fitness=creator.FitnessType)
        self.toolbox = base.Toolbox()
        self.toolbox.register("attr", typeRandom, minValue, maxValue)
        self.toolbox.register("individual", tools.initRepeat, creator.Individual, self.toolbox.attr, size)
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)

        self.toolbox.register("evaluate", evaluate)
        self.toolbox.register("mate", mate)
        self.toolbox.register("mutate", tools.mutFlipBit, indpb=0.1)
        self.toolbox.register("select", tools.selTournament, tournsize=3)

    def configShuffleIndexesTournament(self, typeRandom, minValue, maxValue, evaluate, weights, size, mate):
        creator.create("FitnessType", base.Fitness, weights=weights)
        creator.create("Individual", list, fitness=creator.FitnessType)
        self.toolbox = base.Toolbox()
        self.toolbox.register("attr", typeRandom, minValue, maxValue)
        self.toolbox.register("individual", tools.initIterate, creator.Individual, self.toolbox.attr)
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)

        self.toolbox.register("evaluate", evaluate)

        self.toolbox.register("mate", mate)
        self.toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.1)
        self.toolbox.register("select", tools.selTournament, tournsize=3)

    def start(self, population, hallOfFame):
        random.seed(64)

        pop = self.toolbox.population(n=population)
        hof = tools.HallOfFame(hallOfFame)
        stats = tools.Statistics(lambda ind: ind.fitness.values)
        stats.register("avg", numpy.mean)
        stats.register("std", numpy.std)
        stats.register("min", numpy.min)
        stats.register("max", numpy.max)

        pop, log = algorithms.eaSimple(pop, self.toolbox, cxpb=0.5, mutpb=0.2, ngen=3000,
                                       stats=stats, halloffame=hof, verbose=True)

        return pop, log, hof