import socket

def generate_key_matrix(key):
    key = "".join(dict.fromkeys(key.upper().replace('J', 'I')))
    matrix = []
    for c in key:
        if c not in matrix and c.isalpha():
            matrix.append(c)
    for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c not in matrix:
            matrix.append(c)
    return [matrix[i*5:(i+1)*5] for i in range(5)]

def find_pos(matrix, c):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == c:
                return i, j

def decrypt(cipher_text, key):
    matrix = generate_key_matrix(key)
    text = cipher_text.upper()
    plain = ''
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_pos(matrix, a)
        row2, col2 = find_pos(matrix, b)
        if row1 == row2:
            plain += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plain += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            plain += matrix[row1][col2] + matrix[row2][col1]
    return plain

# --- Networking code ---
s = socket.socket()
s.bind(('localhost', 12444))
s.listen(1)
print("Server listening on port 12444...")
conn, addr = s.accept()
message = conn.recv(1024).decode()
if "|" in message:
    key, cipher = message.split("|", 1)
    print("Received key:", key)
    print("Received encrypted text:", cipher)
    plain = decrypt(cipher, key)
    print("Decrypted message:", plain)
else:
    print("Error: Message format invalid.")
conn.close()
s.close()