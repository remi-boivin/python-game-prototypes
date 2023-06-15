from abc import ABC, abstractmethod


class PictureManagerInterface(ABC):
    """
    The Subject interface declares common operations for both PictureManager and
    the Proxy. As long as the client works with PictureManager using this
    interface, you'll be able to pass it a proxy instead of a real subject.
    """

    @abstractmethod
    def request(self) -> None:
        pass