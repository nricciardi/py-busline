from abc import ABC, abstractmethod

from src.event.event import Event


class EventBusPublishClient(ABC):

    @abstractmethod
    async def publish(self, topic_name: str, event: Event):
        """
        Publish the event in topic

        :param topic_name:
        :param event:
        :return:
        """
