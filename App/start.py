#!/usr/bin/env python
# -*-coding:utf-8-*-

"""
@project: python_foundation
@version: 1.0
@site: https://github.com/Kyod/python_foundation
@software: PyCharm Community Edition
@file: start.py
@time: 2019/1/18 22:09
@author: Kyod
@description: 工程启动入口
"""

import sys
import os
import Common.CommonVariable

def setDefaultEncoding():
    reload(sys)
    sys.setdefaultencoding('utf-8')

def setCurrentDir():
    # 设置当前目录（根据Python的第一个参数，即为本文件）
    path = os.path.abspath(sys.argv[0])
    path = path[:path.rfind(os.path.sep)]
    os.chdir(path)
    # Common.CommonVariable.ShellDir = os.getcwd()

def loadAppConfig():
    Common.CommonVariable.loadAppConfig()

def main():
    # 1、设置字符集
    setDefaultEncoding()
    # 2、设置工程基本路径
    setCurrentDir()
    # 3、加载AppConfig.xml文件（全局配置文件）
    loadAppConfig()


if __name__ == '__main__':
    main()