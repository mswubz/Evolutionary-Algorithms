import random

class Mutation(object):

    def __init__(self, population, chance_of_mutation):
        self.__word = "word"
        self.__population = population
        self.__chance_of_muation = chance_of_mutation

    def mutateWord(self, word):
        index_modification = int(random.random() * len(word))
        if (index_modification == 0):
            word = chr(97 + int(26 * random.random())) + word[1:]
        else:
            word = word[:index_modification] + chr(97 + int(26 * random.random())) + word[index_modification + 1:]
        return word

    def mutatePopulation(self, population, chance_of_mutation):
        for i in range(len(population)):
            if random.random() * 100 < chance_of_mutation:
                population[i] = self.mutateWord(population[i])
        return population
