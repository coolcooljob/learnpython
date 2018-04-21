x=1

while x<=9:
	y=1
	while y<=x:
		print('%d*%d=%d\t'%(y,x,y*x),end='')
		y=y+1
	print('')
	x=x+1
	
print('打印完成')
