import pyNotificationCenter
import socket

host = input("Enter hostname: ")
if	host == '': host="127.0.0.1"
port = 4446

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((host, port))

running = 1
nick = ""

while running:
	# handling different cases
	# checking for username
	if nick == '':
		nick = input("Enter nickname: ")
		server.send("/name "+nick)
		reply = server.recv(1024)
		print("Server says: "+reply)

	# enable message writing
	elif nick != '': 
		'''if not server.recv(1024):
			print("I'm stucked")
			True
		else:
			print(reply)'''
		message = input()

		if "#rename" in message:
			nick = message.replace("#rename ","",1)
			print("Your new username is: "+nick)

		elif "#exit" in message:
			server.close()
			print("System stops...")
			exit(0)
		elif "#shutdown" in message:
			server.send("!!shutdown!!")
			server.close()
			print("System stops...")
			exit(0)

		else:
			server.send("/say "+nick+" wrote: "+message)
			reply = server.recv(1024)
			print(reply)