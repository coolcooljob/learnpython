import threading
import time
from queue import Queue

class Producter(threading.Thread):
	def run(self):
		while True:
			if queue.qsize()<=1000:
				for x in range(100):
					msg='生产'+str(x)
					print('%s创建了%s'%(self.name,msg))
					queue.put(msg)
				time.sleep(1)
class Consumer(threading.Thread):
	def run(self):
		while True:
			if queue.qsize()>100:
				for x in range(3):
					msg=queue.get()
					print('%s消费了%s'%(self.name,msg))
				time.sleep(1)
queue=Queue()
for i in range(500):
	msg='产品'+str(i)
	queue.put(msg)

for i in range(2):
	t=Producter()
	t.start()

for i in range(5):
	c=Consumer()
	c.start()
