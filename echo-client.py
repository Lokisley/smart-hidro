import socket
import time
import json

HOST = "172.16.103.212" #localhost
PORT = 54321
cont = 0

hidro = {
    "id": 0,
    "consumo": 200,
    "vazao": 20
    }

jobj = json.dumps(hidro)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    while True:
        s.sendto(f"{jobj} {cont}".encode('utf-8'), (HOST, PORT))   #envia info para servidor
        data, addr = s.recvfrom(1024)                                   #recebe resposta

        print(f"Received {data.decode('utf-8')} {cont}")                #printa resposta

        time.sleep(1)                                                   #seta delay
        cont += 1