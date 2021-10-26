# callback-based async framework
#  * non-blocking sockets
#  * callbacks
#  * event loop
# -> coroutines
#  * Future
#  * generators
#  * Task is responsible for calling next() on generators


import socket
import time
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ

selector = DefaultSelector()
n_jobs = 0


class Future:
    def __init__(self):
        self.callback = None

    def resolve(self):
        self.callback()

    def __await__(self):
        yield self


class Task:
    def __init__(self, gen):
        self.gen = gen
        self.step()

    def step(self):
        try:
            f = self.gen.send(None)  # next(gen)
        except StopIteration:
            return

        f.callback = self.step


async def get(path):
    global n_jobs
    n_jobs += 1
    s = socket.socket()
    s.setblocking(False)
    try:
        s.connect(('localhost', 5000))
    except BlockingIOError:
        pass

    f = Future()
    selector.register(s.fileno(), EVENT_WRITE, f)
    await f
    selector.unregister(s.fileno())

    s.send(('GET %s HTTP/1.0\r\n\r\n' % path).encode())
    buf = []

    while True:
        f = Future()
        selector.register(s.fileno(), EVENT_READ, f)
        await f
        # by now, by the time the task resumes, the socket now is readble

        selector.unregister(s.fileno())
        chunk = s.recv(1000)

        if chunk:
            buf.append(chunk)
        else:
            # task done
            break

    # Finished.
    print((b''.join(buf)).decode().split('\n')[0])
    n_jobs -= 1


start = time.time()
Task(get('/foo'))  # get() just return a generator, so we need Task class to execute the generator
Task(get('/bar'))

while n_jobs:
    events = selector.select()
    for key, mask in events:
        future = key.data
        future.resolve()  # = f.callback() = task.step() = next(gen) = next(get("/foo"))

print('took %.2f seconds' % (time.time() - start))
