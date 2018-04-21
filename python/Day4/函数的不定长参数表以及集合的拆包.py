def test1(x,y,*args):
	print(x,y)
	print(args)
	sum=x+y
	for i in args:
		sum+=i
	print(sum)
test1(2,4,5,67)	
print('='*30)
def test2(x,y,*args,**kwargs):
	print(x,y)
	print(args)
	print(kwargs)
test2(1,2,456,67,m=2)
print('='*30)
#集合的拆包
nums=[1,2]
nums2={'sds':23,'wwsw':34}
test2(1,*nums,**nums2)
