class Hawaiian:

	def __init__(self):

		self.letters = ['a','e','i','o','u','h','k','l','m','n','p','w']

	def getWords(self,sentence):

		words = sentence.split()
		hawaiian_words = []

		for word in words:

			for letter in word:

				if letter.lower() not in self.letters:

					break

			else:

				hawaiian_words.append(word)

		return tuple(hawaiian_words)

if __name__ == "__main__":

	hawaii = Hawaiian()

	print hawaii.getWords("Pineapple grows in Hawaii")