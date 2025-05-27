import asyncio
import websockets

clients = set()

async def handler(websocket, path):
    clients.add(websocket)
    try:
        async for message in websocket:
            pass  # echo back or handle as needed
    finally:
        clients.remove(websocket)

async def broadcast(message):
    if clients:
        await asyncio.wait([client.send(message) for client in clients])

def start_server():
    return websockets.serve(handler, "0.0.0.0", 8765)
