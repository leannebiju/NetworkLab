import socket
s = socket.socket()
s.connect(('localhost',12345))

def xor(a,b):
    res = []
    for i in range(1,len(b)):
        res.append('0' if a[i]==b[i] else '1')
    return ''.join(res)

data = input("Enter the binary data : ")
key = "1011"

l_key = len(key)

pick = l_key
div = data + '0'*(l_key-1)
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
    
codeword = data+tmp
print("Codeword : ", codeword)

inject = input("Do you want to inject an error : (y/n)")
if inject == 'y':
    pos = int(input(f"Enter position(1-{len(codeword)}) to flip the bit")) - 1
    flipped = list(codeword)
    flipped[pos] = '1' if codeword[pos] == '0' else '0'
    codeword = ''.join(flipped)
    print("Codeword after injection : ", codeword)

print("Sending codeword... ", codeword)
s.send((codeword).encode())