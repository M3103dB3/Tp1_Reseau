from socket import *
serverName ="localhost"
serverPort1= 12000
serverPort2 = 13000

serverSocket1 = socket(AF_INET,SOCK_STREAM)
serverSocket1.bind(('',serverPort1))
serverSocket1.listen(1)

serverSocket2 = socket(AF_INET,SOCK_STREAM)
serverSocket2.bind(('',serverPort2))
serverSocket2.listen(1)
print 'The server is ready to receive'

while 1:
	connectionSocket, addr = serverSocket1.accept()
	sentence = connectionSocket.recv(1024)
	modifiedSentence = sentence.upper()
	connectionSocket.send(modifiedSentence)
	connectionSocket.close()

	connectionSocket2, addr = serverSocket2.accept()
	connectionSocket2.send(modifiedSentence)
	connectionSocket2.close()


