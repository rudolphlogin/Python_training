'''Demonstrate reading text from a file'''
print('\n********* Iterating over lines ***************')
'''Reading text from a file with default encoding'''
with open('C:\\Users\\nbg4kdv\\Documents\\UPS\CDP\\Python\\class and modules\\pep20.txt') as textfile:
	for line in textfile:
		print(line,end='')

print('\n********* Using read() method ************')
with open('C:\\Users\\nbg4kdv\\Documents\\UPS\CDP\\Python\\class and modules\\pep20.txt',encoding='us') as text_file:
	text = text_file.read()
print(text)

print('\n********* Using readlines() method ******************')
'''Reading text from a file with "utf-8" encoding'''
with open('C:\\Users\\nbg4kdv\\Documents\\UPS\CDP\\Python\\class and modules\\pep20.txt',encoding='utf-8') as text_file:
	lines = text_file.readlines()
print(lines)

print('\n********* Using readline() method ***************')
'''Reading text from a file with "lating-1" encoding'''
with open('C:\\Users\\nbg4kdv\\Documents\\UPS\CDP\\Python\\class and modules\\pep20.txt',encoding='latin-1') as text_file:
	while 1:
		line = text_file.readline()
		if not line:
			break
		else:
			print(line,end='')

print('\n********* using error handling *****************')
try:
	''' Reading text from a file with "utf-16" encoding'''
	with open('C:\\Users\\nbg4kdv\\Documents\\UPS\CDP\\Python\\class and modules\\pep20.txt',encoding='utf-16') as text_file:
		for line in text_file:
			print(line,end='')
except UnicodeError:
	print('Problem with Unicode encoding')
