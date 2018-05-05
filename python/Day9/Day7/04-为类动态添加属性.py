#动态的给一个类里面已经定义好的一个实例添加属性以及方法
class Person(object):
	def __init__(self,name,age):
		self.name=name
		self.age=age


p=Person('job',20)
p.sex='male'       #属性可以直接添加
print(p.sex)       
def run(self):   #但是当你想要动态的添加一个方法的时候必须通过13,14行的方法添加，然后发现15行调用的时候已经成功的添加
	print('running')
import  types     #通过导入types模块,利用模块里面的MethodType方法动态的给一个实例添加方法
p.run=types.MethodType(run,p)    #注意需要传两个参数，分别是这个方法名字以及这个实例的名字
p.run()

