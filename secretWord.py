from helpers import *
from deap import tools
from evaluations import evaluateSecretWord

def secretWordAG(ag, configuration):

    # PALAVRA CHAVE
    base = baseToolboxSecretWord()

    print("********** secret Word - mate: cxOnePoint - mutate: mutShuffleIndexes - select: selTournament **********")
    toolShuffleIndexesTournament = configuration.configShuffleIndexesTournament(base, evaluateSecretWord, tools.cxTwoPoint)
    resultsShuffleIndexesTournament = ag.start(300, 1, 800, toolShuffleIndexesTournament)
    saveBestResult(resultsShuffleIndexesTournament[2])
    print("")

    print("********** secret Word - mate: cxOnePoint - mutate: mutShuffleIndexes - select: selRoulette **********")
    toolShuffleIndexesRoulette = configuration.configShuffleIndexesRoulette(base, evaluateSecretWord, tools.cxOnePoint)
    resultsShuffleIndexesRoulette = ag.start(300, 1, 1000, toolShuffleIndexesRoulette)
    saveBestResult(resultsShuffleIndexesRoulette[2])
    print("")

    print("********** secret Word - mate: cxOnePoint - mutate: mutFlipBit - select: selTournament **********")
    toolFlipBitTournament = configuration.configFlipBitTournament(base, evaluateSecretWord, tools.cxOnePoint)
    resultsFlipBitTournament = ag.start(300, 1, 500, toolFlipBitTournament)
    saveBestResult(resultsFlipBitTournament[2])
    print("")

    print("********** secret Word - mate: cxOnePoint - mutate: mutFlipBit - select: selRoulette **********")
    toolFlipBitRoulette = configuration.configFlipBitRoulette(base, evaluateSecretWord, tools.cxOnePoint)
    resultsFlipBitRoulette = ag.start(300, 1, 5000, toolFlipBitRoulette)
    saveBestResult(resultsFlipBitRoulette[2])
    print("")
