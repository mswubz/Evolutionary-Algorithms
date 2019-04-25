import random

class Mutation(object):

    def __init__(self, word, population, chance_of_mutation):
        self.__word = word
        self.__population = population
        self.__chance_of_muation = chance_of_mutation

    @property
    def word(self):
        return self.__word

    @property
    def population(self):
        return self.__word

    @property
    def chance_of_mutation(self):
        return self.__chance_of_muation


    def mutateWord(word):
        index_modification = int(random.random() * len(word))
        if (index_modification == 0):
            word = chr(97 + int(26 * random.random())) + word[1:]
        else:
            word = word[:index_modification] + chr(97 + int(26 * random.random())) + word[index_modification + 1:]
        return word


    def mutatePopulation(population, chance_of_mutation):
        for i in range(len(population)):
            if random.random() * 100 < chance_of_mutation:
                population[i] = mutateWord(population[i])
        return population