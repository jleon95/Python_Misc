class Substitute:

	def __init__(self):

		pass

	def getValue(self,key,code):

		value = ""

		for letter in code:

			number = key.find(letter)

			if number > -1:

				value = value + str((number+1)%10)

		return int(value)

if __name__ == "__main__":

	sub = Substitute()

	print sub.getValue("CRYSTALBUM","MMA")