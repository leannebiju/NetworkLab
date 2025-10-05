from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

print("Connected to server at", serverName, "on port", serverPort)

while True:
    sentence = input("You : ")
    clientSocket.send(sentence.encode())
    if sentence.lower() == 'bye':
        print("Connection closed by You.")
        break
    sentence2 = clientSocket.recv(1024).decode()
    print("Server : ", sentence2)
    if sentence2.lower() == 'bye':
        print("Connection closed by the Server.")
        break

clientSocket.close()
