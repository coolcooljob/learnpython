class A(object):
	name='zs'

	def test1(self):
		print('-------A---test1')

	@classmethod    #类方法一定要在方法的上面加一个修饰器，类方法的参数cls,代表当前的类
	def test2(cls):
		print('------A----test2')

	@staticmethod   #静态方法，属于类，没有默认传递的参数，可以通过类对象来调用，也可以通过类名来调用
	def test3():
		A.name='job'  #更改类属性name，用类来直接访问
		print('------A的test3静态方法')
a=A()
a.test2()   #对象和类都可以访问类方法
A.test2()
a.test3()
print(A.name)
