# coding=utf-8
# 赋值_表达式_打印
# 赋值:
# 1)赋值语句建立对象引用值
# 2)变量名在首次赋值时被创建
# 3)变量名在引用钱必须先赋值
# 4)隐式赋值语句
# 变量名命名规则
# 1\下划线或字母+任意字母数字或下划线 2\区分大小写 3\禁止使用保留字
#表达式
# 1\函数调用 2\方法调用 3\符合表达式 4\范围测试

spam = 'Spam'
spam += '42'
print spam
# 列表赋值
[name, age] = ['jiyu', 23]
# 元组赋值
name1, age1 = 'jiyu', 23
# 序列赋值
a, b, c, d = '1234'
str1 = str2 = 'hello'
# print name
# print a, b, c, d, str1, str2
# print str1 is str2  # true
str2 = 'new'
print str1, str2

L1 = L2 = []
L1.append('abc')
print L1,L2
# L1=L1+L2 与 L1+=L2运行后,L2的结果不同
L1 += L2
print 'L1:', L1, 'L2:', L2
L3 = L4 = []
L3.append('abc')
L3 = L3 + L4
print 'L3: %s ,L4 %s \n try try' % (L3, L4)
