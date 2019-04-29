
class Grades():
	'''Represent a grade as a numeric score with a property'''
	
	def score(self,score=0):
		value = score
		if value >100 or value <0:
			raise valueError('Invalid score')
			self.score =value
			return self.score
		

		

math = Grades()
math.score=90
print('The math score was %s.' %math.score)
try:
	math.score=101
	print('The math score was %s.' %math.score)
except ValueError:
	print('that score is not allowed')