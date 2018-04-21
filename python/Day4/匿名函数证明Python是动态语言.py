def test1(a,b,func):
	res=func(a,b)
	return res
func_new=input('请输入你的操作：')
func_new=eval(func_new)  #将字符串转换成为表达式
print(test1(22,44,func_new))

