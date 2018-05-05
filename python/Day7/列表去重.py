a=[1,3,5,3,7,2,1,3]
def change_list(li):
	temp=[]
	for i in li:
		if i not in temp:
			temp.append(i)
	return temp
print(change_list(a))
	
