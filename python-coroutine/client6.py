import asyncio


async def tcp_echo_client(path):
    message = f'GET {path} HTTP/1.0\r\n\r\n'
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 5000)

    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    # print('Close the connection')
    writer.close()
    await writer.wait_closed()


async def main():
    for i in range(1000):
        await tcp_echo_client("/foo")
        await tcp_echo_client("/bar")


asyncio.run(main())
