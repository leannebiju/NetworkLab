import socket

def decrypt_rail_fence(cipher, key):
    # Create a matrix to mark the zigzag
    rail = [['\n' for _ in range(len(cipher))]
                  for _ in range(key)]
    dir_down = None
    row, col = 0, 0

    # Mark the places with '*'
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        rail[row][col] = '*'
        col += 1
        row += 1 if dir_down else -1

    # Fill the rail matrix with ciphertext
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if (rail[i][j] == '*') and (index < len(cipher)):
                rail[i][j] = cipher[index]
                index += 1

    # Read the matrix in zigzag manner to construct plaintext
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        if (rail[row][col] != '\n'):
            result.append(rail[row][col])
            col += 1
        row += 1 if dir_down else -1
    return "".join(result)

s = socket.socket()
s.bind(('localhost', 15555))
s.listen(1)
print("Server listening on port...")
conn, addr = s.accept()
data = conn.recv(1024).decode()
key_str, cipher = data.split("|", 1)
key = int(key_str)
print(f"Received ciphertext: {cipher}")
plaintext = decrypt_rail_fence(cipher, key)
print(f"Decrypted (rail fence): {plaintext}")
conn.close()
s.close()
