from typing import Callable
from uuid import uuid4

from src.event.event import Event
from src.eventbus.async_local_eventbus import AsyncLocalEventBus
from src.eventbus_client.eventbus_client import EventBusClient
from src.eventbus_client.publisher.local_eventbus_publisher import LocalEventBusPublisher
from src.eventbus_client.subscriber.local_eventbus_closure_subscriber import LocalEventBusClosureSubscriber


class LocalEventBusClient(EventBusClient):

    def __init__(self, on_event_callback: Callable[[str, Event], None], client_id: str = str(uuid4())):

        eventbus_instance = AsyncLocalEventBus()

        EventBusClient.__init__(
            self,
            publisher=LocalEventBusPublisher(eventbus_instance),
            subscriber=LocalEventBusClosureSubscriber(eventbus_instance, on_event_callback),
            client_id=client_id
        )


