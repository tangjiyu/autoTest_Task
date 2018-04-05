# coding=utf-8
# for循环

sum = 0
for x in range(10):
    sum += x
print sum

prod = 1
for item in [1, 2, 3, 4, 5]:
    prod *= item
print prod

S = 'abcdefghijk'
for x in S:
    print x,
print ''

T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:
    print '%d + %d = %d' % (a, b, a + b)

items = ['aaa', 111, (4, 5), 2.34]
keys = [(4, 5), 3.14]
for key in keys:
    if key in items:
        print key, 'was found'
    else:
        print key, 'not found'
# 两个字符串的交集
str1 = 'asdfghjkl'
str2 = 'fghjksop'
res = []
for x in str1:
    if x in str2:
        res.append(x)
print res

# 读取字典
D = {'a': 1, 'b': 2, 'c': 3}
for key in D.keys():
    print key, D[key]

# 并行遍历zip()
L1 = [1, 3, 5, 7, 9]
L2 = [2, 4, 6, 8, 0]
for (x, y) in zip(L1, L2):
    print x, y,
print ' '

D1 = {}
keys = ['a', 'b', 'c']
values = [1, 2, 3]
D1 = zip(keys, values)
print D1

log = open('log.txt', 'w')
print>> log, 'print sys.path'
print>> log, 'saglfuiguigv'
print>> log, 'print 2**3'
log.close()

lines = [line.rstrip() for line in open('log.txt') if line[0] == 'p']
print lines

print [x + y for x in 'abc' for y in 'lmn']
