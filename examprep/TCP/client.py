import socket 
port = int(input("Enter port number : "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', port))

s.send("Message from Client".encode())

data = s.recv(1024).decode()
print("Received : ", data)

s.close()