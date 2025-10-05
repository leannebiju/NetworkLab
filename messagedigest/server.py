import socket
import hashlib

s = socket.socket()
s.bind(('localhost', 12345))
s.listen(1)
print("Server listening on port 12345...")

conn, addr = s.accept()
print("Connected by", addr)

# Receive data in format: message|md5|sha1|sha256|sha512
data = conn.recv(4096).decode()

if data.count('|') == 4:
    message, md5_recv, sha1_recv, sha256_recv, sha512_recv = data.split('|')
    print("Received message:", message)

    # Recalculate digests
    md5_calc = hashlib.md5(message.encode()).hexdigest()
    sha1_calc = hashlib.sha1(message.encode()).hexdigest()
    sha256_calc = hashlib.sha256(message.encode()).hexdigest()
    sha512_calc = hashlib.sha512(message.encode()).hexdigest()

    print("MD5 matches   :", md5_calc == md5_recv)
    print("SHA-1 matches :", sha1_calc == sha1_recv)
    print("SHA-256 matches:", sha256_calc == sha256_recv)
    print("SHA-512 matches:", sha512_calc == sha512_recv)
else:
    print("Invalid data format received.")

conn.close()
s.close()
