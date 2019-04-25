from fitness import Fitness
from selectBreeders import Breeders
from createIndividuals import Individuals
from breederReproduction import Reproduction
from mutation import Mutation

import random

password = "password"
size_Population = 1
Individuals = Individuals(size_Population, password)

print("Welcome to the Knapsack Problem")

print("Enter an integer for the length of password")
password_length = int(input())

password = Individuals.generateWord(password_length)

print("Password is: ")
print(password)

print("Enter an integer for the size of population")
size_Population = int(input())

print("The first population is: ")
first_population = Individuals.generateFirstPopulation(size_Population, password)
print(first_population)

#Fitness = Fitness()
#Breeders = Breeders()
#Reproduction = Reproduction()
#Mutation = Mutation()



