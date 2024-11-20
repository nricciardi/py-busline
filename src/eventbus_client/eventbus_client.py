from abc import ABC
from src.eventbus.eventbus import EventBus
from src.eventbus_client.publisher.local_eventbus_publisher import LocalEventBusPublisher
from src.eventbus_client.subscriber.local_eventbus_subscriber import LocalEventBusSubscriber


class LocalEventBusClient(LocalEventBusPublisher, LocalEventBusSubscriber, ABC):
    """
    Eventbus client which should used by components which wouldn't be a publisher/subscriber, but they need them

    Author: Nicola Ricciardi
    """

    # TODO
