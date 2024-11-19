

class Topic:

    def __init__(self, name: str, content_type: str | None = None, description: str | None = None, priority: int = 0):
        self.__name = name
        self.__description = description
        self.__content_type = content_type
        self.__priority = priority

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str | None:
        return self.__description

    @property
    def content_type(self) -> str | None:
        return self.__content_type

    @property
    def priority(self) -> int:
        return self.__priority
