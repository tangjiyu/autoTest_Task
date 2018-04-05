# coding=utf-8
# 函数

# import  __builtin__
# print dir(__builtin__)

def times(x, y):
    return (y-1) * x

# print times(2,3)
# print times('Ni', 13)

def intersect(seq1,seq2):
    res =[]
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res
# print times(y=2,x=23)
# print intersect([1,2,3],(1,4))

def func(a,b,c,d):
    print a,b,c,d

args =(1,2)
args+=(3,4)
func(*args)

args={'a':1,'b':2,'c':3}
args['d']=4
func(*args)

def func1():
    x=4
    action=(lambda n: x**n)
    return action
x=func1()
print x(2)

def makeActions():
    acts =[]
    for i in range(5):
        acts.append(lambda x: i**x)
    return acts

acts=makeActions()

def f(*args):print args
f(1)
f(1,2,3,4)

def f(**args):print args
f(a=1,b=2)

def f(a,*pargs,**kargs):print a,pargs,kargs
f(1,2,3,x=1,y=2)

def minmax(test,*args):
    res=args[0]
    for arg in args[1:]:
        if test(arg,res):
            res=arg
    return res
def lessthan(x,y):return x<y
def morethan(x,y):return x>y

print minmax(lessthan,4,24,45,2,23,3)
print minmax(morethan,55,65,78,91,3,76)

#仅仅能处理两个子串的交集
# def intersect(*args):
#     res=[]
#     for x in args[0]:
#         if x in args[1]:
#             res.append(x)
#     return res

#能处理一个子串与多个子串的交集
def intersect(*args):
    res=[]
    for x in args[0]:
        for other in args[1:]:
            if x in other:
                res.append(x)
    return res

#可处理两个以上的子串的并集
def union(*args):
    res=[]
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
    return res


print intersect('spam','scam')
print union('spam','scam')

