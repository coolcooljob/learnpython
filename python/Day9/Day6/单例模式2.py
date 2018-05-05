class User(object):
	__instance=None
	def __init__(self,name):
		self.name=name

	def __new__(cls,name):
		if not cls.__instance:   #保证object.__new__(cls)方法只会调用一次
			cls.__instance=object.__new__(cls)   #单例模式2
		return cls.__instance

u1=User('job')
u2=User('jack')
print(u1==u2)
print('u1的内存地址:%s,u2的内存地址:%s'%(id(u1),id(u2)))

