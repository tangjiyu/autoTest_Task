#coding=utf-8
# 5. 输出字典结构数据，例如 a = {'1':{'2':{'3':xxx}}}中所有的节点路径，例如1.2.3.xxx

a = {
     '1':{'2':{'3':'aaa'}},
     '4':{'5':[1,2,3]}
     }
b = {'1':{'2':{'3':('b1','b2','b3')}}}

def viewKeys(dic):
    if isinstance(dic,dict):
        for key in dic.keys():
            print(key+'.'),
            viewKeys(dic[key])
    else:
        print(dic)

viewKeys(a)
viewKeys(b)