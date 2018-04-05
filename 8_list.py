# coding=utf-8
# 列表

L1 = []
L2 = [0, 1, 2, 3]
L3 = ['adb', ['def', 'ghi']]
i = 1
j = 0
print L2[i]
print L3[i][j]
print L2[1:3]
print len(L3)

L1 = L1 + L2
print L1
print L1 * 3

L4 = [x + 10 for x in L2]
print L4
L2.append(4)
L2.extend([5, 6, 7])
L2.index(1)
L2.insert(1, 8)
L2.reverse()
L2.sort()
# 删除最后一个,必须用del或pop,remove(end)会报错
del L2[6:8]
L2.pop()
L2.remove(2)
L2[2] = 2
L2[3:6] = [3, 4, 5, 6]
L2[7:9] = range(3)
L2[10:15] = xrange(10, 15)
print L2

L5=[x**2 for x in range(10)]
print L5
L5[6:]=[]
print L5

