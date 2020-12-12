from deap import tools

class Configuration:

    def configFlipBitTournament(self, toolbox, evaluate, mate):
        toolbox.register("evaluate", evaluate)
        toolbox.register("mate", mate)
        toolbox.register("mutate", tools.mutFlipBit, indpb=0.1)
        toolbox.register("select", tools.selTournament, tournsize=3)
        return toolbox

    def configShuffleIndexesTournament(self, toolbox, evaluate, mate):
        toolbox.register("evaluate", evaluate)
        toolbox.register("mate", mate)
        toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.1)
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

