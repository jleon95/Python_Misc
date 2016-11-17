class Lexer:

	def __init__(self):

		pass

	def tokenize(self,tokens,input):

		consumed = []

		while input:

			previous = ""

			for token in tokens:

				if len(token) > len(previous) and token in input[:len(token)]:

					previous = token

			if previous:

				consumed.append(previous)
				input = input[len(previous):]

			else:

				input = input[1:]

		return tuple(consumed)

if __name__ == "__main__":

	lexer = Lexer()

	print lexer.tokenize(("AbCd","dEfG","GhIj"),"abCdEfGhIjAbCdEfGhIj")