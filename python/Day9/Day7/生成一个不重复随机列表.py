import random
def create_list(n):
	temp=[]
	while True:
		if len(temp)==n:
			break
		i=random.randint(1,n)
		if i not in temp:
			temp.append(i)
	return temp
if __name__=='__main__':   #只有Python解释器主动调用时才执行下面的语句，若是被导入则不执行
	print(create_list(5))

