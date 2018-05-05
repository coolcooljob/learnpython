import threading
import time

def sing():
	for i in range(3):
		print('singing')
		time.sleep(3)

def dance():
	for i in range(3):
		print('dancing')
		time.sleep(2)

st=threading.Thread(target=sing)
dt=threading.Thread(target=dance)

st.start()
dt.start()

while True:
	length=len(threading.enumerate())
	print('当前执行的线程总数为%d'%length)
	if length<=1:
		break
	time.sleep(0.5)
