def sum_2num(a,b):
	sum=a+b
	return sum  #return执行之后，不管return后面有什么代码，都不会执行
def sum_2nonenum(a,b):
	sum=a+b
num1=2
num2=3
s=sum_2num(num1,num2)
s2=sum_2nonenum(num1,num2)
print(s)
