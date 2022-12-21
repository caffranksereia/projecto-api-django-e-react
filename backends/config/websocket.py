async def websocket_application(scope, send, recive ):
    while True:
        event = await recive()
        if event["type"] == "websocket.connect":
            await send({"type": "websocket.accept"})
        if event["type"] == "websocket.disconnect":
            break

        if event["type"] == "websocket.receive":
            if event["text"] == "ping":
                await send({"type":"websocket.send", "text":"pong!"})