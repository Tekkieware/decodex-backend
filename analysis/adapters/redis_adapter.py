import os
import redis
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class RedisAdapter:
    def __init__(self, host: str = 'redis', port: int = 6379, db: int = 0):
        """
        Initialize the Redis client.
        Connects to Redis using the REDIS_URL environment variable if available (for production).
        Falls back to host, port, and db parameters for local development.
        """
        redis_url = os.getenv("REDIS_URL")
        if redis_url:
            self.client = redis.from_url(redis_url)
            print("Connected to Redis via URL.")
        else:
            self.client = redis.Redis(host=host, port=port, db=db)
            print(f"Connected to local Redis at {host}:{port}.")


    def publish(self, channel: str, message: str) -> None:
        """
        Publish a message to a specific Redis channel.
        Args:
            channel (str): The name of the Redis channel.
            message (str): The message to publish.
        """
        try:
            self.client.publish(channel, message)
        except redis.RedisError as e:
            # Handle or log publish errors
            print(f"Redis publish error: {e}")

    def subscribe(self, channel: str) -> Optional[redis.client.PubSub]:
        """
        Subscribe to a Redis channel and return the PubSub object for listening.
        Args:
            channel (str): The name of the Redis channel to subscribe to.
        Returns:
            Optional[redis.client.PubSub]: The PubSub object, or None if an error occurs.
        """
        try:
            pubsub = self.client.pubsub()  # Create a PubSub instance
            pubsub.subscribe(channel)      # Subscribe to the specified channel
            return pubsub                  # Return the PubSub object to the caller
        except redis.RedisError as e:
            # Handle or log subscription errors
            print(f"Redis subscribe error: {e}")
            return None
