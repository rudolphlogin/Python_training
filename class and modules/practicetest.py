''' Provide a class to model a 2d Vector'''

class Vector(object):
	'''A class for 2D vectors which implements vector addition '''
	def __init__(self,x,y):
		'''Initialize the vector object '''
		self.x= x
		self.y = y 
		
	def __add__(self, other):
		''' Implement the method for the "+" operator '''
		x = self.x + other.x
		y = self.y + other.y
		return Vector(x,y)
	def __repr__(self):
		''' Provide a useful representation of the vector object '''
		return 'Vector(' + str(self.x)+ ',' + str(self.y) + ')'