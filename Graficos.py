import matplotlib
import matplotlib.pyplot as plt

class Grafico:
    def plotarGraf(gen, best_per_gen):
        t = gen
        s = best_per_gen

        fig, ax = plt.subplots()
        ax.plot(t, s)

        ax.set(xlabel='Gerações', ylabel='Melhor fitness')
        ax.grid()

        plt.show()