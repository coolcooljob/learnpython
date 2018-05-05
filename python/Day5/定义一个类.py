class Car:
	def start(self):
		print('汽车启动！')
	def print_car_info(self):
		print('车的名字是%s,颜色是%s'%(self.name,self.color))

c=Car()  #创建一个对象
c.name='迈腾'
c.color='金色'
c.start()
c.print_car_info()
