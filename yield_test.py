def fab(max):
    a,b=0,1
    while a<max:
        yield a
        a,b=b,a+b

for i in fab(20):
    print i,',',