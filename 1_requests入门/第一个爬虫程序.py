# -*- coding: utf-8 -*-
"""
爬虫：通过编写程序来获取网上的资源
需求：用程序去模拟浏览器，输入网址，并且从该网址中获取资源
python搞定以上需求
作者：高振涵
日期：2022-08-30
"""

from urllib.request import urlopen

url = 'http://www.baidu.com'
resp = urlopen(url)

with open('my baidu.html', mode ='w', encoding='UTF-8') as fin:
    fin.write(resp.read().decode('UTF-8'))
print('over!')