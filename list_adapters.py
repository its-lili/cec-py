#!/usr/bin/python

import cec


print("init cec")
try:
    cec.init()
except Exception as e:
    print(e)
print("init cec success")

print("list adapters")
try:
    print(cec.list_adapters())
except Exception as e:
    print(e)

print("list devices")
try:
    print(cec.list_devices())
except Exception as e:
    print(e)

print("done")
