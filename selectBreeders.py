import random
import operator

class Breeders(object):

    def __init__(self, population, password, populationSorted, best_sample, lucky_few):
        self.__population = population
        self.__password = password
        self.__populationSorted = populationSorted
        self.__best_sample = best_sample
        self.__lucky_few = lucky_few

    @property
    def population(self):
        return self.__population

    @property
    def password(self):
        return self.__password

    @property
    def populationSorted(self):
        return self.__populationSorted

    @property
    def best_sample(self):
        return self.__best_sample

    @property
    def lucky_few(self):
        return self.__lucky_few


    def computePerfPopulation(population, password):
        populationPerf = {}
        for individual in population:
            populationPerf[individual] = fitness(password, individual)
        return sorted(populationPerf.items(), key=operator.itemgetter(1), reverse=True)


    def selectFromPopulation(populationSorted, best_sample, lucky_few):
        nextGeneration = []
        for i in range(best_sample):
            nextGeneration.append(populationSorted[i][0])
        for i in range(lucky_few):
            nextGeneration.append(random.choice(populationSorted)[0])
        random.shuffle(nextGeneration)
        return nextGeneration
