from socket import *

clientSocket = socket(AF_INET, SOCK_DGRAM)
serverName = 'localhost'
serverPort = 12000

clientSocket.connect((serverName, serverPort))
print(f"Connected to UDP server at {serverName}:{serverPort}")

while True:
    sentence = input("You: ")
    clientSocket.send(sentence.encode())

    if sentence.lower() == 'bye':
        print("Connection closed by you.")
        break

    reply = clientSocket.recv(1024).decode()
    print("Server:", reply)

    if reply.lower() == 'bye':
        print("Connection closed by server.")
        break

clientSocket.close()
