import asyncio

# 创建一个execute的方法
async def execute(x):
    print("number:",x)


# 调用之后并没有执行 返回了一个协程对象
coroutine=execute(1)
print("coroutine",type(coroutine))
print("after calling execute")

# 使用 get_event_loop() 方法创建了一个事件循环 loop
loop=asyncio.get_event_loop()
# 并调用了 loop 对象的 run_until_complete() 方法将协程注册到事件循环 loop 中，然后启动。
loop.run_until_complete(coroutine)
print("after calling loop")