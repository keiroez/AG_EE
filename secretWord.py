from helpers import *
from deap import tools
from evaluations import evaluateSecretWord, SIZE, POPULATION

def secretWordAG(ag, configuration):

    # PALAVRA CHAVE
    base = baseToolboxSecretWord()

    print("********** secret Word - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selTournament **********")
    toolShuffleIndexesTournament = configuration.configShuffleIndexesTournament(base, evaluateSecretWord, tools.cxTwoPoint)
    resultsShuffleIndexesTournament = ag.start(POPULATION, 1, SIZE, toolShuffleIndexesTournament)
    saveBestResult(resultsShuffleIndexesTournament[1], "results/ag_secret_word_two_point_shuffle_indexes_tournament.csv")
    print("")

    print("********** secret Word - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selRoulette **********")
    toolShuffleIndexesRoulette = configuration.configShuffleIndexesRoulette(base, evaluateSecretWord, tools.cxTwoPoint)
    resultsShuffleIndexesRoulette = ag.start(POPULATION, 1, SIZE, toolShuffleIndexesRoulette)
    saveBestResult(resultsShuffleIndexesRoulette[1], "results/ag_secret_word_two_point_shuffle_indexes_roulette.csv")
    print("")

    print("********** secret Word - mate: cxOnePoint - mutate: mutShuffleIndexes - select: selTournament **********")
    toolShuffleIndexesTournament = configuration.configShuffleIndexesTournament(base, evaluateSecretWord, tools.cxOnePoint)
    resultsShuffleIndexesTournament = ag.start(POPULATION, 1, SIZE, toolShuffleIndexesTournament)
    saveBestResult(resultsShuffleIndexesTournament[1], "results/ag_secret_word_one_point_shuffle_indexes_tournament.csv")
    print("")

    print("********** secret Word - mate: cxOnePoint - mutate: mutShuffleIndexes - select: selRoulette **********")
    toolShuffleIndexesRoulette = configuration.configShuffleIndexesRoulette(base, evaluateSecretWord, tools.cxOnePoint)
    resultsShuffleIndexesRoulette = ag.start(POPULATION, 1, SIZE, toolShuffleIndexesRoulette)
    saveBestResult(resultsShuffleIndexesRoulette[1], "results/ag_secret_word_one_point_shuffle_indexes_roulette.csv")
    print("")

def secretWordEEPlus(ee, configuration):

    # PALAVRA CHAVE
    base = baseToolboxSecretWord()

    print("********** secret Word - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selTournament **********")
    toolShuffleIndexesTournament = configuration.configShuffleIndexesTournament(base, evaluateSecretWord, tools.cxTwoPoint)
    resultsShuffleIndexesTournament = ee.startPlus(POPULATION, 1, SIZE, toolShuffleIndexesTournament)
    saveBestResult(resultsShuffleIndexesTournament[1], "results/ee_plus_secret_word_two_point_shuffle_indexes_tournament.csv")
    print("")

    print("********** secret Word - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selRoulette **********")
    toolShuffleIndexesRoulette = configuration.configShuffleIndexesRoulette(base, evaluateSecretWord, tools.cxTwoPoint)
    resultsShuffleIndexesRoulette = ee.startPlus(POPULATION, 1, SIZE, toolShuffleIndexesRoulette)
    saveBestResult(resultsShuffleIndexesRoulette[1], "results/ee_plus_secret_word_two_point_shuffle_indexes_roulette.csv")
    print("")

    print("********** secret Word - mate: cxOnePoint - mutate: mutShuffleIndexes - select: selTournament **********")
    toolShuffleIndexesTournament = configuration.configShuffleIndexesTournament(base, evaluateSecretWord, tools.cxOnePoint)
    resultsShuffleIndexesTournament = ee.startPlus(POPULATION, 1, SIZE, toolShuffleIndexesTournament)
    saveBestResult(resultsShuffleIndexesTournament[1], "results/ee_plus_secret_word_one_point_shuffle_indexes_tournament.csv")
    print("")

    print("********** secret Word - mate: cxOnePoint - mutate: mutShuffleIndexes - select: selRoulette **********")
    toolShuffleIndexesRoulette = configuration.configShuffleIndexesRoulette(base, evaluateSecretWord, tools.cxOnePoint)
    resultsShuffleIndexesRoulette = ee.startPlus(POPULATION, 1, SIZE, toolShuffleIndexesRoulette)
    saveBestResult(resultsShuffleIndexesRoulette[1], "results/ee_plus_secret_word_one_point_shuffle_indexes_roulette.csv")
    print("")

def secretWordEEComma(ee, configuration):

    # PALAVRA CHAVE
    base = baseToolboxSecretWord()

    print("********** secret Word - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selTournament **********")
    toolShuffleIndexesTournament = configuration.configShuffleIndexesTournament(base, evaluateSecretWord, tools.cxTwoPoint)
    resultsShuffleIndexesTournament = ee.startComma(POPULATION, 1, SIZE, toolShuffleIndexesTournament)
    saveBestResult(resultsShuffleIndexesTournament[1], "results/ee_comma_secret_word_two_point_shuffle_indexes_tournament.csv")
    print("")

    print("********** secret Word - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selRoulette **********")
    toolShuffleIndexesRoulette = configuration.configShuffleIndexesRoulette(base, evaluateSecretWord, tools.cxTwoPoint)
    resultsShuffleIndexesRoulette = ee.startComma(POPULATION, 1, SIZE, toolShuffleIndexesRoulette)
    saveBestResult(resultsShuffleIndexesRoulette[1], "results/ee_comma_secret_word_two_point_shuffle_indexes_roulette.csv")
    print("")

    print("********** secret Word - mate: cxOnePoint - mutate: mutShuffleIndexes - select: selTournament **********")
    toolShuffleIndexesTournament = configuration.configShuffleIndexesTournament(base, evaluateSecretWord, tools.cxOnePoint)
    resultsShuffleIndexesTournament = ee.startComma(POPULATION, 1, SIZE, toolShuffleIndexesTournament)
    saveBestResult(resultsShuffleIndexesTournament[1],"results/ee_comma_secret_word_one_point_shuffle_indexes_tournament.csv")
    print("")

    print("********** secret Word - mate: cxOnePoint - mutate: mutShuffleIndexes - select: selRoulette **********")
    toolShuffleIndexesRoulette = configuration.configShuffleIndexesRoulette(base, evaluateSecretWord, tools.cxOnePoint)
    resultsShuffleIndexesRoulette = ee.startComma(POPULATION, 1, SIZE, toolShuffleIndexesRoulette)
    saveBestResult(resultsShuffleIndexesRoulette[1], "results/ee_comma_secret_word_one_point_shuffle_indexes_roulette.csv")
    print("")
