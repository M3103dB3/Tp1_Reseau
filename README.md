# Tp1_Reseau

Tadja Mehdi

##1)Client/Serveur UDP en Python

###UDPclient:
```python
from socket import *
serverName = ‘hostname’ 
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
serverSocket.bind((’’, serverPort))
print ”The server is ready to receive”
while 1:
     	message, clientAddress = serverSocket.recvfrom(2048)
     	modifiedMessage = message.upper()
          print modifiedMessage
    	serverSocket.sendto(modifiedMessage, clientAddress)
```    
