from AlgoritmosGeneticos import AlgoritmosGeneticos
from Graficos import plotarGraf
import random
from deap.benchmarks.binary import chuang_f1
if __name__ == '__main__':
    ag = AlgoritmosGeneticos()
    toolbox = ag.config_1(random.randint, 0, 1, chuang_f1)
    results = ag.start(toolbox, 50, 1)

    plotarGraf(results[1].select('gen'), results[1].select('min'))
