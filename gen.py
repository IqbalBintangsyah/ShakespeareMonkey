import numpy
import string
import random

def cal_pop_fitness(target, pop):
    #to count fitness for each individual
    fitness = []
    for each in pop:
        count = 0
        char = 0
        for c in each:
            if c == target[char]:
                count+=1
            char+=1
        fitness.append(count)
    return fitness

def fitness_persentage(fitness, gene):
    #overall population fitness in percent
    sum = 0
    for fit_point in fitness:
        sum += fit_point
    persentage = (sum/(gene*len(fitness)))*100
    return persentage

def select_mating_pool(pop, fitness, gene):
    # Selecting the parent with rejection sampling
    parents = []
    parents_num = len(pop)//2
    acceptance_chance = max(fitness)
    for p in range (parents_num):
        accept1 = False
        while not accept1:
            #Generating random numbers to select parent candidate
            parent1_index = int(numpy.random.uniform(0, len(pop)))
            #Reject or accept
            chance = int(numpy.random.uniform(1,acceptance_chance))
            #print(str(chance) + " x " + str(fitness[parent1_index]))
            if chance<=fitness[parent1_index]:
                accept1 = True
                #print("____________________________")
        accept2 = False
        while not accept2:
            #Generating random numbers to select parent candidate
            parent2_index = int(numpy.random.uniform(0, len(pop)))
            #Make sure parent2 != parent1
            while parent2_index==parent1_index:
                parent2_index = int(numpy.random.uniform(0, len(pop)))
            #Reject or accept
            chance = int(numpy.random.uniform(1,acceptance_chance))
            if chance<=fitness[parent1_index]:
                accept2 = True
        parents_couple = (pop[parent1_index], pop[parent2_index])
        parents.append(parents_couple)
    return parents

def crossover(parents, offspring_size, gene):
    offspring = []
    #The point at which crossover takes place between two parents. Usually, it is at the center.
    crossover_point = int(numpy.random.uniform(0, gene, 1))

    for k in range(offspring_size//2):
        #Each pai of parents will produce 2 offsprings
        offspring_parent = parents[k]
        #The first offspring will have its first half of its genes taken from the first parent.          
        first_half_gene = offspring_parent[0][:crossover_point]
        offspring.append(first_half_gene)
        #and will have its second half of its genes taken from the second parent.
        last_half_gene = offspring_parent[1][crossover_point:]
        offspring[2*k] = offspring[2*k] + ''.join(last_half_gene)
        #The other offspring will have the first half from the second parent
        first_half_gene = offspring_parent[1][:crossover_point]
        offspring.append(first_half_gene)
        #and the second half from the first parent
        last_half_gene = offspring_parent[0][crossover_point:]
        offspring[(2*k)+1] = offspring[(2*k)+1] + ''.join(last_half_gene)
    return offspring

def mutation(offspring_crossover, gene):

    # Mutation changes a single gene in each offspring randomly.

    for idx in offspring_crossover:
        letter = random.choice(string.ascii_letters)
        #To determine which gene get mutation
        random_value = int(numpy.random.uniform(0, gene, 1))
        #To determine wether mutation occurs or not
        chances = random.randint(1, 2)
        if chances==1:
            idx = idx[:random_value] + letter + idx[random_value+1:]
    return offspring_crossover
