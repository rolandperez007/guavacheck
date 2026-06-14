import asyncio
import websockets


async def test():
    uri = "ws://localhost:8000/ws"

    async with websockets.connect(uri) as ws:
        await ws.send("hello from client")

        response = await ws.recv()
        print("RECEIVED:", response)


asyncio.run(test())
