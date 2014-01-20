import pyNotificationCenter
import socket

class Client:

	# writing our attributes
	host = ""
	port = ""
	nick = ""

	# writing the constructor
	def __init__(self):
		# asking for host ip
		Client.host=raw_input("Please enter server hostname:  ") 
		if	Client.host == '': host="127.0.0.1" # if host is empty use localhost as standard
		Client.port=4446 # port is similar in the whole system
		# setting our socket var
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((Client.host, Client.port))
		Client.nick = input("Please choose a username: ")
		sock.send("/name " + Client.nick)
		welcome=sock.recv(1024) # receive welcome msg with data upto 1024 bytes
		print("Message from server: "+welcome)
		self.serverNotification(welcome)

	def connect(self):
		sock = socket(AF_INET, SOCK_STREAM)
		return sock.connect((Client.host, Client.port))

	def serverNotification(self, message):
		pyNotificationCenter.notify("PyChat", "Server says:", message, sound=True)

	def sendMessage(self):
		# getting input from the user and determing which command was used...
		message = input()
		if '/say' in message: # send a message if the user used /send
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect((Client.host, Client.port))
			sock.send(Client.nick+" wrote: "+message)

		if '/shutdown' in message: # remote shutdown of server and client
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect((Client.host, Client.port))
			sock.send('/shutdown')
			reply=sock.recv(1024)
			print(reply)
			self.shutDown()

		if '/rename ' in message: # enable renaming
			oldNick = Client.nick
			Client.nick = message.replace("/rename ","",1)
			print "Your new username is: "+Client.nick
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect((Client.host, Client.port))
			sock.send("/rename")

		if '/exit' in message: # quitting the program by using /exit
			self.closeSocket()

		if '/help ' in message:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect((Client.host, Client.port))
			sock.send("/help")

		reply=sock.recv(1024)
		print(reply)

	def closeSocket(self):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((Client.host, Client.port))
		print("System shutdown...")
		sock.close()
		exit(0)

	def shutDown(self):
		print("System shutdown...")
		exit(0)

	def __del__(self):
		self.closeSocket()

import client
client = Client()
while 1:
	client.sendMessage()