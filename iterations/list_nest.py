'''Demonstrate nested list comprehensions'''
from pprint import PrettyPrinter

matrix_a = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
	]
matrix_b = [
	[2,4,6],
	[12,15,18],
	[28,32,36]
	]
matrix_add =[
	[0,0,0],
	[0,0,0],
	[0,0,0]
	]
rows = range(len(matrix_a))
cols = range(len(matrix_a[0]))

for row in rows:
	for col in cols:
		matrix_add[row][col] = matrix_a[row][col]+ matrix_b[row][col]
print(matrix_add)

# another method

matrix_add = [[matrix_a[row][col]+matrix_b[row][col] for col in cols] for row in rows]
print(matrix_add)


#multiplication table

rows = cols = range(1,10)
multi_table = [[row * col for col in cols] for row in rows]
print(multi_table)
#with pretty printer
pp = PrettyPrinter()
pp.pprint(multi_table)

