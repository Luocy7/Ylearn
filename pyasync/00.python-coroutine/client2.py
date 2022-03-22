import socket
from base import timeit
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ

selector = DefaultSelector()


def get(path):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(False)

    try:
        s.connect(('localhost', 5000))
    except BlockingIOError:
        pass

    selector.register(s.fileno(), EVENT_WRITE)
    selector.select()
    selector.unregister(s.fileno())

    # s is writable!
    s.send(('GET %s HTTP/1.0\r\n\r\n' % path).encode())

    buf = []
    while True:
        selector.register(s.fileno(), EVENT_READ)
        selector.select()
        selector.unregister(s.fileno())

        chunk = s.recv(1000)
        if not chunk:
            break
        buf.append(chunk)

    s.close()
    print((b''.join(buf)).decode().split('\n')[0])


@timeit
def main():
    get('/foo')
    get('/bar')


main()
