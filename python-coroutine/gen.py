def fib(max_n):
    n, a, b = 0, 0, 1
    while n < max_n:
        # print(f"b={b}")
        x = yield b  # x=gen.send() 传入的值
        # print(f"x={x}")
        a, b = b, a + b
        n = n + 1


def gen():
    value = 0
    while True:
        receive = yield value
        if receive == "end":
            break
        value = f"got: {receive}"


g1 = gen()
print(g1.send(None))
print(g1.send('hello'))
print(g1.send(123456))
print(g1.send('end'))

"""

其实receive=yield value包含了3个步骤：
1、向函数外抛出（返回）value
2、暂停(pause)，等待next()或send()恢复
3、赋值receive=MockGetValue() 。 这个MockGetValue()是假想函数，用来接收send()发送进来的值
执行流程：
1、通过g.send(None)或者next(g)启动生成器函数，并执行到第一个yield语句结束的位置。这里是关键，很多人就是在这里搞糊涂的。运行receive=yield value语句时，我们按照开始说的拆开来看，实际程序只执行了1，2两步，程序返回了value值，并暂停(pause)，并没有执行第3步给receive赋值。因此yield value会输出初始值0。这里要特别注意：在启动生成器函数时只能send(None),如果试图输入其它的值都会得到错误提示信息。

2、通过g.send('hello')，会传入hello，从上次暂停的位置继续执行，那么就是运行第3步，赋值给receive。然后计算出value的值，并回到while头部，遇到yield value，程序再次执行了1，2两步，程序返回了value值，并暂停(pause)。此时yield value会输出”got: hello”，并等待send()激活。

3、通过g.send(123456)，会重复第2步，最后输出结果为”got: 123456″。

4、当我们g.send(‘e’)时，程序会执行break然后推出循环，最后整个函数执行完毕，所以会得到StopIteration异常。

从上面可以看出， 在第一次send(None)启动生成器（执行1–>2，通常第一次返回的值没有什么用）之后，对于外部的每一次send()，生成器的实际在循环中的运行顺序是3–>1–>2，也就是先获取值，然后dosomething，然后返回一个值，再暂停等待

https://blog.csdn.net/soonfly/article/details/78361819
"""
