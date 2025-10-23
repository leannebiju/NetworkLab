import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('localhost', 12345))

data, addr = s.recvfrom(1024)

print("Received : ", data.decode())

s.sendto("Hello from UDP".encode(),addr)

s.close()