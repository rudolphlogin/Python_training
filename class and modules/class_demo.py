'''Demonstrate class definitions'''
class Base_Model():
	'''Represent base model of a car'''
	trim = 'normal'
	engine_liters = 1.5
	
	def engine_sound(self):
		return 'putt,putt'
	def horn_sound(self):
		return 'beep,beep'
	def __str__(self):
		return 'Base_Model'
	
coop = Base_Model()
print('%s has %s trim level %s.'%(coop,coop.trim))
print('%s has %s  liter engine.'%(coop,coop.engine_liters))
print('%s engine sounds like %s.'%(coop,coop.engine_sound()))
print('%s hourn sounds like %s.'%(coop,coop.horn_sound()))