class Iditarod:

	def __init__(self):

		pass

	def avgMinutes(self,times):

		times_converted = []

		for time in times:

			hours = (int(time[0])*10+int(time[1]))%12
			m = time[6]
			minutes = int(time[3])*10+int(time[4])

			if len(time) == 15:

				day = int(time[-1])

			else:

				day = int(time[-2])*10 + int(time[-1])

			total_minutes = minutes + 1440*(day-1)

			if hours < 8:

				total_minutes -= 8*60 - hours*60

			else:

				total_minutes += (hours-8)*60

			if m == 'P':

				total_minutes += 12*60

			times_converted.append(total_minutes)

		return int(round(sum(times_converted) / float(len(times))))

if __name__ == "__main__":

	idit = Iditarod()

	print idit.avgMinutes(("02:00 PM, DAY 19","02:00 PM, DAY 20", "01:58 PM, DAY 20"))