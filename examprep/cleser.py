import socket

weather={"delhi":"summer", "mumbai":"winter", "chennai":"spring", "kolkata":"autumn"}

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', int(input("Enter Port No: "))))
sock.listen()
conn, addr=sock.accept()

while True:
	city=conn.recv(1024).decode()
	if city in weather:
		conn.send(weather[city].encode())
	elif city=="quit":
		break
	else:
		conn.send("na".encode())

conn.close()
sock.close()
