from helpers import *
from deap import tools
from evaluations import evaluateSecretWord

def secretWordAG(ag, configuration):

    # PALAVRA CHAVE
    base = baseToolboxSecretWord()

    print("********** secret Word - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selTournament **********")
    toolShuffleIndexesTournament = configuration.configShuffleIndexesTournament(base, evaluateSecretWord, tools.cxTwoPoint)
    resultsShuffleIndexesTournament = ag.start(100, 1, 500, toolShuffleIndexesTournament)
    saveBestResult(resultsShuffleIndexesTournament[1], "results/ag_secret_word_shuffle_indexes_tournament.csv")
    print("")

    print("********** secret Word - mate: cxTwoPoint - mutate: mutShuffleIndexes - select: selRoulette **********")
    toolShuffleIndexesRoulette = configuration.configShuffleIndexesRoulette(base, evaluateSecretWord, tools.cxTwoPoint)
    resultsShuffleIndexesRoulette = ag.start(100, 1, 500, toolShuffleIndexesRoulette)
    saveBestResult(resultsShuffleIndexesRoulette[1], "results/ag_secret_word_shuffle_indexes_roulette.csv")
    print("")

    print("********** secret Word - mate: cxTwoPoint - mutate: mutFlipBit - select: selTournament **********")
    toolFlipBitTournament = configuration.configFlipBitTournament(base, evaluateSecretWord, tools.cxTwoPoint)
    resultsFlipBitTournament = ag.start(100, 1, 500, toolFlipBitTournament)
    saveBestResult(resultsFlipBitTournament[1], "results/ag_secret_word_flip_bit_tournament.csv")
    print("")

    print("********** secret Word - mate: cxTwoPoint - mutate: mutFlipBit - select: selRoulette **********")
    toolFlipBitRoulette = configuration.configFlipBitRoulette(base, evaluateSecretWord, tools.cxTwoPoint)
    resultsFlipBitRoulette = ag.start(100, 1, 500, toolFlipBitRoulette)
    saveBestResult(resultsFlipBitRoulette[1], "results/ag_secret_word_flip_bit_roulette.csv")
    print("")
