#!/usr/bin/env python3

import socket


class telloclient():
    def __init__(self, target, port, result_port):
        self.target = target
        self.port = port
        self.result_port = result_port
        self.target_address = (self.target, self.port)
        self.local_address = (self.target, self.result_port)


    def client(self, command):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(self.local_address)
        try:
            command = command.encode(encoding="utf-8")
            sent = s.sendto(command, self.target_address)
            result, server = s.recvfrom(1518)
            s.close()
            return result
        except Exception as e:
            s.close()
            return "Error: " + str(e)