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
    print("(PALAVRA CHAVE) - Melhor geração da conf de Ag OneShuffleIndexesRoulette: {}".format(bestGenAgSecretWordOneShuffleIndexesRoulette))
    print("(PALAVRA CHAVE) - Melhor geração da conf de Ag OneShuffleIndexesTournament: {}".format(bestGenAgSecretWordOneShuffleIndexesTournament))
    print("(PALAVRA CHAVE) - Melhor geração da conf de Ee Plus TwoShuffleIndexesRoulette: {}".format(bestGenEePlusSecretWordTwoShuffleIndexesRoulette))
    print("(PALAVRA CHAVE) - Melhor geração da conf de Ee Plus TwoShuffleIndexesTournament: {}".format(bestGenEePlusSecretWordTwoShuffleIndexesTournament))
    print("(PALAVRA CHAVE) - Melhor geração da conf de Ee Plus OneShuffleIndexesRoulette: {}".format(bestGenEePlusSecretWordOneShuffleIndexesRoulette))
    print("(PALAVRA CHAVE) - Melhor geração da conf de Ee Plus OneShuffleIndexesTournament: {}".format(bestGenEePlusSecretWordOneShuffleIndexesTournament))
    print("(PALAVRA CHAVE) - Melhor geração da conf de Ee Comma TwoShuffleIndexesRoulette: {}".format(bestGenEeCommaSecretWordTwoShuffleIndexesRoulette))
    print("(PALAVRA CHAVE) - Melhor geração da conf de Ee Comma TwoShuffleIndexesTournament: {}".format(bestGenEeCommaSecretWordTwoShuffleIndexesTournament))
    print("(PALAVRA CHAVE) - Melhor geração da conf de Ee Comma OneShuffleIndexesRoulette: {}".format(bestGenEeCommaSecretWordOneShuffleIndexesRoulette))
    print("(PALAVRA CHAVE) - Melhor geração da conf de Ee Comma OneShuffleIndexesTournament: {}".format(bestGenEeCommaSecretWordOneShuffleIndexesTournament))

def readGrienwank():
    bestGenAgGrienwankShuffleIndexesRoulette = getGenSolveProblem('results/ag_grienwank_shuffle_indexes_roulette.csv',
                                                               'min', minValue=0.0)
    bestGenAgGrienwankShuffleIndexesTournament = getGenSolveProblem('results/ag_grienwank_shuffle_indexes_tournament.csv',
                                                                 'min', minValue=0.0)
    bestGenAgGrienwankUniformIntRoulette = getGenSolveProblem('results/ag_grienwank_uniform_int_roulette.csv', 'min',
                                                           minValue=0.0)
    bestGenAgGrienwankUniformIntTournament = getGenSolveProblem('results/ag_grienwank_uniform_int_tournament.csv', 'min',
                                                             minValue=0.0)
    bestGenEePlusGrienwankShuffleIndexesRoulette = getGenSolveProblem(
        'results/ee_plus_grienwank_shuffle_indexes_roulette.csv', 'min', minValue=0.0)
    bestGenEePlusGrienwankShuffleIndexesTournament = getGenSolveProblem(
        'results/ee_plus_grienwank_shuffle_indexes_tournament.csv', 'min', minValue=0.0)
    bestGenEePlusGrienwankUniformIntRoulette = getGenSolveProblem('results/ee_plus_grienwank_uniform_int_roulette.csv',
                                                               'min', minValue=0.0)
    bestGenEePlusGrienwankUniformIntTournament = getGenSolveProblem('results/ee_plus_grienwank_uniform_int_tournament.csv',
                                                                 'min', minValue=0.0)
    bestGenEeCommaGrienwankShuffleIndexesRoulette = getGenSolveProblem(
        'results/ee_comma_grienwank_shuffle_indexes_roulette.csv', 'min', minValue=0.0)
    bestGenEeCommaGrienwankShuffleIndexesTournament = getGenSolveProblem(
        'results/ee_comma_grienwank_shuffle_indexes_tournament.csv', 'min', minValue=0.0)
    bestGenEeCommaGrienwankUniformIntRoulette = getGenSolveProblem('results/ee_comma_grienwank_uniform_int_roulette.csv',
                                                                'min', minValue=0.0)
    bestGenEeCommaGrienwankUniformIntTournament = getGenSolveProblem(
        'results/ee_comma_grienwank_uniform_int_tournament.csv', 'min', minValue=0.0)

    print("\n\n\n(GRIENWANK) - Melhor geração da conf de Ag shuffleIndexesRoulette: {}".format(
        bestGenAgGrienwankShuffleIndexesRoulette))
    print("(GRIENWANK) - Melhor geração da conf de Ag shuffleIndexesTournament: {}".format(
        bestGenAgGrienwankShuffleIndexesTournament))
    print("(GRIENWANK) - Melhor geração da conf de Ag uniformIntRoulette: {}".format(bestGenAgGrienwankUniformIntRoulette))
    print("(GRIENWANK) - Melhor geração da conf de Ag uniformIntTournament: {}".format(
        bestGenAgGrienwankUniformIntTournament))
    print("(GRIENWANK) - Melhor geração da conf de Ee Plus shuffleIndexesRoulette: {}".format(
        bestGenEePlusGrienwankShuffleIndexesRoulette))
    print("(GRIENWANK) - Melhor geração da conf de Ee Plus shuffleIndexesTournament: {}".format(
        bestGenEePlusGrienwankShuffleIndexesTournament))
    print("(GRIENWANK) - Melhor geração da conf de Ee Plus uniformIntRoulette: {}".format(
        bestGenEePlusGrienwankUniformIntRoulette))
    print("(GRIENWANK) - Melhor geração da conf de Ee Plus uniformIntTournament: {}".format(
        bestGenEePlusGrienwankUniformIntTournament))
    print("(GRIENWANK) - Melhor geração da conf de Ee Comma shuffleIndexesRoulette: {}".format(
        bestGenEeCommaGrienwankShuffleIndexesRoulette))
    print("(GRIENWANK) - Melhor geração da conf de Ee Comma shuffleIndexesTournament: {}".format(
        bestGenEeCommaGrienwankShuffleIndexesTournament))
    print("(GRIENWANK) - Melhor geração da conf de Ee Comma uniformIntRoulette: {}".format(
        bestGenEeCommaGrienwankUniformIntRoulette))
    print("(GRIENWANK) - Melhor geração da conf de Ee Comma uniformIntTournament: {}".format(
        bestGenEeCommaGrienwankUniformIntTournament))

