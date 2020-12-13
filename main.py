from genetic_algorithms import GeneticAlgorithms
from configuration import Configuration
from secretWord import secretWordAG
from eightQueens import eightQueensAG
from chuangF1 import chuangF1AG
from helpers import showResultLog

if __name__ == '__main__':
    ag = GeneticAlgorithms()
    configuration = Configuration()

    #secretWordAG(ag, configuration)
    #eightQueensAG(ag, configuration)
    #chuangF1AG(ag, configuration)

    showResultLog('results/ag_eight_queens_shuffle_indexes_roulette.csv')

