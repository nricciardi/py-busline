from typing import Callable
from src.event.event import Event
from src.eventbus.eventbus import EventBus
from src.eventbus_client.subscriber.closure_subscriber import ClosureSubscriber


class LocalEventBusClosureSubscriber(ClosureSubscriber):

    def __init__(self, eventbus_instance: EventBus, on_event_callback: Callable[[Event], None]):
        ClosureSubscriber.__init__(self, on_event_callback)
        self._eventbus = eventbus_instance

    async def _internal_subscribe(self, topic_name: str):
        self._eventbus.add_subscriber(topic_name, self)

    async def _internal_unsubscribe(self, topic_name: str | None = None):
        self._eventbus.remove_subscriber(self, topic_name)