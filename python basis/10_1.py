# coding=utf-8
# 基本语句
# 初学者常常犯错是忘记冒号
# 相对于C,Python省略了分号,圆括号,大括号
x=10;y=2

if x>y:
    print 'x>y',True
else:
    print 'x>y',False

# while True:
#     reply = raw_input('Enter text:')
#     if reply == 'stop':
#         break
#     print reply.upper()
#     if reply.isdigit():
#         print reply,'^2=',int(reply)**2
#     try:
#         num = int(reply)
#     except:
#         print 'not num!'*8
#     else:
#         print int(reply)**2
# print 'byebye'

while True:
    reply = raw_input('Enter text:')
    # print(type(reply))
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print 'not num!'*8
    else:
        num = int(reply)
        if num <20:
            print 'low'
        else:
            print num**2
print 'byebye'