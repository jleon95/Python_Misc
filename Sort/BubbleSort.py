import time
import random
from sys import argv

def bubble_sort(elements):

	end = len(elements)

	if end:

		for i in xrange(0, len(elements)):

			for j in range(1, end):

				if elements[j-1] > elements[j]:

					elements[j-1], elements[j] = elements[j], elements[j-1]

			end -= 1

###############################################################################

if __name__ == "__main__":

	seed = int(argv[1])
	random.seed(seed)

	list = random.sample(xrange(0, 5000), 5000)

	#print "We have an unordered list of elements: \n%r" % list

	before = time.clock()
	bubble_sort(list)
	after = time.clock()

	print "The list has been sorted in %f" % (after-before)