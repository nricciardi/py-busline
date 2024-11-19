from src.event.event import Event
from src.eventbus.eventbus import EventBus
from src.eventbus_client.publisher.publisher import Publisher


class LocalEventBusPublisher(Publisher):

    def __init__(self, eventbus_instance: EventBus):
        self._eventbus = eventbus_instance

    async def _internal_publish(self, topic_name: str, event: Event):
        self.on_publishing(topic_name, event)
        await self._eventbus.put_event(topic_name, event)
        self.on_published(topic_name, event)