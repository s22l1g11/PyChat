# TCP Client Code
host=raw_input("Please enter server hostname:  ") 
if host == '': host="127.0.0.1"
#host="127.0.0.1"            # Set the server address to variable host
 
port=4446               # Sets the variable port to 4444
 
from socket import *             # Imports socket module
 
s=socket(AF_INET, SOCK_STREAM)      # Creates a socket
 
s.connect((host,port))          # Connect to server address

nick=raw_input("Please choose a username: ")	# choosing a nickname for the server
s.send(nick)	# sending the nickname

msg=s.recv(1024)            # Receives data upto 1024 bytes and stores in variables msg
 
print "Message from server : " + msg

while True:
	s.send(input())
 
s.close()                            # Closes the socket 
# End of code