age=int(input('请输入你的年龄：'))
i=1
while i<=100:
	if i==age:
		print('你的年龄为%d!'%i)
		break
	else:
		print('猜错了！')
		i+=1
