import socket

def xor(a, b):
    res = []
    for i in range(1, len(b)):
        res.append('0' if a[i] == b[i] else '1')
    return ''.join(res)

def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0:pick]
    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0'*pick, tmp) + dividend[pick]
        pick += 1
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)
    return tmp

def decodeData(data, key):
    l_key = len(key)
    appended_data = data
    remainder = mod2div(appended_data, key)
    return remainder

s = socket.socket()
s.bind(('localhost', 12345))
s.listen(1)
print("Server listening for data...")
conn, addr = s.accept()
codeword = conn.recv(1024).decode()
print(f"Received codeword: {codeword}")
key = "1011"
remainder = decodeData(codeword, key)
if '1' in remainder:
    print("Error detected in received data.")
else:
    print("No error detected in received data.")
conn.close()