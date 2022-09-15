# -*- coding: utf-8 -*-
"""
作者：高振涵
日期：2022-09-08
"""
import requests
import re
import csv
from bs4 import BeautifulSoup

url = 'https://shanghai.zbj.com/search/service/?l=0&kw=小程序&r=1'
resp = requests.get(url)
obj = re.compile(r'<div class="search-result-list" data-v-f1777e88>.*?<div data-styleonly="" class="service-card-wrap" data-v-f1777e88>'
                 r'.*?<div class="shop-info.*?">(?P<title>.*?)</div>.*?</a>.*?'
                 r'<div class="price">.*?<span>(?P<price>.*?)</span>', re.S)

page_content = resp.text

f = open('bajie.csv','w',encoding='utf-8')
csvwriter = csv.writer(f)

result = obj.finditer(page_content)
for i in result:
    dic = i.groupdict()
    csvwriter.writerow(dic.values())
f.close()
resp.close()
print('over!!')

# 拿到每一个服务商的div
# divs = html.xpath('/html/body/div[2]/div/div/div[3]/div/div[3]/div[4]/div[1]')
# print(divs.text)
# for div in divs:
#     price = div.xpath('./div[1]/div[1]/div[3]/div[1]/span/text()')
#     print(price)
