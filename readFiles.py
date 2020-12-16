from helpers import *

def readEightQueens():
    bestGenAgEightQueensShuffleIndexesRoulette = getGenSolveProblem(
        'results/ag_eight_queens_shuffle_indexes_roulette.csv', 'min', minValue=0)
    bestGenAgEightQueensShuffleIndexesTournament = getGenSolveProblem(
        'results/ag_eight_queens_shuffle_indexes_tournament.csv', 'min', minValue=0)
    bestGenAgEightQueensUniformIntRoulette = getGenSolveProblem('results/ag_eight_queens_uniform_int_roulette.csv',
                                                                'min', minValue=0)
    bestGenAgEightQueensUniformIntTournament = getGenSolveProblem('results/ag_eight_queens_uniform_int_tournament.csv',
                                                                  'min', minValue=0)
    bestGenEePlusEightQueensShuffleIndexesRoulette = getGenSolveProblem(
        'results/ee_plus_eight_queens_shuffle_indexes_roulette.csv', 'min', minValue=0)
    bestGenEePlusEightQueensShuffleIndexesTournament = getGenSolveProblem(
        'results/ee_plus_eight_queens_shuffle_indexes_tournament.csv', 'min', minValue=0)
    bestGenEePlusEightQueensUniformIntRoulette = getGenSolveProblem(
        'results/ee_plus_eight_queens_uniform_int_roulette.csv', 'min', minValue=0)
    bestGenEePlusEightQueensUniformIntTournament = getGenSolveProblem(
        'results/ee_plus_eight_queens_uniform_int_tournament.csv', 'min', minValue=0)
    bestGenEeCommaEightQueensShuffleIndexesRoulette = getGenSolveProblem(
        'results/ee_comma_eight_queens_shuffle_indexes_roulette.csv', 'min', minValue=0)
    bestGenEeCommaEightQueensShuffleIndexesTournament = getGenSolveProblem(
        'results/ee_comma_eight_queens_shuffle_indexes_tournament.csv', 'min', minValue=0)
    bestGenEeCommaEightQueensUniformIntRoulette = getGenSolveProblem(
        'results/ee_comma_eight_queens_uniform_int_roulette.csv', 'min', minValue=0)
    bestGenEeCommaEightQueensUniformIntTournament = getGenSolveProblem(
        'results/ee_comma_eight_queens_uniform_int_tournament.csv', 'min', minValue=0)

    print("\n\n\n(8 RAINHAS) - Melhor geração da conf de Ag shuffleIndexesRoulette: {}".format(
        bestGenAgEightQueensShuffleIndexesRoulette))
    print("(8 RAINHAS) - Melhor geração da conf de Ag shuffleIndexesTournament: {}".format(
        bestGenAgEightQueensShuffleIndexesTournament))
    print("(8 RAINHAS) - Melhor geração da conf de Ag uniformIntRoulette: {}".format(
        bestGenAgEightQueensUniformIntRoulette))
    print("(8 RAINHAS) - Melhor geração da conf de Ag uniformIntTournament: {}".format(
        bestGenAgEightQueensUniformIntTournament))
    print("(8 RAINHAS) - Melhor geração da conf de Ee Plus shuffleIndexesRoulette: {}".format(
        bestGenEePlusEightQueensShuffleIndexesRoulette))
    print("(8 RAINHAS) - Melhor geração da conf de Ee Plus shuffleIndexesTournament: {}".format(
        bestGenEePlusEightQueensShuffleIndexesTournament))
    print("(8 RAINHAS) - Melhor geração da conf de Ee Plus uniformIntRoulette: {}".format(
        bestGenEePlusEightQueensUniformIntRoulette))
    print("(8 RAINHAS) - Melhor geração da conf de Ee Plus uniformIntTournament: {}".format(
        bestGenEePlusEightQueensUniformIntTournament))
    print("(8 RAINHAS) - Melhor geração da conf de Ee Comma shuffleIndexesRoulette: {}".format(
        bestGenEeCommaEightQueensShuffleIndexesRoulette))
    print("(8 RAINHAS) - Melhor geração da conf de Ee Comma shuffleIndexesTournament: {}".format(
        bestGenEeCommaEightQueensShuffleIndexesTournament))
    print("(8 RAINHAS) - Melhor geração da conf de Ee Comma uniformIntRoulette: {}".format(
        bestGenEeCommaEightQueensUniformIntRoulette))
    print("(8 RAINHAS) - Melhor geração da conf de Ee Comma uniformIntTournament: {}".format(
        bestGenEeCommaEightQueensUniformIntTournament))


def readSecretWord():
    bestGenAgSecretWordTwoShuffleIndexesRoulette = getGenSolveProblem('results/ag_secret_word_two_point_shuffle_indexes_roulette.csv', 'max', maxValue=1)
    bestGenAgSecretWordTwoShuffleIndexesTournament = getGenSolveProblem('results/ag_secret_word_two_point_shuffle_indexes_tournament.csv', 'max', maxValue=1)
    bestGenAgSecretWordOneShuffleIndexesRoulette = getGenSolveProblem('results/ag_secret_word_one_point_shuffle_indexes_roulette.csv', 'max', maxValue=1)
    bestGenAgSecretWordOneShuffleIndexesTournament = getGenSolveProblem('results/ag_secret_word_one_point_shuffle_indexes_tournament.csv', 'max', maxValue=1)
    bestGenEePlusSecretWordTwoShuffleIndexesRoulette = getGenSolveProblem('results/ee_plus_secret_word_two_point_shuffle_indexes_roulette.csv', 'max', maxValue=1)
    bestGenEePlusSecretWordTwoShuffleIndexesTournament = getGenSolveProblem('results/ee_plus_secret_word_two_point_shuffle_indexes_tournament.csv', 'max', maxValue=1)
    bestGenEePlusSecretWordOneShuffleIndexesRoulette = getGenSolveProblem('results/ee_plus_secret_word_one_point_shuffle_indexes_roulette.csv', 'max', maxValue=1)
    bestGenEePlusSecretWordOneShuffleIndexesTournament = getGenSolveProblem('results/ee_plus_secret_word_one_point_shuffle_indexes_tournament.csv', 'max', maxValue=1)
    bestGenEeCommaSecretWordTwoShuffleIndexesRoulette = getGenSolveProblem('results/ee_comma_secret_word_two_point_shuffle_indexes_roulette.csv', 'max', maxValue=1)
    bestGenEeCommaSecretWordTwoShuffleIndexesTournament = getGenSolveProblem('results/ee_comma_secret_word_two_point_shuffle_indexes_tournament.csv', 'max', maxValue=1)
    bestGenEeCommaSecretWordOneShuffleIndexesRoulette = getGenSolveProblem('results/ee_comma_secret_word_one_point_shuffle_indexes_roulette.csv', 'max', maxValue=1)
    bestGenEeCommaSecretWordOneShuffleIndexesTournament = getGenSolveProblem('results/ee_comma_secret_word_one_point_shuffle_indexes_tournament.csv', 'max', maxValue=1)

    print("\n\n\n(PALAVRA CHAVE) - Melhor geração da conf de Ag TwoShuffleIndexesRoulette: {}".format(bestGenAgSecretWordTwoShuffleIndexesRoulette))
    print("(PALAVRA CHAVE) - Melhor geração da conf de Ag TwoShuffleIndexesTournament: {}".format(bestGenAgSecretWordTwoShuffleIndexesTournament))
    print("\n\n\n(PALAVRA CHAVE) - Melhor geração da conf de Ag OneShuffleIndexesRoulette: {}".format(bestGenAgSecretWordOneShuffleIndexesRoulette))
    print("(PALAVRA CHAVE) - Melhor geração da conf de Ag OneShuffleIndexesTournament: {}".format(bestGenAgSecretWordOneShuffleIndexesTournament))
    print("(PALAVRA CHAVE) - Melhor geração da conf de Ee Plus TwoShuffleIndexesRoulette: {}".format(bestGenEePlusSecretWordTwoShuffleIndexesRoulette))
    print("(PALAVRA CHAVE) - Melhor geração da conf de Ee Plus TwoShuffleIndexesTournament: {}".format(bestGenEePlusSecretWordTwoShuffleIndexesTournament))
    print("(PALAVRA CHAVE) - Melhor geração da conf de Ee Plus OneShuffleIndexesRoulette: {}".format(bestGenEePlusSecretWordOneShuffleIndexesRoulette))
    print("(PALAVRA CHAVE) - Melhor geração da conf de Ee Plus OneShuffleIndexesTournament: {}".format(bestGenEePlusSecretWordOneShuffleIndexesTournament))
    print("(PALAVRA CHAVE) - Melhor geração da conf de Ee Comma TwoShuffleIndexesRoulette: {}".format(bestGenEeCommaSecretWordTwoShuffleIndexesRoulette))
    print("(PALAVRA CHAVE) - Melhor geração da conf de Ee Comma TwoShuffleIndexesTournament: {}".format(bestGenEeCommaSecretWordTwoShuffleIndexesTournament))
    print("(PALAVRA CHAVE) - Melhor geração da conf de Ee Comma OneShuffleIndexesRoulette: {}".format(bestGenEeCommaSecretWordOneShuffleIndexesRoulette))
    print("(PALAVRA CHAVE) - Melhor geração da conf de Ee Comma OneShuffleIndexesTournament: {}".format(bestGenEeCommaSecretWordOneShuffleIndexesTournament))

def readChuang_f1():
    bestGenAgChuangShuffleIndexesRoulette = getGenSolveProblem('results/ag_chuang_f1_shuffle_indexes_roulette.csv',
                                                               'min', minValue=0.0)
    bestGenAgChuangShuffleIndexesTournament = getGenSolveProblem('results/ag_chuang_f1_shuffle_indexes_tournament.csv',
                                                                 'min', minValue=0.0)
    bestGenAgChuangUniformIntRoulette = getGenSolveProblem('results/ag_chuang_f1_uniform_int_roulette.csv', 'min',
                                                           minValue=0.0)
    bestGenAgChuangUniformIntTournament = getGenSolveProblem('results/ag_chuang_f1_uniform_int_tournament.csv', 'min',
                                                             minValue=0.0)
    bestGenEePlusChuangShuffleIndexesRoulette = getGenSolveProblem(
        'results/ee_plus_chuang_f1_shuffle_indexes_roulette.csv', 'min', minValue=0.0)
    bestGenEePlusChuangShuffleIndexesTournament = getGenSolveProblem(
        'results/ee_plus_chuang_f1_shuffle_indexes_tournament.csv', 'min', minValue=0.0)
    bestGenEePlusChuangUniformIntRoulette = getGenSolveProblem('results/ee_plus_chuang_f1_uniform_int_roulette.csv',
                                                               'min', minValue=0.0)
    bestGenEePlusChuangUniformIntTournament = getGenSolveProblem('results/ee_plus_chuang_f1_uniform_int_tournament.csv',
                                                                 'min', minValue=0.0)
    bestGenEeCommaChuangShuffleIndexesRoulette = getGenSolveProblem(
        'results/ee_comma_chuang_f1_shuffle_indexes_roulette.csv', 'min', minValue=0.0)
    bestGenEeCommaChuangShuffleIndexesTournament = getGenSolveProblem(
        'results/ee_comma_chuang_f1_shuffle_indexes_tournament.csv', 'min', minValue=0.0)
    bestGenEeCommaChuangUniformIntRoulette = getGenSolveProblem('results/ee_comma_chuang_f1_uniform_int_roulette.csv',
                                                                'min', minValue=0.0)
    bestGenEeCommaChuangUniformIntTournament = getGenSolveProblem(
        'results/ee_comma_chuang_f1_uniform_int_tournament.csv', 'min', minValue=0.0)

    print("\n\n\n(CHUANG F1) - Melhor geração da conf de Ag shuffleIndexesRoulette: {}".format(
        bestGenAgChuangShuffleIndexesRoulette))
    print("(CHUANG F1) - Melhor geração da conf de Ag shuffleIndexesTournament: {}".format(
        bestGenAgChuangShuffleIndexesTournament))
    print("(CHUANG F1) - Melhor geração da conf de Ag uniformIntRoulette: {}".format(bestGenAgChuangUniformIntRoulette))
    print("(CHUANG F1) - Melhor geração da conf de Ag uniformIntTournament: {}".format(
        bestGenAgChuangUniformIntTournament))
    print("(CHUANG F1) - Melhor geração da conf de Ee Plus shuffleIndexesRoulette: {}".format(
        bestGenEePlusChuangShuffleIndexesRoulette))
    print("(CHUANG F1) - Melhor geração da conf de Ee Plus shuffleIndexesTournament: {}".format(
        bestGenEePlusChuangShuffleIndexesTournament))
    print("(CHUANG F1) - Melhor geração da conf de Ee Plus uniformIntRoulette: {}".format(
        bestGenEePlusChuangUniformIntRoulette))
    print("(CHUANG F1) - Melhor geração da conf de Ee Plus uniformIntTournament: {}".format(
        bestGenEePlusChuangUniformIntTournament))
    print("(CHUANG F1) - Melhor geração da conf de Ee Comma shuffleIndexesRoulette: {}".format(
        bestGenEeCommaChuangShuffleIndexesRoulette))
    print("(CHUANG F1) - Melhor geração da conf de Ee Comma shuffleIndexesTournament: {}".format(
        bestGenEeCommaChuangShuffleIndexesTournament))
    print("(CHUANG F1) - Melhor geração da conf de Ee Comma uniformIntRoulette: {}".format(
        bestGenEeCommaChuangUniformIntRoulette))
    print("(CHUANG F1) - Melhor geração da conf de Ee Comma uniformIntTournament: {}".format(
        bestGenEeCommaChuangUniformIntTournament))

