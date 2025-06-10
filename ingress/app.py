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
    required_keys = {"code", "language"}
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
