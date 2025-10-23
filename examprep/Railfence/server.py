import socket 

s = socket.socket()
s.bind(('localhost', 12345))
s.listen(1)
conn, addr = s.accept()
data = conn.recv(1024).decode()

key, ct = data.split('|',1)
key = int(key)
print("Received : ", ct)

rail = [['\n' for _ in range(len(ct))]for i in range(key)]
dir_down = None
row, col = 0,0

for i in range(len(ct)):
    if row == 0:
        dir_down = True
    if row == key-1:
        dir_down = False
    rail[row][col] = '*'
    col+=1
    row+=1 if dir_down else -1

index = 0
for i in range(key):
    for j in range(len(ct)):
        if(rail[i][j]=='*' and (index<len(ct))):
            rail[i][j] = ct[index]
            index+=1

result=[]
row, col = 0,0 
for i in range(len(ct)):
    if row == 0:
        dir_down = True
    if row == key -1:
        dir_down = False
    if(rail[row][col] != '\n'):
        result.append(rail[row][col])
        col+=1
    row += 1 if dir_down else -1

text = ''.join(result)

print("Decrypted text : ", text)