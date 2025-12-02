import socket 

s = socket.socket()
s.connect(('localhost', 12345))

text = input("Enter text to compress : ")

dict_size = 256
dictionary = {chr(i): i for i in range(dict_size)}
w = ""
compressed = []

for c in text:
    wc = w+c
    if wc in dictionary:
        w = wc
    else:
        compressed.append(dictionary[w])
        dictionary[wc] = dict_size
        print(f"Adding '{wc}' to dictionary with code {dict_size}")
        dict_size += 1
        w = c

if w:
    compressed.append(dictionary[w])

msg = ','.join(str(k) for k in compressed)
print("Compressed codes sent : ", msg)

s.send(msg.encode())