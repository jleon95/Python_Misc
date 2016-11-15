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

def local_search(matrix, current_path, max_eval):

	size = len(matrix)
	current_cost = calculate_cost(matrix, current_path)

	improvement = True
	evals = 1

	while evals < max_eval and improvement:

		for i in xrange(size):

			improvement = False

			for j in xrange(size):

				current_path[i], current_path[j] = current_path[j], current_path[i]
				neighbor_cost = calculate_cost(matrix, current_path)
				evals += 1

				if neighbor_cost < current_cost:

					current_cost = neighbor_cost
					improvement = True

				else:

					current_path[i], current_path[j] = current_path[j], current_path[i]

	return current_cost

###############################################################################			

if __name__ == "__main__":

	filename = argv[1]
	seed = int(argv[2])
	max_evaluations = int(argv[3])
	random.seed(seed)

	matrix = TSParser.create_adjacency_matrix(TSParser.read_file(filename))

	path = [x for x in xrange(len(matrix))]
	shuffle(path)

	before = time.clock()
	cost = local_search(matrix, path, max_evaluations)
	after = time.clock()

	print "Path: \n%s" % " ".join(str(n) for n in path)
	print "Total cost: %f" % cost
	print "Runtime: %f" % (after-before)