class Person(object):
	def __init__(self,name,age):
		self.name=name
		self.age=age



p=Person('job',21)
@classmethod     #为类添加类方法
def func1(cls):
	print('classMethod')
Person.func1=func1      #直接通过类去添加类方法
p.func1()               #发现可以成功的调用类方法

@staticmethod
def func2():
	print('staticMethod')
Person.func2=func2        #和添加类方法一样，静态方法也可以直接类来直接添加
p.func2()                #也可以直接调用
