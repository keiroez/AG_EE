from genetic_algorithms import GeneticAlgorithms
from configuration import Configuration
from secretWord import secretWordAG
from eightQueens import eightQueensAG
from chuangF1 import chuangF1AG
from helpers import getGenSolveProblem

if __name__ == '__main__':
    ag = GeneticAlgorithms()
    configuration = Configuration()

    #secretWordAG(ag, configuration)
    #eightQueensAG(ag, configuration)
    #chuangF1AG(ag, configuration)

    bestGenSecretWordShuffleIndexesRoulette = getGenSolveProblem('results/ag_secret_word_shuffle_indexes_roulette.csv', 'max', maxValue=1)
    bestGenSecretWordShuffleIndexesTournament = getGenSolveProblem('results/ag_secret_word_shuffle_indexes_tournament.csv', 'max', maxValue=1)
    bestGenSecretWordFlipBitRoulette = getGenSolveProblem('results/ag_secret_word_flip_bit_roulette.csv', 'max', maxValue=1)
    bestGenSecretWordFlipBitTournament = getGenSolveProblem('results/ag_secret_word_flip_bit_tournament.csv', 'max', maxValue=1)

    print("\n\n\n(PALAVRA CHAVE) - Melhor geração da conf de shuffleIndexesRoulette: {}".format(bestGenSecretWordShuffleIndexesRoulette))
    print("(PALAVRA CHAVE) - Melhor geração da conf de shuffleIndexesTournament: {}".format(bestGenSecretWordShuffleIndexesTournament))
    print("(PALAVRA CHAVE) - Melhor geração da conf de flipBitRoulette: {}".format(bestGenSecretWordFlipBitRoulette))
    print("(PALAVRA CHAVE) - Melhor geração da conf de flipBitTournament: {}".format(bestGenSecretWordFlipBitTournament))


    bestGenEightQueensShuffleIndexesRoulette = getGenSolveProblem('results/ag_eight_queens_shuffle_indexes_roulette.csv', 'min', minValue=0)
    bestGenEightQueensShuffleIndexesTournament = getGenSolveProblem('results/ag_eight_queens_shuffle_indexes_tournament.csv', 'min', minValue=0)
    bestGenEightQueensUniformIntRoulette = getGenSolveProblem('results/ag_eight_queens_uniform_int_roulette.csv', 'min', minValue=0)
    bestGenEightQueensUniformIntTournament = getGenSolveProblem('results/ag_eight_queens_uniform_int_tournament.csv', 'min', minValue=0)

    print("\n\n\n(8 RAINHAS) - Melhor geração da conf de shuffleIndexesRoulette: {}".format(bestGenEightQueensShuffleIndexesRoulette))
    print("(8 RAINHAS) - Melhor geração da conf de shuffleIndexesTournament: {}".format(bestGenEightQueensShuffleIndexesTournament))
    print("(8 RAINHAS) - Melhor geração da conf de uniformIntRoulette: {}".format(bestGenEightQueensUniformIntRoulette))
    print("(8 RAINHAS) - Melhor geração da conf de uniformIntTournament: {}".format(bestGenEightQueensUniformIntTournament))

    bestGenChuangShuffleIndexesRoulette = getGenSolveProblem('results/ag_chuang_f1_shuffle_indexes_roulette.csv', 'min', minValue=0.0)
    bestGenChuangShuffleIndexesTournament = getGenSolveProblem('results/ag_chuang_f1_shuffle_indexes_tournament.csv', 'min', minValue=0.0)
    bestGenChuangUniformIntRoulette = getGenSolveProblem('results/ag_chuang_f1_uniform_int_roulette.csv', 'min', minValue=0.0)
    bestGenChuangUniformIntTournament = getGenSolveProblem('results/ag_chuang_f1_uniform_int_tournament.csv', 'min', minValue=0.0)

    print("\n\n\n(CHUANG F1) - Melhor geração da conf de shuffleIndexesRoulette: {}".format(bestGenChuangShuffleIndexesRoulette))
    print("(CHUANG F1) - Melhor geração da conf de shuffleIndexesTournament: {}".format(bestGenChuangShuffleIndexesTournament))
    print("(CHUANG F1) - Melhor geração da conf de uniformIntRoulette: {}".format(bestGenChuangUniformIntRoulette))
    print("(CHUANG F1) - Melhor geração da conf de uniformIntTournament: {}".format(bestGenChuangUniformIntTournament))