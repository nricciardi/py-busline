# Busline for Python

Simple but structured eventbus for Python.

```python
from src.eventbus.async_local_eventbus import AsyncLocalEventBus
from src.eventbus_client.subscriber.closure_subscriber import ClosureSubscriber
from src.event.event import Event
from src.eventbus_client.publisher import Publisher


def on_event_callback(e: Event):
    print(e)


eventbus = AsyncLocalEventBus()

publisher = Publisher(eventbus)
subscriber = ClosureSubscriber(on_event_callback)

eventbus.add_subscriber(
    "test-topic",  # name of topic
    subscriber
)

publisher.publish("test-topic", Event())  # empty event
```
