#自定义一个密码长度不够的异常
class PasswordException(Exception):
	def __init__(self,pw,min_length):
		self.password=pw
		self.min_length=min_length
	def __str__(self):
		return '%s的密码错误，密码的最小长度是%s'%(self.password,self.min_length)

def reg(username,password):
	if len(password) < 6:
		raise PasswordException(password,6)
	else:
		print('用户名为：%s,密码为:%s'%(username,password))

try:
	reg('job','12345')
except Exception as ex:
	print(ex)

