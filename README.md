# Tp1_Reseau

Tadja Mehdi

##1)Client/Serveur UDP en Python

###UDPclient:
```python
from socket import *
serverName = ‘localhost’ 
serverPort = 12000 
clientSocket = socket(socket.AF_INET, socket.SOCK_DGRAM)  
message = raw_input(’Input lowercase sentence:’) 
clientSocket.sendto(message,(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)                  
print modifiedMessage
clientSocket.close()
```
###UDPserver:
```python
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((’localhost’, serverPort))
print ”The server is ready to receive”
while 1:
     	message, clientAddress = serverSocket.recvfrom(2048)
     	modifiedMessage = message.upper()
          print modifiedMessage
    	serverSocket.sendto(modifiedMessage, clientAddress)
```    
##2)Client/Server UPD en Netcat
###UDPclient:
pour créé un client netcat on tape: nc -u localhost 12000   
le -u sert à dire qu'on travail en UDP
localhost est l'ip sur lequel on veut envoyer le msg
12000 est le port sur lequel le server se trouve et avec lequel on veut communiquer
on écrit ensuite le message que l'on veut envoyer

###UDPserver:
pour créer un server netcat on tape: nc -l -u 12000
le -l sert à dire au server d'écouter 
le -u sert à dire qu'on travail en UDP
12000 est le port sur lequel le serveur va travailler et communiquer avec le client

##3)Client/Server TCP en python:
###TCPclient.py:
'''python
from socket import *
serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = raw_input('Input lowercase sentence:')
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
print 'From Server:', modifiedSentence
clientSocket.close()    
'''

###TCPserver.py:
'''python
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print 'The server is ready to receive'
while 1:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024)
	capitalizedSentence = sentence.upper()
	connectionSocket.send(capitalizedSentence)
	print capitalizedSentence	
	connectionSocket.close()
'''

