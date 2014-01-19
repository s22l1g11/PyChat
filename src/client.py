import pyNotificationCenter
import socket

class Client:

	# writing our attributes
	host = ""
	port = ""
	nick = ""
	sock = ""

	# writing the constructor
	def __init__(self):
		# asking for host ip
		Client.host=raw_input("Please enter server hostname:  ") 
		if	Client.host == '': host="127.0.0.1" # if host is empty use localhost as standard
		Client.port=4446 # port is similar in the whole system
		# setting our socket var
		Client.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		Client.sock.connect((Client.host, Client.port))
		Client.nick = input("Please choose a username: ")
		Client.sock.send(Client.nick)
		welcome=Client.sock.recv(1024) # receive welcome msg with data upto 1024 bytes
		print("Message from server: "+welcome)
		self.serverNotification(welcome)

	def connect(self):
		sock = socket(AF_INET, SOCK_STREAM)
		return sock.connect((Client.host, Client.port))

	def serverNotification(self, message):
		pyNotificationCenter.notify("PyChat", "Server says:", message, sound=True)

	def sendMessage(self):
		message = input()
		Client.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		Client.sock.connect((Client.host, Client.port))
		Client.sock.send(message)
		reply=Client.sock.recv(1024)
		print("Reply: "+reply)

	def closeSocket(self):
		print("System shutdown...")
		Client.sock.close()

	def __del__(self):
		self.closeSocket()

import client
client = Client()
while 1:
	client.sendMessage()