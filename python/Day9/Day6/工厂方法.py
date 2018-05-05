#工厂方法模式
class Person(object):
	def __init__(self,name):
		self.name=name
	def work(self):
		print(self.name+'开始工作了')
		#axe=StoneAxe()
		#axe.cut_tree()
		#axe=Factory.create_axe(axe_type)
		#axe.cut_tree()
		Factory=Stone_Axe_Factory()
		axe=Factory.create_axe()
		axe.cut_tree()
class Axe(object):
	def cut_tree(self):
		print('斧头%s开始砍树'%self.name)
class StoneAxe(Axe):
	def cut_tree(self):
		print('使用石头做的斧头砍树')
class SteelAxe(Axe):
	def cut_tree(self):
		print('使用刚做的斧头砍树')
class Factory(object):	  #定义工厂这个类，工厂方法模式
	#静态方法
	@staticmethod
	def create_axe(type):
		pass
class Stone_Axe_Factory(Factory):   #定义专门生产石头斧头的工厂的子类
	def create_axe(self):
		return StoneAxe()       
class Steel_Axe_Factory(Factory):    #定义专门生产刚做的斧头的工厂的子类
	def create_axe(self):
		return SteelAxe()
p=Person('zs')
p.work()
