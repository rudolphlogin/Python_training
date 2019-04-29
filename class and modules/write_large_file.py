'''Demonstrate working with large file'''
from timeit import timeit

def file_iter():
	''' Process single line into string in memory '''
	with open('C:\\Users\\nbg4kdv\\Documents\\UPS\CDP\\Python\\product.txt', mode ='r') as text_file:
		with open('C:\\Users\\nbg4kdv\\Documents\\UPS\CDP\\Python\\out.txt', mode='w') as out_file:
			for line in text_file:
				out_file.write(line)
def file_readlines():
	''' Process all lines into list in memory '''
	with open('games.txt', mode='r') as text_file:
		with open('out.txt',mode='w') as out_file:
			lines = text_file.readines()
			out_file.writelines(lines)
def file_readline():
	'''Process one line into string in memeroy'''
	with open('product.txt',mode='r') as text_file:
		with open('out.txt',mode='w') as out_file:
			while 1:
				line = text_file.readline()
				if not line:
					break
				else:
					out_file.write(line)
def file_read():
	'''Processes all lines into string in memory '''
	with open('games.txt',mode='r') as text_file:
		with open('out'txt', mode='w') as out_file:
			out_file.write(text_file.read())
if __name__ ='__main__':
	print('iterator: %5.3f seconds ' % timeit(stmt='file_iter()',
					setup ='from__main__ import file iter',number=10))
					