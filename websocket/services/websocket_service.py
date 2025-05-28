import asyncio
import json
import logging

from adapters.redis_adapter import RedisAdapter
from adapters.socket_manager import broadcast, start_server

# Configure logger for visibility into server activity
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


async def notify_clients():
    """
    Launches a WebSocket server and listens to Redis messages from the 'result_channel',
    broadcasting incoming messages to all connected WebSocket clients.
    """
    redis_adapter = RedisAdapter()
    pubsub = redis_adapter.subscribe("result_channel")

    async def redis_listener():
        """
        Listens for new messages from the 'result_channel' and broadcasts them to clients.
        """
        logger.info("Listening for messages on 'result_channel'...")

        loop = asyncio.get_event_loop()

        # `pubsub.listen()` is blocking — run in a thread to avoid blocking the event loop
        def sync_redis_loop():
            for message in pubsub.listen():
                if message["type"] == "message":
                    decoded = message["data"].decode()
                    logger.info(f"Received Redis message: {decoded}")
                    asyncio.run_coroutine_threadsafe(broadcast(decoded), loop)

        await asyncio.to_thread(sync_redis_loop)

    # Start both the WebSocket server and Redis listener concurrently
    await asyncio.gather(
        start_server(),
        redis_listener()
    )
