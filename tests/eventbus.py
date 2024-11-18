import asyncio
import unittest
from src.eventbus.async_eventbus import AsyncEventBus
from src.subscriber.closure_subscriber import ClosureSubscriber
from src.event.event import Event
from src.publisher.publisher import Publisher
from src.eventbus.queued_eventbus import QueuedEventBus


class TestEventBus(unittest.IsolatedAsyncioTestCase):

    async def test_queued_eventbus(self):

        eventbus = QueuedEventBus()

        publisher = Publisher(eventbus)

        event = Event()
        received_event: Event = None

        def callback(e: Event):
            nonlocal received_event

            received_event = e

        subscriber = ClosureSubscriber(callback)

        eventbus.add_subscriber(
            "test",
            subscriber
        )

        await publisher.publish("test", event)

        await asyncio.sleep(1)

        self.assertEqual(event, received_event)

        eventbus.remove_subscriber(subscriber)
        received_event = None

        await publisher.publish("test", event)

        self.assertEqual(received_event, None)

    async def test_async_eventbus(self):

        eventbus = AsyncEventBus()

        publisher = Publisher(eventbus)

        event = Event()
        received_event = None

        def callback(e: Event):
            nonlocal received_event

            received_event = e

        subscriber = ClosureSubscriber(callback)

        eventbus.add_subscriber(
            "test",
            subscriber
        )

        await publisher.publish("test", event)

        self.assertEqual(event, received_event)

        eventbus.remove_subscriber(subscriber)
        received_event = None

        await publisher.publish("test", event)

        self.assertEqual(received_event, None)


if __name__ == '__main__':
    unittest.main()