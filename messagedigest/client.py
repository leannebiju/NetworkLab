import socket
import hashlib

s = socket.socket()
s.connect(('localhost', 12345))
print("Connected to server.")

message = input("Enter message to send: ")

# Calculate message digests
md5_digest = hashlib.md5(message.encode()).hexdigest()
sha1_digest = hashlib.sha1(message.encode()).hexdigest()
sha256_digest = hashlib.sha256(message.encode()).hexdigest()
sha512_digest = hashlib.sha512(message.encode()).hexdigest()

# Format data as: message|md5|sha1|sha256|sha512
data = f"{message}|{md5_digest}|{sha1_digest}|{sha256_digest}|{sha512_digest}"

s.send(data.encode())
print("Message and digests sent.")

s.close()