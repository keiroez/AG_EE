from genetic_algorithms import GeneticAlgorithms
from evolutionary_strategies import EvolutionaryStrategies
from configuration import Configuration
from secretWord import *
from eightQueens import *
from grienwank import *
from helpers import getGenSolveProblem, getLogArray, plotCharComparation
from readFiles import *

if __name__ == '__main__':

    ag = GeneticAlgorithms()
    ee = EvolutionaryStrategies()
    configuration = Configuration()


    readGrienwank()
    readEightQueens()
    readSecretWord()
'''
    grienwankAG(ag, configuration)
    grienwankEEComma(ee, configuration)
    grienwankEEPlus(ee, configuration)

    secretWordAG(ag, configuration)
    secretWordEEPlus(ee, configuration)
    secretWordEEComma(ee, configuration)

    eightQueensAG(ag, configuration)
    eightQueensEEPlus(ee, configuration)
    eightQueensEEComma(ee, configuration)
    
 

best1, gen1 = getLogArray('min', 'results/ag_eight_queens_shuffle_indexes_roulette.csv')
best2, gen2 = getLogArray('min', 'results/ag_eight_queens_shuffle_indexes_tournament.csv')
best3, gen3 = getLogArray('min', 'results/ag_eight_queens_uniform_int_roulette.csv')c
best4, gen4 = getLogArray('min', 'results/ag_eight_queens_uniform_int_tournament.csv')

plotCharComparation(best1, gen1, best2, gen2, best3, gen3, best4, gen4)

'''

