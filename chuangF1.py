from helpers import *
from deap import tools
from deap.benchmarks.binary import chuang_f1
from evaluations import  SIZE


def chuangF1AG(ag, configuration):
    baseChuang = baseToolboxChuang_f1()

    print("********** chuang f1 - mate: cxOnePoint - mutate: mutShuffleIndexes - select: selTournament **********")
    toolShuffleIndexesTournament = configuration.configShuffleIndexesTournament(baseChuang, chuang_f1,
                                                                                tools.cxOnePoint)
    resultsShuffleIndexesTournament = ag.start(200, 1, SIZE, toolShuffleIndexesTournament)
    saveBestResult(resultsShuffleIndexesTournament[1], "results/ag_chuang_f1_shuffle_indexes_tournament.csv")
    print("")

    print("********** chuang f1 - mate: cxOnePoint - mutate: mutShuffleIndexes - select: selRoulette **********")
    toolShuffleIndexesRoulette = configuration.configShuffleIndexesRoulette(baseChuang, chuang_f1,
                                                                            tools.cxOnePoint)
    resultsShuffleIndexesRoulette = ag.start(200, 1, SIZE, toolShuffleIndexesRoulette)
    saveBestResult(resultsShuffleIndexesRoulette[1], "results/ag_chuang_f1_shuffle_indexes_roulette.csv")
    print("")

    print("********** chuang f1 - mate: cxOnePoint - mutate: mutUniformInt - select: selTournament **********")
    toolUniformIntTournament = configuration.configUniformIntTournament(baseChuang, chuang_f1, tools.cxOnePoint)
    resultsUniformIntTournament = ag.start(200, 1, SIZE, toolUniformIntTournament)
    saveBestResult(resultsUniformIntTournament[1], "results/ag_chuang_f1_uniform_int_tournament.csv")
    print("")

    print("********** chuang f1 - mate: cxOnePoint - mutate: mutUniforInt - select: selRoulette **********")
    toolUniformIntRoulette = configuration.configUniformIntRoulette(baseChuang, chuang_f1, tools.cxOnePoint)
    resultsUniformIntRoulette = ag.start(200, 1, SIZE, toolUniformIntRoulette)
    saveBestResult(resultsUniformIntRoulette[1], "results/ag_chuang_f1_uniform_int_roulette.csv")
    print("")

def chuangF1EEPlus(ee, configuration):
    baseChuang = baseToolboxChuang_f1()

    print("********** chuang f1 - mate: cxOnePoint - mutate: mutShuffleIndexes - select: selTournament **********")
    toolShuffleIndexesTournament = configuration.configShuffleIndexesTournament(baseChuang, chuang_f1,
                                                                                tools.cxOnePoint)
    resultsShuffleIndexesTournament = ee.startPlus(200, 1, SIZE, toolShuffleIndexesTournament)
    saveBestResult(resultsShuffleIndexesTournament[1], "results/ee_plus_chuang_f1_shuffle_indexes_tournament.csv")
    print("")

    print("********** chuang f1 - mate: cxOnePoint - mutate: mutShuffleIndexes - select: selRoulette **********")
    toolShuffleIndexesRoulette = configuration.configShuffleIndexesRoulette(baseChuang, chuang_f1,
                                                                            tools.cxOnePoint)
    resultsShuffleIndexesRoulette = ee.startPlus(200, 1, SIZE, toolShuffleIndexesRoulette)
    saveBestResult(resultsShuffleIndexesRoulette[1], "results/ee_plus_chuang_f1_shuffle_indexes_roulette.csv")
    print("")

    print("********** chuang f1 - mate: cxOnePoint - mutate: mutUniformInt - select: selTournament **********")
    toolUniformIntTournament = configuration.configUniformIntTournament(baseChuang, chuang_f1, tools.cxOnePoint)
    resultsUniformIntTournament = ee.startPlus(200, 1, SIZE, toolUniformIntTournament)
    saveBestResult(resultsUniformIntTournament[1], "results/ee_plus_chuang_f1_uniform_int_tournament.csv")
    print("")

    print("********** chuang f1 - mate: cxOnePoint - mutate: mutUniforInt - select: selRoulette **********")
    toolUniformIntRoulette = configuration.configUniformIntRoulette(baseChuang, chuang_f1, tools.cxOnePoint)
    resultsUniformIntRoulette = ee.startPlus(200, 1, SIZE, toolUniformIntRoulette)
    saveBestResult(resultsUniformIntRoulette[1], "results/ee_plus_chuang_f1_uniform_int_roulette.csv")
    print("")

def chuangF1EEComma(ee, configuration):
    baseChuang = baseToolboxChuang_f1()

    print("********** chuang f1 - mate: cxOnePoint - mutate: mutShuffleIndexes - select: selTournament **********")
    toolShuffleIndexesTournament = configuration.configShuffleIndexesTournament(baseChuang, chuang_f1,
                                                                                tools.cxOnePoint)
    resultsShuffleIndexesTournament = ee.startComma(200, 1, SIZE, toolShuffleIndexesTournament)
    saveBestResult(resultsShuffleIndexesTournament[1], "results/ee_comma_chuang_f1_shuffle_indexes_tournament.csv")
    print("")

    print("********** chuang f1 - mate: cxOnePoint - mutate: mutShuffleIndexes - select: selRoulette **********")
    toolShuffleIndexesRoulette = configuration.configShuffleIndexesRoulette(baseChuang, chuang_f1,
                                                                            tools.cxOnePoint)
    resultsShuffleIndexesRoulette = ee.startComma(200, 1, SIZE, toolShuffleIndexesRoulette)
    saveBestResult(resultsShuffleIndexesRoulette[1], "results/ee_comma_chuang_f1_shuffle_indexes_roulette.csv")
    print("")

    print("********** chuang f1 - mate: cxOnePoint - mutate: mutUniformInt - select: selTournament **********")
    toolUniformIntTournament = configuration.configUniformIntTournament(baseChuang, chuang_f1, tools.cxOnePoint)
    resultsUniformIntTournament = ee.startComma(200, 1, SIZE, toolUniformIntTournament)
    saveBestResult(resultsUniformIntTournament[1], "results/ee_comma_chuang_f1_uniform_int_tournament.csv")
    print("")

    print("********** chuang f1 - mate: cxOnePoint - mutate: mutUniforInt - select: selRoulette **********")
    toolUniformIntRoulette = configuration.configUniformIntRoulette(baseChuang, chuang_f1, tools.cxOnePoint)
    resultsUniformIntRoulette = ee.startComma(200, 1, SIZE, toolUniformIntRoulette)
    saveBestResult(resultsUniformIntRoulette[1], "results/ee_comma_chuang_f1_uniform_int_roulette.csv")
    print("")