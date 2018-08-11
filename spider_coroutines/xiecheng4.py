import asyncio
import requests

# 定义了有个request()方法,请求百度,并返回状态码
async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status

# 定义一个callback()方法,这个方法接受一个参数,是task对象
def callback(task):
    # 打印task对象的结果
    print("I  AM A BOY")
    print('Status:', task.result())

coroutine = request()
# 当 coroutine 对象执行完毕之后，就去执行声明的 callback() 方法。
task = asyncio.ensure_future(coroutine)
# 调用 add_done_callback() 方法，将 callback() 方法传递给了封装好的 task 对象，
# 当 task 执行完毕之后,再调用 callback() 方法task 对象还会作为参数传递给 callback() 方法，
# 调用 task 对象的 result() 方法就可以获取返回结果了
task.add_done_callback(callback)
print('first Task:', task)


loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('second Task:', task)