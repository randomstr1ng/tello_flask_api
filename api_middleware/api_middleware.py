#!/usr/bin/env python3

import socket, threading
from argparse import ArgumentParser

def parse_options():
        description = "TThis script setup a middleware for the DJI Tello API to as a proxy between the Drone and the API Server."
        parser = ArgumentParser(description=description)
        parser.add_argument("-ph","--proxy_host", dest="proxy_host", help="Listen IP address of the Proxy Service", required=True)
        parser.add_argument("-pp","--proxy_port", dest="proxy_port", help="Listen Port of the Proxy Service", required=True)
        parser.add_argument("-ah","--client_host", dest="client_host", help="Listen IP address of the API Service", required=True)
        parser.add_argument("-ap","--client_port", dest="client_port", help="Listen Port of the API Service", required=True)
        parser.add_argument("-lh","--local_host", dest="host", help="Listen IP address of the Local Server", required=True)
        parser.add_argument("-lp","--local_port", dest="port", help="Listen Port of the Local Server", required=True)
        parser.add_argument("-th","--target_host", dest="target_host", help="Target IP Address (Drone IP)", required=True)
        parser.add_argument("-tp","--target_port", dest="target_port", help="Target Port (Drone UDP Port)", required=True)
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
options = parse_options

drone_address = (options["target_host"], options["target_port"])
recvaddr = (options["proxy_host"],options["proxy_port"])
clientaddr = (options["client_host"], options["client_port"])
locaddr = (options["host"],options["port"])
  
proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
proxy_socket.bind(recvaddr)
 
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(locaddr)

print('DJI Tello Drone API Middleware\n')
print(f'[*] Listener: udp://{options["proxy_host"]}:{options["proxy_port"]}')
print(f'[*] Receiver: udp://{options["target"]}:{options["target_port"]}')

recvThread = threading.Thread(target=get_return)
recvThread.start()

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


