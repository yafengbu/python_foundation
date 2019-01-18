#!/usr/bin/env python
# -*-coding:utf-8-*-

"""
@project: python_foundation
@version: 1.0
@site: https://github.com/Kyod/python_foundation
@software: PyCharm Community Edition
@file: CommonVariable.py
@time: 2019/1/18 22:08
@author: Kyod
@description: 声明全局变量
"""

import XMLFile

ShellDir = None
gAppConfig = None
gLogger = None

def loadAppConfig():
    gAppConfig = XMLFile.CAppConfigFile()
