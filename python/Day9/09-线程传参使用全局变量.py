import threading
import time
#线程共享全局变量
g_num=100
def worker1(num):
	global g_num
	for i in range(3):
		g_num+=1
		print('in worker1 g_num:%d'%g_num)

def worker2(num):
	print('in worker2 g_num:%d'%g_num)

print('主线程,g_num:%d'%g_num)

w1=threading.Thread(target=worker1,args=(g_num,))
w1.start()
time.sleep(1)

w2=threading.Thread(target=worker2,args=(g_num,))
w2.start()
print('主线程,g_num:%d'%g_num)
