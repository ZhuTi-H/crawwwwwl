# -*- coding: utf-8 -*-
"""
作者：高振涵
日期：2022-09-05
"""

from lxml import etree

tree = etree.parse('b.html')
# result = tree.xpath('/li/*/li[1]/a/text()')   # xpath从1开始数
# result = tree.xpath('/li//li/a[@href="zy/dzzy/dmtzy.htm"]/text()')
#
# print(result)

# li_list = tree.xpath('/li/ul/li')
#
# for li in li_list:
#     result = li.xpath('./a/text()')
#     print(result)
#     result2 = li.xpath('./a/@href')
#     print(result2)
#
# print(tree.xpath('/li/*/li/a/@href'))
print(tree.xpath('//*[@id="nav"]/div/div/ul/li[4]/ul/li[1]/ul/li[1]/a'))