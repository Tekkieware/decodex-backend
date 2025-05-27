import asyncio
from services.websocket_service import notify_clients

if __name__ == "__main__":
    asyncio.run(notify_clients())
