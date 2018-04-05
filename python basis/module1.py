import fileinput

for line in fileinput.input(inplace='True'):
    num=fileinput.filelineno()
    print "%-20s #%2d" %(line,num)
