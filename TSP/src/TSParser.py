from math import sqrt

def euclidean_distance(orig, dest):

	return sqrt((orig[0] - dest[0])**2 + (orig[1] - dest[1])**2)

def read_file(name):

	with open(name) as file:

		points = []

		content = file.readlines()
		content.pop(0)

		for line in content:

			points.append((float(line.split()[1]), float(line.split()[2])))

	return points

def create_adjacency_matrix(points):

	size = len(points)

	matrix = [[0 for row in xrange(size)] for col in xrange(size)]

	for row in xrange(size):

		for col in xrange(size):

			matrix[row][col] = euclidean_distance(points[row], points[col])
	
	return matrix