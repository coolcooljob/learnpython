class User(object):
	__instance=None
	def __init__(self,name):
		self.name=name

	@classmethod
	def get_instance(cls,name):
		if not cls.__instance:
			cls.__instance=User(name)
		return cls.__instance

#u1=User('zs')
#u2=User('ls')
u1=User.get_instance('ls')
u2=User.get_instance('ww')
print(u1==u2)   #==判断表达式
print('u1对象的内存地址:%s,u2对象的内存地址：%s'%(id(u1),id(u2)))
