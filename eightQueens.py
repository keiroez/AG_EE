from helpers import *
from deap import tools
from evaluations import evaluateEightQueens


def eightQueensAG(ag, configuration):
    baseRainha = baseToolboxEightQueens()
    print("********** 8 rainhas - mate: cxOnePoint - mutate: mutShuffleIndexes - select: selTournament **********")
    toolShuffleIndexesTournament = configuration.configShuffleIndexesTournament(baseRainha, evaluateEightQueens,
                                                                                tools.cxOnePoint)
    resultsShuffleIndexesTournament = ag.start(300, 1, 800, toolShuffleIndexesTournament)
    saveBestResult(resultsShuffleIndexesTournament[2])
    print("")

    print("********** 8 rainhas - mate: cxOnePoint - mutate: mutShuffleIndexes - select: selRoulette **********")
    toolShuffleIndexesRoulette = configuration.configShuffleIndexesRoulette(baseRainha, evaluateEightQueens,
                                                                            tools.cxOnePoint)
    resultsShuffleIndexesRoulette = ag.start(300, 1, 1000, toolShuffleIndexesRoulette)
    saveBestResult(resultsShuffleIndexesRoulette[2])
    print("")

    print("********** 8 rainhas - mate: cxOnePoint - mutate: mutFlipBit - select: selTournament **********")
    toolFlipBitTournament = configuration.configFlipBitTournament(baseRainha, evaluateEightQueens, tools.cxOnePoint)
    resultsFlipBitTournament = ag.start(300, 1, 500, toolFlipBitTournament)
    saveBestResult(resultsFlipBitTournament[2])
    print("")

    print("********** 8 rainhas - mate: cxOnePoint - mutate: mutFlipBit - select: selRoulette **********")
    toolFlipBitRoulette = configuration.configFlipBitRoulette(baseRainha, evaluateEightQueens, tools.cxOnePoint)
    resultsFlipBitRoulette = ag.start(300, 1, 5000, toolFlipBitRoulette)
    saveBestResult(resultsFlipBitRoulette[2])
    print("")
