import random

class Individuals:

    def __init__(self, sizePopulation, password):
        self.__sizePopulation = sizePopulation
        self.__password = password

    def generateWord(length):
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
