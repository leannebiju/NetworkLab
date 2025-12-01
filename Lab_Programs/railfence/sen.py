import socket

def encrypt_rail_fence(text, key):
    if key == 1:
        return text
    rail = ['' for _ in range(key)]
    dir_down = False
    row = 0
    for ch in text:
        rail[row] += ch
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
        row += 1 if dir_down else -1
    return ''.join(rail)

s = socket.socket()
s.connect(('localhost', 15555))
key = int(input("Enter rail fence key (number of rails): "))
pt = input("Enter plaintext: ")
ct = encrypt_rail_fence(pt, key)
print("Encrypted message (sent):", ct)
# Send both key and ciphertext as one string
message = f"{key}|{ct}"
s.send(message.encode())
s.close()
