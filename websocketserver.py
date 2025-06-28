import asyncio
import websockets
import datetime

clients = set()

async def handler(websocket):
    print(f"[{datetime.datetime.now()}] New client connected: {websocket.remote_address}")
    clients.add(websocket)
    try:
        async for message in websocket:
            print(f"[{datetime.datetime.now()}] Received voice packet: {len(message)} bytes")
            dead_clients = set()
            for client in list(clients):
                if client != websocket:
                    try:
                        await client.send(message)
                    except websockets.exceptions.ConnectionClosed:
                        dead_clients.add(client)
            clients.difference_update(dead_clients)
    except websockets.exceptions.ConnectionClosed:
        print(f"[{datetime.datetime.now()}] Client disconnected: {websocket.remote_address}")
    finally:
        clients.discard(websocket)

async def main():
    print("\nVoice WebSocket server running on ws://192.168.100.5:8765")
    async with websockets.serve(handler, "192.168.31.10", 8765):
        await asyncio.Future()

asyncio.run(main())
