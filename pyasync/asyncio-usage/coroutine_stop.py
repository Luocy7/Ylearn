import asyncio
import time

from pprint import pprint
from threading import Thread


def now():
    return time.time()


async def do_some_work(x):
    print('Waiting: ', x)
    await asyncio.sleep(x)
    print(f'Done after {x}s')


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


def more_work(x):
    print(f'More work {x}')
    time.sleep(x)
    print(f'Finished more work {x}')


start = now()


def coroutine_cancel():
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(do_some_work(i)) for i in [1, 2, 4]]
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt:
        for task in asyncio.Task.all_tasks():
            pprint(task)
            print(task.cancel())
        loop.stop()
        loop.run_forever()
    finally:
        loop.close()


def coroutine_cancel1():
    loop = asyncio.get_event_loop()

    async def main():
        tasks = [asyncio.ensure_future(do_some_work(i)) for i in [1, 2, 4]]
        done, pending = await asyncio.wait(tasks)
        for task in done:
            print('Task ret: ', task.result())

    otask = asyncio.ensure_future(main())
    try:
        loop.run_until_complete(otask)
    except KeyboardInterrupt:
        print(asyncio.Task.all_tasks())
        print(asyncio.gather(*asyncio.Task.all_tasks()).cancel())
        loop.stop()
        loop.run_forever()
    finally:
        loop.close()


def thread_block():
    new_loop = asyncio.new_event_loop()
    t = Thread(target=start_loop, args=(new_loop,))
    t.start()

    new_loop.call_soon_threadsafe(more_work, 6)
    new_loop.call_soon_threadsafe(more_work, 3)


def thread_noblock():
    new_loop = asyncio.new_event_loop()
    t = Thread(target=start_loop, args=(new_loop,))
    t.start()

    asyncio.run_coroutine_threadsafe(do_some_work(6), new_loop)
    asyncio.run_coroutine_threadsafe(do_some_work(4), new_loop)


if __name__ == '__main__':
    # coroutine_cancel()
    thread_block()
    # thread_noblock()
    print('TIME: ', now() - start)
