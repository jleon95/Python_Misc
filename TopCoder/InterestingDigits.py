class InterestingDigits:

	def __init__(self):

		pass

	def digits(self,base):

		interesting_digits = []

		for digit in xrange(2,base):

			multiple = digit*2
			interesting = True

			while len(convert_to_base(multiple,base)) < 3 and interesting:

				digit_sum = sum(number for number in convert_to_base(multiple,base))

				if digit_sum % digit:

					interesting = False

				multiple += digit

			if interesting:

				interesting_digits.append(digit)

		return tuple(interesting_digits)

def convert_to_base(number,base):

	digits = []

	while number:

		digits.append(number % base)
		number //= base

	return digits[::-1]

if __name__ == "__main__":

	int_d = InterestingDigits()

	print int_d.digits(26)