import socket 

HOST = "172.16.103.212" #localhost
PORT = 54321

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    # s.listen(1)
    while True:
        data, addr = s.recvfrom(1024)
        print(f"Connection received from {addr}")
        if not data:
            break
        print(f"Received: {data.decode('utf-8')}")
        s.sendto("Roger that".encode('utf-8'), addr)