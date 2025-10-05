from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('The server is ready to receive')

connectionSocket, addr = serverSocket.accept()
print(f'Connection established with {addr}')

while True:
    sentence = connectionSocket.recv(1024).decode()
    print("Client : ", sentence)
    if sentence.lower() == 'bye':
        print("Connection closed by the Client.")
        break
    sentence2 = input('You : ')
    connectionSocket.send(sentence2.encode())
    if sentence2.lower() == 'bye':
        print("Connection closed by You.")
        break
connectionSocket.close()
serverSocket.close()    
