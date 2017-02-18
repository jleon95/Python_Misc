class HuffmanDecoding:

	def __init__(self):

		self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	def decode(self,archive,dictionary):

		decoded = ""

		while archive:

			for index,entry in enumerate(dictionary):

				if archive.startswith(entry):

					decoded += self.letters[index]
					archive = archive[len(entry):]
					break

		return decoded

if __name__ == "__main__":

	hm = HuffmanDecoding()

	print hm.decode("001101100101100110111101011001011001010",("110","011","10","0011","00011","111","00010","0010","010","0000"))