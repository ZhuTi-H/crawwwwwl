# -*- coding: utf-8 -*-
"""
requests是第三方
作者：高振涵
日期：2022-08-30
"""

import requests

query = input('输入一个你喜欢的明星：')

url = f'https://www.sogou.com/web?query={query}'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                   'Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
}  # headers是一个小的反爬，在请求过程中，网站进行了对用户是否是自动程序的识别，而在请求头里面，User-Agent就是给网站来识别用户的。
# 因此我们把本身的User-Agent进行复制，从而让网站认识到我们是一个用户而非是自动程序。

resp = requests.get(url,headers = headers)

print(resp.text)# 能够拿到页面源代码

with open('my sogoustars.html', 'w', encoding='UTF-8') as fin:
    fin.write(resp.text)
print('over!')
resp.close()