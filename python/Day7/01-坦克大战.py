import pygame,sys
from pygame.locals import *

#坦克大战的主窗口
class TankMain(object):
	#开始游戏
	def startGame(self):
		pygame.init()   #pygame初始化，加载一些系统资源
		screen=pygame.display.set_mode((600,500),0,32)  #创建一个屏幕的窗口宽，高
		screen.display.set_caption('坦克大战')   #给窗口设置标题
	while True:	
		screen.fill(0,0,0)   #给窗口设置黑色的背景色
		screen.blit(self.write_text()),(0,5)  #显示左上角的文字
		pygame.display.update()    #显示重置
	#关闭游戏
	def stopGame(self):
		sys.exit()

	#设置游戏窗口的标题
	def set_title(self):
		pass

	def write_text():
		font=
if __name=='__main__':
	game=TankMain()
	game.startGame()
	
	
