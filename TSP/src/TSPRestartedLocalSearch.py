import TSParser
import TSPLocalSearch
import time
import random
from random import shuffle
from sys import argv

def restarted_local_search(matrix, path, max_evaluations, max_restarts):

	best_path = []
	best_cost = TSPLocalSearch.calculate_cost(matrix, path)

	for i in xrange(1,max_restarts):

		current_cost = TSPLocalSearch.local_search(matrix, path, max_evaluations)

		if current_cost < best_cost:

			best_cost = current_cost
			best_path = list(path)

		shuffle(path)

	path = best_path

	return best_cost

###############################################################################			

if __name__ == "__main__":

	filename = argv[1]
	seed = int(argv[2])
	max_evaluations = int(argv[3])
	max_restarts = int(argv[4])
	random.seed(seed)

	matrix = TSParser.create_adjacency_matrix(TSParser.read_file(filename))

	path = [x for x in xrange(len(matrix))]
	shuffle(path)

	before = time.clock()
	cost = restarted_local_search(matrix, path, max_evaluations, max_restarts)
	after = time.clock()

	print "Path: \n%s" % " ".join(str(n) for n in path)
	print "Total cost: %f" % cost
	print "Runtime: %f" % (after-before)