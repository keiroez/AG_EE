from helpers import *
from deap import tools
from evaluations import evaluateSecretWord, SIZE

def secretWordAG(ag, configuration):

    # PALAVRA CHAVE
    base = baseToolboxSecretWord()

    print("********** secret Word - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selTournament **********")
    toolShuffleIndexesTournament = configuration.configShuffleIndexesTournament(base, evaluateSecretWord, tools.cxTwoPoint)
    resultsShuffleIndexesTournament = ag.start(200, 1, SIZE, toolShuffleIndexesTournament)
    saveBestResult(resultsShuffleIndexesTournament[1], "results/ag_secret_word_shuffle_indexes_tournament.csv")
    print("")

    print("********** secret Word - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selRoulette **********")
    toolShuffleIndexesRoulette = configuration.configShuffleIndexesRoulette(base, evaluateSecretWord, tools.cxTwoPoint)
    resultsShuffleIndexesRoulette = ag.start(200, 1, SIZE, toolShuffleIndexesRoulette)
    saveBestResult(resultsShuffleIndexesRoulette[1], "results/ag_secret_word_shuffle_indexes_roulette.csv")
    print("")

def secretWordEEPlus(ee, configuration):

    # PALAVRA CHAVE
    base = baseToolboxSecretWord()

    print("********** secret Word - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selTournament **********")
    toolShuffleIndexesTournament = configuration.configShuffleIndexesTournament(base, evaluateSecretWord, tools.cxTwoPoint)
    resultsShuffleIndexesTournament = ee.startPlus(200, 1, SIZE, toolShuffleIndexesTournament)
    saveBestResult(resultsShuffleIndexesTournament[1], "results/ee_plus_secret_word_shuffle_indexes_tournament.csv")
    print("")

    print("********** secret Word - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selRoulette **********")
    toolShuffleIndexesRoulette = configuration.configShuffleIndexesRoulette(base, evaluateSecretWord, tools.cxTwoPoint)
    resultsShuffleIndexesRoulette = ee.startPlus(200, 1, SIZE, toolShuffleIndexesRoulette)
    saveBestResult(resultsShuffleIndexesRoulette[1], "results/ee_plus_secret_word_shuffle_indexes_roulette.csv")
    print("")

def secretWordEEComma(ee, configuration):

    # PALAVRA CHAVE
    base = baseToolboxSecretWord()

    print("********** secret Word - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selTournament **********")
    toolShuffleIndexesTournament = configuration.configShuffleIndexesTournament(base, evaluateSecretWord, tools.cxTwoPoint)
    resultsShuffleIndexesTournament = ee.startComma(200, 1, SIZE, toolShuffleIndexesTournament)
    saveBestResult(resultsShuffleIndexesTournament[1], "results/ee_comma_secret_word_shuffle_indexes_tournament.csv")
    print("")

    print("********** secret Word - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selRoulette **********")
    toolShuffleIndexesRoulette = configuration.configShuffleIndexesRoulette(base, evaluateSecretWord, tools.cxTwoPoint)
    resultsShuffleIndexesRoulette = ee.startComma(200, 1, SIZE, toolShuffleIndexesRoulette)
    saveBestResult(resultsShuffleIndexesRoulette[1], "results/ee_comma_secret_word_shuffle_indexes_roulette.csv")
    print("")
