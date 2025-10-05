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

def encodeData(data, key):
    l_key = len(key)
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    return codeword

# --- Begin main execution ---
s = socket.socket()
s.connect(('localhost', 12345))
data = input("Enter the binary data: ")
key = "1011"
codeword = encodeData(data, key)
print(f"Generated codeword: {codeword}")

# Error injection option
inject = input("Do you want to inject an error? (y/n): ").lower()
if inject == 'y':
    pos = int(input(f"Enter position (1-{len(codeword)}) to flip the bit: ")) - 1
    flipped = list(codeword)
    flipped[pos] = '1' if codeword[pos] == '0' else '0'
    codeword = ''.join(flipped)
    print(f"Codeword after error injection: {codeword}")

print(f"Transmitting codeword: {codeword}")
s.send(codeword.encode())
s.close()