'''Demonstrate class properties'''
class Grader():
	'''Represent a grade as a numeric score'''
	def __init__(self,score=0):
		self.score = score
math= Grader(90)
print('The math score was %s.' %math.score)
math.score=101
print('The math score was %s.' %math.score)

class Grades():
	'''Represent a grade as a numeric score with a property'''
	def __init__(self,score=0):
		self.scoreMatch = score
	@property
	def score(self):
		return self.scoreMatch
		
	@score.setter
	def score(self,value):
		if value >100 or value <0:
			raise valueError('Invalid score')
		self.scoreMatch =value

math = Grades(90)
print('The math score was %s.' %math.score)
try:
	math.score=101
	print('The math score was %s.' %math.score)
except ValueError:
	print('that score is not allowed')