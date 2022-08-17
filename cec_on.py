#!/usr/bin/python

import cec


print("init cec")
try:
    cec.init()
except Exception as e:
    print(e)
print("init cec success")

print("get TV")
tv = cec.Device(cec.CECDEVICE_TV)
print("get TV success")


print("Turn TV ON")
try:
    tv.power_on()
except Exception as e:
    print(e)
