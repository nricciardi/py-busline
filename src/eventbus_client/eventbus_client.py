from abc import ABC
from uuid import uuid4

from src.eventbus.eventbus import EventBus
from src.eventbus_client.publisher.local_eventbus_publisher import LocalEventBusPublisher
from src.eventbus_client.publisher.publisher import Publisher
from src.eventbus_client.subscriber.local_eventbus_subscriber import LocalEventBusSubscriber
from src.eventbus_client.subscriber.subscriber import Subscriber


class EventBusClient(Publisher, Subscriber, ABC):
    """
    Eventbus client which should used by components which wouldn't be a publisher/subscriber, but they need them

    Author: Nicola Ricciardi
    """

    def __init__(self, publisher: Publisher, subscriber: Subscriber, client_id: str = str(uuid4())):
        Publisher.__init__(self, client_id)
        Subscriber.__init__(self, client_id)


