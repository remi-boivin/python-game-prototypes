from interface import PictureManagerInterface
from subject import PictureManager


class ProxyPictureManagerInterface(PictureManagerInterface):
    """
    The Proxy has an interface identical to the PictureManager.
    """

    def __init__(self, real_subject: PictureManager) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        """
        The most common applications of the Proxy pattern are lazy loading,
        caching, controlling the access, logging, etc. A Proxy can perform one
        of these things and then, depending on the result, pass the execution to
        the same method in a linked PictureManager object.
        """

        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.", end="")
