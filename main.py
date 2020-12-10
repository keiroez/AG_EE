from genetic_algorithms import GeneticAlgorithms
from helpers import plotChart, generateWord
import random
from deap import tools
from deap.benchmarks.binary import chuang_f1
from evaluations import  evaluateEightQueens, WORD_BASE, evaluateSecretWord
if __name__ == '__main__':

    ag = GeneticAlgorithms()

    # BENCHMARKS
    # ag.configFlipBitTournament(random.randint, 0, 1, chuang_f1, (-1.0,), 10, tools.cxTwoPoint)
    # results = ag.start(50, 1, 1000)
    # plotChart(results[1].select('gen'), results[1].select('min'))

    # 8 RAINHAS
    # ag.configShuffleIndexesTournament(random.sample, range(8), 8, evaluateEightQueens, (-1.0,), 10, tools.cxPartialyMatched)
    # results = ag.start(50, 1, 1000)
    # plotChart(results[1].select('gen'), results[1].select('min'))

    # PALAVRA CHAVE
    ag.configShuffleIndexesTournament(generateWord, len(WORD_BASE), 8, evaluateSecretWord, (1.0,), 10, tools.cxOnePoint)
    results = ag.start(300, 10, 1000)
    plotChart(results[1].select('gen'), results[1].select('min'))