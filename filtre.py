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
	print capitalizedSentence	
	connectionSocket.close()

	connectionSocket, addr = serverSocket.accept()
	connectionSocket.send(capitalizedSentence)
	
	connectionSocket.close()

	serverName = "localhost"
  	serverPort = 13000
	clientSocket.connect((serverName,serverPort))
	clientSocket.send(capitalizedSentence)
	clientSocket.close()  