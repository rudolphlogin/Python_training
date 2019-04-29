'''Demonstrate writing text to a file'''

from io import UnsupportedOperation

print('Default Windows 10 encoding "cp1252".')
with open('C:\\Users\\nbg4kdv\\Documents\\UPS\CDP\\Python\\written.txt',mode='w') as out_file:
	out_file.write('This is the first line of text.\n')
	
with open('C:\\Users\\nbg4kdv\\Documents\\UPS\CDP\\Python\\written.txt',mode='a') as append_file:
	append_file.write('This line is appended at the end.\n')

with open('C:\\Users\\nbg4kdv\\Documents\\UPS\CDP\\Python\\written.txt',mode='r') as in_file:
	print(in_file.read())

lines = (
	'Line 1\n','Line 2\n',
	'Line 3\n','Line 4\n'
	)
''' Using a file without the "with" context'''
try:
	out_file = open('C:\\Users\\nbg4kdv\\Documents\\UPS\CDP\\Python\\without.txt',mode='w',buffering=1,encoding='us')
	out_file.writelines(lines)
	out_file.flush()
finally:
	out_file.close()
	
try:
	in_file = open('without.txt',encoding='us')
	print(in_file.tell(),end=' <- File position before first read\n')
	print(in_file.read(7))
	print(in_file.tell(),end='<- File position after first read\n')
	print(in_file.read(7))
	print(in_file.tell(),end='<- File position after second read\n')
	in_file.seek(0,0) # seek(offset, from_what) from_what=0 is BOF
	print(in_file.tell(),end ='<- BOF after seek(0,0)\n')
	in_file.seek(0,2) # from_what=2 is EOF
	print(in_file.tell(),end=' <- BOF after seek(0,0)\n')
	print(in_file.read()) # print from position to end
	print(in_file.tell(), end=' <- EOF after read() \n')
	in_file.seek(7,1) # from_what =1 is relative to position  -- it is not supported in python 3
	print(in_file.tell(), end=' <- File position after relative seek \n')
except UnsupportedOperation:
	print('Text files do not support relative seeks')
finally:
	in_file.close()
	