# Voice Relay WebSocket Server

A simple asynchronous WebSocket server written in Python that relays incoming voice packets from one client to all other connected clients. Useful for implementing a basic voice chat signaling or relay layer.

---

## Features

- Accepts multiple WebSocket client connections concurrently.
- Receives voice data packets (binary messages) from clients.
- Broadcasts received packets to all other connected clients except the sender.
- Automatically removes disconnected clients.
- Prints connection, disconnection, and message logs with timestamps.

---

## Requirements

- Python 3.7 or higher
- `websockets` library

Install the required library with:

```bash
pip install websockets
```

## Usage

Run the server script:

```bash
python server.py
```

The server will start and listen on IP `192.168.31.10` port `8765` (change these in the script if needed).

Clients can connect via WebSocket to `ws://192.168.31.10:8765`.

When a client sends a voice packet (binary message), the server will forward it to all other connected clients.

## How It Works

- The server maintains a set of currently connected clients.
- Each time a new client connects, it is added to the set.
- Incoming messages from a client are relayed to all other clients.
- If a client disconnects, it is removed from the set.
- Logs with timestamps provide visibility into client connections and data flow.

## Notes

- This server does not process or decode voice data; it simply forwards raw packets.
- IP and port are hardcoded; you should update `websockets.serve(handler, "192.168.31.10", 8765)` to your server's actual IP address.
- For production use, consider adding authentication, encryption (`wss://`), error handling, and scalability improvements.
