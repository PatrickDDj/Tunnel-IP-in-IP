from device import Device
from ip_package import *
import sys

if __name__ == '__main__':
    port = int(sys.argv[1])
    next_port = int(sys.argv[2])
    flag = int(sys.argv[3])
    device = Device('127.0.0.1', port, '127.0.0.1', next_port)
    device.start()

    if flag==1:
        device.create_tunnel()
        inner_ip_package = Inner_IP_Package('127.0.0.1', '127.0.0.1', "Hello World!")
        device.send(inner_ip_package)
        device.close_tunnel()

