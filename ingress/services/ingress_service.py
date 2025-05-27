from models.message import Message
from adapters.redis_adapter import RedisAdapter

redis_adapter = RedisAdapter()

async def process_message(message: dict):
    msg = Message(**message)
    redis_adapter.publish("code_channel", msg.json())
    return {"status": "sent"}
