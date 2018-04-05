# coding=utf-8
# while

a = 1
b = 10
while a < b:
    print a,
    a += 1
    if a == 4:
        pass
    else:
        a += 1
else:
    print 'a=b,end!'

x = 10
while x:
    x -= 1
    if x % 2 != 0:
        continue
    print x,

print '\nEnter a num:'
line = raw_input()
try:
    y = int(line)
except:
    print 'not num!' * 8
else:
    x = y / 2
    found=False
    while x > 1:
        if y % x == 0:
            print y, 'has factor', x
            # break
            found=True
        x -= 1
    if not found:
        print y, 'is prime'
