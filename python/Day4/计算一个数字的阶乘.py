'''i=1
res=1
n=4
while i<=n:
	res=res*i
	i+=1
print(res)'''

def  test1(n):
	if n==1:
		return 1
	else:
		return n*test1(n-1)
print(test1(16))
