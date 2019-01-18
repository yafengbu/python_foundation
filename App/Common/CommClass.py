#!/usr/bin/env python
# -*-coding:utf-8-*-

"""
@project: python_foundation
@version: 1.0
@site: https://github.com/Kyod/python_foundation
@software: PyCharm Community Edition
@file: CommClass.py
@time: 2019/1/18 23:00
@author: Kyod
@description: 本文主要实现异常类
"""

import sys
import traceback
import string

class MyException(Exception):
    pass

class IgnoreException(Exception):
    def __init__(self, strTip):
        self.strTip = strTip

    def __str__(self):
        return self.strTip

class LogicException(Exception):
    def __init__(self, strErrorCode, strErrorMsg):
        self.strErrorCode = str(strErrorCode)
        self.strErrorMsg = strErrorMsg

    def __str__(self):
        return "(see FAQ %s, %s)"%(self.strErrorCode, self.strErrorMsg)

class RedefindException(Exception):
    def __init__(self, strErrorCode, strErrorMsg):
        self.strErrorCode = str(strErrorCode)
        self.strErrorMsg = strErrorMsg
        (etype, value, tb) = sys.exc_info()
        tblist = traceback.extract_tb(tb)
        self.strTracebackMsg = string.join(traceback.format_exception_only(etype, value)+traceback.format_list(tblist))

    def __str__(self):
        return "(see FAQ %s, %s)" % (self.strErrorCode, self.strErrorMsg)

    def tb(self):
        return self.strTracebackMsg

if __name__ == '__main__':
    pass