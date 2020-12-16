from helpers import *
from deap import tools
from deap.benchmarks.binary import chuang_f1
from evaluations import  SIZE


def chuangF1AG(ag, configuration):
    baseChuang = baseToolboxChuang_f1()

    print("********** chuang f1 - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selTournament **********")
    toolShuffleIndexesTournament = configuration.configShuffleIndexesTournament(baseChuang, chuang_f1,
                                                                                tools.cxTwoPoint)
    resultsShuffleIndexesTournament = ag.start(200, 1, SIZE, toolShuffleIndexesTournament)
    saveBestResult(resultsShuffleIndexesTournament[1], "results/ag_chuang_f1_shuffle_indexes_tournament.csv")
    print("")

    print("********** chuang f1 - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selRoulette **********")
    toolShuffleIndexesRoulette = configuration.configShuffleIndexesRoulette(baseChuang, chuang_f1,
                                                                            tools.cxTwoPoint)
    resultsShuffleIndexesRoulette = ag.start(200, 1, SIZE, toolShuffleIndexesRoulette)
    saveBestResult(resultsShuffleIndexesRoulette[1], "results/ag_chuang_f1_shuffle_indexes_roulette.csv")
    print("")

    print("********** chuang f1 - mate: cxTwoPoint - mutate: mutUniformInt - select: selTournament **********")
    toolUniformIntTournament = configuration.configUniformIntTournament(baseChuang, chuang_f1, tools.cxTwoPoint)
    resultsUniformIntTournament = ag.start(200, 1, SIZE, toolUniformIntTournament)
    saveBestResult(resultsUniformIntTournament[1], "results/ag_chuang_f1_uniform_int_tournament.csv")
    print("")

    print("********** chuang f1 - mate: cxTwoPoint - mutate: mutUniforInt - select: selRoulette **********")
    toolUniformIntRoulette = configuration.configUniformIntRoulette(baseChuang, chuang_f1, tools.cxTwoPoint)
    resultsUniformIntRoulette = ag.start(200, 1, SIZE, toolUniformIntRoulette)
    saveBestResult(resultsUniformIntRoulette[1], "results/ag_chuang_f1_uniform_int_roulette.csv")
    print("")

def chuangF1EEPlus(ee, configuration):
    baseChuang = baseToolboxChuang_f1()

    print("********** chuang f1 - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selTournament **********")
    toolShuffleIndexesTournament = configuration.configShuffleIndexesTournament(baseChuang, chuang_f1,
                                                                                tools.cxTwoPoint)
    resultsShuffleIndexesTournament = ee.startPlus(200, 1, SIZE, toolShuffleIndexesTournament)
    saveBestResult(resultsShuffleIndexesTournament[1], "results/ee_plus_chuang_f1_shuffle_indexes_tournament.csv")
    print("")

    print("********** chuang f1 - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selRoulette **********")
    toolShuffleIndexesRoulette = configuration.configShuffleIndexesRoulette(baseChuang, chuang_f1,
                                                                            tools.cxTwoPoint)
    resultsShuffleIndexesRoulette = ee.startPlus(200, 1, SIZE, toolShuffleIndexesRoulette)
    saveBestResult(resultsShuffleIndexesRoulette[1], "results/ee_plus_chuang_f1_shuffle_indexes_roulette.csv")
    print("")

    print("********** chuang f1 - mate: cxTwoPoint - mutate: mutUniformInt - select: selTournament **********")
    toolUniformIntTournament = configuration.configUniformIntTournament(baseChuang, chuang_f1, tools.cxTwoPoint)
    resultsUniformIntTournament = ee.startPlus(200, 1, SIZE, toolUniformIntTournament)
    saveBestResult(resultsUniformIntTournament[1], "results/ee_plus_chuang_f1_uniform_int_tournament.csv")
    print("")

    print("********** chuang f1 - mate: cxTwoPoint - mutate: mutUniforInt - select: selRoulette **********")
    toolUniformIntRoulette = configuration.configUniformIntRoulette(baseChuang, chuang_f1, tools.cxTwoPoint)
    resultsUniformIntRoulette = ee.startPlus(200, 1, SIZE, toolUniformIntRoulette)
    saveBestResult(resultsUniformIntRoulette[1], "results/ee_plus_chuang_f1_uniform_int_roulette.csv")
    print("")

def chuangF1EEComma(ee, configuration):
    baseChuang = baseToolboxChuang_f1()

    print("********** chuang f1 - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selTournament **********")
    toolShuffleIndexesTournament = configuration.configShuffleIndexesTournament(baseChuang, chuang_f1,
                                                                                tools.cxTwoPoint)
    resultsShuffleIndexesTournament = ee.startComma(200, 1, SIZE, toolShuffleIndexesTournament)
    saveBestResult(resultsShuffleIndexesTournament[1], "results/ee_comma_chuang_f1_shuffle_indexes_tournament.csv")
    print("")

    print("********** chuang f1 - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selRoulette **********")
    toolShuffleIndexesRoulette = configuration.configShuffleIndexesRoulette(baseChuang, chuang_f1,
                                                                            tools.cxTwoPoint)
    resultsShuffleIndexesRoulette = ee.startComma(200, 1, SIZE, toolShuffleIndexesRoulette)
    saveBestResult(resultsShuffleIndexesRoulette[1], "results/ee_comma_chuang_f1_shuffle_indexes_roulette.csv")
    print("")

    print("********** chuang f1 - mate: cxTwoPoint - mutate: mutUniformInt - select: selTournament **********")
    toolUniformIntTournament = configuration.configUniformIntTournament(baseChuang, chuang_f1, tools.cxTwoPoint)
    resultsUniformIntTournament = ee.startComma(200, 1, SIZE, toolUniformIntTournament)
    saveBestResult(resultsUniformIntTournament[1], "results/ee_comma_chuang_f1_uniform_int_tournament.csv")
    print("")

    print("********** chuang f1 - mate: cxTwoPoint - mutate: mutUniforInt - select: selRoulette **********")
    toolUniformIntRoulette = configuration.configUniformIntRoulette(baseChuang, chuang_f1, tools.cxTwoPoint)
    resultsUniformIntRoulette = ee.startComma(200, 1, SIZE, toolUniformIntRoulette)
    saveBestResult(resultsUniformIntRoulette[1], "results/ee_comma_chuang_f1_uniform_int_roulette.csv")
    print("")