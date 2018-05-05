class Person(object):
	def __init__(self,name):
		self.name=name
	def work(self,axe_type):
		print(self.name+'开始工作了')
		#axe=StoneAxe()
		#axe.cut_tree()
		axe=Factory.create_axe(axe_type)
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
class Factory(object):	
	#静态方法
	@staticmethod
	def create_axe(type):
		if type=='stone':
			return StoneAxe()
		elif type=='steel':
			return SteelAxe()
		else:
			print('不好意思，输入错误！')
p=Person('zs')
p.work('stone')
