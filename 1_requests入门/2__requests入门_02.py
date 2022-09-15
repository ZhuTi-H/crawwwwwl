# -*- coding: utf-8 -*-
"""
取到百度翻译的结果
作者：高振涵
日期：2022-08-31
"""
import requests

url = 'https://fanyi.baidu.com/sug'

s = input('请输入你要翻译的英文')
dat = {
    'kw': s
}
#发post请求
resp = requests.post(url, data=dat)
print(resp.json()) # 讲服务器返回的内容直接处理成json => dict
resp.close()