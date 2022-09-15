# -*- coding: utf-8 -*-
"""
1. 拿到主页面的源代码，提取到子页面的链接
2. 通过href拿到子页面的内容，找到地址
作者：高振涵
日期：2022-09-04
"""
import requests
import time

from bs4 import BeautifulSoup

url = 'https://pic.netbian.com/4kbeijing/index_2.html'
resp = requests.get(url)
resp.encoding = 'gbk'

page = BeautifulSoup(resp.text, 'html.parser')

alist = page.find('ul', class_="clearfix").find_all('a')

for a in alist:
    href = 'https://pic.netbian.com/' + a.get('href').strip('/')
    child_page_resp = requests.get(href)
    child_page_resp.encoding = 'gbk'
    child_page_text = child_page_resp.text
    child_page = BeautifulSoup(child_page_text, 'html.parser')
    img = child_page.find('div', class_="photo-pic").find_all('img')
    for ig in img:
        src = 'https://pic.netbian.com/' + ig.get('src').strip('/')
    img_name = src.split('/')[-1]
    img_resp = requests.get(src)
    img_resp.content # 这里拿到的是字节
    with open('img/'+img_name, 'wb')as fin:
        fin.write(img_resp.content)
    print('over!!', img_name)
    time.sleep(1)
print('all over')



