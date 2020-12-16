from helpers import *
from deap import tools
from evaluations import SIZE
from deap.benchmarks import griewank


def grienwankAG(ag, configuration):
    baseGrienwank = baseToolGriewank()

    print("********** grienwank - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selTournament **********")
    toolShuffleIndexesTournament = configuration.configShuffleIndexesTournament(baseGrienwank, griewank,
                                                                                tools.cxTwoPoint)
    resultsShuffleIndexesTournament = ag.start(200, 1, SIZE, toolShuffleIndexesTournament)
    saveBestResult(resultsShuffleIndexesTournament[1], "results/ag_grienwank_shuffle_indexes_tournament.csv")
    print("")

    print("********** grienwank - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selRoulette **********")
    toolShuffleIndexesRoulette = configuration.configShuffleIndexesRoulette(baseGrienwank, griewank,
                                                                            tools.cxTwoPoint)
    resultsShuffleIndexesRoulette = ag.start(200, 1, SIZE, toolShuffleIndexesRoulette)
    saveBestResult(resultsShuffleIndexesRoulette[1], "results/ag_grienwank_shuffle_indexes_roulette.csv")
    print("")

    print("********** grienwank - mate: cxTwoPoint - mutate: mutUniformInt - select: selTournament **********")
    toolUniformIntTournament = configuration.configUniformIntTournament(baseGrienwank, griewank, tools.cxTwoPoint)
    resultsUniformIntTournament = ag.start(200, 1, SIZE, toolUniformIntTournament)
    saveBestResult(resultsUniformIntTournament[1], "results/ag_grienwank_uniform_int_tournament.csv")
    print("")

    print("********** grienwank - mate: cxTwoPoint - mutate: mutUniforInt - select: selRoulette **********")
    toolUniformIntRoulette = configuration.configUniformIntRoulette(baseGrienwank, griewank, tools.cxTwoPoint)
    resultsUniformIntRoulette = ag.start(200, 1, SIZE, toolUniformIntRoulette)
    saveBestResult(resultsUniformIntRoulette[1], "results/ag_grienwank_uniform_int_roulette.csv")
    print("")

def grienwankEEPlus(ee, configuration):
    baseGrienwank = baseToolGriewank()

    print("********** grienwank - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selTournament **********")
    toolShuffleIndexesTournament = configuration.configShuffleIndexesTournament(baseGrienwank, griewank,
                                                                                tools.cxTwoPoint)
    resultsShuffleIndexesTournament = ee.startPlus(200, 1, SIZE, toolShuffleIndexesTournament)
    saveBestResult(resultsShuffleIndexesTournament[1], "results/ee_plus_grienwank_shuffle_indexes_tournament.csv")
    print("")

    print("********** grienwank - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selRoulette **********")
    toolShuffleIndexesRoulette = configuration.configShuffleIndexesRoulette(baseGrienwank, griewank,
                                                                            tools.cxTwoPoint)
    resultsShuffleIndexesRoulette = ee.startPlus(200, 1, SIZE, toolShuffleIndexesRoulette)
    saveBestResult(resultsShuffleIndexesRoulette[1], "results/ee_plus_grienwank_shuffle_indexes_roulette.csv")
    print("")

    print("********** grienwank - mate: cxTwoPoint - mutate: mutUniformInt - select: selTournament **********")
    toolUniformIntTournament = configuration.configUniformIntTournament(baseGrienwank, griewank, tools.cxTwoPoint)
    resultsUniformIntTournament = ee.startPlus(200, 1, SIZE, toolUniformIntTournament)
    saveBestResult(resultsUniformIntTournament[1], "results/ee_plus_grienwank_uniform_int_tournament.csv")
    print("")

    print("********** grienwank - mate: cxTwoPoint - mutate: mutUniforInt - select: selRoulette **********")
    toolUniformIntRoulette = configuration.configUniformIntRoulette(baseGrienwank, griewank, tools.cxTwoPoint)
    resultsUniformIntRoulette = ee.startPlus(200, 1, SIZE, toolUniformIntRoulette)
    saveBestResult(resultsUniformIntRoulette[1], "results/ee_plus_grienwank_uniform_int_roulette.csv")
    print("")

def grienwankEEComma(ee, configuration):
    baseGrienwank = baseToolGriewank()

    print("********** grienwank - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selTournament **********")
    toolShuffleIndexesTournament = configuration.configShuffleIndexesTournament(baseGrienwank, griewank,
                                                                                tools.cxTwoPoint)
    resultsShuffleIndexesTournament = ee.startComma(200, 1, SIZE, toolShuffleIndexesTournament)
    saveBestResult(resultsShuffleIndexesTournament[1], "results/ee_comma_grienwank_shuffle_indexes_tournament.csv")
    print("")

    print("********** grienwank - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selRoulette **********")
    toolShuffleIndexesRoulette = configuration.configShuffleIndexesRoulette(baseGrienwank, griewank,
                                                                            tools.cxTwoPoint)
    resultsShuffleIndexesRoulette = ee.startComma(200, 1, SIZE, toolShuffleIndexesRoulette)
    saveBestResult(resultsShuffleIndexesRoulette[1], "results/ee_comma_grienwank_shuffle_indexes_roulette.csv")
    print("")

    print("********** grienwank - mate: cxTwoPoint - mutate: mutUniformInt - select: selTournament **********")
    toolUniformIntTournament = configuration.configUniformIntTournament(baseGrienwank, griewank, tools.cxTwoPoint)
    resultsUniformIntTournament = ee.startComma(200, 1, SIZE, toolUniformIntTournament)
    saveBestResult(resultsUniformIntTournament[1], "results/ee_comma_grienwank_uniform_int_tournament.csv")
    print("")

    print("********** grienwank - mate: cxTwoPoint - mutate: mutUniforInt - select: selRoulette **********")
    toolUniformIntRoulette = configuration.configUniformIntRoulette(baseGrienwank, griewank, tools.cxTwoPoint)
    resultsUniformIntRoulette = ee.startComma(200, 1, SIZE, toolUniformIntRoulette)
    saveBestResult(resultsUniformIntRoulette[1], "results/ee_comma_grienwank_uniform_int_roulette.csv")
    print("")