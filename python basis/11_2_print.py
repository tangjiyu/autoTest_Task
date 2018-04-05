# coding=utf-8
# 赋值_表达式_打印
#print
import sys
greeting='hello world'
sys.stdout.write(greeting+'\n')
print greeting
print type(greeting)

temp =sys.stdout
sys.stdout = open('log.txt','w')
print 'spam,stdout=temp'
print 1,2,3
print '**'*20
sys.stdout.close()
sys.stdout =temp
print 'back here'

# #下面部分等同于上面对sys.stdout重定向
# log = open('log.txt','w')
# print >>log,'spam>>out'
# print >>log,1,2,3
# print >>log,'**'*20
# log.close()

# print open('log.txt').read()
# print >>sys.stderr,'Bad!'*8

#一次性读取文件全部内容
print("一次性读取文件全部内容:")
for line in open('log.txt').readlines():
    print line.upper()
#逐行读取, 读取大文件性能更好
print("逐行读取, 读取大文件性能更好")
f=open('log.txt')
while True:
    line =f.readline()
    if not line:
        break
    print line.upper()

# 跨行字符串,三重引号
'''
L=[4,5,6]
X=L*4
Y=[L]*4 # 4处对原L的引用!!!
print X
print Y
L[1]=0
print Y
'''