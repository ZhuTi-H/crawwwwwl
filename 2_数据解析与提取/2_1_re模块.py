# -*- coding: utf-8 -*-
"""
学了正则表达式后，利用re模块来进行操作实现功能
作者：高振涵
日期：2022-09-01
"""

import re

lst = re.findall(r'\d+', '我女朋友的电话号码是18081041112,我的电话号码是17701707838')

print(lst)

# ！！！！最重要的是finditer ！！！！
# finditer = 匹配字符串中所有的内容[返回的是迭代器]，需要调取迭代器中的内容需要用到.group()函数
it = re.finditer(r'\d+', '我女朋友的电话号码是18081041112,我的电话号码是17701707838')

print(it)

for i in it:
    print(i.group())

# search，找到一个结果就返回，返回的是match对象，拿数据需要用到.group()
s = re.search(r'\d+', '我女朋友的电话号码是18081041112,我的电话号码是17701707838')
print(s.group())

# match是相当于正则表达式前面增加一个^，从头开始找，第一个不是就pass
m = re.match(r'\d+', '我女朋友的电话号码是18081041112,我的电话号码是17701707838')
print(m)


# 由于爬网页的时候所需要的正则表达式可能很复杂，并且要调用很多遍，所以我们要对正则表达式进行预加载
# (?P<名字>正则)可以单独从正则的内容中提取倒想要的固定位置的信息
obj = re.compile(r"<div class='\w+'><span id = '\d+'>(?P<stars>.*?)</span></div>", re.S) # re.S: 让.能匹配换行符

s = '''
<div class='jay'><span id = '1'>周杰伦</span></div>
<div class='jj'><span id = '2'>林俊杰</span></div>
<div class='zz'><span id = '3'>猪猪</span></div>
<div class='bb'><span id = '4'>宝宝</span></div>
'''

result = obj.finditer(s)

for i in result:
    print(i.group('stars'))
