import numpy
import gen
import string
import random

def string_generate(lenght):
	strings = ''.join(random.choices(string.ascii_letters + ' ', k=lenght))
	return strings

target = "Kimi no Na Wa"
pop_num = 200
gene = len(target)
new_pop = []
for pop in range (pop_num):
	new_pop.append(string_generate(gene))
b = False
generation = 0
while generation<50:
	print(f"Generation : ", generation)
	print(new_pop)
	fitness = gen.cal_pop_fitness(target, new_pop)
	print(fitness)
	parents = gen.select_mating_pool(new_pop, fitness, gene)
	offspring = gen.crossover(parents, pop_num, gene)
	mutation = gen.mutation(offspring, gene)
	new_pop = mutation
	if max(fitness)==gene:
		b = True
	print(max(fitness))
	fitness_percent = gen.fitness_persentage(fitness, gene)
	print("%s %%"% fitness_percent)
	generation +=1