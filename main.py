from genetic_algorithms import GeneticAlgorithms
from helpers import plotChart
import random
from deap import tools
from deap.benchmarks.binary import chuang_f1
if __name__ == '__main__':

    ag = GeneticAlgorithms()

    toolbox = ag.configFlipBitTournament(random.randint, 0, 1, chuang_f1, (-1.0,), 10, tools.cxTwoPoint)
    results = ag.start(toolbox, 50, 1)

    plotChart(results[1].select('gen'), results[1].select('min'))
