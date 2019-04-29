# Functions are defined with the "def" keyword in Python
import random
faces =('heads','tails','jithesh','rohit')

def subproc():
	print('I do something')
	print('But return nothing')
	
subproc()
print (subproc())

def funcproc():
	return random.choice(faces)
for flipcoin in range(10):
	print(funcproc(),end=' ')
print()

def iadd(arg1,arg2):
	return arg1+arg2
print ('iadd(3,5) -->',iadd(3,5))
print('iadd("dy","namic") -->',iadd("dy","namic"))

def isum(*args):
	'''Return a total of the numeric args'''
	print('args -->',args)
	total = 0
	for arg in args:
		total = total + arg
	return total

print('isum(1,2,3,4,5,6,70) -->', isum(1,2,3,45,6,70))
params =(1,2,3,4,5,6,70)

print('isum(params) -->',isum(*params))

def ilist(alpha,beta='default',gama='assumed'):
	return alpha,beta,gama

print("ilist('required')-->",ilist('required'))
print("ilist('pos1','pos2','pos3')-->",ilist('pos1','pos2','pos3'))
print("ilist(gama ='pos1',alpha ='pos2',beta='pos3')-->",ilist(gama ='pos1',alpha ='pos2',beta='pos3'))

def iflex(**kwargs):
	print('kwargs -->',kwargs)
	for key in kwargs:
		print(key,'->',kwargs[key])
	return tuple(kwargs.values())
	
alphabet ={}
print('iflex(**alphabet) ->',iflex(**alphabet))
alphabet = {'delta':'$','sigma':'E','pi':'n'}
print('iflex(**alphabet) ->',iflex(**alphabet))


