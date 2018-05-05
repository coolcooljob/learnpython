class User:
	def __init__(self,pw):
		if  len(pw)>=6:
			self.__password=pw
		else:
			print('密码是：%s,密码不符合要求！'%pw)
	def __str__(self):
		return '密码是%s'%self.__password
	def get_password(self):
		return self.__password
u1=User('123')
print(u1.get_password())
print(u1)

