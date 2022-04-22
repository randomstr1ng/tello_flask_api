#!/usr/bin/env python3

import socket, threading

#####################################################################################################################
# Setup Middleware socket
proxy_host = "127.0.0.1"
proxy_port = 9090
client_host = "127.0.0.1"
client_port = 9092
recvaddr = (proxy_host,proxy_port)
clientaddr = (client_host, client_port )
proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
proxy_socket.bind(recvaddr)

#####################################################################################################################
# Setup target
target = "10.20.30.32"
target_port = 8889
drone_address = (target, target_port)

# Misc Banner
print("DJI Tello Drone Middleware\n")
print(f"[*] Listener: udp://{proxy_host}:{proxy_port}")
print(f"[*] Receiver: udp://{target}:{target_port}")

#####################################################################################################################
# Result Socket Setup
host = ""
port = 8889
locaddr = (host,port)
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(locaddr)

def get_return():
    while True:
        try:
            data, server = udp_socket.recvfrom(1518)
            print(f"Return Value: {data.decode(encoding='utf-8')}")
            proxy_socket.sendto(data, clientaddr)
        except Exception:
            print("\n END .... \n")
            break

recvThread = threading.Thread(target=get_return)
recvThread.start()

#####################################################################################################################
# Run Server
while True:
    try:
        command, server = proxy_socket.recvfrom(1518)
        print(f"Got Command: {command.decode(encoding='utf-8')}")
        if not command:
            break
        sent = udp_socket.sendto(command, drone_address)
        print(f"Data sent: {sent}")
    except KeyboardInterrupt:
        print("Close Console...")
        udp_socket.close()
        break