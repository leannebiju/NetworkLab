import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serveraddress = ('localhost', 12345)

message = "Hi from Client"

s.sendto(message.encode(), serveraddress)

data, _ = s.recvfrom(1024)
print("Received : ", data.decode())

s.close()