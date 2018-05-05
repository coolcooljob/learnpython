#装饰器例子
def makeBold(func):   #写一个加粗的装饰器
	def wrapper():
		return '<b>'+func()+'</b>'
	return wrapper

def makeItalic(func):   #写一个加上斜体的装饰器
	def wrapper():
		return '<i>'+func()+'</i>'
	return wrapper

@makeBold
def func1():
	return 'hello world-1'

@makeItalic
def func2():
	return 'hello world-2'

@makeBold
@makeItalic
def func3():
	return 'hello world-3'

print(func1())
print(func2())
print(func3())
