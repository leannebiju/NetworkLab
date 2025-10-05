from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))
print("UDP Server is ready to receive messages...")

while True:
    msg, clientAddr = serverSocket.recvfrom(1024)
    sentence = msg.decode()
    print("Client:", sentence)

    if sentence.lower() == 'bye':
        print("Connection closed by client.")
        break

    sentence2 = input("You: ")
    serverSocket.sendto(sentence2.encode(), clientAddr)

    if sentence2.lower() == 'bye':
        print("Connection closed by you.")
        break

serverSocket.close()