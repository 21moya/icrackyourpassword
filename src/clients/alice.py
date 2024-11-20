import socket

PORT = 47183

def get_password(student_id, fakeB, HOST):
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
                s.sendall(str(fakeB).encode() + b"\n")

            elif message.startswith("The hex"):
                pw = message.split("\n")[1]
                if not pw: 
                    pw = s.recv(4096).decode("utf-8")       
                s.close()
                return {"password": pw, "decimal": decimal}