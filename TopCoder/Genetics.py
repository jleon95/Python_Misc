class Genetics:

	def __init__(self):

		pass

	def getOffspring(self, g1, g2, dom):

		offspring = ""

		for index in xrange(len(g1)):

			if g1[index] == g2[index]:

				offspring += g1[index]

			elif g1[index].isupper():

				if dom[index] == 'D':

					offspring += g1[index]

				else:

					offspring += g2[index]

			else:

				if dom[index] == 'D':

					offspring += g2[index]

				else:

					offspring += g1[index]

		return offspring

if __name__ == "__main__":

	genetics = Genetics()

	print genetics.getOffspring("MGskgzTFQoclnDjZu","mgSKGzTFQoClnDJzU","DDDDDRDDDDRDDDDDD")