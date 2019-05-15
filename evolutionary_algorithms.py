import random as r
import csv

class Gene:
    """This class represents a template for all genes. Every gene has a fitness and weight value. The fitness value determines how adept the gene is in surviving
    its environment. The weight value determines how much environmental carrying capacity (the space of the knapsack) that the gene takes up."""
    def __init__(self, fitness, weight):
        self.fitness = fitness
        self.weight = weight 

GENES = [Gene(r.randint(0,30),r.randint(0,30)) for x in range (0,30)]
#This variable randomly creates between 0 and 30 genes. Their fitness score and weights can also range from 0 to 30. 

ENVIRONMENT_CAPACITY = 10*len(GENES)
#This variable represents the carrying capacity of the environment. It is dynamically scalable to be always be ten times the number of genes. 

POP_SIZE = 10
#This variable represents the size of each generation's population. Each gene gets assigned a randomized binary ID

MAXIMUM_GENERATION = 250
#This variable represents the total number of generations that will be modeled. *NOTE* Excel caps out graphing at a max of 250 generations.
#For more possibilities and better alternative graphings please use MATLAB.

UNIFORM_INITIAL_POPULATION = False
#This boolean determines if the initial gene population will be either all zeros or random. A random binary population will have a higher initial
#fitness score and will therefore be optimized quicker.

def fitness(gene):
    """This function determines the fitness each gene. A gene's fitness score determines how applicable it is to survive in its environment."""
    
    """fitness(target) will return the fitness of permutation named "target".
    Higher scores are better and are equal to the total fitness of genes in the permutation.
    If total_weight is higher than the capacity, return 0 because the permutation cannot be used.
    """
    fit_counter = 0
    capacity_counter = 0
    length = 0
    for i in gene:        
        if length >= len(GENES):
            break
        if (i == 1):
            fit_counter += GENES[length].fitness
            capacity_counter += GENES[length].weight
        length += 1
    if capacity_counter > ENVIRONMENT_CAPACITY:
        #Environmental carrying capacity has been exceeded.
        return 0
    else:
        return fit_counter

def generate_ancestors(quantity):
    """Creates the initial group of gene ancestors."""
    return [create_gene() for i in range (0, quantity)]

def create_gene():
    """Creates each individual gene according to if the initial population is uniform or not."""
    if UNIFORM_INITIAL_POPULATION:
        return [r.randint(0,0) for i in range (0, len(GENES))]
    else:
        return [r.randint(0,1) for i in range (0, len(GENES))]

def perform_mutation(gene):
    """Randomly causes a mutation an element of the gene's permutation. Since the gene's array is binary, this mutation consists of either
    a one becoming a zero or a zero becoming a one.""" 
    if gene[r.randint(0, len(gene)-1)] == 1:
        gene[r.randint(0, len(gene)-1)] = 0
    else:
        gene[r.randint(0, len(gene)-1)] = 1

def evolution(population):
    """Models the reproduction process. As genes breed new genes are created. These new genes derive half their data from their mother and half from 
    their father, which is then modified by any mutations that may or may not take place."""
    p_likelihood = 0.2
    #This variable determines the parent's gene availability for reproduction.

    mutation_probability = 0.08
    #This variable represents the likelihood for mutation to occur for every instance of breeding.

    parent_lottery = 0.05
    #This variable determines the parent's chances of "getting lucky".

    p_length = int(p_likelihood*len(population))

    parents = population[:p_length]

    not_parents = population[p_length:]

    for i in not_parents:
        if parent_lottery > r.random():
            parents.append(i)

    for j in parents:
        if mutation_probability > r.random():
            perform_mutation(j)

    kids = []
    k_length = len(population) - len(parents)

    while len(kids) < k_length :
        m = population[r.randint(0, len(parents)-1)]
        f = population[r.randint(0, len(parents)-1)]        
        m_midpoint = len(m)//2
        kid = m[:m_midpoint]+ f[m_midpoint:]
        if mutation_probability > r.random():
            perform_mutation(kid)
        kids.append(kid)

    parents.extend(kids)
    return parents

def main():
    """Ties all the functions and logic together into one neat and organized function."""
    init_gen = 1
    pop = generate_ancestors(POP_SIZE)
    with open ("output.csv", "w+", newline='') as output: 
        #This code will write the results to a file called output.csv stored on your local computer. From here you can graph the data using Microsoft Excel.
        writer = csv.writer(output)
        lines = []
        for g in range(0, MAXIMUM_GENERATION):
            print(f"Generation {init_gen} with {len(pop)}")
            pop = sorted(pop, key=lambda x: fitness(x), reverse=True)
            total = 0
            for i in pop:        
                print(f"{str(i)}, fit: {fitness(i)}") 
                total += fitness(i)
            avg = total / len(pop)
            lines.append([init_gen, avg])
            pop = evolution(pop)
            init_gen += 1
        print(lines)
        writer.writerows(lines)

if __name__ == "__main__":
    """Runs the script."""
    main()
