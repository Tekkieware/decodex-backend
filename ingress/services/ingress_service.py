from typing import Dict, Any
from models.message import Message
from adapters.redis_adapter import RedisAdapter
import logging

# Set up logging for better observability
logger = logging.getLogger(__name__)

# Create a Redis adapter instance (you may want to reuse this in a broader context)
redis_adapter = RedisAdapter()

async def process_message(message: Dict[str, Any]) -> Dict[str, str]:
    """
    Process an incoming message by validating and publishing it to the Redis 'code_channel'.

    Args:
        message (dict): A dictionary containing 'code', 'language', and 'user_id'.

    Returns:
        dict: A status response indicating success or failure.
    """
    required_keys = {"code", "language", "user_id"}

    # Validate that all required keys are present
    if not required_keys.issubset(message):
        missing = required_keys - message.keys()
        logger.warning(f"Missing fields in message: {missing}")
        return {"status": "error", "detail": f"Missing fields: {', '.join(missing)}"}

    try:
        # Construct the Message object
        msg = Message(**message)

        # Publish serialized message to Redis
        redis_adapter.publish("code_channel", msg.json())

        logger.info(f"Message from user {msg.user_id} published to code_channel.")
        return {"status": "sent"}

    except Exception as e:
        # Log and return error if processing fails
        logger.error(f"Failed to process message: {e}", exc_info=True)
        return {"status": "error", "detail": str(e)}
