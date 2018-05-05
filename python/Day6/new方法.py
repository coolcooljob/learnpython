class User(object):
	def __init__(self,username,password):
		self.username=username
		self.password=password
		print('对象已经构建好了！')

	#new方法是当对象构建的时候由解释器自动回调,该方法必须返回当前类的对象
	def __new__(cls,username,password):
		print('user类开始构建！')
		return object.__new__(cls)

	def __str__(self):
		return '用户名：%s,密码：%s'%(self.username,self.password)

u=User('zs','12343')
print(u)
		
		
