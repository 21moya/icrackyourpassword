import socket
import gmpy2
from utils import helpers

PORT = 8081

def verify_password(student_id, fakeA, small_a, password, HOST):
    decimal = 0

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        while True:
            message = s.recv(4096).decode("utf-8")

            if message.startswith("Welcome"):
                s.sendall(student_id.encode() + b"\n")

            elif message.startswith("The decimal"):
                message = s.recv(4096).decode("utf-8")
                decimal = message.split("\n")[0]
                s.sendall(str(fakeA).encode() + b"\n")

            elif message.startswith("Please"):
                key = helpers.calc_hash(gmpy2.mpz(decimal), small_a)
                ct = helpers.encrypt_pt(key, password)
                s.sendall(ct.encode() + b"\n")

            elif message.startswith("Login"):
                if message == "Login successful":
                    s.close()
                    return True
                else:
                    s.close()
                    return False