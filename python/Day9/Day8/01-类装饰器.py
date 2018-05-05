class Call_sb(object):
	def __call__(self):     #使用__call__
		print('call me')


c=Call_sb()
c()       #生成一个类的实例，这个实例可以当做是一个函数来使用
