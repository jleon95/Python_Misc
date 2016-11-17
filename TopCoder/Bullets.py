class Bullets:

	def __init__(self):

		pass

	def match(self,guns,bullet):

		number = -1

		for gun in guns:

			for start in xrange(len(gun)):

				for scratch in xrange(start,len(gun)+start):

					if gun[scratch%len(gun)] != bullet[scratch-start]:

						break

				else:

					number = guns.index(gun)

		return number

if __name__ == "__main__":

	bullets = Bullets()

	print bullets.match(("|| || ||","| | | | ","||| ||| ","||||||||"),"|| ||| |")
