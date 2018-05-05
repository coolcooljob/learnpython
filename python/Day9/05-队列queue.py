from multiprocessing import Process,Queue
import os,time,random

def write(q):
	for item in 'ABC':
		print('正在往消息队列写入%s'%item)
		q.put(item)
		time.sleep(random.random())

def reader(q):
	while True:
		if not q.empty():
			item=q.get()
			print('从消息队列取出%s'%item)
			time.sleep(random.random())
		else:
			break
#创建消息队列
q=Queue
#创建写入进程
pw=Process(target=write,args=(q,))
pw.start()
pw.join()
#创建读取进程
pr=Process(target=reader,args=(q,))
pr.start()
pr.join()

print('所有数据已经读完!')
