#!/usr/bin/env python
# -*-coding:utf-8-*-

"""
@project: python_foundation
@version: 1.0
@site: https://github.com/Kyod/python_foundation
@software: PyCharm Community Edition
@file: 3oop.py
@time: 2018/10/28 0:27
@author: Kyod
@description: 面向对象基础学习
"""

class FooClass(object):
    '''my first class'''
    version = "1.0"

    def __init__(self, name = 'John'):
        self.name = name
        print '__init__方法：', 'created a class for', self.name

    def showName(self):
        '''display instance attribute and class name'''
        print 'showName方法：', 'Instance name is', self.name  # 调用默认参数
        print 'showName方法：', 'Class name is', self.__class__.__name__  # 打印类名

    def shower(self):
        '''display class(static) attibute'''
        print 'shower方法：', self.version
    def addMe2Me(self, x):
        '''applay + operation to argument'''
        return x + x

if __name__ == '__main__':
    fool = FooClass()
    fool.showName()
    fool.shower()
    print 'addMe2Me方法：', fool.addMe2Me(5)
    print 'addMe2Me方法：', fool.addMe2Me('xyz')
    print '==================================='
    foo2 = FooClass('Kyod')
    foo2.showName()