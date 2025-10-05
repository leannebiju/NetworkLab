import socket

def calc_parity(data_bits):
    # Calculate parity bits for positions 1, 2, and 4
    p1 = data_bits[0] ^ data_bits[1] ^ data_bits[3]
    p2 = data_bits[0] ^ data_bits[2] ^ data_bits[3]
    p4 = data_bits[1] ^ data_bits[2] ^ data_bits[3]
    return [p1, p2, p4]

def encode_hamming(data_bits):
    # Return codeword [p1 p2 d0 p4 d1 d2 d3]
    p1, p2, p4 = calc_parity(data_bits)
    return [p1, p2, data_bits[0], p4, data_bits[1], data_bits[2], data_bits[3]]

def introduce_error(code):
    ans = input("Do you want to introduce a single-bit error? (y/n): ").strip().lower()
    if ans == 'y':
        pos = int(input(f"Enter codeword bit position (1-7) to flip: "))
        if 1 <= pos <= 7:
            code[pos - 1] = 1 - code[pos - 1]
    return code

def run_client():
    s = socket.socket()
    s.connect(('localhost', 12346))
    data = input("Enter 4 data bits : ")
    data_bits = [int(b) for b in data]
    codeword = encode_hamming(data_bits)
    print("Generated codeword:", ''.join(map(str, codeword)))
    codeword = introduce_error(codeword)
    print("Transmitted codeword:", ''.join(map(str, codeword)))
    s.send(''.join(str(b) for b in codeword).encode())
    s.close()

if __name__ == "__main__":
    run_client()