from helpers import *
from deap import tools
from evaluations import SIZE, POPULATION
from deap.benchmarks import griewank


def grienwankAG(ag, configuration):
    baseGrienwank = baseToolGriewank()

    print("********** grienwank - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selTournament **********")
    toolShuffleIndexesTournament = configuration.configShuffleIndexesTournament(baseGrienwank, griewank,
                                                                                tools.cxTwoPoint)
    resultsShuffleIndexesTournament = ag.start(POPULATION, 1, SIZE, toolShuffleIndexesTournament)
    saveBestResult(resultsShuffleIndexesTournament[1], "results/ag_grienwank_shuffle_indexes_tournament.csv")
    print("")

    print("********** grienwank - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selRoulette **********")
    toolShuffleIndexesRoulette = configuration.configShuffleIndexesRoulette(baseGrienwank, griewank,
                                                                            tools.cxTwoPoint)
    resultsShuffleIndexesRoulette = ag.start(POPULATION, 1, SIZE, toolShuffleIndexesRoulette)
    saveBestResult(resultsShuffleIndexesRoulette[1], "results/ag_grienwank_shuffle_indexes_roulette.csv")
    print("")

    print("********** grienwank - mate: cxTwoPoint - mutate: mutUniformInt - select: selTournament **********")
    toolUniformIntTournament = configuration.configUniformIntTournament(baseGrienwank, griewank, tools.cxTwoPoint)
    resultsUniformIntTournament = ag.start(POPULATION, 1, SIZE, toolUniformIntTournament)
    saveBestResult(resultsUniformIntTournament[1], "results/ag_grienwank_uniform_int_tournament.csv")
    print("")

    print("********** grienwank - mate: cxTwoPoint - mutate: mutUniforInt - select: selRoulette **********")
    toolUniformIntRoulette = configuration.configUniformIntRoulette(baseGrienwank, griewank, tools.cxTwoPoint)
    resultsUniformIntRoulette = ag.start(POPULATION, 1, SIZE, toolUniformIntRoulette)
    saveBestResult(resultsUniformIntRoulette[1], "results/ag_grienwank_uniform_int_roulette.csv")
    print("")

def grienwankEEPlus(ee, configuration):
    baseGrienwank = baseToolGriewank()

    print("********** grienwank - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selTournament **********")
    toolShuffleIndexesTournament = configuration.configShuffleIndexesTournament(baseGrienwank, griewank,
                                                                                tools.cxTwoPoint)
    resultsShuffleIndexesTournament = ee.startPlus(POPULATION, 1, SIZE, toolShuffleIndexesTournament)
    saveBestResult(resultsShuffleIndexesTournament[1], "results/ee_plus_grienwank_shuffle_indexes_tournament.csv")
    print("")

    print("********** grienwank - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selRoulette **********")
    toolShuffleIndexesRoulette = configuration.configShuffleIndexesRoulette(baseGrienwank, griewank,
                                                                            tools.cxTwoPoint)
    resultsShuffleIndexesRoulette = ee.startPlus(POPULATION, 1, SIZE, toolShuffleIndexesRoulette)
    saveBestResult(resultsShuffleIndexesRoulette[1], "results/ee_plus_grienwank_shuffle_indexes_roulette.csv")
    print("")

    print("********** grienwank - mate: cxTwoPoint - mutate: mutUniformInt - select: selTournament **********")
    toolUniformIntTournament = configuration.configUniformIntTournament(baseGrienwank, griewank, tools.cxTwoPoint)
    resultsUniformIntTournament = ee.startPlus(POPULATION, 1, SIZE, toolUniformIntTournament)
    saveBestResult(resultsUniformIntTournament[1], "results/ee_plus_grienwank_uniform_int_tournament.csv")
    print("")

    print("********** grienwank - mate: cxTwoPoint - mutate: mutUniforInt - select: selRoulette **********")
    toolUniformIntRoulette = configuration.configUniformIntRoulette(baseGrienwank, griewank, tools.cxTwoPoint)
    resultsUniformIntRoulette = ee.startPlus(POPULATION, 1, SIZE, toolUniformIntRoulette)
    saveBestResult(resultsUniformIntRoulette[1], "results/ee_plus_grienwank_uniform_int_roulette.csv")
    print("")

def grienwankEEComma(ee, configuration):
    baseGrienwank = baseToolGriewank()

    print("********** grienwank - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selTournament **********")
    toolShuffleIndexesTournament = configuration.configShuffleIndexesTournament(baseGrienwank, griewank,
                                                                                tools.cxTwoPoint)
    resultsShuffleIndexesTournament = ee.startComma(POPULATION, 1, SIZE, toolShuffleIndexesTournament)
    saveBestResult(resultsShuffleIndexesTournament[1], "results/ee_comma_grienwank_shuffle_indexes_tournament.csv")
    print("")

    print("********** grienwank - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selRoulette **********")
    toolShuffleIndexesRoulette = configuration.configShuffleIndexesRoulette(baseGrienwank, griewank,
                                                                            tools.cxTwoPoint)
    resultsShuffleIndexesRoulette = ee.startComma(POPULATION, 1, SIZE, toolShuffleIndexesRoulette)
    saveBestResult(resultsShuffleIndexesRoulette[1], "results/ee_comma_grienwank_shuffle_indexes_roulette.csv")
    print("")

    print("********** grienwank - mate: cxTwoPoint - mutate: mutUniformInt - select: selTournament **********")
    toolUniformIntTournament = configuration.configUniformIntTournament(baseGrienwank, griewank, tools.cxTwoPoint)
    resultsUniformIntTournament = ee.startComma(POPULATION, 1, SIZE, toolUniformIntTournament)
    saveBestResult(resultsUniformIntTournament[1], "results/ee_comma_grienwank_uniform_int_tournament.csv")
    print("")

    print("********** grienwank - mate: cxTwoPoint - mutate: mutUniforInt - select: selRoulette **********")
    toolUniformIntRoulette = configuration.configUniformIntRoulette(baseGrienwank, griewank, tools.cxTwoPoint)
    resultsUniformIntRoulette = ee.startComma(POPULATION, 1, SIZE, toolUniformIntRoulette)
    saveBestResult(resultsUniformIntRoulette[1], "results/ee_comma_grienwank_uniform_int_roulette.csv")
    print("")