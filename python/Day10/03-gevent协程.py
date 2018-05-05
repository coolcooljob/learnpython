#gevent自动进行协程之间的切换
import gevent

def fun(num):
	for i in range(num):
		print('%s%s'%(gevent.getcurrent(),str(i)))
		gevent.sleep(1)   #利用gevent中的sleep方法模拟耗时操作
g1=gevent.spawn(fun,5)
g2=gevent.spawn(fun,5)
g3=gevent.spawn(fun,5)

g1.join()
g2.join()
g3.join()
