from fitness import Fitness

import random
import operator

class Breeders:

    def __init__(self, population, password, best_sample, lucky_few):
        self.__population = population
        self.__password = password
        self.__populationSorted = []
        self.__best_sample = best_sample
        self.__lucky_few = lucky_few

    Fitness = Fitness()
    
    def computePerfPopulation(self, population, password):
        populationPerf = {}
        for individual in population:
            populationPerf[individual] = Fitness.fitness(password, individual)
        return sorted(populationPerf.items(), key=operator.itemgetter(1), reverse=True)


    def selectFromPopulation(self, populationSorted, best_sample, lucky_few):
        nextGeneration = []
        for i in range(best_sample):
            nextGeneration.append(populationSorted[i][0])
        for i in range(lucky_few):
            nextGeneration.append(random.choice(populationSorted)[0])
        random.shuffle(nextGeneration)
        return nextGeneration
