#!/usr/bin/python

import websocket
import json
import cec

websocket.enableTrace(True)

print("init cec")
try:
    cec.init()
except Exception as e:
    print(e)
print("init cec success")

print("get TV")
tv = cec.Device(cec.CECDEVICE_TV)
print("get TV success")


def on_message(wsapp, data):
    data = json.loads(data)
    command = data.get('command')
    try:
        if command == 'CEC_ON':
            print("Turn TV ON")
            tv.power_on()
        elif command == 'CEC_STANDBY':
            print("Turn TV OFF")
            tv.standby()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # `${wsScheme}://${window.location.host}/ws/chat/${conversationId}/`
    # factory = WebSocketClientFactory("wss://app.itslido.com/ws/chat/1/")
    # Local host token
    token = "12fa1492621bc58e05ce82b79fc6a9f3ac737ad4"
    url = "ws://0.0.0.0:8000/ws/chat/1/"
    # Prod token
    token = "52275c2080c60594b80abc84f54ce9b16ea1fdb8"
    url = "wss://app.getlido.eu/ws/chat/1/"

    wsapp = websocket.WebSocketApp(
        url,
        on_message=on_message,
        header={"authorization": f"Token {token}"}
    )
    wsapp.run_forever()
