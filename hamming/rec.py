import socket

def detect_and_correct(received):
    # Calculate syndrome bits – position in codeword if single error
    s1 = received[0] ^ received[2] ^ received[4] ^ received[6]
    s2 = received[1] ^ received[2] ^ received[5] ^ received[6]
    s4 = received[3] ^ received[4] ^ received[5] ^ received[6]
    syndrome = s4*4 + s2*2 + s1*1
    if syndrome == 0:
        print("No error detected.")
    else:
        print(f"Error at position {syndrome}. Correcting it.")
        received[syndrome-1] = 1 - received[syndrome-1]
    return received

def run_server():
    s = socket.socket()
    s.bind(('localhost', 12346))
    s.listen(1)
    print("Server listening...")
    conn, addr = s.accept()
    codeword = conn.recv(1024).decode()
    print(f"Received codeword: {codeword}")
    received = [int(b) for b in codeword]
    corrected = detect_and_correct(received)
    data_bits = f'{corrected[2]}{corrected[4]}{corrected[5]}{corrected[6]}'
    print(f"Corrected codeword: {''.join(map(str, corrected))}")
    print(f"Extracted data bits: {data_bits}")
    conn.close()
    s.close()

if __name__ == "__main__":
    run_server()