import random
import numpy

from deap import base
from deap import creator
from deap import tools
from deap import algorithms

class GeneticAlgorithms:

    def start(self, population, hallOfFame, ngen, toolbox):
        pop = toolbox.population(n=population)
        hof = tools.HallOfFame(hallOfFame)
        stats = tools.Statistics(lambda ind: ind.fitness.values)
        stats.register("avg", numpy.mean)
        stats.register("std", numpy.std)
        stats.register("min", numpy.min)
        stats.register("max", numpy.max)

        pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=ngen,
                                       stats=stats, halloffame=hof, verbose=True)

        return pop, log, hof
