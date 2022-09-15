# -*- coding: utf-8 -*-
"""
作者：高振涵
日期：2022-09-04
"""
import requests

from bs4 import BeautifulSoup

url = 'https://ms.shu.edu.cn/info/1245/15493.htm'
resp = requests.get(url)
resp.encoding = 'utf-8'

page = BeautifulSoup(resp.text, 'html.parser')
print(page)

table = page.find('table', id="dnn_ctr44082_ArtDetail_Table3")

trs = table.find_all('tr')[2:]
for tr in trs:
    tds = tr.find_all('td') # 每行的td
    name = tds[2].text
    id = tds[1].text
    zhuanye = tds[3].text
    print(name, ',' , id, ',' , zhuanye)