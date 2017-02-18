import string

class Billboard:

	def __init__(self):

		pass

	def enlarge(self,message,letters):

		dict = {}
		answer = []

		for encoding in letters:

			letter = encoding[0]
			rep = string.split(encoding[2:],"-")
			dict[letter] = rep

		for row in xrange(5):

			row_content = ""

			for letter in message:

				row_content += dict[letter][row] + "."

			answer.append(row_content[:-1])

		return (tuple(answer))


if __name__ == "__main__":

	billboard = Billboard()

	print billboard.enlarge("TOPCODER",("T:#####-..#..-..#..-..#..-..#.." ,
		"O:#####-#...#-#...#-#...#-#####" ,"P:####.-#...#-####.-#....-#...." ,
		"C:.####-#....-#....-#....-.####" ,"D:####.-#...#-#...#-#...#-####." ,
		"E:#####-#....-####.-#....-#####" ,"R:####.-#...#-####.-#.#..-#..##"))