#echo服务器(自发自收)
from socket import *

udpSocket=socket(AF_INET,SOCK_DGRAM) #申明一个socket,固定格式
bindAddr=('',9988) 
udpSocket.bind(bindAddr)   #绑定一个段口
#定义一个全局变量
num=1
while True:
	recvData=udpSocket.recvfrom(1024)    #接收数据
	udpsocket.sendto(recvData[0],recvData[1])  #发送数据
	print('收到第%d条信息，内容:%s'%(num,recvData[0]))
	num+=1

udpSocket.close()
