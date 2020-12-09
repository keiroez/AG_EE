from genetic_algorithms import GeneticAlgorithms
from helpers import plotChart
import random
from deap import tools
from deap.benchmarks.binary import chuang_f1
from evaluations import  evaluateEightQueens
if __name__ == '__main__':

    ag = GeneticAlgorithms()

    # BENCHMARKS
    # ag.configFlipBitTournament(random.randint, 0, 1, chuang_f1, (-1.0,), 10, tools.cxTwoPoint)
    # results = ag.start(50, 1)
    # plotChart(results[1].select('gen'), results[1].select('min'))

    # 8 RAINHAS
    ag.configShuffleIndexesTournament(random.sample, range(8), 8, evaluateEightQueens, (-1.0,), 10, tools.cxPartialyMatched)
    results = ag.start(50, 1)
    plotChart(results[1].select('gen'), results[1].select('min'))