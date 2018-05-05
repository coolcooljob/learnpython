class Test(object):
	def  __init__(self,func):
		print('--初始化--')
		self.func=func

	def __call__(self):
		print('装饰器中的功能')
		self.func()

@Test    #类装饰器,生成Test的一个对象，所以会调用__init__方法，并且会把下面所定义的函数当做参数传进去
def test():
	print('---test---')    #如果把这行注释，重新运行程序，依然会打印‘--初始化--’
	#pass


test()
