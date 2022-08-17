#!/usr/bin/python

import websocket
import json

websocket.enableTrace(True)


def on_message(wsapp, data):
    data = json.loads(data)
    command = data.get('command')
    try:
        if command == 'CEC_ON':
            pass
        elif command == 'CEC_STANDBY':
            pass
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # `${wsScheme}://${window.location.host}/ws/chat/${conversationId}/`
    # factory = WebSocketClientFactory("wss://app.itslido.com/ws/chat/1/")

    wsapp = websocket.WebSocketApp(
        "ws://0.0.0.0:8000/ws/chat/1/",
        on_message=on_message,
        header={"authorization": "Token 12fa1492621bc58e05ce82b79fc6a9f3ac737ad4"}
    )
    wsapp.run_forever()
