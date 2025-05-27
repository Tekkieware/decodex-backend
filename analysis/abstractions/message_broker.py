from abc import ABC, abstractmethod

class MessageBroker(ABC):
    @abstractmethod
    def publish(self, channel: str, message: str):
        pass

    @abstractmethod
    def subscribe(self, channel: str):
        pass
