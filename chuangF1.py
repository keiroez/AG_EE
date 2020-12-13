from helpers import *
from deap import tools
from deap.benchmarks.binary import chuang_f1


def chuangF1AG(ag, configuration):
    baseChuang = baseToolboxChuang_f1()

    print("********** chuang f1 - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selTournament **********")
    toolShuffleIndexesTournament = configuration.configShuffleIndexesTournament(baseChuang, chuang_f1,
                                                                                tools.cxTwoPoint)
    resultsShuffleIndexesTournament = ag.start(100, 1, 500, toolShuffleIndexesTournament)
    saveBestResult(resultsShuffleIndexesTournament[1], "results/ag_chuanf_f1_shuffle_indexes_tournament.csv")
    print("")

    print("********** chuang f1 - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selRoulette **********")
    toolShuffleIndexesRoulette = configuration.configShuffleIndexesRoulette(baseChuang, chuang_f1,
                                                                            tools.cxTwoPoint)
    resultsShuffleIndexesRoulette = ag.start(100, 1, 500, toolShuffleIndexesRoulette)
    saveBestResult(resultsShuffleIndexesRoulette[1], "results/ag_chuanf_f1_shuffle_indexes_roulette.csv")
    print("")

    print("********** chuang f1 - mate: cxTwoPoint - mutate: mutUniformInt - select: selTournament **********")
    toolUniformIntTournament = configuration.configUniformIntTournament(baseChuang, chuang_f1, tools.cxTwoPoint)
    resultsUniformIntTournament = ag.start(100, 1, 500, toolUniformIntTournament)
    saveBestResult(resultsUniformIntTournament[1], "results/ag_chuanf_f1_uniform_int_tournament.csv")
    print("")

    print("********** chuang f1 - mate: cxTwoPoint - mutate: mutUniforInt - select: selRoulette **********")
    toolUniformIntRoulette = configuration.configUniformIntRoulette(baseChuang, chuang_f1, tools.cxTwoPoint)
    resultsUniformIntRoulette = ag.start(100, 1, 500, toolUniformIntRoulette)
    saveBestResult(resultsUniformIntRoulette[1], "results/ag_chuanf_f1_uniform_int_roulette.csv")
    print("")