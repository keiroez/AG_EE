from genetic_algorithms import GeneticAlgorithms
from evolutionary_strategies import EvolutionaryStrategies
from configuration import Configuration
from secretWord import *
from eightQueens import *
from grienwank import *
from helpers import getGenSolveProblem, plotTop4BestEightQueens, plotTop4BestGrienwank, plotTop4BestSecretWord
from readFiles import *

if __name__ == '__main__':

    ag = GeneticAlgorithms()
    ee = EvolutionaryStrategies()
    configuration = Configuration()
    '''
    readGrienwank()
    readEightQueens()
    readSecretWord()

    grienwankAG(ag, configuration)
    grienwankEEComma(ee, configuration)
    grienwankEEPlus(ee, configuration)

    secretWordAG(ag, configuration)
    secretWordEEPlus(ee, configuration)
    secretWordEEComma(ee, configuration)

    eightQueensAG(ag, configuration)
    eightQueensEEPlus(ee, configuration)
    eightQueensEEComma(ee, configuration)

    plotTop4BestGrienwank()
    plotTop4BestSecretWord()
    plotTop4BestEightQueens()
    '''