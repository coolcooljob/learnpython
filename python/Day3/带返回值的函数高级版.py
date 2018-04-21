def sum_2num(a,b):
	if not isinstance(a,(int,float)):
		print('函数的a是%s,不是一个数字类型'%a)
		return
	elif not isinstance(b,(int,float)):
		print('函数的b是%s,不是一个数字类型'%b)
		return
	sum=a+b
	return sum  #return执行之后，不管return后面有什么代码，都不会执行
	print('反正不会打印我！')


s1=sum_2num('abc',2 )
print(s1)
s2=sum_2num(3,'asd' )
print(s2)
s3=sum_2num(3,5 )
print(s3)
