#既有返回值又有不定参数的通用装饰器
def deco(func):
	def wrapper(*args,**kwargs):
		return 'hello world'
		ret=func()    #func()
		return ret
	return wrapper

@deco
def func1():
	print('hello job')
	
print(func1())
