names=['laowang','lisi','zhangsan']
stus={'name':'laowang'}
a='laogao'
def test1():
	print('原始的全局变量为%s'%names)
	names[2]='laoxiao'
	stus['age']=23
	#a='gobin'   #定义了一个局部变量
	global a
	a='gobin'   #修改全局变量
test1()
print('最后的全局变量为%s'%names)
print('最后的全局变量stus为%s'%stus)
print('最后的全局变量a为%s'%a)
