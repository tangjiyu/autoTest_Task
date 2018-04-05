# coding=utf-8
# if测试

# if/else表达式
A = 't' if 'spam' else 'f'
print A
B = ['false', 'true'][bool('t')]
print B
print 2 < 3, 3 > 2

#停在第一个真上
print 2 or 3, 3 or 2

#停在第一个假上
print 2 and 3,3 and 2
print [] and 3
