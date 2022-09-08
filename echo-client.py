import socket

HOST = "172.16.103.212" #localhost
PORT = 54321

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello World")
    data = s.recv(1024)

print(f"Received {data}")