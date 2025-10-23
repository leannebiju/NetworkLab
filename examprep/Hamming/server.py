import socket

s = socket.socket()
s.bind(('localhost', 12345))
s.listen(1)
conn, addr = s.accept()
data = conn.recv(1024).decode()

print("Received codeword : ", data)

db = [int(b) for b in data]

s4 = db[3] ^ db[4] ^ db[5] ^ db[6]
s2 = db[1] ^ db[2] ^ db[5] ^ db[6]
s1 = db[0] ^ db[2] ^ db[4] ^ db[6]
syndrome = s4*4 + s2*2 + s1*1

if syndrome == 0:
    print("No error detected")
else:
    print("Error detected")
    print("Correcting...")
    db[syndrome-1] = 1 - db[syndrome-1]
    dbc = [db[2], db[4], db[5], db[6]]
    print("Corrected data : ", ''.join(str(b) for b in db))
    print("Original word : ", ''.join(str(b) for b in dbc))