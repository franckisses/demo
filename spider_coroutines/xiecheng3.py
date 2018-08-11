import asyncio

async def execute(x):
    print('Number:', x)
    return x

coroutine = execute(1)
print('Coroutine:', coroutine)
print('After calling execute')

#定义task对象的另一种方式,通过asyncio的ensure_future()方法,返回task对象
task = asyncio.ensure_future(coroutine)
print('first Task:', task)

# 创建一个事件循环
loop = asyncio.get_event_loop()
# 将task事件添加到事件循环中去
loop.run_until_complete(task)
print('second Task:', task)
print('After calling loop')