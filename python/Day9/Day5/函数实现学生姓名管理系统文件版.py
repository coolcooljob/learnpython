import os
#定义一个通过存放学生信息的文件读取学生信息的函数
def read_stus():
	if os.path.exists(file_name):
		f=open(file_name,'r')
		while True:
			student_str=f.readline
			if student_str=='':
				break
			else:
				student_info_list=student_str.split('\t')
				student={'name':student_info_list[0],'age':student_info_list[1],'qq':student_info_list[1]}
				stus.append(student)
#定义一个将学生信息写入file_name文件的函数，如果这个文件存在，则先把这个文件备份(back-file_name),然后重新写一个文件并且将原来的文件覆盖
def write_stus_to_file():
	if os.path.exists(file_name):
		if os.path.exists(backup_file):
			os.remove(backup_file)
		os.rename(file_name,'backup-'+file_name)
	f=open(file_name,'w')
	for student in stus:
		student_str='%s\t%s\t%s'%(student['name'],student['name'],student['qq'])
		f.write(student_str)
	f.close()
#定义一个打印菜单选项的函数
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
#定义一个增加学生信息的函数
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
#定义一个删除学生信息的函数
def del_student():
	for i in stus['']['name']:
		if name not in stus():
			print('学生不存在！')
		else:
			print('正在删除')
			stus.remove(name)
			print(stus)
			print('删除成功！')
#定义一个修改学生信息的文件
def modify_student():
	name=input('请输入你要修改的学生姓名！')
	if name in stus():
		name1=input('请输入你修改后的学生姓名！')
		stus.replace('name','name1')
		print('已经成功的将学生%s的名字修改为%s'%(name,name1))
	else:
		print('学生%s未在名单中！请重新输入！')	
#定义一个查找学生信息的函数
def search_student(name):
	name=input('请输入你要查询的学生姓名！')
	for item in stus:
		if item['name']==name.strip():
			print('%s学生存在！%name')
			print_student(item)
			break
		else:
			print('学生%s没有找到！'%name)
#定义一个打印学生信息的函数
def print_student(item):
	print('%s\t%s\t%s'%(stu['name'],stu['age'],stu['qq']))
#定义一个打印所有学生信息的函数
def print_all_student():
	print('序号\t姓名\t年龄\tQQ号')
	for i,item in enumerate(stus,1):
		print('%s'%i)
		print_student()
#主函数
def main():
	read_stus()
	print_menu()		  
	while True:
		operate=input('请输入你想要的操作：')
		if operate=='1':
			add_student()
			write_stus_to_file()		
		elif operate=='2':
			name=input('请输入要删除的学生姓名：')
			del_student()
			write_stus_to_file()
		elif operate=='3':
			modify_student()
		elif operate=='4':
			research_student()
		elif operate=='5':
			pass
		elif operate=='6':
			print_all_student()
		else:
			break
file_name='stus.txt'
back_file='backup-stus.txt'
stus=[]
main()
