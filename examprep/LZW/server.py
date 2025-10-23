import socket 

s = socket.socket()
s.bind(('localhost', 12345))
s.listen(1)
conn, addr = s.accept()
data = conn.recv(1024).decode()

print("Received compressed code : ", data)

dict_size = 256
dictionary = {i: chr(i) for i in range(dict_size)}
compressed = [int(k) for k in data.split(',')]
result = w = chr(compressed[0])

for k in compressed[1:]:
    if k in dictionary:
        entry = dictionary[k]
    elif k==dict_size:
        entry = w + w[0]
    else:
        raise ValueError("Invalid compressed code")
    result+=entry
    dictionary[dict_size] = w + entry[0]
    dict_size += 1
    w = entry

print("Decompressed Text : ", result)