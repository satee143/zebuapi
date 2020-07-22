from abc import ABC,abstractmethod


class Computer():
	@abstractmethod
	def process(self):
		print('working')
class laptop(Computer):
	def write(self):
		print('work')
class  desktop(laptop):
	def progr(self):
		print('works fine')		

com=desktop()
com.process()