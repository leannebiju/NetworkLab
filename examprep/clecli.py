import socket

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', int(input("Enter Port No: "))))
while True:
	msg=input("Enter City for Weather: ")
	sock.send(msg.encode())
	if msg=="quit":
		break
	data=sock.recv(1024).decode()
	if data=="na":
		print("No Data Available")
	else:
		print("Weather:", data)
sock.close()
