from device import Device
from ip_package import Inner_IP_Package, Outer_IP_Package
import json

if __name__ == '__main__':
    device = Device('127.0.0.1', 8894)
    device.start()

    device.create_tunnel('127.0.0.1', 8891)
    device.send("1. DD is Smart")
    device.close_tunnel()

    device.create_tunnel('127.0.0.1', 8892)
    device.send("2. DD is Smart")
    device.close_tunnel()

    device.create_tunnel('127.0.0.1', 8893)
    device.send("3. DD is Smart")
    device.close_tunnel()



