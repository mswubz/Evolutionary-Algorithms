from fitness import Fitness
from selectBreeders import Breeders
from createIndividuals import Individuals
from breederReproduction import Reproduction
from mutation import Mutation

import random

def generateWord (length):
    ''' Generates a random word of input length '''
    i = 0
    result = ""
    while i < length:
        letter = chr(97 + int(26 * random.random()))
        result += letter
        i +=1
    return result


print("Welcome to the Knapsack Problem")

print("Enter an integer for the length of password")
password_length = int(input())

password = generateWord(password_length)

print("Password is: ")
print(password)

print("Enter an integer for the size of population")
size_Population = int(input())

Individuals = Individuals(password, size_Population)

print("The first population is: ")
first_population = Individuals.generateFirstPopulation(size_Population, password)
print(first_population)

#Fitness = Fitness()
#Breeders = Breeders()
#Reproduction = Reproduction()
#Mutation = Mutation()



