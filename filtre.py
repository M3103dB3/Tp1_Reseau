from socket import *
serverPort1= 12000
serverSocket1 = socket(AF_INET,SOCK_STREAM)
serverSocket1.bind(('',serverPort1))
serverSocket1.listen(1)

serverPort2 = 13000
serverSocket2 = socket(AF_INET,SOCK_STREAM)
serverSocket2.bind(('',serverPort2))
serverSocket2.listen(1)



print 'The server is ready to receive'
while 1:
	connectionSocket1, addr = serverSocket1.accept()
	connectionSocket2, addr = serverSocket2.accept()
	
	sentence1 = connectionSocket1.recv(1024)
	capitalizedSentence1 = sentence1.upper()
	connectionSocket2.send(capitalizedSentence1)
	print capitalizedSentence1	
	connectionSocket1.close()

	sentence2 = connectionSocket2.recv(1024)
	capitalizedSentence2 = sentence2.upper()
	connectionSocket1.send(capitalizedSentence2)
	print capitalizedSentence	
	connectionSocket2.close()


