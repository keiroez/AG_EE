from genetic_algorithms import GeneticAlgorithms
from evolutionary_strategies import EvolutionaryStrategies
from configuration import Configuration
from secretWord import *
from eightQueens import *
from chuangF1 import *
from helpers import getGenSolveProblem, getLogArray, plotCharComparation

if __name__ == '__main__':

    ag = GeneticAlgorithms()
    ee = EvolutionaryStrategies()
    configuration = Configuration()
    '''
    secretWordAG(ag, configuration)
    secretWordEEPlus(ee, configuration)
    secretWordEEComma(ee, configuration)
    
    eightQueensAG(ag, configuration)
    eightQueensEEPlus(ee, configuration)
    eightQueensEEComma(ee, configuration)
    
    chuangF1AG(ag, configuration)
    chuangF1EEComma(ee, configuration)
    chuangF1EEPlus(ee, configuration)

    '''
    bestGenAgSecretWordShuffleIndexesRoulette = getGenSolveProblem('results/ag_secret_word_shuffle_indexes_roulette.csv', 'max', maxValue=1)
    bestGenAgSecretWordShuffleIndexesTournament = getGenSolveProblem('results/ag_secret_word_shuffle_indexes_tournament.csv', 'max', maxValue=1)
    bestGenEePlusSecretWordShuffleIndexesRoulette = getGenSolveProblem('results/ee_plus_secret_word_shuffle_indexes_roulette.csv', 'max', maxValue=1)
    bestGenEePlusSecretWordShuffleIndexesTournament = getGenSolveProblem('results/ee_plus_secret_word_shuffle_indexes_tournament.csv', 'max', maxValue=1)
    bestGenEeCommaSecretWordShuffleIndexesRoulette = getGenSolveProblem('results/ee_comma_secret_word_shuffle_indexes_roulette.csv', 'max', maxValue=1)
    bestGenEeCommaSecretWordShuffleIndexesTournament = getGenSolveProblem('results/ee_comma_secret_word_shuffle_indexes_tournament.csv', 'max', maxValue=1)

    print("\n\n\n(PALAVRA CHAVE) - Melhor geração da conf de Ag shuffleIndexesRoulette: {}".format(bestGenAgSecretWordShuffleIndexesRoulette))
    print("(PALAVRA CHAVE) - Melhor geração da conf de Ag shuffleIndexesTournament: {}".format(bestGenAgSecretWordShuffleIndexesTournament))
    print("(PALAVRA CHAVE) - Melhor geração da conf de Ee Plus shuffleIndexesRoulette: {}".format(bestGenEePlusSecretWordShuffleIndexesRoulette))
    print("(PALAVRA CHAVE) - Melhor geração da conf de Ee Plus shuffleIndexesTournament: {}".format(bestGenEePlusSecretWordShuffleIndexesTournament))
    print("(PALAVRA CHAVE) - Melhor geração da conf de Ee Comma shuffleIndexesRoulette: {}".format(bestGenEeCommaSecretWordShuffleIndexesRoulette))
    print("(PALAVRA CHAVE) - Melhor geração da conf de Ee Comma shuffleIndexesTournament: {}".format(bestGenEeCommaSecretWordShuffleIndexesTournament))


    bestGenAgEightQueensShuffleIndexesRoulette = getGenSolveProblem('results/ag_eight_queens_shuffle_indexes_roulette.csv', 'min', minValue=0)
    bestGenAgEightQueensShuffleIndexesTournament = getGenSolveProblem('results/ag_eight_queens_shuffle_indexes_tournament.csv', 'min', minValue=0)
    bestGenAgEightQueensUniformIntRoulette = getGenSolveProblem('results/ag_eight_queens_uniform_int_roulette.csv', 'min', minValue=0)
    bestGenAgEightQueensUniformIntTournament = getGenSolveProblem('results/ag_eight_queens_uniform_int_tournament.csv', 'min', minValue=0)
    bestGenEePlusEightQueensShuffleIndexesRoulette = getGenSolveProblem('results/ee_plus_eight_queens_shuffle_indexes_roulette.csv', 'min', minValue=0)
    bestGenEePlusEightQueensShuffleIndexesTournament = getGenSolveProblem('results/ee_plus_eight_queens_shuffle_indexes_tournament.csv', 'min', minValue=0)
    bestGenEePlusEightQueensUniformIntRoulette = getGenSolveProblem('results/ee_plus_eight_queens_uniform_int_roulette.csv', 'min', minValue=0)
    bestGenEePlusEightQueensUniformIntTournament = getGenSolveProblem('results/ee_plus_eight_queens_uniform_int_tournament.csv', 'min', minValue=0)
    bestGenEeCommaEightQueensShuffleIndexesRoulette = getGenSolveProblem('results/ee_comma_eight_queens_shuffle_indexes_roulette.csv', 'min', minValue=0)
    bestGenEeCommaEightQueensShuffleIndexesTournament = getGenSolveProblem('results/ee_comma_eight_queens_shuffle_indexes_tournament.csv', 'min', minValue=0)
    bestGenEeCommaEightQueensUniformIntRoulette = getGenSolveProblem('results/ee_comma_eight_queens_uniform_int_roulette.csv', 'min', minValue=0)
    bestGenEeCommaEightQueensUniformIntTournament = getGenSolveProblem('results/ee_comma_eight_queens_uniform_int_tournament.csv', 'min', minValue=0)
    

    print("\n\n\n(8 RAINHAS) - Melhor geração da conf de Ag shuffleIndexesRoulette: {}".format(bestGenAgEightQueensShuffleIndexesRoulette))
    print("(8 RAINHAS) - Melhor geração da conf de Ag shuffleIndexesTournament: {}".format(bestGenAgEightQueensShuffleIndexesTournament))
    print("(8 RAINHAS) - Melhor geração da conf de Ag uniformIntRoulette: {}".format(bestGenAgEightQueensUniformIntRoulette))
    print("(8 RAINHAS) - Melhor geração da conf de Ag uniformIntTournament: {}".format(bestGenAgEightQueensUniformIntTournament))
    print("(8 RAINHAS) - Melhor geração da conf de Ee Plus shuffleIndexesRoulette: {}".format(bestGenEePlusEightQueensShuffleIndexesRoulette))
    print("(8 RAINHAS) - Melhor geração da conf de Ee Plus shuffleIndexesTournament: {}".format(bestGenEePlusEightQueensShuffleIndexesTournament))
    print("(8 RAINHAS) - Melhor geração da conf de Ee Plus uniformIntRoulette: {}".format(bestGenEePlusEightQueensUniformIntRoulette))
    print("(8 RAINHAS) - Melhor geração da conf de Ee Plus uniformIntTournament: {}".format(bestGenEePlusEightQueensUniformIntTournament))
    print("(8 RAINHAS) - Melhor geração da conf de Ee Comma shuffleIndexesRoulette: {}".format(bestGenEeCommaEightQueensShuffleIndexesRoulette))
    print("(8 RAINHAS) - Melhor geração da conf de Ee Comma shuffleIndexesTournament: {}".format(bestGenEeCommaEightQueensShuffleIndexesTournament))
    print("(8 RAINHAS) - Melhor geração da conf de Ee Comma uniformIntRoulette: {}".format(bestGenEeCommaEightQueensUniformIntRoulette))
    print("(8 RAINHAS) - Melhor geração da conf de Ee Comma uniformIntTournament: {}".format(bestGenEeCommaEightQueensUniformIntTournament))

    bestGenAgChuangShuffleIndexesRoulette = getGenSolveProblem('results/ag_chuang_f1_shuffle_indexes_roulette.csv', 'min', minValue=0.0)
    bestGenAgChuangShuffleIndexesTournament = getGenSolveProblem('results/ag_chuang_f1_shuffle_indexes_tournament.csv', 'min', minValue=0.0)
    bestGenAgChuangUniformIntRoulette = getGenSolveProblem('results/ag_chuang_f1_uniform_int_roulette.csv', 'min', minValue=0.0)
    bestGenAgChuangUniformIntTournament = getGenSolveProblem('results/ag_chuang_f1_uniform_int_tournament.csv', 'min', minValue=0.0)
    bestGenEePlusChuangShuffleIndexesRoulette = getGenSolveProblem('results/ee_plus_chuang_f1_shuffle_indexes_roulette.csv', 'min', minValue=0.0)
    bestGenEePlusChuangShuffleIndexesTournament = getGenSolveProblem('results/ee_plus_chuang_f1_shuffle_indexes_tournament.csv', 'min', minValue=0.0)
    bestGenEePlusChuangUniformIntRoulette = getGenSolveProblem('results/ee_plus_chuang_f1_uniform_int_roulette.csv', 'min', minValue=0.0)
    bestGenEePlusChuangUniformIntTournament = getGenSolveProblem('results/ee_plus_chuang_f1_uniform_int_tournament.csv', 'min', minValue=0.0)
    bestGenEeCommaChuangShuffleIndexesRoulette = getGenSolveProblem('results/ee_comma_chuang_f1_shuffle_indexes_roulette.csv', 'min', minValue=0.0)
    bestGenEeCommaChuangShuffleIndexesTournament = getGenSolveProblem('results/ee_comma_chuang_f1_shuffle_indexes_tournament.csv', 'min', minValue=0.0)
    bestGenEeCommaChuangUniformIntRoulette = getGenSolveProblem('results/ee_comma_chuang_f1_uniform_int_roulette.csv', 'min', minValue=0.0)
    bestGenEeCommaChuangUniformIntTournament = getGenSolveProblem('results/ee_comma_chuang_f1_uniform_int_tournament.csv', 'min', minValue=0.0)


    print("\n\n\n(CHUANG F1) - Melhor geração da conf de Ag shuffleIndexesRoulette: {}".format(bestGenAgChuangShuffleIndexesRoulette))
    print("(CHUANG F1) - Melhor geração da conf de Ag shuffleIndexesTournament: {}".format(bestGenAgChuangShuffleIndexesTournament))
    print("(CHUANG F1) - Melhor geração da conf de Ag uniformIntRoulette: {}".format(bestGenAgChuangUniformIntRoulette))
    print("(CHUANG F1) - Melhor geração da conf de Ag uniformIntTournament: {}".format(bestGenAgChuangUniformIntTournament))
    print("(CHUANG F1) - Melhor geração da conf de Ee Plus shuffleIndexesRoulette: {}".format(bestGenEePlusChuangShuffleIndexesRoulette))
    print("(CHUANG F1) - Melhor geração da conf de Ee Plus shuffleIndexesTournament: {}".format(bestGenEePlusChuangShuffleIndexesTournament))
    print("(CHUANG F1) - Melhor geração da conf de Ee Plus uniformIntRoulette: {}".format(bestGenEePlusChuangUniformIntRoulette))
    print("(CHUANG F1) - Melhor geração da conf de Ee Plus uniformIntTournament: {}".format(bestGenEePlusChuangUniformIntTournament))
    print("(CHUANG F1) - Melhor geração da conf de Ee Comma shuffleIndexesRoulette: {}".format(bestGenEeCommaChuangShuffleIndexesRoulette))
    print("(CHUANG F1) - Melhor geração da conf de Ee Comma shuffleIndexesTournament: {}".format(bestGenEeCommaChuangShuffleIndexesTournament))
    print("(CHUANG F1) - Melhor geração da conf de Ee Comma uniformIntRoulette: {}".format(bestGenEeCommaChuangUniformIntRoulette))
    print("(CHUANG F1) - Melhor geração da conf de Ee Comma uniformIntTournament: {}".format(bestGenEeCommaChuangUniformIntTournament))


best1, gen1 = getLogArray('min', 'results/ag_eight_queens_shuffle_indexes_roulette.csv')
best2, gen2 = getLogArray('min', 'results/ag_eight_queens_shuffle_indexes_tournament.csv')
best3, gen3 = getLogArray('min', 'results/ag_eight_queens_uniform_int_roulette.csv')
best4, gen4 = getLogArray('min', 'results/ag_eight_queens_uniform_int_tournament.csv')

plotCharComparation(best1, gen1, best2, gen2, best3, gen3, best4, gen4)

