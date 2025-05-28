import redis
from typing import Any, Optional


class RedisAdapter:
    def __init__(self, host: str = 'redis', port: int = 6379, db: int = 0):
        """
        Initialize the Redis client with the given host, port, and database index.
        Defaults to host='redis', port=6379, db=0.
        """
        self.client = redis.Redis(host=host, port=port, db=db)

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
