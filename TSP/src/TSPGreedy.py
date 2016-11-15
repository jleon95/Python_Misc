import TSParser
import time
from sys import argv

def greedy_algorithm(matrix):

	size = len(matrix)
	best_cost = float('inf')
	best_path = []

	for i in range(size):

		visited = [False for x in range(size)]
		current_city = i
		visited[current_city] = True
		current_path = [current_city]
		current_cost = 0.0

		for j in range(size-1):

			best_distance = float('inf')

			for k in range(size):

				if not visited[k] and 0 < matrix[current_city][k] < best_distance:

					best_neighbor = k
					best_distance = matrix[current_city][k]

			visited[best_neighbor] = True
			current_path.append(best_neighbor)
			current_cost += best_distance
			current_city = best_neighbor

		current_cost += matrix[current_path[-1]][current_path[0]]
		current_path.append(current_path[0])

		if current_cost < best_cost:

			best_cost = current_cost
			best_path = list(current_path)

	return best_path, best_cost

###############################################################################

if __name__ == "__main__":

	filename = argv[1]

	matrix = TSParser.create_adjacency_matrix(TSParser.read_file(filename))

	before = time.clock()
	path, cost = greedy_algorithm(matrix)
	after = time.clock()

	print "Path: \n%s" % " ".join(str(n) for n in path)
	print "Total cost: %f" % cost
	print "Runtime: %f" % (after-before)