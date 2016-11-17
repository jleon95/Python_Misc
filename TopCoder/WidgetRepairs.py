class WidgetRepairs:

	def __init__(self):

		pass

	def days(self,arrivals,numPerDay):

		unrepaired = current_day = days = 0

		while current_day < len(arrivals) or unrepaired > 0:

			if current_day < len(arrivals):
			
				unrepaired += arrivals[current_day]
				current_day += 1

			if unrepaired:

				unrepaired = max(0, unrepaired-numPerDay)
				days += 1

		return days

if __name__ == "__main__":

	wr = WidgetRepairs()

	print wr.days((6, 5, 4, 3, 2, 1, 0, 0, 1, 2, 3, 4, 5, 6),3)
			