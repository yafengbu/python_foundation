#!/usr/bin/env python
# -*-coding:utf-8-*-

"""
@project: python_foundation
@version: 1.0
@site: https://github.com/Kyod/python_foundation
@software: PyCharm Community Edition
@file: 7keyLengthCheck.py
@time: 2018/10/28 2:33
@author: Kyod
@description: 标识符检查（长度 >= 2）
"""

import string

alphas = string.letters + '_'
nums = string.digits
print alphas, nums

myInput = raw_input('Idendifier to test ? ')

if len(myInput) >= 2:
    if myInput[0] not in alphas:
        print 'invalid: first symbol mut be alphabetic.'
    else:
        for otherChar in myInput[1:]:
            if otherChar not in alphas + nums:
                print 'invalid: remaining symbol mut be alphabetic.'
                break
        else:
             print 'okay!'
else:
    print 'invalid: length of Identifier mut be >= 2.'