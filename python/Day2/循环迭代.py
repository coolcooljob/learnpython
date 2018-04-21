names=['zs','ls','ww','sl']
names2=('zs','ls','ww','sl')
#第一种迭代
j=0
print('序号\t姓名')
for i in names:
	j+=1
	print('%d\t%s'%(j,i))
print('='*30)
#第二种
for i,item in enumerate(names,1):
	print('%d\t%s'%(i,item))

