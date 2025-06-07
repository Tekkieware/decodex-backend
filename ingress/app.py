import json
import uuid
import logging
from typing import Dict, Any

from models.message import Message
from adapters.redis_adapter import RedisAdapter
from adapters.websocket_adapter import WebSocketAdapter

logger = logging.getLogger(__name__)
redis_adapter = RedisAdapter()


async def process_message(message: Dict[str, Any]) -> Dict[str, str]:
    required_keys = {"code", "language", "user_id"}
    if not required_keys.issubset(message):
        missing = required_keys - message.keys()
        return {"status": "error", "detail": f"Missing fields: {', '.join(missing)}"}

    try:
        # Generate unique analysis_id
        analysis_id = str(uuid.uuid4())
        message["analysis_id"] = analysis_id

        msg = Message(**message)
        redis_adapter.publish("code_channel", msg.json())
        return {"status": "sent", "analysis_id": analysis_id}

    except Exception as e:
        return {"status": "error", "detail": str(e)}


async def listen_to_results(ws_adapter: WebSocketAdapter):
    pubsub = redis_adapter.subscribe("result_channel")
    if pubsub is None:
        logger.error("Failed to subscribe to result_channel.")
        return

    import asyncio
    logger.info("Subscribed to result_channel, waiting for messages...")

    while True:
        message = await asyncio.to_thread(pubsub.get_message, timeout=1.0)
        if message and message['type'] == 'message':
            try:
                data = json.loads(message['data'])
                analysis_id = data.get("analysis_id")
                if analysis_id:
                    await ws_adapter.send_to_analysis(analysis_id, json.dumps(data))
                else:
                    logger.warning("Result message missing analysis_id.")
            except Exception as e:
                logger.error(f"Error processing result message: {e}", exc_info=True)

        await asyncio.sleep(0.1)
