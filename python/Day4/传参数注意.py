def test1(x,y):
	x=x.replace('c','C')  #x.replace只是将变量改变了，但是在内存中并没有一个元素指向它，也就是说并没有一个元素去接收它。
	y.append(10)
	return x,y
a='asejc'
b=[1,345,3]
m=test1(a,b)
print(m)
