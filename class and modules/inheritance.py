'''Demos of inheritance'''
class Base_Model():
	trim = 'normal'
	engine_liters = 1.5
	
	def engine_sound(self):
		return 'putt,putt'
	def horn_sound(self):
		return 'beep,beep'
	def __str__(self):
		return 'Base Model'
		
coop = Base_Model()
print('%s has %s trim level.'%(coop,coop.trim))
print('%s has %s trim level.'%(coop,coop.engine_liters))
print('%s has %s trim level.'%(coop,coop.engine_sound()))
print('%s has %s trim level.'%(coop,coop.horn_sound()))


class Sport_Model(Base_Model):
	engine_liters=2.0
	def engine_sound(self):
		return 'VROOM, VROOM'
	def __str__(self):
		return 'sport Model'

coop_sport = Sport_Model()
print('%s has %s trim level.'%(coop_sport,coop_sport.trim))
print('%s has %s trim level.'%(coop_sport,coop_sport.engine_liters))
print('%s has %s trim level.'%(coop_sport,coop_sport.engine_sound()))
print('%s has %s trim level.'%(coop_sport,coop_sport.horn_sound()))
	










