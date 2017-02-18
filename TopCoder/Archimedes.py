import math

class Archimedes:

	def __init__(self):

		pass

	def approximatePi(self, numSides):

		side = 2 * math.sin(math.radians(180.0/numSides)) # Using Pi to estimate Pi...
		perimeter = side * numSides

		return perimeter/2.0

if __name__ == "__main__":

	archimedes = Archimedes()

	print archimedes.approximatePi(17280)
