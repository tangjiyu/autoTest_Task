# coding=utf-8
# 元组

t1 = (0,)
t2 = (0, 'Ni', 1.2, 3)
t3 = ('abc', ('def', 'ghi'))
print t1[0]
print t3[1][1]
print t2[1:]
t4 = t2 + t3
print t4
print 'def' in t3[1]  # true

T = ('cc', 'aa', 'bb', 'dd')
# 元组-->列表
tmp = list(T)
tmp.sort()
print tmp
# 列表-->元组
T = tuple(tmp)
print T
