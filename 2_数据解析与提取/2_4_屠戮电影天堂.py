# -*- coding: utf-8 -*-
"""
1.定位到你想要爬的板块
2.从板块中提取到你想要的子页面的链接地址
3.请求子页面的链接地址，拿到想要的下载地址
作者：高振涵
日期：2022-09-03
"""

import requests
import re

demain = 'https://dy.dytt8.net/index2.htm'
demain2 = 'https://dy.dytt8.net/'
resp = requests.get(demain)  # verify=False即是去除安全验证，会得到warning
resp.encoding = 'gb2312'  # 指定字符集
# print(resp.text)

obj1 = re.compile(r'2022新片精品.*?</tr>(?P<content>.*?)</table>', re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'>2", re.S)
obj3 = re.compile(r'◎译　　名(?P<name>.*?)<br />.*?<br /><br /><br /><a target="_blank" '
                  r'href="(?P<download>.*?)"><strong>', re.S)
result1 = obj1.finditer(resp.text)
final_href_list = []
for it in result1:
    content = it.group('content')
    # print(content)

# 提取子页面链接的方案
result2 = obj2.finditer(content)
for itt in result2:
    final_href = demain2 + itt.group('href').strip('/')
    # print(final_href)

# 提取子页面内容
    final_href_list.append(final_href)
txt_file = open('my movie.txt', 'a', encoding='utf-8')
for href in final_href_list:
    final_resp = requests.get(href)
    final_resp.encoding = 'gb2312'
    # print(final_resp.text)
    # break
    result3 = obj3.search(final_resp.text)
    # print(result3.group('name'), result3.group('download'))
    txt_file.write(result3.group('name'))
    txt_file.write('\n')
    txt_file.write(result3.group('download'))
    txt_file.write('\n')
print('over!')
resp.close()





