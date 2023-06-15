from pictureManagerInterface import PictureManagerInterface


class PictureManager(PictureManagerInterface):
    """
    The PictureManager contains some core business logic. Usually, PictureManagers are
    capable of doing some useful work which may also be very slow or sensitive -
    e.g. correcting input data. A Proxy can solve these issues without any
    changes to the PictureManager's code.
    """

    def initialize(self) -> None:
        """
            The Subject interface declares common operations for both PictureManager and
            the Proxy. As long as the client works with PictureManager using this
            interface, you'll be able to pass it a proxy instead of a real subject.
        """

    def resize(self) -> None:
        """
            The Subject interface declares common operations for both PictureManager and
            the Proxy. As long as the client works with PictureManager using this
            interface, you'll be able to pass it a proxy instead of a real subject.
        """

    def display(self) -> None:
        """
            The Subject interface declares common operations for both PictureManager and
            the Proxy. As long as the client works with PictureManager using this
            interface, you'll be able to pass it a proxy instead of a real subject.
        """
