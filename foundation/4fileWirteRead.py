#!/usr/bin/env python
# -*-coding:utf-8-*-

"""
@project: python_foundation
@version: 1.0
@site: https://github.com/Kyod/python_foundation
@software: PyCharm Community Edition
@file: 4fileWirteRead.py
@time: 2018/10/28 0:40
@author: Kyod
@description: 文件读写
"""

import os

fname = "test2.txt"
def createFile():
    '''创建一个文件'''
    ls = os.linesep
    print "文件全路径：", os.path.abspath(fname)
    if os.path.exists(fname):
        print "ERRO: '%s' already exists" % os.path.abspath(fname)

    '''获取文件内容'''
    all = []
    print "\nEnter lines ('.' by itself to quit).\n"
    while True:
        entry = raw_input('> ')
        if entry == '.':
            break
        else:
            all.append(entry)

    fobj = open(fname, 'w')
    fobj.writelines(['%s%s' % (x, ls) for x in all])
    fobj.close()
    print 'DONE!'

def readFile():
    try:
        fobj = open(fname, 'r')
    except IOError, e:
        print "ERRO: No such file or directory: %s" % os.path.abspath(fname)
    finally:
        for eachLine in fobj:
            print eachLine,  #一次性读入所有行，再一行一行输出（使用逗号“，”来抑制自动生成的换行符）
        fobj.close()

if __name__ == '__main__':
    # createFile()
    readFile()