import time
import random
from sys import argv

def insertion_sort(elements):

	if elements:

		for i in xrange(1, len(elements)):

			current = i

			j = i - 1

			while j >= 0 and elements[j] > elements[current]:

				j -= 1

			value = elements[current]
			elements.remove(value)
			elements.insert(j+1,value)

###############################################################################

if __name__ == "__main__":

	seed = int(argv[1])
	random.seed(seed)

	list = random.sample(xrange(0, 1000), 1000)

	#print "We have an unordered list of elements: \n%r" % list

	before = time.clock()
	insertion_sort(list)
	after = time.clock()

	print "The list has been sorted in %f" % (after-before)