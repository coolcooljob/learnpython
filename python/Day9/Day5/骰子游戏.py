import random
#定义一个游戏的类，里面包括两个玩家
class Game:
	def __init__(self,player1,player2):  #初始化游戏
		self.player1=player1
		self.player2=player2
		print('游戏初始化完成！')

	def start_game(self):    #开始游戏
		self.player1.cast()   #玩家1投掷骰子
		self.player2.cast()   #玩家2投掷骰子
		print(self.player1)
		print(self.player2)

#定义玩家这个类，里面包括抛骰子，猜点数，以及自动输出玩家信息和点数信息
class Player:
	def __init__(self,name,sex,*dice):
		self.name=name
		self.sex=sex
		self.dices=dice

	def cast(self):    #玩家抛骰子
		for dice in self.dices:
			dice.move()
		
	def guess_dice(self): #猜骰子的点数，比如4个2
		return (4,2)

	def __str__(self):   #将玩家信息转化为字符串，默认调用
		player_dice_count_list=[self.dices[0].count,self.dices[1].count,self.dices[2].count]
		return '姓名为：%s,投掷的骰子点数信息为：%s'%(self.name,str(player_dice_count_list))

#定义一个骰子的类，初始点数为0，随机在1到6之间滚动
class Dice:
	def __init__(self):
		self.count=0

    #骰子滚动之后的点数
	def move(self):
		self.count=random.randint(1,6)
#游戏开始之前，先准备6个骰子
d1=Dice()
d2=Dice()
d3=Dice()
d4=Dice()
d5=Dice()
d6=Dice()

#实例化两个玩家
p1=Player('Job','boy',d1,d2,d3)
p2=Player('Mary','girl',d4,d5,d6)

#玩5次游戏
for i in range(1,6):
	print('第%d次游戏的情况'%i)
	game=Game(p1,p2)
	game.start_game()

		
