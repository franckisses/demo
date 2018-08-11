import asyncio

async def execute(x):
    print('Number:', x)
    return x

coroutine = execute(1)
print('Coroutine:', coroutine)
print('After calling execute')

loop = asyncio.get_event_loop()
# 调用了它的 create_task() 方法将 coroutine 对象转化为了 task 对象
task = loop.create_task(coroutine)
print('Task:', task)
# 将 task 对象添加到事件循环中得到执行，随后我们再打印输出一下
# task 对象，发现它的状态就变成了 finished，同时还可以看到其 result 变成了 1
loop.run_until_complete(task)
print('Task:', task)
print('After calling loop')