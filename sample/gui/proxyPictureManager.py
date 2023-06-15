from pictureManagerInterface import PictureManagerInterface
from pictureManager import PictureManager


class ProxyPictureManagerInterface(PictureManagerInterface):
    """
    The Proxy has an interface identical to the PictureManager.
    """

    def __init__(self) -> None:
        self._picture_manager = None

    def initialize(self) -> None:
        """
        The most common applications of the Proxy pattern are lazy loading,
        caching, controlling the access, logging, etc. A Proxy can perform one
        of these things and then, depending on the result, pass the execution to
        the same method in a linked PictureManager object.
        """

        if self._picture_manager is None:
            self._picture_manager = PictureManager()
        self._picture_manager.initialize()
        self.log_access()

    def resize(self) -> None:
        """
            The Subject interface declares common operations for both PictureManager and
            the Proxy. As long as the client works with PictureManager using this
            interface, you'll be able to pass it a proxy instead of a real subject.
        """
        self._picture_manager.resize()

    def display(self) -> None:
        """
            The Subject interface declares common operations for both PictureManager and
            the Proxy. As long as the client works with PictureManager using this
            interface, you'll be able to pass it a proxy instead of a real subject.
        """
        self._picture_manager.display()

    def log_access(self) -> None:
        """
            The most common applications of the Proxy pattern are lazy loading,
            caching, controlling the access, logging, etc. A Proxy can perform one
            of these things and then, depending on the result, pass the execution to
            the same method in a linked PictureManager object.
        """

        print("Proxy: Logging the time of request.", end="")
