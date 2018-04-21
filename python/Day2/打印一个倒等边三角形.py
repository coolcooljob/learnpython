i=int(input('请输入等边三角形的行数：'))
a=0
while a<i:   #打印行
	b=0
	while b<a:   #打印当前行的空格，第一行不打印空格，第二行打印一个空格...
		print(' ',end='')  
		b+=1
	c=i-a    #打印当前行的*
	while c>0:
		print('*',end=' ')
		c-=1
	print('')
	a+=1
