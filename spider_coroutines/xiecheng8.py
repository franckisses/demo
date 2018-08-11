"""
这次它遇到 await 方法确实挂起了，也等待了，但是最后却报了这么个错，
这个错误的意思是 requests 返回的 Response 对象不能和 await 一起使用，
为什么呢？因为根据官方文档说明，await 后面的对象必须是如下格式之一：
A native coroutine object returned from a native coroutine function，
一个原生 coroutine 对象。
A generator-based coroutine object returned from a function decorated with types.coroutine()，
一个由 types.coroutine() 修饰的生成器，这个生成器可以返回 coroutine 对象。
An object with an await__ method returning an iterator，
一个包含 __await 方法的对象返回的一个迭代器。

改进见xiecheng9.py
"""
import asyncio,random
import requests
import time


async def request():
    url = 'http:www,sina.com.cn'
    print('Waiting for', url)
    response = await requests.get(url)
    print('Get response from', url, 'Result:', response.text)

tasks = [asyncio.ensure_future(request()) for _ in range(5)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cost time:', end - start)