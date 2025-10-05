def generate_key_matrix(key):
    key = "".join(dict.fromkeys(key.upper().replace('J', 'I')))  # Remove duplicates, upcase, J→I
    matrix = []
    for c in key:
        if c not in matrix and c.isalpha():
            matrix.append(c)
    for c in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c not in matrix:
            matrix.append(c)
    return [matrix[i*5:(i+1)*5] for i in range(5)]

def prepare_text(text):
    text = text.upper().replace('J', 'I').replace(' ', '')
    res = ''
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            res += a + 'X'
            i += 1
        else:
            res += a + b
            i += 2
    if len(res) % 2:
        res += 'X'
    return res

def find_pos(matrix, c):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == c:
                return i, j

def encrypt(plain_text, key):
    matrix = generate_key_matrix(key)
    text = prepare_text(plain_text)
    cipher = ''
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_pos(matrix, a)
        row2, col2 = find_pos(matrix, b)
        if row1 == row2:
            cipher += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            cipher += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            cipher += matrix[row1][col2] + matrix[row2][col1]
    return cipher

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

# --- Example usage ---
key = input("Enter Playfair key: ")
pt = input("Enter plaintext: ")
ct = encrypt(pt, key)
print("Encrypted:", ct)
print("Decrypted (for check):", decrypt(ct, key))
