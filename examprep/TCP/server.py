import socket
port = int(input("Enter port number : "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating socket

s.bind(('localhost', port))

s.listen(1) #listen for one connection

conn, addr = s.accept()

data = conn.recv(1024).decode()
print("Received : ", data)

conn.send("Hello from Server!".encode())

conn.close()
s.close()