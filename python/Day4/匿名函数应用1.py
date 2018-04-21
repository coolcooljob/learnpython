def test(a,b,func):
	res=func(a,b)
	return res
print(test(12,33,lambda x,y:x+y))
