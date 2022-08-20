import os
import pty
import time

import serial

master, slave = pty.openpty()
port = os.ttyname(slave)

port = "/dev/tty1"
# port = "/dev/pts/1"
# port = "/dev/serial0"
# port = "/dev/ttyAMA0"

print(f"port: {port}")
ser = serial.Serial(port)

# To Write to the device
while True:
    msg = b'TV_ON'
    print(f"Send msg: {msg}")
    ser.write(msg)
    time.sleep(1)

# To read from the device
# os.read(master, 1000)
