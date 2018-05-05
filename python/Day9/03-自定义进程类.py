from multiprocessing import Process
import os,time

class MyProcess(Process):
	def __init__(self,interval):
		super().__init__()
		self.interval=interval

	def run(self):
		print('子进程')
		starttime=time.time()
		time.sleep(self.interval)
		stoptime=time.time()
		print('子进程id:%d,父进程id:%d,执行了%s时间'%(os.getpid(),os.getppid(),stoptime-starttime))

print('父进程id:%d'%os.getpid())
starttime=time.time()
childs=[]
for x in range(5):
	p=MyProcess(x+1)
	p.start()
	childs.append(p)
for p in childs:
	p.join()
stoptime=time.time()
print('子进程结束,花费时间%s'%(stoptime-starttime))
