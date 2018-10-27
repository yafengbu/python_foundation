#!/usr/bin/env python
# -*-coding:utf-8-*-

"""
@project: python_foundation
@version: 1.0
@site: https://github.com/Kyod/python_foundation
@software: PyCharm Community Edition
@file: 2list_dict.py
@time: 2018/10/27 22:05
@author: dell
@description: 基础类型学习（String、Number、List、Tuple、Dict）
"""

def func_string():
    str1 = "abcdefg"
    print str1
    print str1[1:3]
    floatStr = "32.123456789"
    print float(floatStr), int("32")
    print float('%0.3f' % 32.123456789) #32.123
    print "%0.3e"%0.123456789 #1.235e-01

def func_number():
    print "=======十进制转换为其他进制========"
    x = "16"
    print "转换为十进制:", int(x)
    print "十进制转换为二进制:", bin(int(x))
    print "十进制转换为二进制：", DecToBin(int(x))
    print "十进制转换为八进制:", oct(int(x))
    print "十进制转换为十六进制:", hex(int(x))

    print "=======其他进制转换为十进制========"
    xStr = "101"
    print "二进制转换为十进制：", int(xStr, base=2)
    print "八进制转换为十进制：", int(xStr, base=8)
    print "十六进制转换为十进制：", int(xStr, base=16)
def DecToBin(num):
    '''
    十进制转换为二进制   具体实现：
    # /(传统除法)    //(浮点除法，结果四舍五入)
    '''
    result = ''
    if num:
        result = DecToBin(num // 2)
        return result + str(num % 2)
    else:
        return result

def func_list():
    aList = [1, 2, "a", "b", "cdef"]
    print aList

    print '=============列表遍历====================='
    print '第一种遍历:'
    for i in aList:
        print i

    print '第二种遍历:根据索引遍历'
    for i in range(len(aList)):
        print i, ':', aList[i]

    print '第三种遍历:枚举'
    for key,val in enumerate(aList):
        print key, ':', val

    print '第四种遍历：迭代器'
    for i in iter(aList):
        print i

    print '=============列表解析====================='
    squared = [x ** 2 for x in range(4)]
    for i in squared:
        print i

def func_tuple():
    aTuple = ('robots', 77, 90, 'try')
    print "aTuple = ", aTuple
    bTuple = (("apple", "banana"), ("grape", "orange"), ("watermelon",), ("grapefruit",))
    print "bTuple = ", bTuple

    print '=============元组遍历====================='
    print '第一种遍历:'
    for i in aTuple:
        print i

    print '第二种遍历：根据索引遍历'
    for i in range(len(bTuple)):
        for j in range(len(bTuple[i])):
            print "bTuple[%d][%d] ="%(i,j), bTuple[i][j]

    print '第三种遍历：map()遍历'
    k = 0
    for a in map(ret, bTuple):
        j = 0
        for x in a:
            print "tuple[%d][%d] =" % (k, j), x
            j += 1
        k+=1
def ret(x):
    return x

def func_dict():
    print '=============字典赋值====================='
    aDict = {'host': 'earth'}
    aDict['port'] = 8080
    print "aDict = ", aDict
    bDict = {"a": "apple", "b": "banana", "o": "orange"}
    print "bDict = ", bDict.keys()

    print '=============字典遍历====================='
    print '第一种遍历:'
    for key in bDict:
        print key, bDict[key]

    print '第二种遍历:'
    for k, v in bDict.items():
        print k, v

    print '第三种遍历:iteritems()返回值不是列表，而是一个迭代器'
    for k, v in dict.iteritems(bDict):
        print k, v

    print '第四种遍历：zip() 返回的是一个对象'
    for k, v in zip(bDict.keys(), bDict.values()):
        print k, v

if __name__ == '__main__':
    # func_string()
    func_number()
    # func_list()
    # func_tuple()
    # func_dict()
    print '==============range()经常和len()一起用于字符串索引================'
    foo = 'abcd'
    for i in range(len(foo)):
        print foo[i], '(%d)' % i
