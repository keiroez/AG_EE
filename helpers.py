import string
import random
import csv
from ast import literal_eval

import matplotlib.pyplot as plt
from deap import creator, base, tools
from evaluations import WORD_BASE, SIZE


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


def saveBestResult(data, path):
    writer = csv.writer(open(path, 'w'))
    writer.writerow(data)

def getGenSolveProblem(path, problemType, maxValue=None, minValue=None):
    gen = SIZE
    best = None
    with open(path, 'r') as file:
        reader = csv.reader(file)
        if problemType == 'min':
            for logs in reader:
                for log in logs:
                    array_log = literal_eval(log)
                    if array_log['min'] == minValue:
                        gen = array_log['gen']
                        best = array_log['min']
                        break
                    if array_log['gen'] == SIZE and best is None:
                        best = array_log['min']
        else:
            val = 0
            for logs in reader:
                for log in logs:
                    array_log = literal_eval(log)
                    if array_log['max'] == maxValue:
                        gen = array_log['gen']
                        best = array_log['max']
                        break
                    if array_log['gen'] == SIZE and best is None:
                        best = array_log['max']


    return gen, best