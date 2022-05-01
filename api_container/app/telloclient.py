#!/usr/bin/env python3

import socket


class telloclient():
    def __init__(self, result_port):
        self.result_port = result_port
        self.result_host = "0.0.0.0"
        self.local_address = (self.result_host, self.result_port)


    def client(self, command, port, target="127.0.0.1"):
        target_address = (target, port)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(self.local_address)
        try:
            command = command.encode(encoding="utf-8")
            sent = s.sendto(command, target_address)
            result, server = s.recvfrom(1518)
            s.close()
            return result
        except Exception as e:
            s.close()
            return "Error: " + str(e)