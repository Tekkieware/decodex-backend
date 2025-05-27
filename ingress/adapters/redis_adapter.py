import redis

class RedisAdapter:
    def __init__(self):
        self.client = redis.Redis(host='redis', port=6379, db=0)

    def publish(self, channel, message):
        self.client.publish(channel, message)

    def subscribe(self, channel):
        pubsub = self.client.pubsub()
        pubsub.subscribe(channel)
        return pubsub
