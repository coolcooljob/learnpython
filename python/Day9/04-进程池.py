from multiprocessing import Pool
import os,time

def worker(msg):
	print('子进程pid:%d'%os.getpid())
	starttime=time.time()
	time.sleep(3)
	stoptime=time.time()
	print('msg:%s,花费%d时间'%(msg,stoptime-starttime))

#创建进程池
pool=Pool(3)
for i in range(10):
	#pool.apply_async(worker,(i,))   #异步的去向进程池去请求
	pool.apply(worker,(i,))          #同步的去向进程池去请求
#关闭进程池
pool.close()
#父进程等待子进程执行完毕
pool.join()
print('子进程执行完毕！')
