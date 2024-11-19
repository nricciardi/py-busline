import asyncio
import unittest
from src.eventbus_client.subscriber.closure_subscriber import ClosureSubscriber
from src.event.event import Event
from src.eventbus_client.publisher import Publisher
from src.eventbus.queued_local_eventbus import QueuedLocalEventBus


class TestEventBus(unittest.IsolatedAsyncioTestCase):

    async def test_queued_eventbus(self):

        eventbus = QueuedLocalEventBus()

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


if __name__ == '__main__':
    unittest.main()