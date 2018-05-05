class Person(object):
	__slots__=('name','age')    #限制类的属性
	def __init__(self,name):
		self.name=name

p=Person('job')
print(p.name)
p.age=20
print(p.age)
p.sex='male'     #此属性不能成功的添加
print(p.sex)
