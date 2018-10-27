#!/usr/bin/env python
# -*-coding:utf-8-*-

"""
@project: python_foundation
@version: 1.0
@site: https://github.com/Kyod/python_foundation
@software: PyCharm Community Edition
@file: 5moduleFoundation.py
@time: 2018/10/28 1:17
@author: Kyod
@description: 本文件用于。。。
"""

import types
from decimal import Decimal
from string import Template

def func():
    lista = [1, 'python', 4]
    # print id(lista) # id() 函数用于获取对象的内存地址。
    # print cmp('abc', 'aaxyz') # >> 1
    # print type({}).__name__ # >> dict
    # a = 2
    # print isinstance(a, int) # isinstance()判断一个对象是否是一个已知的类型 >> True
    # print isinstance(a, str) # >> False
    # print isinstance(a, (str, int, list))  # 是元组中的一个返回 True
    # print types.IntType
    # print "=============================="
    # a = 10
    # b = 10
    # print (a is b)
    # print '================================'
    # print 2e3
    # print 2e-3
    # a = 2.34 + 5j
    # print a
    # print a.real
    # print a.imag
    # print a.conjugate() # #求取共轭复数
    # print '================================'
    # print 1.0 / 2.0
    # print 1.0 // 2.0

    # print '================================'
    # dec = Decimal('.1')
    # print dec
    # print dec + Decimal('1.0')
    # print type(dec)
    # print 'A'

    # print '==========================='
    count = raw_input('Enter your count:')
    count = int(count)
    if count >= 80:
        print 'A'
    elif count >= 60:
        print 'B'
    elif count >= 30:
        print 'C'
    else:
        print 'D'

def func2():
    # string = "abc"
    # string2 = "---".join(string)
    # print string2 # >> a---b---c

    lista = [1, 2, 3]
    # listb = ['abc', 'def', 'xyz']
    # listb.extend(lista)
    # print listb # >> ['abc', 'def', 'xyz', 1, 2, 3]

    # print '=================='
    # s = 'abcde'
    # for i in [None] + range(-1, -len(s), -1):
    #     print i, '========', s[:i]

    print '================================='
    print enumerate(lista)
    print type(enumerate(lista))
    for key,val in enumerate(lista):
        print key, ':', val

def func3():
    s = Template('There are ${howmany} ${lang} Quotation Symbols.')
    print s.substitute(lang='Python', howmany='3')
    # print s.substitute(lang = 'Python')
    # print s.safe_substitute(lang='Python')

    str1 = 'abc'
    str2 = 'lmn'
    str3 = 'xyz'
    print cmp(str1, str2)
    print max(str2, str1)
    print '=============================='
    s = 'bar'
    print type(enumerate(s))
    for i, t in enumerate(s):
        print i, t
    s1, s2 = 'foo', 'bar'
    print type(zip(s1, s2)) # >> <type 'list'>
    print zip(s1, s2) # >> [('f', 'b'), ('o', 'a'), ('o', 'r')]
    print basestring

    print '===================='
    hi = '''hi
    there'''
    print hi

if __name__ == '__main__':
    # func()
    # func2()
    func3()