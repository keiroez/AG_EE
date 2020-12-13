import string
import random
import csv
import matplotlib.pyplot as plt
from deap import creator, base, tools
from evaluations import WORD_BASE


def plotChart(gen, best_per_gen):
    t = gen
    s = best_per_gen

    fig, ax = plt.subplots()
    ax.plot(t, s)

    ax.set(xlabel='Gerações', ylabel='Melhor fitness')
    ax.grid()

    plt.show()


def generateWord(min, max):
    return ''.join([random.choice(string.ascii_letters) for _ in range(max)])


def baseToolboxEightQueens():
    creator.create("FitnessType", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessType)
    TAMANHO = 8
    toolbox = base.Toolbox()
    toolbox.register("FitnessType", random.sample, range(TAMANHO), TAMANHO)
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.FitnessType)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    return toolbox

def baseToolboxSecretWord():
    creator.create("FitnessType", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessType)
    toolbox = base.Toolbox()
    toolbox.register("attr", generateWord, 0, len(WORD_BASE),)
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.attr,)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    return toolbox

def baseToolboxChuang_f1():
    creator.create("FitnessType", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessType)
    toolbox = base.Toolbox()
    toolbox.register("attr", random.randint, 0, 1,)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr, 10)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    return toolbox


def saveBestResult(data):
    writer = csv.writer(open("best_result.csv", 'w'))
    for row in data:
        writer.writerow(row)