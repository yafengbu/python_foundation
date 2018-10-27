#!/usr/bin/env python
# encoding: utf-8

"""
@project: python_foundation
@version: 1.0
@site: https://github.com/Kyod/python_foundation
@software: PyCharm Community Edition
@file: .py
@time: 2018/10/27 20:06
@author: dell
"""

def func():
    print "I am in func."
    pass

class Main():
    def __init__(self):
        print "I am in Main.__init__."

    def funcInMain(self):
        print "I am in Main.funcInMain."

if __name__ == '__main__':
    print "======================="
    print "Hello World."
    print "======================="
    func()
    print "======================="
    mainInstance = Main()
    mainInstance.funcInMain()
    print "======================="