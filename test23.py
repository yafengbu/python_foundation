#!/usr/bin/env python
# -*-coding:utf-8-*-

from datetime import datetime, tzinfo,timedelta

"""
tzinfo是关于时区信息的类
tzinfo是一个抽象类，所以不能直接被实例化
"""
class UTC(tzinfo):
    """UTC"""
    def __init__(self,offset = 0):
        self._offset = offset

    def utcoffset(self, dt):
        return timedelta(hours=self._offset)

    def tzname(self, dt):
        return "UTC +%s" % self._offset

    def dst(self, dt):
        return timedelta(hours=self._offset)

#北京时间
# beijing = datetime(2011,11,11,0,0,0,tzinfo = UTC(8))
beijing = datetime.now(tz=UTC(8))

#曼谷时间
# bangkok = datetime(2011,11,11,0,0,0,tzinfo = UTC(7))
bangkok = datetime.now(tz=UTC(7))

#北京时间转成曼谷时间
beijing.astimezone(UTC(7))
#计算时间差时也会考虑时区的问题
timespan = beijing - bangkok

import collections
cnt = collections.Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print cnt

import pickle
import json

d = [1, 2, 3, 4]
print(pickle.dumps(d))
print(type(pickle.dumps(d)))

print(json.dumps(d))
print(type(json.dumps(d)))