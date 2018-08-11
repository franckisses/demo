"""
aiohttp 是一个支持异步请求的库，
利用它和 asyncio 配合我们可以非常方便地实现异步请求操作。
在这里我们将请求库由 requests 改成了 aiohttp，
通过 aiohttp 的 ClientSession 类的 get() 方法进行请求
"""
import asyncio
import requests
import time

start = time.time()

async def get(url):
    return requests.get(url)

async def request():
    url = 'http://127.0.0.1:5000'
    print('Waiting for', url)
    response = await get(url)
    print('Get response from', url, 'Result:', response.text)

tasks = [asyncio.ensure_future(request()) for _ in range(5)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cost time:', end - start)