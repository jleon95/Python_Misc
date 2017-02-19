import TSParser
import time
import random
from random import shuffle
from sys import argv

def calculate_cost(matrix, path):

	size = len(matrix)
	cost = 0.0

	for i in xrange(size):

		cost += matrix[path[i-1]][path[i]]

	return cost

def selection_operator(population): # Binary tournament selection

	not_selected = list(population)
	parents_population = []

	while len(not_selected) > 1:

		candidates = random.sample(range(len(not_selected)),2) # Selecting 2 candidates

		if not_selected[candidates[0]][0] < not_selected[candidates[1]][0]: # If candidate1 is better than candidate2

			parents_population.append(not_selected[candidates[0]][1])
			not_selected.pop(candidates[0])

		else:

			parents_population.append(not_selected[candidates[1]][1])
			not_selected.pop(candidates[1])

	parents_population.append(not_selected[0][1])

	return parents_population
	

def order_crossover_operator(parent1, parent2, size): # Two children from two parents

	start = random.randint(0, len(parent1)-size)

	chunk1 = parent1[start:start+size]
	chunk2 = parent2[start:start+size]
	not_chunk1 = [x for x in parent2 if x not in chunk1]
	not_chunk2 = [x for x in parent1 if x not in chunk2]
	offspring1 = []
	offspring1.extend(not_chunk1[0:start])
	offspring1.extend(chunk1)
	offspring1.extend(not_chunk1[start:])
	offspring2 = []
	offspring2.extend(not_chunk2[0:start])
	offspring2.extend(chunk2)
	offspring2.extend(not_chunk2[start:])
	
	return [offspring1, offspring2]

def swap_mutation_operator(permutation): # Swap two positions of the permutation.

	positions = random.sample(range(len(permutation)), 2)
	permutation[positions[0]], permutation[positions[1]] = permutation[positions[1]], permutation[positions[0]]

def evaluation(new_population, elitism_needed, gen_best, gen_worst):

	old_population = []

	for solution in new_population: # Evaluation of new generation

		old_population.append([calculate_cost(matrix,solution),list(solution)])

		if old_population[-1][0] < gen_best[0]: # Looking for the best of this generation

			gen_best = [old_population[-1][0], len(old_population)-1]

		if elitism_needed and old_population[-1][0] > gen_worst[0]: # Looking for the worst of this generation

			gen_worst = [old_population[-1][0], len(old_population)-1]

	return old_population, gen_best, gen_worst

def genetic_algorithm(matrix, generations, population_size):

	crossovers = int(0.7 * population_size / 2) # Proportion of crossovers in a population
	mutations = int(0.005 * population_size * len(matrix)) # Proportion of mutations in a population
	current_solution = [x for x in range(len(matrix))]
	best_solution = [calculate_cost(matrix, current_solution), list(current_solution)] # Pair (cost, solution)
	generation_best_solution = [calculate_cost(matrix, current_solution), list(current_solution)] # Same as above, used for elitism
	old_population = [list(best_solution)]

	for x in range(population_size-1): # Initializing the population

		shuffle(current_solution)
		cost = calculate_cost(matrix,current_solution)
		old_population.append([cost,list(current_solution)])

		if cost < best_solution[0]: # Updating best solution so far

			best_solution[0], best_solution[1] = cost, list(current_solution)
			generation_best_solution[0], generation_best_solution[1] = cost, list(current_solution)
		
	for generation in xrange(generations): # Main loop

		parents_population = selection_operator(old_population) # Selection
		new_population = []

		for c in range(crossovers): # Crossover (two children for each pair of parents)

			new_population.extend(order_crossover_operator(parents_population[c*2], parents_population[c*2+1],3))

		new_population.extend(parents_population[crossovers*2:]) ## Add the remaining ones from last generation

		for m in range(mutations): # Mutation 

			swap_mutation_operator(random.sample(new_population,1)[0])

		best_has_survived = generation_best_solution[1] in new_population # See if elitism is needed (not exhaustive)

		new_gen_best = [float("inf"),-1] # Cost of the best of the generation and where it is located
		new_gen_worst = [0.0,-1] # Cost of the worst and where it is located

		old_population, new_gen_best, new_gen_worst = evaluation(new_population, not best_has_survived, new_gen_best, new_gen_worst) # Evaluation

		if new_gen_best[0] < best_solution[0]: # Looking for the best overall

			best_solution = [new_gen_best[0], old_population[new_gen_best[1]][1]]

		if not best_has_survived: # Elitism

			old_population[new_gen_worst[1]] = list(generation_best_solution)

		if new_gen_best[0] < generation_best_solution[0]: # Maybe the best of last generation is still better than the current one's

			generation_best_solution = [new_gen_best[0], old_population[new_gen_best[1]][1]]

	return best_solution[1], best_solution[0]

###############################################################################

if __name__ == "__main__":

	filename = argv[1]
	seed = int(argv[2])
	generations = int(argv[3])
	population_size = int(argv[4])
	random.seed(seed)

	matrix = TSParser.create_adjacency_matrix(TSParser.read_file(filename))

	before = time.clock()
	path, cost = genetic_algorithm(matrix, generations, population_size)
	after = time.clock()

	print "Path: \n%s" % " ".join(str(n) for n in path)
	print "Total cost: %f" % cost
	print "Runtime: %f" % (after-before)