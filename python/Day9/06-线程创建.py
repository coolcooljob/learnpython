import threading
import time
#创建线程中执行的方法
def fun(num):
	print('线程%d执行！'%num)
	time.sleep(2)
#创建5个线程
for i in range(5):
	t=threading.Thread(target=fun,args=(i+1,))
	t.start()
