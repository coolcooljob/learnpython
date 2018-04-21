print('='*50)
print('学生管理系统'.center(40))
print('输入1，表示添加学生')
print('输入2，表示删除学生')
print('输入3，表示修改学生')
print('输入4，表示查询学生')
print('输入5，表示退出')
print('输入6，表示查看所有学生')
#一个学生包含很多信息，一个学生一个字典，学生列表用列表来存储

stus=[]
while True:
	operate=input('请输入你想要的操作：')
	if operate=='1':
		name=input('请输入你要添加的学生姓名：')
		age=input('请输入你要添加的学生年龄：')
		qq=input('请输入你要添加的学生qq号：')
		#一个学生包括三个信息，存到字典中
		stu={}
		stu['name']=name
		stu['age']=age
		stu['qq']=qq
		stus.append(stu)
		print('添加成功！')		
	elif operate=='2':
		name=input('请输入你要删除的学生姓名：')
		if name not in stus:
			print('抱歉！可能没有这个学生%s！检查一下是不是输错了！'%name)
			continue
		else:
			stus.remove(name)
			print(stus)
			print('成功删除学生%s'%name)
	elif operate=='3':
		name=input('请输入您要修改的学生姓名：')
		if name in stus:
			name_now=input('请输入您修改后的学生姓名：')
			stus.pop()
			stus.append(name_now.strip())
			print(stus)
			print('已经成功修改此学生姓名！')
		else:
			print('不好意思！您所要修改的学生不存在！')		
	elif operate=='4':
		name=input('请输入你要查询的学生姓名：')
		for item in stus:
			if item['name']==name.strip():
				print('%s学生存在，年龄为%s,QQ号为%s'%(item['name'],item['age'],item['qq']))
				break
		else:
			print('不好意思！没有找到你要查询的学生姓名！')
	elif operate=='5':
		break
	else:
		print('序号\t姓名\t年龄\tQQ号')
		for i,item in enumerate(stus,1):
			print('%s\t%s\t%s\t%s'%(i,item['name'],item['age'],item['qq']))
