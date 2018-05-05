import functools
def note(func):   #写一个装饰器
	@functools.wraps(func)   #利用functool.wraps(func)消除装饰器的副作用
	def inner():
		'inner'   #说明文档，后面调用__doc__时会打印
		print('note---inner')
		return func()
	return inner

@note
def fun():
	'fun'
	print('I am fun')


fun()                #调用已经装饰好的函数
print(fun.__doc__)   #打印说明文档,未消除之前是inner,消除影响之后是原来的说明文档fun
print(fun)
