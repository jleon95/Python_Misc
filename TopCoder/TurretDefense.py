class TurretDefense:

	def __init__(self):

		pass

	def firstMiss(self,xs,ys,times):

		curr_xs = curr_ys = curr_time = counter = 0

		for seconds in times:

			distance = abs(curr_xs-xs[counter]) + abs(curr_ys-ys[counter])

			if distance > (seconds-curr_time):

				return counter

			curr_xs = xs[counter]
			curr_ys = ys[counter]
			curr_time = times[counter]
			counter = counter + 1

		return -1

if __name__ == "__main__":

	turret = TurretDefense()

	print turret.firstMiss((1,2,3,4,15),(1,2,3,4,15),(100,200,300,400,405))