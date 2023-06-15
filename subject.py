from interface import PictureManagerInterface


class PictureManager(PictureManagerInterface):
    """
    The PictureManager contains some core business logic. Usually, PictureManagers are
    capable of doing some useful work which may also be very slow or sensitive -
    e.g. correcting input data. A Proxy can solve these issues without any
    changes to the PictureManager's code.
    """

    def request(self) -> None:
        print("PictureManager: Handling request.")
