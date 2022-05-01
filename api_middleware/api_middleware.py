#!/usr/bin/env python3

import socket, threading
from argparse import ArgumentParser

def parse_options():
    description = "This script setup a middleware UDP Proxy for the DJI Tello API and the Drone."
    parser = ArgumentParser(description=description)
    parser.add_argument("-ph","--proxy_host", dest="proxy_host", help="Listen IP address of the Proxy Service on the Local Server", default="0.0.0.0")
    parser.add_argument("-pp","--proxy_port", dest="proxy_port", help="Listen Port of the Proxy Service", required=True)
    parser.add_argument("-ch","--client_host", dest="client_host", help="IP address of the API Server for back communication", required=True)
    parser.add_argument("-cp","--client_port", dest="client_port", help="Port of the API Server for back communication", required=True)
    parser.add_argument("-lh","--local_host", dest="local_host", help="Listen IP address of the Local Server for Drone communication", default="0.0.0.0")
    parser.add_argument("-lp","--local_port", dest="local_port", help="Listen Port of the Local Server for Drone communication", default=8889)
    parser.add_argument("-di","--drone_ip", dest="drone_ip", help="IP address of Drone", required=True)
    parser.add_argument("-dp","--drone_port", dest="drone_port", help="UDP port Drone accepts commands", default=8889)
    options = parser.parse_args()
    return options

def get_return():
    while True:
        try:
            data, server = udp_socket.recvfrom(1518)
            print(f"Return Value: {data.decode(encoding='utf-8')}")
            proxy_socket.sendto(data, clientaddr)
        except Exception:
            print("\n END .... \n")
            break
#####################################################################################################################
# Main
options = parse_options()

drone_address = (options.drone_ip, int(options.drone_port))
recvaddr = (options.proxy_host, int(options.proxy_port))
clientaddr = (options.client_host, int(options.client_port))
locaddr = (options.local_host, int(options.local_port))
  
proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
proxy_socket.bind(recvaddr)
 
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(locaddr)

print('DJI Tello Drone API Middleware\n')
print(f'[*] Listener: udp://{options.proxy_host}:{options.proxy_port}')
print(f'[*] Receiver: udp://{options.drone_ip}:{options.drone_port}')

recvThread = threading.Thread(target=get_return)
recvThread.start()

while True:
    try:
        command, server = proxy_socket.recvfrom(1518)
        print(f"Got Command: {command.decode(encoding='utf-8')}")
        if not command:
            break
        if "ping" in command.decode(encoding='utf-8'):
            data = "pong"
            sent = proxy_socket.sendto(data.encode(encoding="utf-8"), clientaddr)
            print(f"Data sent: {sent}")
        else:
            sent = udp_socket.sendto(command, drone_address)
            print(f"Data sent: {sent}")
    except KeyboardInterrupt:
        print("Close Console...")
        udp_socket.close()
        break