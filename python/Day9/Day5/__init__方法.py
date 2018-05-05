class Person:
#初始化方法，并不是构造一个行的对象
	def __init__(self,name,age,height):
		self.name=name
		self.age=age
		self.height=height
		print('初始化！')
#将对象转换成一个字符串的方法，默认调用
	def __str__(self):
		return '姓名：%s,年龄：%s,身高: %s'%(self.name,self.age,self.height)
	def introduce(self):
		print('姓名：%s,年龄：%s,身高：%s'%(self.name,self.age,self.height))

p1=Person('job','21','176')
p1.introduce()
print(p1)
