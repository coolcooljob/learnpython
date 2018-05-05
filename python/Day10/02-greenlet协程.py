#协程,需要手动切换
from greenlet import greenlet
import time

def test1():
	while True:
		print('---in test1---')
		g2.switch()
		time.sleep(0.5)
def test2():
	while True:
		print('---in test2---')
		g1.switch()
		time.sleep(0.5)

#生成两个切换器，注意传入自己定义的函数
g1=greenlet(test1)
g2=greenlet(test2)

#一开始还是切换到g1去执行
g1.switch()

