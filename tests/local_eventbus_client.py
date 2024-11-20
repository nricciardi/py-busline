import unittest
from src.eventbus.async_local_eventbus import AsyncLocalEventBus
from src.eventbus_client.eventbus_client import EventBusClient
from src.eventbus_client.publisher.local_eventbus_publisher import LocalEventBusPublisher
from src.event.event import Event
from src.eventbus_client.subscriber.closure_event_listener import ClosureEventListener
from src.eventbus_client.subscriber.local_eventbus_closure_subscriber import LocalEventBusClosureSubscriber


class TestLocalEventBusClient(unittest.IsolatedAsyncioTestCase):

    async def test_async_eventbus(self):

        local_eventbus_instance = AsyncLocalEventBus()       # singleton

        received_event = None

        event = Event()

        def subscriber_callback(topic_name: str, e: Event):
            print(f"subscriber event received: {e}")

        def client_callback(topic_name: str, e: Event):
            nonlocal received_event

            received_event = e

        subscriber = LocalEventBusClosureSubscriber(local_eventbus_instance, subscriber_callback)
        publisher = LocalEventBusPublisher(local_eventbus_instance)

        client = EventBusClient(publisher, subscriber, ClosureEventListener(client_callback))

        await client.subscribe("test")

        await client.publish("test", event)

        self.assertIs(event, received_event)

        await client.unsubscribe()
        received_event = None

        await client.publish("test", event)

        self.assertIs(received_event, None)


if __name__ == '__main__':
    unittest.main()