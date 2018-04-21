def get_num(n):#获取斐波那契数列中底n个数的值
	if n==1 or n==2:
		return 1
	return get_num(n-1)+get_num(n-2)
nums=[]
for i in range(1,20): #将获取的数字存放在一个列表中
	nums.append(get_num(i))
print(nums)

	
	
