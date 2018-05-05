from multiprocessing import Process
import os
def fun(name):
	print('子进程pid:%d'%os.getpid())
print('父进程')
#创建子进程
p=Process(target=fun,args=('job',))
#开始执行
p.start()
#父进程等待子进程执行完毕
p.join()
print('子进程结束！')
