# -*- coding: utf-8 -*-
r"""
正则表达式的种类
     .  匹配除换行符以外的任意字符
    \w  匹配数字、字母、下划线            \W 匹配非数字、字母、下划线
    \s  匹配任意的空白符                 \S 匹配非空白符
    \d  匹配数字                        \D 匹配非数字
    \n  匹配换行符
    \t  匹配一个制表符

    ^   匹配字符串的开始
    $   匹配字符串的结束
    eg: re.findall('^\d\d\d$','123')        ['123']

    *     重复零次或者更多次
    +     重复一次或者更多次                 .*    贪婪匹配
    ?     重复零次或者一次                   .*?   惰性匹配
    {n}   重复n次
    {n,}  重复n次或者更多次
    {n,m} 重复n到m次

作者：高振涵
日期：2022-09-02
"""
