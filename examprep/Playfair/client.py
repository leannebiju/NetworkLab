import socket 

s = socket.socket()
s.connect(('localhost', 12345))

key = input("Enter Playfair Key : ")

key = key.upper().replace('J', 'I')
matrix = []

def findpos(c):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == c:
                return i,j

for c in key:
    if c not in matrix and c.isalpha():
        matrix.append(c)
for c in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
    if c not in matrix:
        matrix.append(c)

matrix = [matrix[i*5:(i+1)*5] for i in range (5)]

pt = input("Enter plain text : ")

text = pt
text = text.upper().replace('J', 'I').replace(' ','')
res = ''
i = 0
while i<len(text):
    a = text[i]
    b = text[i+1]
    if(a==b):
        res += a+'X'
        i+=1
    else:
        res += a+b
        i+=2
    if len(res)%2:
        res+='X'

ct = ''

for i in range (0,len(text), 2):
    a,b = res[i], res[i+1]
    r1, c1 = findpos(a)
    r2, c2 = findpos(b)
    if r1 == r2:
        ct += matrix[r1][(c1+1)%5] + matrix [r2][(c2+1)%5]
    elif c1==c2:
        ct += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
    else:
        ct += matrix [r1][c2] + matrix [r2][c1]
        
print("Encrypted message sent : ", ct)
msg = key + "|" + ct
s.send(msg.encode())  