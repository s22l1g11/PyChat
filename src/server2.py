import select 
import socket 
import sys 
import re
import time

host = '127.0.0.1' 
port = 4446 
backlog = 5 
size = 1024 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind((host,port)) 
print("Listening for connections...")
server.listen(backlog) 
input = [server,] 
connections = []
running = 1 
while running: 
  inputready,outputready,exceptready = select.select(input,[],[]) 

  for s in inputready: 

    if s == server: 
      # handle the server socket 
      client, address = server.accept() 
      input.append(client) 
      print 'new client added%s'%str(address)
      connections.append(client.getsockname())
      print "Your connections: ",connections

    else:
      # handle all other sockets 
      data = s.recv(size) 
      if data:
        print '%s received from %s'%(data,s.getsockname())
#        s.send(data) 
        
        message = data

        if '/name ' in message:
          message = message.replace("/name ","",1)
          print message + " entered the room."
          data = "Hello "+message
          s.send(data)
        elif '/say ' in message:
          sender = re.findall('\[(.*?)\]', message)
          message = message.replace("/say ","",1)
          #message = message.replace(sender,"",1)
          data = message
          for user in connections:
            s.sendto(data, user)
        elif '!!shutdown!!' in message:
          time.sleep(2)
          s.close()
          exit(0)
        elif '/rename' in message:
          data = "renaming accepted!"
          s.send(data)
        elif '/help' in message:
          print("hello!")
          data = "You can use the following commands:\n/say [message] - to say something\n/rename [new username] - to change your username\n/help - to display this menue"
          s.send(data)

        #s.send(data)
      else: 
        s.close() 
        input.remove(s) 
server.close()