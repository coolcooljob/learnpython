def print_menu():
	print('='*50)
	print('学生管理系统'.center(40))
	print('输入1，表示添加学生')
	print('输入2，表示删除学生')
	print('输入3，表示修改学生')
	print('输入4，表示查询学生')
	print('输入5，表示打印当前学生')
	print('输入6，表示打印所有学生')
	print('输入7，表示退出')
#一个学生包含很多信息，一个学生一个字典，学生列表用列表来存储
def add_student():
	name=input('请输入你要增加的学生姓名：')
	age=int(input('请输入你要输入的学生年龄：'))
	qq=input('请输入你要输入的学生的qq号:')
	stu={}
	stu['name']=name
	stu['age']=age
	stu['qq']=qq
	stus.append(stu)
	print('添加成功!')
	print(stus)
def del_student():
	name=input('请输入你要删除的学生姓名：')
	for i in stus['']['name']:
		if name not in stus():
			print('学生不存在！')
		else:
			print('正在删除')
			stus.remove(name)
			print(stus)
			print('删除成功！')
def modify_student():
	name=input('请输入你要修改的学生姓名！')
	if name in stus():
		name1=input('请输入你修改后的学生姓名！')
		stus.replace('name','name1')
		print('已经成功的将学生%s的名字修改为%s'%(name,name1))
	else:
		print('学生%s未在名单中！请重新输入！')	
def search_student(name):
	name=input('请输入你要查询的学生姓名！')
	for item in stus:
		if item['name']==name.strip():
			print('%s学生存在！%name')
			print_student(item)
			break
		else:
			print('学生%s没有找到！'%name)
def print_student(item):
	print('%s\t%s\t%s'%(stu['name'],stu['age'],stu['qq']))
def print_all_student():
	print('序号\t姓名\t年龄\tQQ号')
	for i,item in enumerate(stus,1):
		print('%s'%i)
		print_student()
def main():
	print_menu()		  
	while True:
		operate=input('请输入你想要的操作：')
		if operate=='1':
			add_student()		
		elif operate=='2':
			pass
		elif operate=='3':
			pass
		elif operate=='4':
			pass
		elif operate=='5':
			print_student(stus['stu'])
		elif operate=='6':
			print_all_student()
		else:
			break
stus=[]
main()
