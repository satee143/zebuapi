class Engine:
	a=10
	b=30
	def __init__(self):
		self.b=20
	def m1(self):
		print('Engine specific functo')
		
class car:
	def __init__(self):
		self.engine=Engine()
	def m2(self):
		print('car using engine class')
		print(self.engine.a)
		print(self.engine.b)
		print(Engine.b)
		self.Engine.m1()
		
c=car()
c.m2()