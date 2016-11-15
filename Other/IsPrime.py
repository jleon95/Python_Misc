from math import sqrt
from sys import argv

def IsPrime(number):

	top_value = int(sqrt(number)) + 1

	for i in xrange(2, top_value):

		if not number % i:

			return False

	return True

###############################################################################

if __name__ == "__main__":

	number = argv[1]

	if IsPrime(int(number)):

		print "%s is a prime number." % number

	else:

		print "%s is not a prime number." % number