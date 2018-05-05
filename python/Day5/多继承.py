class A:
	def test(self):
		pass
class B:
	def test(self):
		pass
class C(A,B):    #c多继承a和b
	def test(self):
		pass
c=C()
print(C.__mro__)   #只要c这个类定义了，那么它多继承的优先级就可以表示出来，打印这个多继承的优先级
