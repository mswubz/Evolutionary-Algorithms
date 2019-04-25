import random

class Individuals(object):

    def __init__(self, length, sizePopulation, password):
        self.__length = length
        self.__sizePopulation = sizePopulation
        self.__password = password

    @property
    def length(self):
        return self.__length

    @property
    def sizePopulation(self):
        return self.__sizePopulation

    @property
    def password(self):
        return self.__password

    def generateWord (length):
        ''' Generates a random word of input length '''
        i = 0
        result = ""
        while i < length:
            letter = chr(97 + int(26 * random.random()))
            result += letter
            i +=1
        return result

    def generateFirstPopulation(sizePopulation, password):
        ''' Generates the first population with input size and password '''
        population = []
        i = 0
        while i < sizePopulation:
            population.append(generateAWord(len(password)))
            i+=1
        return population
