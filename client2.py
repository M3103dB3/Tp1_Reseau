from socket import *
serverName = "localhost"
serverPort = 13000
clientSocket2 = socket(AF_INET, SOCK_STREAM)
clientSocket2.connect((serverName,serverPort))

modifiedSentence = clientSocket2.recv(1024)
print 'From Server:', modifiedSentence
clientSocket2.close()    