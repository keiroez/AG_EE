from genetic_algorithms import GeneticAlgorithms
from helpers import *
from configuration import Configuration
import random
from deap import tools
from deap.benchmarks.binary import chuang_f1
from evaluations import  evaluateEightQueens, WORD_BASE, evaluateSecretWord
if __name__ == '__main__':

    ag = GeneticAlgorithms()
    configurantion = Configuration()

    # BENCHMARKS
    # ag.configFlipBitTournament(random.randint, 0, 1, chuang_f1, (-1.0,), 10, tools.cxTwoPoint)


    # PALAVRA CHAVE
    base = baseToolboxSecretWord()

    toolShuffleIndexesTournament = configurantion.configShuffleIndexesTournament(base, evaluateSecretWord, tools.cxOnePoint)
    resultsShuffleIndexesTournament = ag.start(300, 1, 1000, toolShuffleIndexesTournament)
    saveBestResult(resultsShuffleIndexesTournament[2])

'''
    toolShuffleIndexesRoulette = configurantion.configShuffleIndexesRoulette(base, evaluateSecretWord, tools.cxOnePoint)
    resultsShuffleIndexesRoulette = ag.start(300, 1, 1000, toolShuffleIndexesRoulette)
    saveBestResult(resultsShuffleIndexesRoulette[2])
    
    toolFlipBitTournament = configurantion.configFlipBitTournament(base, evaluateSecretWord, tools.cxOnePoint)
    resultsFlipBitTournament = ag.start(300, 1, 500, toolFlipBitTournament)
    saveBestResult(resultsFlipBitTournament[2])
    
    toolFlipBitRoulette = configurantion.configFlipBitRoulette(base, evaluateSecretWord, tools.cxOnePoint)
    resultsFlipBitRoulette = ag.start(300, 1, 5000, toolFlipBitRoulette)
    saveBestResult(resultsFlipBitRoulette[2])
'''

    # 8 RAINHAS
    # ag.configShuffleIndexesTournament(random.sample, range(8), 8, evaluateEightQueens, (-1.0,), 10, tools.cxPartialyMatched)
    # results = ag.start(50, 1, 1000)
    # plotChart(results[1].select('gen'), results[1].select('min'))
