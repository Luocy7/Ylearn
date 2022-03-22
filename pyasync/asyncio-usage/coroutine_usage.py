import asyncio
import time


def now():
    return time.time()


async def do_some_work(x):
    print('Waiting: ', x)
    await asyncio.sleep(x)
    return f'Done after {x}s'


start = now()
loop = asyncio.get_event_loop()


def define_coroutine():
    loop.run_until_complete(do_some_work(2))


def create_task():
    # task = asyncio.create_task(do_some_work(2))
    task = loop.create_task(do_some_work(2))
    print(task)
    loop.run_until_complete(task)
    print(task)


def bind_callback():
    """
    绑定回调，在task执行完毕的时候可以获取执行的结果，回调的最后一个参数是future对象，通过该对象可以获取协程返回值。
    如果回调需要多个参数，可以通过偏函数导入
    """

    def callback(future):
        print('Callback: ', future.result())

    task = asyncio.ensure_future(do_some_work(2))
    task.add_done_callback(callback)
    loop.run_until_complete(task)

    # def callback(t, future):
    #     print('Callback:', t, future.result())
    #
    # task.add_done_callback(functools.partial(callback, 2))


def future_result():
    task = asyncio.ensure_future(do_some_work(2))
    loop.run_until_complete(task)

    print('Task ret: {}'.format(task.result()))


def test_coroutine():
    """
    asyncio实现并发，就需要多个协程来完成任务，每当有任务阻塞的时候就await，然后其他协程继续工作。创建多个协程的列表，然后将这些协程注册到事件循环中
    """
    tasks = [asyncio.ensure_future(do_some_work(i)) for i in [1, 2, 4]]
    loop.run_until_complete(asyncio.wait(tasks))

    for task in tasks:
        print('Task ret: ', task.result())


def coroutine_nest():
    """使用async可以定义协程，协程用于耗时的io操作，我们也可以封装更多的io操作过程，这样就实现了嵌套的协程，即一个协程中await了另外一个协程，如此连接起来"""

    async def main():
        tasks = [asyncio.ensure_future(do_some_work(i)) for i in [1, 2, 4]]
        dones, pendings = await asyncio.wait(tasks)
        for task in dones:
            print('Task ret: ', task.result())

        # 如果使用的是 asyncio.gather创建协程对象，那么await的返回值就是协程运行的结果
        # results = await asyncio.gather(*tasks)
        # for result in results:
        #     print('Task ret: ', result)

    loop.run_until_complete(main())


def coroutine_nest1():
    """不在main协程函数里处理结果，直接返回await的内容，那么最外层的run_until_complete将会返回main协程的结果"""

    async def main():
        tasks = [asyncio.ensure_future(do_some_work(i)) for i in [1, 2, 4]]
        return await asyncio.gather(*tasks)

    results = loop.run_until_complete(main())

    for result in results:
        print('Task ret: ', result)


def coroutine_nest2():
    async def main():
        tasks = [asyncio.ensure_future(do_some_work(i)) for i in [1, 2, 4]]
        for task in asyncio.as_completed(tasks):
            result = await task
            print('Task ret: {}'.format(result))

    loop.run_until_complete(main())


if __name__ == '__main__':
    # define_coroutine()
    # create_task()
    # bind_callback()
    # future_result()
    # test_coroutine()
    # coroutine_nest()
    # coroutine_nest1()
    coroutine_nest2()
    print('TIME: ', now() - start)
