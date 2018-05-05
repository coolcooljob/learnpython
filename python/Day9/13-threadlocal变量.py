import threading
#创建全局thread_local变量
local_school=threading.local()
def process_student():
	#获取当前线程关联的学生
	name=local_school.student
	print('hello %s in %s'%(name,threading.current_thread().name))
def processThread(name):
	local_school.student=name
	process_student()

t1=threading.Thread(target=processThread,args=('job',),name='t1')
t2=threading.Thread(target=processThread,args=('jack',),name='t2')
t1.start()
t2.start()
