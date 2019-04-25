import random

class Individuals(object):

    def __init__(self, sizePopulation, password):
        self.__sizePopulation = sizePopulation
        self.__password = password

    @property
    def sizePopulation(self):
        return self.__sizePopulation

    @property
    def password(self):
        return self.__password



    def generateFirstPopulation(sizePopulation, password):
        ''' Generates the first population with input size and password '''
        population = []
        i = 0
        while i < sizePopulation:
            population.append(generateAWord(len(password)))
            i+=1
        return population
