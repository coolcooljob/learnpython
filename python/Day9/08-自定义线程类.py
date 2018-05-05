import threading,time
class MyThread(threading.Thread):
	def run(self):    #自定义类方法来创建线程实例主要是创建run方法
		for i in range(3):
			time.sleep(1)
			msg='I am '+self.name+'@'+str(i)
			print(msg)
for i in range(5):
	t=MyThread()
	t.start()
