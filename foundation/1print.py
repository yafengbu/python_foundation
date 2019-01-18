#!/usr/bin/env python
# -*-coding:utf-8-*-

"""
@project: python_foundation
@version: 1.0
@site: https://github.com/Kyod/python_foundation
@software: PyCharm Community Edition
@file: 1print.py
@time: 2018/10/27 20:48
@author: Kyod
@description: print语句的学习
"""
import sys
import os

def func():
    str1 = u'小明,'
    str2 = 'welcome to you.'
    print str1, str2
    print "%s is number %d." % (str2, 1)

    for i in range(10, 101, 20):
        print i

def func2():
    user = raw_input('Enter your name:')
    print 'welcome to you,', user
    count = raw_input('Enter your number:')
    print 'Double your number is: %d.' % (int(count) * 2)

def fuc3():
    # 重定向输出   到标准错误输出
    print >> sys.stderr, 'Fatal error:invalid input'

def func4():
    # 重定向输出   到自定义文件
    '''
    'a' 模式：打开一个文件用于追加。
    如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    '''
    # outFile = open('D:\\workspace-python\\testPython\\src\\studyFirst\\temp\\test.txt', 'a')
    # outFile = open('D:/pythonProgram/python_foundation/foundation/test.txt', 'a')
    currentPath = os.getcwd()
    outFileName = "test.txt"
    outFilePath = os.path.join(currentPath, outFileName)
    try:
        outFile = open(outFilePath, 'a')
        print >> outFile, 'Fatal error:invalid input'
    except IOError, e:
        print 'file open erro:', e
    finally:
        outFile.close()

if __name__ == '__main__':
    func()
    # print '==========================='
    # func2()
    # print '=' * 27
    # fuc3()
    # func4()
