'''Demonstrate class initialization'''
import locale
import sys

class Base_Model():
	'''Represent the base model of a car'''
	trim = 'normal'
	engine_liters = 1.5
	miles_range = 1000
	tank_capacity =50

	def __init__(self,price,transmission='automatic',color='white'):
		self.price = price
		self.transmission = transmission
		self.color= color
	@classmethod
	def miles_per_liter(jith):
		print(jith.miles_range/jith.tank_capacity)


	def info(self):
		if sys.platform.startswith('win'):
			locale.setlocale(locale.LC_ALL,'us')
		else:
			locale.setlocale(locale.LC_ALL,'en_US.utf8')
		print('The price of %s was %s.' %(self,locale.currency(self.price)))
	def __str__(self):
		return 'a %s base model with %s transmission' %(self.color,self.transmission)

Base_Model.miles_per_liter()
