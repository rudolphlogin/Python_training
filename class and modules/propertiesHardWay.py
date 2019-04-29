class Hardway():
	'''Demonstrate property function'''
	def __init__(self,value=True):
		self.hardset(value)
	
	harddoc = 'Properties can have a getter, setter,deleter and doc string'
	def hardset(self,value):
		if value:
			self.way = True
		else:	
			self.way = False
	def hardget(self):
		return self.way
	def harddel(self):
		self.way= None
	hard = property(fget= hardget,fset=hardset,fdel=harddel,doc=harddoc)	
	
'''calls'''	
not_decorated = Hardway()
not_decorated.hard='test'
print('The value of not_decorated.hard is',not_decorated.hard)
del not_decorated.hard
print('The value of not decorated.hard is',not_decorated.hard)
print(Hardway.hard.__doc__)