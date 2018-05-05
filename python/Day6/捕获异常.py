a='1234'
try:
	f=open('text.txt','r')
	f.write('hello\n')
	f.write('world %d'%a)
except Exception as ex:
	print(ex)
else:
	print('没有任何的异常！')
finally:
	print('不管怎样都会打印我的！完了之后必须关闭文件1')
