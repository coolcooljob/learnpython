def avg_3num(a,b,c):
	if is_number(a) and is_number(b) and is_number(c):
		return (a+b+c)/3
	else:
		print('不好意思！您输入的数据类型有误！')
def is_number(a):
	if not isinstance(a,(int,float)):
		return False
	else:
		return True
s=avg_3num(2,4,6)
print(s)
s1=avg_3num(2,46,'adf')
print(s1)
s2=avg_3num(2,'scdsdgfgdggh',6)
print(s2)
