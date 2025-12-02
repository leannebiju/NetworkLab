import socket
import threading

def recvmsg():
	while True:
		try:
			data = clisock.recv(1024).decode()
			if not data or data == "quit":
				break
			print("Server:", data)
		except:
			break
	try:
		clisock.close()
	except:
		pass

clisock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clisock.connect(('127.0.0.1', int(input("Enter Server Socket No: "))))
threading.Thread(target=recvmsg, daemon=True).start()

while True:
	msg=input()
	if msg == "quit":
		clisock.send(msg.encode())
		break
	try:
		clisock.send(msg.encode())
	except:
		break

try:
	clisock.close()
except:
	pass