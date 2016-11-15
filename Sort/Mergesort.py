import time
import random
from sys import argv

def mergesort(elements):

	if len(elements) < 2:

		return elements

	else:

		middle = len(elements)//2

		left_half = mergesort(elements[:middle])
		right_half = mergesort(elements[middle:])

		if(left_half[-1] <= right_half[0]):

			left_half.extend(right_half)
			return left_half

		elements = merge(left_half, right_half)

		return elements

def merge(left_half, right_half):

	result = []

	while left_half and right_half:

		if(left_half[0] <= right_half[0]):

			result.append(left_half[0])
			left_half.pop(0)

		else:

			result.append(right_half[0])
			right_half.pop(0)


	if left_half:

		result.extend(left_half)

	else:

		result.extend(right_half)

	return result

###############################################################################

if __name__ == "__main__":

	seed = int(argv[1])
	random.seed(seed)
	
	list = random.sample(xrange(0, 1000), 1000)

	#print "We have an unordered list of elements: \n%r" % list

	before = time.clock()
	ordered = mergesort(list)
	after = time.clock()

	print "The list has been sorted in %f" % (after-before)