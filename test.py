from interface import PictureManagerInterface
from subject import PictureManager
from proxy import ProxyPictureManagerInterface


def client_code(subject: PictureManagerInterface) -> None:
    """
    The client code is supposed to work with all objects (both subjects and
    proxies) via the Subject interface in order to support both real subjects
    and proxies. In real life, however, clients mostly work with their real
    subjects directly. In this case, to implement the pattern more easily, you
    can extend your Proxy from the real subject's class.
    """

    # ...

    subject.request()

    # ...


if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = PictureManager()
    client_code(real_subject)

    print("")

    print("Client: Executing the same client code with a Proxy:")
    proxyPictureManagerInterface = ProxyPictureManagerInterface(real_subject)
    client_code(proxyPictureManagerInterface)
