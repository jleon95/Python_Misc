class Whisper:

	def __init__(self):

		pass

	def toWhom(self,usernames,typed):

		if not typed.startswith("/msg "):

			return "not a whisper"

		typed = typed[5:]
		current_user = ""

		for user in usernames:

			if len(user) > len(current_user) and (user + " ").lower() in typed[:len(user)+1].lower():

				current_user = user

		if not current_user:

			return "user is not logged in"

		return current_user

if __name__ == "__main__":

	whisper = Whisper()

	print whisper.toWhom(("abc",)," /msg abc note the leading space")