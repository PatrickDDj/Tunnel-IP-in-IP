import socket
import threading
from ip_package import *

class Device:

    def __init__(self, host, port, next_host=None, next_port=None):
        self.source_address = host
        self.server = socket.socket()
        self.server.bind((host, port))
        self.server.listen(5)
        self.port = port
        self.next_port = next_port
        self.next_host = next_host

    def run(self):
        print("Device %d started!" % self.port)
        while True:
            client, addr = self.server.accept()
            print('Connection from ', addr)
            message = self.decode_message(client.recv(1024))

            print("message : ", message)

            if self.next_host != None:
                self.create_tunnel()
                self.send(message)
                self.close_tunnel()

    def start(self):
        th = threading.Thread(target=self.run)
        th.start()

    def create_tunnel(self):
        if self.next_port != None:
            port = self.next_port
            host = self.next_host
            self.destination_address = host
            self.client = socket.socket()
            self.client.connect((host, port))
            print("Tunnel created (from %s:%d to %s:%d)" % (self.source_address, self.port ,self.client.getsockname()[0], self.client.getsockname()[1]))

    def send(self, message):
        steam = self.encode_message(message)
        self.client.send(steam)

    def close_tunnel(self):
        print("Tunnel closed (from %s:%d to %s:%d)" % (self.source_address, self.port, self.client.getsockname()[0], self.client.getsockname()[1]))
        self.client.close()


    def encode_message(self, message):
        inner_ip_package = Inner_IP_Package(self.source_address, self.destination_address, message)
        print("-------------------------------------------")
        print("Inner IP Package created:")
        print(inner_ip_package.__dict__)
        print("-------------------------------------------")

        outer_ip_package = Outer_IP_Package(inner_ip_package.encode())
        print("-------------------------------------------")
        print("Outer IP Package created:")
        print(outer_ip_package.__dict__)
        print("-------------------------------------------")
        stream = outer_ip_package.encode()
        return stream

    def decode_message(self, steam):
        outer_ip_package = Outer_IP_Package.decode(steam)
        print("-------------------------------------------")
        print("Outer IP Package received:")
        print(outer_ip_package.__dict__)
        print("-------------------------------------------")

        inner_ip_package = Inner_IP_Package.decode(outer_ip_package.payload)
        print("-------------------------------------------")
        print("Inner IP Package received:")
        print(inner_ip_package.__dict__)
        print("-------------------------------------------")

        return inner_ip_package.payload
