#第一种生成器,利用类似列表生成式的方式,也可以利用for循环来输出
'''g=(x for x in range(4))
for i in g:
	print(i)'''
#第二种，利用函数
def fib(times):
	n=0
	a,b=0,1
	while n<times:
		yield b    #print(b),函数已经变成一个生成器，要想调用必须用next(),或者搭配for循环
		a,b=b,a+b
		n+=1
	return 'done'
g=fib(5)
next(g)
for x in g:	
	print(x)
