money=int(input('请输入您的余额:'))
seat=int(input('经查询，座位还有:'))
if money>=2:
	print('可以上车了！')
	if seat>0:
		print('有座位，可以坐下了!')
	else:
		print('不好意思，没座位了！')
else:
	print('不好意思，您的余额不足，没法买票！')
