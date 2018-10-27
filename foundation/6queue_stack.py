#!/usr/bin/env python
# -*-coding:utf-8-*-

"""
@project: python_foundation
@version: 1.0
@site: https://github.com/Kyod/python_foundation
@software: PyCharm Community Edition
@file: 6queue_stack.py
@time: 2018/10/28 2:14
@author: Kyod
@description: 用列表模拟队列/堆栈
"""

class QueueClass(object):
    '''
    用列表模拟队列
    '''
    queue = []

    def expendQ(self):
        self.queue.append(raw_input('Enter New string: ').strip())

    def removeQ(self):
        if len(self.queue) == 0:
            print 'Cannot pop from an empty queue!'
        else:
            print 'Remove [', self.queue.pop(0), ']'

    def viewQ(self):
        print self.queue  # calls str() internally

    CMDs = {'e': expendQ, 'd': removeQ, 'v': viewQ}

    def showmenu(self):
        pr = """
        (E)xpendQueue
        (R)emoveQueue
        (V)iewQueue
        (Q)uit
        Enter choice: """

        while True:
            while True:
                try:
                    choice = raw_input(pr).strip()[0].lower()
                except(EOFError, KeyboardInterrupt, IndexError):
                    choice = 'q'

                print '\nYou picked: [%s]'%choice
                if choice not in 'devq':
                    print 'Invalid option, try again'
                else:
                    break

            if choice == 'q':
                break
            self.CMDs[choice](self)

class StackClass(object):
    '''
    用列表模拟堆栈
    '''
    stack = []

    def pushit(self):
        self.stack.append(raw_input('Enter New string: ').strip())

    def popit(self):
        if len(self.stack) == 0:
            print 'Cannot pop from an empty stack!'
        else:
            print 'Remove [', self.stack.pop(), ']'

    def viewstack(self):
        print self.stack  # calls str() internally

    CMDs = {'u': pushit, 'o': popit, 'v': viewstack}

    def showmenu(self):
        pr = """
        P(U)sh
        P(O)p
        (V)iew
        (Q)uit
        Enter choice: """

        while True:
            while True:
                try:
                    choice = raw_input(pr).strip()[0].lower()
                except(EOFError, KeyboardInterrupt, IndexError):
                    choice = 'q'

                print '\nYou picked: [%s]'%choice
                if choice not in 'uovq':
                    print 'Invalid option, try again'
                else:
                    break

            if choice == 'q':
                break
            self.CMDs[choice](self)

if __name__ == '__main__':
    queue = QueueClass()
    queue.showmenu()
    # stack = StackClass()
    # stack.showmenu()