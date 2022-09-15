# -*- coding: utf-8 -*-
"""
作者：高振涵
日期：2022-09-11
1.登录 -->得到cookie
2.带着cookie去请求书架url-->得到暑假内容

我们可以使用session进行请求 -->session 可以认为是 一连串的请求，整个过程中cookie不会丢失
"""

import requests

# session = 会话
session = requests.session()

url = 'https://passport.17k.com/ck/user/login'
data = {
    'loginName': '17701707838',
    'password': '794960974_zhu'
}

resp1 = session.post(url , data=data)

# print(resp.cookies)    # 看cookie
# 刚才的session中有cookie
resp2 = session.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919')
print(resp2.json())

session.close()

