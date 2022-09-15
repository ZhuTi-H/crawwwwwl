# -*- coding: utf-8 -*-
"""
作者：高振涵
日期：2022-09-01
"""

import requests
import re

url = 'https://movie.douban.com/j/chart/top_list'

# 重新封装参数

param = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': '0',
    'limit': '20'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
}

resp = requests.get(url=url, params=param, headers=headers)

with open  ('rating.txt' , mode='w', encoding='utf-8') as fin:
    fin.write(resp.text)

# s = """
# 'rating': ['9.6', '50'], 'rank': 1
# """
#
# obj = re.compile(r"'rating': ['9.6', '50']", re.S)
#
# result = obj.finditers(s)
#
# for i in result:
#     print(i)

# print(s)
print(resp.json())

resp.close()
# 爬虫不好使的时候，怀疑是被反爬了
# 此时怀疑第一个原因就是user-agent
# 那么就去找headers，发现自己是python-requests
