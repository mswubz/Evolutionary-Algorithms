import random

class Individuals:

    def __init__(self, sizePopulation, password, length):
        self.__sizePopulation = sizePopulation
        self.__password = password
        self.__length = length

    def generateWord(self, length):
        i = 0
        result = ""
        while i < length:
            letter = chr(97 + int(26 * random.random()))
            result += letter
            i +=1
        return result

    def generateFirstPopulation(self, sizePopulation, password):
        ''' Generates the first population with input size and password '''
        population = []
        i = 0
        while i < sizePopulation:
            population.append(self.generateWord(len(password)))
            i+=1
        return population
