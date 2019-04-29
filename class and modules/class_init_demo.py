'''Demonstrate class initialization'''
import locale
import sys

class Base_Model():
	'''Represent the base model of a car'''
	trim = 'normal'
	engine_liters = 1.5
	
	def __init__(self,price,transmission='automatic',color='white'):
		self.price = price
		self.transmission = transmission
		self.color= color
	def info(self):
		if sys.platform.startswith('win'):
			locale.setlocale(locale.LC_ALL,'us')
		else:
			locale.setlocale(locale.LC_ALL,'en_US.utf8')
		print('The price of %s was %s.' %(self,locale.currency(self.price)))
	def __str__(self):
		return 'a %s base model with %s transmission' %(self.color,self.transmission)
		
coop = Base_Model(2500)
coop.info()
coop_blue = Base_Model(price=25500,color='red')
coop_blue.info()
coop_param = Base_Model(25600,'manual','green')
coop_param.info()