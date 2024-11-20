from abc import ABC, abstractmethod
from uuid import uuid4


class EventBusConnector(ABC):
    """
    Abstract class which is used as base class to create a component which interacts with eventbus

    Author: Nicola Ricciardi
    """

    def __init__(self, connector_id: str = str(uuid4())):
        self._id = connector_id

    @abstractmethod
    async def connect(self):
        """
        Connect to eventbus

        :return:
        """

    @abstractmethod
    async def disconnect(self):
        """
        Disconnect to eventbus

        :return:
        """