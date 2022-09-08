import socket

HOST = "172.16.103.212" #localhost
PORT = 54321

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto("Hello World".encode('utf-8'), (HOST, PORT))
    data, addr = s.recvfrom(1024)

print(f"Received {data.decode('utf-8')}")

s.close()