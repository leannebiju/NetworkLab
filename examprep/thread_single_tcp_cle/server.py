import socket
import threading

def recvmsg():
	while True:
		try:
			data = conn.recv(1024).decode()
			if not data or data == "quit":
				break
			print("Client:", data)
		except:
			break
	try:
		conn.close()
	except:
		pass
	try:
		sersock.close()
	except:
		pass

sersock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sersock.bind(('127.0.0.1', int(input("Enter Server Port No: "))))
sersock.listen()
conn, addr = sersock.accept()
threading.Thread(target=recvmsg, daemon=True).start()

while True:
	msg = input()
	if msg == "quit":
		conn.send(msg.encode())
		break
	else:
		try:
			conn.send(msg.encode())
		except:
			break
try:
	conn.close()
except:
	pass
try:
	sersock.close()
except:
	pass