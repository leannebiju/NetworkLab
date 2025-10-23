import socket 

s = socket.socket()
s.connect(('localhost', 12345))

pt = input("Enter text to send : ")
key = int(input("Enter key(number of rails): "))

ct = ''

if key == 1:
    ct = pt
else:
    rail = ['' for _ in range(key)]
    dir_down = False
    row = 0
    for ch in pt:
        rail[row] += ch
        if row == 0 or row == key-1:
            dir_down = not dir_down
        row+=1 if dir_down else -1
    ct = ''.join(rail)

print("Sending encrypted message : ", ct)
msg = f"{key}|{ct}"
s.send(msg.encode())