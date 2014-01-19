# TCP Server Code
 
host="127.0.0.1"                # Set the server address to variable host
port=4446                   # Sets the variable port to 4444
from socket import *                # Imports socket module
 
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
	nick = q.recv(1024)
	print nick + " entered the room."
	data = "Hello "+nick
	 
	q.send(data)                        # Sends data to client
	


print "Stopping the server..."
s.close()
 
# End of code
