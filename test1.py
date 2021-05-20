from device import Device
import sys

if __name__ == '__main__':
    port = int(sys.argv[1])
    device = Device('127.0.0.1', port)
    device.start()

