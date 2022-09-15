# -*- coding: utf-8 -*-
"""
拿到页面源代码  requests
用re来提取有效信息  re
作者：高振涵
日期：2022-09-02
"""

import requests
import re
import csv  # 新内容

url = 'https://movie.douban.com/top250'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
}
resp = requests.get(url,headers=headers)
page_content = resp.text

# 解析数据

obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<title>.*?)</span>.*?<br>(?P<time>.*?)&', re.S)

f = open('data.csv','w',encoding='utf-8')
csvwriter = csv.writer(f)

result = obj.finditer(page_content)
for i in result:
    # print(i.group('title'), i.group('time').strip())
    dic = i.groupdict()
    dic['time'] = dic['time'].strip()
    csvwriter.writerow(dic.values())

f.close()
resp.close()
print('over!')

