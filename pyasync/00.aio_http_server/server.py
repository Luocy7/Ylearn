"""
使用`aiohttp`库实现一个简单的 web 服务器, 为其他示例提供接口
对于一个`/aio`请求, 它会随机沉睡`1-30`秒再返回, 返回的内容是一个json字符串, 结构为`{delay: 沉睡的秒数}`
"""

import asyncio
import random

from aiohttp import web


async def aio_api(req: web.Request):
    # 随机沉睡 1-30s 再返回
    delay = random.randint(1, 30)
    resp = {
        'delay': delay,
    }
    print('delay: %d' % delay)
    await asyncio.sleep(delay)
    return web.json_response(resp)


async def path_param_handler(req: web.Request):
    name = req.match_info.get('name', 'Anonymous')
    text = "Hello, " + name
    return web.Response(text=text)


route_list = [
    web.get('/aio', aio_api),
    web.get('/{name}', path_param_handler)
]

app = web.Application()
app.add_routes(route_list)
web.run_app(app, port=3000)
