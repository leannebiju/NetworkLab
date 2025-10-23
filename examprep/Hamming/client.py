import socket

s = socket.socket()
s.connect(('localhost', 12345))

data = input("Enter binary data of 4 bits : ")
db = [int(b) for b in data]

p1 = db[0] ^ db[1] ^ db[3]
p2 = db[0] ^ db[2] ^ db[3]
p4 = db[1] ^ db[2] ^ db[3]

# P1 P2 D1 P4 D2 D3 D4 

codeword = [p1, p2, db[0], p4, db[1], db[2], db[3]]
codewords = [str(b) for b in codeword]
codewords = ''.join(codewords)

print("Parity bit added codeword : ", codewords)

inject = input("Do you want to inject error? (y/n) ")
if inject == 'y':
    pos = int(input("Enter bit position to flip (1-7) ")) - 1
    codeword[pos] = 1 - codeword[pos]

codeword = ''.join(str(b) for b in codeword)
print("Sending error induced codeword : ", codeword)

s.send(codeword.encode())