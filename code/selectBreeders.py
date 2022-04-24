
import random
import operator

class Breeders:

    def __init__(self, population, password, best_sample, lucky_few):
        self.__population = population
        self.__password = password
        self.__populationSorted = []
        self.__best_sample = best_sample
        self.__lucky_few = lucky_few
    
    def fitness(self, password, test_word):
        if (len(test_word) != len(password)):
            print("Taille Incompatible")
            return
        else:
            score = 0
            i = 0
            while (i < len(password)):
                if (password[i] == test_word[i]):
                    score += 1
                i += 1
            return score * 100 / len(password)
    
    def computePerfPopulation(self, population, password):
        populationPerf = {}
        for individual in population:
            populationPerf[individual] = self.fitness(password, individual)
        return sorted(populationPerf.items(), key=operator.itemgetter(1), reverse=True)


    def selectFromPopulation(self, populationSorted, best_sample, lucky_few):
        nextGeneration = []
        for i in range(best_sample):
            nextGeneration.append(populationSorted[i][0])
        for i in range(lucky_few):
            nextGeneration.append(random.choice(populationSorted)[0])
        random.shuffle(nextGeneration)
        return nextGeneration
