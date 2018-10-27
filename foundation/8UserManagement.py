#!/usr/bin/env python
# -*-coding:utf-8-*-

"""
@project: python_foundation
@version: 1.0
@site: https://github.com/Kyod/python_foundation
@software: PyCharm Community Edition
@file: 8UserManagement.py
@time: 2018/10/28 2:40
@author: Kyod
@description: 登录系统的用户管理
"""

class UserManagement(object):
    '''
    登录系统的用户管理
    '''
    def __init__(self):
        self.db = {}
        self.flag = True

    def newUser(self):
        prompt = 'login desired: '
        while self.flag:
            name = raw_input(prompt)
            if self.db.has_key(name):
                prompt = 'name taken, try another: '
                continue

            pwd = raw_input('passwd: ')
            self.db[name] = pwd
            print "You are sign up successed."
            self.flag = False

    def oldUser(self):
        name = raw_input('login: ')
        pwd = raw_input('passwd: ')
        passwd = self.db.get(name)
        if passwd == pwd:
            print 'welcome back', name
        else:
            print 'login incorrect'

    def showmenu(self):
        prompt = """
        (N)ew User Login
        (E)xisting User Login
        (Q)uit
        Enter choice: """

        done = False
        while not done:
            chosen = False
            while not chosen:
                try:
                    choice = raw_input(prompt).strip()[0].lower()
                except(EOFError, KeyboardInterrupt):
                    choice = 'q'
                print '\nYou picked: [%s]'%choice
                if choice not in 'neq':
                    print 'Invalid option, try again'
                else:
                    chosen = True

            if choice == 'q':
                done = True
            if choice == 'n':
                self.newUser()
            if choice == 'e':
                self.oldUser()

if __name__ == '__main__':
    inst = UserManagement()
    inst.showmenu()