#!/usr/bin/python

import cec
import serial
import sys

init_cec = False

if init_cec:
    print("init cec")
    try:
        cec.init()
    except Exception as e:
        print(e)
    print("init cec success")

    print("get TV")
    tv = None
    while not tv:
        try:
            tv = cec.Device(cec.CECDEVICE_TV)
        except Exception as e:
            print(f'error getting tv -> {e}')
    print("get TV success")


def tv_on():
    print("Turn TV ON")
    try:
        tv.power_on()
    except Exception as e:
        print(e)


port = "/dev/tty0"
# port = "/dev/tty1"
# port = "/dev/pts/1"
if len(sys.argv) > 1:
    port = sys.argv[1]

print(f"Port: {port}")
serial_port = serial.Serial(
    port=port,
    baudrate=9600,
    # bytesize=8,
    # timeout=1,
    # stopbits=serial.STOPBITS_ONE
)

print("start serial read")
serial_string = ""  # Used to hold data coming over UART
while True:
    # Wait until there is data waiting in the serial buffer
    if serial_port.in_waiting > 0:

        # Read data out of the buffer until a carraige return / new line is found
        serial_string = serial_port.readline()

        # Print the contents of the serial data
        try:
            message = serial_string.decode("Ascii")
            print(message)
            if message == "TV_ON":
                tv_on()
        except:
            pass
