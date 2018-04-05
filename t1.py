# print('hello world!')
input = open('data.txt','w')
D =dict(name='jiyu',age=24)
x=12
y='hai'
z=0.1111
input.write(str(D)+'\n')
input.write("%d \n%s \n%f \n" %(x,y,z))
input.close()

output =open('data.txt','r')
line=output.readline()
L=eval(line)
L['age']=25
L['name']='tangjiyu'
print L
parts=line.split(',')
print parts
# print("parts:")
# print parts
# print("output.readline()")
# print line
lines=output.readlines()
# print("output.readlines()")
# print lines
# for line in lines:
#     print line