from helpers import *
from deap import tools
from evaluations import evaluateEightQueens


def eightQueensAG(ag, configuration):
    baseRainha = baseToolboxEightQueens()

    print("********** 8 rainhas - mate: cxOnePoint - mutate: mutShuffleIndexes - select: selTournament **********")
    toolShuffleIndexesTournament = configuration.configShuffleIndexesTournament(baseRainha, evaluateEightQueens,
                                                                                tools.cxOnePoint)
    resultsShuffleIndexesTournament = ag.start(100, 1, 500, toolShuffleIndexesTournament)
    saveBestResult(resultsShuffleIndexesTournament[1], "results/ag_eight_queens_shuffle_indexes_tournament.csv")
    print("")

    print("********** 8 rainhas - mate: cxOnePoint - mutate: mutShuffleIndexes - select: selRoulette **********")
    toolShuffleIndexesRoulette = configuration.configShuffleIndexesRoulette(baseRainha, evaluateEightQueens,
                                                                            tools.cxOnePoint)
    resultsShuffleIndexesRoulette = ag.start(100, 1, 500, toolShuffleIndexesRoulette)
    saveBestResult(resultsShuffleIndexesRoulette[1], "results/ag_eight_queens_shuffle_indexes_roulette.csv")
    print("")

    print("********** 8 rainhas - mate: cxOnePoint - mutate: mutUniformInt - select: selTournament **********")
    toolUniformIntTournament = configuration.configUniformIntTournament(baseRainha, evaluateEightQueens, tools.cxOnePoint)
    resultsUniformIntTournament = ag.start(100, 1, 500, toolUniformIntTournament)
    saveBestResult(resultsUniformIntTournament[1], "results/ag_eight_queens_uniform_int_tournament.csv")
    print("")

    print("********** 8 rainhas - mate: cxOnePoint - mutate: mutUniforInt - select: selRoulette **********")
    toolUniformIntRoulette = configuration.configUniformIntRoulette(baseRainha, evaluateEightQueens, tools.cxOnePoint)
    resultsUniformIntRoulette = ag.start(100, 1, 500, toolUniformIntRoulette)
    saveBestResult(resultsUniformIntRoulette[1], "results/ag_eight_queens_uniform_int_roulette.csv")
    print("")