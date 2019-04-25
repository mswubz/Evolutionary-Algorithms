import random

class Reproduction(object):

    def __init__(self, individual1, individual2, breeders, number_of_child):
        self.__individual1 = individual1
        self.__individual2 = individual2
        self.__breeders = breeders
        self.__number_of_child = number_of_child

    @property
    def individual1(self):
        return self.__individual1

    @property
    def individual2(self):
        return self.__individual2

    @property
    def breeders(self):
        return self.__breeders

    @property
    def number_of_child(self):
        return self.__number_of_child

    def createChild(individual1, individual2):
        child = ""
        for i in range(len(individual1)):
            if (int(100 * random.random()) < 50):
                child += individual1[i]
            else:
                child += individual2[i]
        return child


    def createChildren(breeders, number_of_child):
        nextPopulation = []
        for i in range(len(breeders) / 2):
            for j in range(number_of_child):
                nextPopulation.append(createChild(breeders[i], breeders[len(breeders) - 1 - i]))
        return nextPopulation
