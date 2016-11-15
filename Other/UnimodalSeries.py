import random
import time
from random import randint
from sys import argv

def unimodal_series(list, start, end):

	if not list:

		return None

	elif len(list) < 2:

		return start

	else:

		middle = (start+end)//2

		if list[middle-1] < list[middle] > list[middle+1]:

			return middle

		elif list[middle-1] < list[middle] < list[middle+1]:

			return unimodal_series(list, middle, end)

		else:

			return unimodal_series(list, start, middle)

###############################################################################

if __name__ == "__main__":

	size = int(argv[1])
	seed = int(argv[2])
	random.seed(seed)

	midpoint = randint(1,size-1)

	left_half = random.sample(xrange(size*2), midpoint)
	left_half.sort()
	right_half = random.sample(xrange(left_half[-1]), size - midpoint)
	right_half.sort()
	right_half = right_half[::-1]
	left_half.extend(right_half)
	 
	before = time.clock()
	p = unimodal_series(left_half, 0, len(left_half))
	after = time.clock()

	print "The unimodal series is: \n%r" %left_half
	print "The top of this unimodal series is %d, in the position number %d" % (left_half[p], p+1)