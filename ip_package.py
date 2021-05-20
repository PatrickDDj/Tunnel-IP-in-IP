import json


class Inner_IP_Package:
    def __init__(self, source_address=None, destination_address=None, payload=None):
        # version : 4 bits
        self.version = 4

        # IHL : 4 bits
        self.IHL = 5

        # service : 8 bits
        self.service = 9

        # total length : 16 bits
        self.total_length = self.IHL + len(payload)

        # identification : 16 bits
        self.identification = 1

        # R : 1 bit
        self.R = 0

        # DF : 1 bit
        self.DF = 0

        # MF : 1 bit
        self.MF = 0

        # offset : 13 bits
        self.offset = 0

        # ttl : 8 bits
        self.ttl = 255

        # protocal : 8 bits
        self.protocal = 17

        # source address
        self.source_address = source_address

        # destination address
        self.destination_address = destination_address

        self.payload = payload

    def encode(self):
        return json.dumps(self.__dict__)

    def decode(steam):
        info = json.loads(steam)
        return Inner_IP_Package(info['source_address'], info['destination_address'], info['payload'])


class Outer_IP_Package:
    def __init__(self, inner_ip_package_info):

        inner_ip_package = Inner_IP_Package.decode(inner_ip_package_info)
        # version : 4 bits
        self.version = 4

        # IHL : 4 bits
        self.IHL = 5

        # service : 8 bits
        self.service = 9

        # total length : 16 bits
        self.total_length = self.IHL + inner_ip_package.total_length

        # identification : 16 bits
        self.identification = inner_ip_package.identification

        # R : 1 bit
        self.R = 0

        # DF : 1 bit
        self.DF = 0

        # MF : 1 bit
        self.MF = 0

        # offset : 13 bits
        self.offset = 0

        # ttl : 8 bits
        self.ttl = 255

        # protocal : 8 bits
        self.protocal = 4

        # source address
        self.source_address = inner_ip_package.source_address

        # destination address
        self.destination_address = inner_ip_package.destination_address

        self.payload = inner_ip_package_info

    def encode(self):
        return json.dumps(self.__dict__).encode('utf-8')

    def decode(steam):
        info = json.loads(steam.decode('utf-8'))
        return Outer_IP_Package(info['payload'])


