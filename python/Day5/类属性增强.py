class User(object):
	name='Job'    #公共的类属性
	__passwd='1244325'   #私有的类属性
	def __init__(self,sex,username):
		self.sex=sex   #方法属性
		self.username=username

u1=User('男','Jack')
print(u1.name)
print(u1.username)

