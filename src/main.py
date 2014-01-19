class PyChat:

	def __init__(self):
		which = raw_input("Please choose:\n1 - Server\n2 - Client\n3 - Help\n4 - Exit\n")
		if int(which) == 1:
			import server
		elif int(which) == 2:
			import client
		elif int(which) == 3:
			print("umm...")
		elif int(which) == 4:
			print("System stops...")
			exit(0)

chat = PyChat()