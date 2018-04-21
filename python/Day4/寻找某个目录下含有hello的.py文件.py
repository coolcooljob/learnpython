import os
file_list=[]
#递归函数，当前函数中的所有文件路径全部采用绝对路径，parent_dir:文件所在父目录的 绝对路径，file_name表示当前你要处理的文件
def find_hello(parent_dir,file_name):
#当前你要处理的文件的绝对路径
	file_abspath=os.path.join(parent_dir,file_name)
	if os.path.isdir(file_abspath):
#进入目录，列出该目录下的所有文件列表
		for f in os.listdir(file_abspath):
			find_hello(file_abspath,f)	
	else:
		if file_abspath.endswith('.py'):
			if read_and_find_hello(file_abspath):
				file_list.append(file_abspath)
def read_and_find_hello(py_file):
	flag=False
	f=open(py_file)
	while True:
		line=f.readline()
		if line=='':
			break
		if 'hello' in line:
			flag=True
			break
	f.close()	
	return flag
find_hello('/home','python')
print(file_list)
