from sys import argv

def binary_search(elements, number):

	if not elements:

		return False

	else:

		middle = len(elements)//2

		if number == elements[middle]:

			return True

		elif number < elements[middle]:

			return binary_search(elements[:middle], number)

		else:

			return binary_search(elements[middle+1:], number)

###############################################################################

if __name__ == "__main__":

	find = argv[1]

	elements = [i for i in range(0,10)]

	print "You want to find an element in this list: \n%r" % elements

	if binary_search(elements, int(find)):

		print "%s was found." % find

	else:

		print "%s was not found." % find  