#try的嵌套
f=None
a='123'
try:
	f=open('test.txt','r')
	try:
		content=f.read()
		content.index('fdfg')
	except ValueError as ex:
		print(ex)
except FileNotFoundError as ex:
	print(ex)
else:
	print('好像没有什么异常哟！')
finally:
	print('不管怎样都会打印我的饿！接下来要关闭文件了哟！')
	if f:
		f.close()
