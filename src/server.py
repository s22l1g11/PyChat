# TCP Server Code
 
host="127.0.0.1"                # Set the server address to variable host
port=4446                   # Sets the variable port to 4444
from socket import *                # Imports socket module
import re
 
s=socket(AF_INET, SOCK_STREAM)
#s.close() was for debugging
s.bind((host,port))                 # Binds the socket. Note that the input to 
                                            # the bind function is a tuple

print "Start listening for connections..."                   
while True:

	s.listen(1)                         # Sets socket to listening state with a  queue
	                                            # of 1 connection
	 
	q,addr=s.accept()               # Accepts incoming request from client and returns
	                                            # socket and address to variables q and addr
	message = q.recv(1024)

	if '/name ' in message:
		message = message.replace("/name ","",1)
		print message + " entered the room."
		data = "Hello "+message
	elif '/say ' in message:
		sender = re.findall('\[(.*?)\]', message)
		message = message.replace("/say ","",1)
		#message = message.replace(sender,"",1)
		data = message
	elif '/shutdown' in message:
		data = "Stopping the server..."
		q.send(data)
		s.close()
		break
	elif '/rename' in message:
		data = "reanming accepted!"
	elif '/help ' in message:
		print("hello!")
		data = "You can use the following commands:\n/say [message] - to say something\n/rename [new username] - to change your username\n/help - to display this menue"

	q.send(data)                        # Sends data to client
	


print "Stopping the server..."
s.close()
 
# End of code
