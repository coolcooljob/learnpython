print('='*50)
print('学生姓名管理系统'.center(40))
print('输入1，表示添加学生')
print('输入2，表示删除学生')
print('输入3，表示修改学生')
print('输入4，表示查询学生')
print('输入5，表示退出')

stus=[]
while True:
	operate=input('请输入你想要的操作：')
	if operate=='1':
		name=input('请输入你要添加的学生姓名：')
		stus.append(name.strip())
		print(stus)
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
		if name in stus:
			print('学生%s在名单中！'%name)
		else:
			print('不好意思！您所查询的学生%s不存在！'%name)
	else:
		break
