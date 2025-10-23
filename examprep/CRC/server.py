import socket

def xor(a,b):
    res = []
    for i in range(1,len(b)):
        res.append('0' if a[i]==b[i] else '1')
    return ''.join(res)

s = socket.socket()
s.bind(('localhost',12345))
s.listen(1)
conn, addr = s.accept()
data = conn.recv(1024).decode()
print("Received codeword : ", data)

key = "1011"

l_key = len(key)

pick = l_key
div = data
tmp = div[0:pick]

while pick<len(div):
    if tmp[0] == '1':
        tmp = xor(key,tmp) + div[pick]
    else:
        tmp = xor('0'*(l_key), tmp) + div[pick]
    pick = pick + 1
if tmp[0] == '1':
    tmp = xor(key,tmp)
else:
    tmp = xor('0'*(l_key), tmp)
    
if '1' in tmp:
    print("Error in received data")
else:
    print("Error free data received")