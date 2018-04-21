h=float(input('请输入身高：'))
w=float(input('请输入体重：'))
bmi=h/(w**2)
print('小明的身高为%2.f,体重为%2.f'%(h,w))

bmi=w/(h**2)
if bmi<18:
	print('过轻')
elif bmi>=18 and bmi<=23:
	print('正常')
else :
	print('过重')
print('小明的bmi为：%s'%bmi)
