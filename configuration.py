from deap import tools

class Configuration:

    def configFlipBitTournament(self, toolbox, evaluate, mate):
        toolbox.register("evaluate", evaluate)
        toolbox.register("mate", mate)
        toolbox.register("mutate", tools.mutFlipBit, indpb=0.1)
        toolbox.register("select", tools.selTournament, tournsize=3)
        return toolbox

    def configFlipBitRoulette(self, toolbox, evaluate, mate):
        toolbox.register("evaluate", evaluate)
        toolbox.register("mate", mate)
        toolbox.register("mutate", tools.mutFlipBit, indpb=0.1)
        toolbox.register("select", tools.selRoulette)
        return toolbox

    def configShuffleIndexesTournament(self, toolbox, evaluate, mate):
        toolbox.register("evaluate", evaluate)
        toolbox.register("mate", mate)
        toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.1)
        toolbox.register("select", tools.selTournament, tournsize=3)
        return toolbox

    def configUniformIntTournament(self, toolbox, evaluate, mate):
        toolbox.register("evaluate", evaluate)
        toolbox.register("mate", mate)
        toolbox.register("mutate", tools.mutUniformInt, low=0, up=4, indpb=0.1)
        toolbox.register("select", tools.selTournament, tournsize=3)
        return toolbox

    def configFlipBitRoulette(self, toolbox, evaluate, mate):
        toolbox.register("evaluate", evaluate)
        toolbox.register("mate", mate)
        toolbox.register("mutate", tools.mutFlipBit, indpb=0.1)
        toolbox.register("select", tools.selRoulette)
        return toolbox

    def configShuffleIndexesRoulette(self, toolbox, evaluate, mate):
        toolbox.register("evaluate", evaluate)
        toolbox.register("mate", mate)
        toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.1)
        toolbox.register("select", tools.selRoulette)
        return toolbox

    def configUniformIntRoulette(self, toolbox, evaluate, mate):
        toolbox.register("evaluate", evaluate)
        toolbox.register("mate", mate)
        toolbox.register("mutate", tools.mutUniformInt, low=0, up=4, indpb=0.1)
        toolbox.register("select", tools.selRoulette)
        return toolbox

    def configGaussianRoulette(self, toolbox, evaluate, mate):
        toolbox.register("evaluate", evaluate)
        toolbox.register("mate", mate)
        toolbox.register("mutate", tools.mutGaussian, mu=0.5, sigma=0.4, indpb=0.1)
        toolbox.register("select", tools.selRoulette)
        return toolbox

    def configGaussianTournament(self, toolbox, evaluate, mate):
        toolbox.register("evaluate", evaluate)
        toolbox.register("mate", mate)
        toolbox.register("mutate", tools.mutGaussian, mu=0.5, sigma=0.4, indpb=0.1, )
        toolbox.register("select", tools.selTournament, tournsize=3)
        return toolbox

