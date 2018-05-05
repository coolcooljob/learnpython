#map
m=map(lambda x,y:x+y,[1,2,3],[4,5,6])
for i in m:
	print(i)
def func(x,y):
	return (x,y)
m1=map(func,[0,1,2],['a','b','c'])
for i in m1:
	print(i)
print('='*30)
#filter  过滤器
f=filter(lambda x:x%2,[1,2,3,4])
for i in f:
	print(i)
f1=filter(None,'hello')
for i in f1:
	print(i)
print('='*30)
#reduce  累积
from functools import reduce
r=reduce(lambda x,y:x+y,[1,2,3,4],5)
print(r)
r1=reduce(lambda x,y:x+y,['aa','bb','cc'],'dd')
print(r1)

