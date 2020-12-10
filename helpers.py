import string
import random
import matplotlib.pyplot as plt


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
