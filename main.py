from genetic_algorithms import GeneticAlgorithms
from configuration import Configuration
from secretWord import secretWordAG
from eightQueens import eightQueensAG


if __name__ == '__main__':
    ag = GeneticAlgorithms()
    configuration = Configuration()

    # secretWordAG(ag, configuration)
    eightQueensAG(ag, configuration)




