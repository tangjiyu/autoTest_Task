# coding=utf-8
# 字典

D1 = {}
D2 = {'spam': 2, 'eggs': 3}
D3 = {'food': {'ham': 1, 'eggs': 2}}
print D2.get('spam')
print D2.get('space','none')
print D3['food']['ham']
print "D2.has_key('eggs'):", D2.has_key('eggs')
print D2.keys()
print D2.values()
print D2.items()
D4 = D2.copy()
# print '****'*20
# print D4
# print D2==D4
# print D2 is D4
# print D2.get('spam')
D2.update(D3)
D2.pop('eggs')
D2['spam']=44
D2['apple']=6
# print D2,len(D2)

D4=dict.fromkeys(['a1','b2'])
keylist=['a','b','c']
valslist=[1,2,3]
print(zip(keylist,valslist))
D5=dict(zip(keylist,valslist))
D6=dict(name='BOb',age=42)
print D4,D5,D6

dt=dict(zip(['a','b','c'],[1,2,3]))
dt=dict(zip(sorted(dt.keys()),[dt[x]+1 for x in sorted(dt.keys())]))
print dt