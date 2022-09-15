# -*- coding: utf-8 -*-
"""
xpath是在XML文档中搜索内容的一门语言
html是xml的一个子集
作者：高振涵
日期：2022-09-05
"""

import requests
from lxml import html
etree = html.etree

xml = """
        <div id="c_340041926" class="">牛羊等牲畜疑似受惊，差点闯出栅栏，牧民阻拦，大声喝斥着，平日间几头很凶的藏獒此时低伏在地，嘶吼着，很不安.</div>
"""
tree = etree.XML(xml)
result = tree.xpath('/div/text()')

print(result)

