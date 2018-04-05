#coding=utf-8
# 3. 编写一个函数，利用正则匹配，获取一个文件中双引号之间的内容
import re

pattern=re.compile("(\"[^\"]*\")")

f=open("data.txt")
result1=[]
result2=[]
for line in f:
    #一行中有一对双引号
    s=pattern.search(line)
    if s!=None:
        result1.append(s.group())
    #一行中有多对双引号
    s=pattern.findall(line)
    if s!=[]:
        result2.append(s)
print(result1)
print(result2)
f.close()


#双引号跨行
f=open("data.txt")
lines=f.readlines()
s=pattern.findall(''.join(lines))
print(s)
f.close()
