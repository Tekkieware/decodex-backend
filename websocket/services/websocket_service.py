import asyncio
import json
from adapters.redis_adapter import RedisAdapter
from adapters.socket_manager import broadcast, start_server

async def notify_clients():
    redis_adapter = RedisAdapter()
    pubsub = redis_adapter.subscribe("result_channel")

    async def listen():
        for message in pubsub.listen():
            if message["type"] == "message":
                await broadcast(message["data"].decode())

    await asyncio.gather(start_server(), listen())
