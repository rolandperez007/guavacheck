import asyncio
import websockets


async def test():
    uri = "ws://127.0.0.1:8000/ws/austin"

    async with websockets.connect(uri) as ws:
        await ws.send("show me lekki apartments")

        while True:
            try:
                msg = await ws.recv()
                print(msg)
            except:
                break


asyncio.run(test())
