import random
import numpy

from deap import base
from deap import creator
from deap import tools
from deap import algorithms

class Configurations:
    def configFlipBitTournament(self, typeRandom, minValue, maxValue, evaluate, weights, size, mate):
        creator.create("FitnessType", base.Fitness, weights=weights)
        creator.create("Individual", list, fitness=creator.FitnessType)
        toolbox = base.Toolbox()
        toolbox.register("attr", typeRandom, minValue, maxValue)
        toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr, size)
        toolbox.register("population", tools.initRepeat, list, toolbox.individual)

        toolbox.register("evaluate", evaluate)
        toolbox.register("mate", mate)
        toolbox.register("mutate", tools.mutFlipBit, indpb=0.1)
        toolbox.register("select", tools.selTournament, tournsize=3)
        return toolbox

    def configShuffleIndexesTournament(self, typeRandom, minValue, maxValue, evaluate, weights, size, mate):
        creator.create('FitnessType', base.Fitness, weights=weights)
        creator.create('Individual', list, fitness=creator.FitnessType)

        toolbox = base.Toolbox()
        toolbox.register('attr', typeRandom, minValue, maxValue)
        toolbox.register('individual', tools.initIterate, creator.Individual, toolbox.attr)
        toolbox.register('population', tools.initRepeat, list, toolbox.individual)

        toolbox.register("evaluate", evaluate)
        toolbox.register("mate", mate)
        toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.1)
        toolbox.register("select", tools.selTournament, tournsize=3)
        return toolbox