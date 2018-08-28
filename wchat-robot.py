# import itchat
# from itchat.content import *
# import json
# import requests


# @itchat.msg_register([TEXT])
# def text_reply(msg):
#     info = msg['Text'].encode('utf-8')
#     # 调用了图灵机器人的api
#     url = 'http://www.tuling123.com/openapi/api'
#     # key是图灵机器人的给定的接口,    loc:微信号   userid:图灵机器人的给的验证码
#     data = {u"key": "8fc0873d82ea42f3b684d3ba7976ad93",
#             "info": info, u"loc": "842549758", "userid": "286703"}
#     response = (requests.post(url, data).content).decode()
#     s = json.loads(response, encoding='utf-8')
#     print('s == %s' % s)
#     if s['code'] == 100000:
#         itchat.send(s['text'], msg['FromUserName'])

# itchat.auto_login(hotReload=True)
# itchat.run(debug=True)
a = [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1]
for x in a:
    if x:
        print(1)
    else:
        print(0)
