class School(object):
	def __init__(self,subject1):
		self.subject1=subject1
		self.subject2='cpp'
    
    #重写__getattribute__属性拦截访问器
	def __getattribute__(self,obj):
		if obj=='subject1':
			return 'redirect python'
		else:
			return object.__getattribute__(self,obj)

s=School('python')
print(s.subject1)
print(s.subject2)
