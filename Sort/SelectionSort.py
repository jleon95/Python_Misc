import time
import random
from sys import argv

def selection_sort(elements):

	for i in xrange(0, len(elements)):

		smallest = i

		for j in xrange(i+1, len(elements)):

			if elements[j] < elements[smallest]:

				smallest = j

		elements[smallest], elements[i] = elements[i], elements[smallest]

###############################################################################

if __name__ == "__main__":

	seed = int(argv[1])
	random.seed(seed)

	list = random.sample(xrange(0, 1000), 1000)

	#print "We have an unordered list of elements: \n%r" % list

	before = time.clock()
	selection_sort(list)
	after = time.clock()

	print "The list has been sorted in %f" % (after-before)