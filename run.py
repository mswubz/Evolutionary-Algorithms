from fitness import Fitness
from selectBreeders import Breeders
from createIndividuals import Individuals
from breederReproduction import Reproduction
from mutation import Mutation

import random

password = "password"
size_Population = 1
length = 1
Individuals = Individuals(size_Population, password, length)

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
population = first_population


print("Which word is the closest to the password? (array starts at 0)")
print("The password is: " + password)
numInArray = int(input())
best_sample = population[numInArray]

temp_population = population
del temp_population[numInArray]

print("How many other individuals would you like to keep in the population at random?")
print("Choose a number less than: " + str(len(temp_population)))
numOfLuckyFew = int(input())

which_lucky_few = []
lucky_few = []

def isInList(list, number, range):
    '''If the number is not in the list returns false, if is in list generates a new random number '''
    if number not in list:
        return number
    else:
        number = random.randint(0, range)
        return isInList(list, number, range)


for x in range(numOfLuckyFew):
    num = random.randint(0, numOfLuckyFew)
    isInList(which_lucky_few, num, numOfLuckyFew)
    which_lucky_few.append(num)

for x in range(numOfLuckyFew):
    lucky_few.append(temp_population[which_lucky_few[x]])

print("The lucky few that will survive are: " + str(lucky_few))

Breeders = Breeders(population, password, best_sample, lucky_few)

print(Breeders.computePerfPopulation(population, password))
print(Breeders.populationSorted)

print("What chance of mutation?")
chance_of_mutation = int(input())

Mutation = Mutation(population, chance_of_mutation)

population = Mutation.mutatePopulation(population, chance_of_mutation)

print("The new population is: ")
print(population)

#Fitness = Fitness()
#Reproduction = Reproduction()
#Mutation = Mutation()
