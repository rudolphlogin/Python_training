''' Examples for PEP 8, the style guide for python code

while PEP 8 covers many topics in detail here are some key points:
* Readability counts, as code is read more often than written.
* Following a standard for coding style improves readability.
* Consistency with your code is more important than that with PEP 8.
'''
# each group of imports is separated by a space
import os # standard library imports should be first
import sys # don't use import os, sys

import xdb # next, should be related third-party packages installed with pip

import comments # last, should be local modules
import doc_strings # do not use wildcard imports

class Layout():
	''' For each level of indentation four spaces should be used.
	
	while python 2 allows the mising of tabs and spaces, python 3
	does not. Unless maintaining consistency with existing code,
	only spaces should be used for indentation.
	
	Lines of text should be limited to maximum of 79 characters.
	Most lines of text, especially comments or documentation should
	be limited to 72 characters. Python allows line wrapping within 
	paired delimiters as shown below.
	'''
	
	@classmethod
	def meaningful_name_of_method(cls,
								  first_parameter,
								  second_parameter):
	    ''' Use indent that matches opening delimiter.
		
		For class methods, the first parameter is conventionally named "cls".
		'''
		pass
	def meaninful_method_name(
		    first_long_named_parameter,
			second_long_named_parameter,
			third_long_named_parameter):
		''' Use the same indent for each parameter.
		
		The indentation can be indented to other than four spaces.
		'''
		pass
	def read_write(self):
	    '''Normal methods conventionally use a first parameter named "self".'''
		with open('/somestimes/the/path/to/the/file/can/be/deep') as file_source,\ # \ used to continuation of the line
			 open('/backslash/can/be/used/to/continue/a/single/line/','w') as file_dest:
				file_dest.write(file_source.read())
				
seq_layout_one =(
    'alpha','beta',
	'gama','delta'
	) # one level indentation is always good.
seq_layout_two = [
	'one', 'two',
	'three','four'
] # without indentation also fine

class NamingConventions():
	''' General rules for naming python objects
	
	Avoid:
	* single letter names, especially o,O,i,I, l and L.
	* Meaningless names
	* Names of found in __builtins__
	* Names of packages installed on the system
	'''
	
	CONSTANT =24	# Use all uppercase to indicate a "constant" variable.
	
	def package_and_module(self):
		''' Module names should be short, all lowercase, and avoid underscores.
		
		Package names should also be short, all lowercase, and not use underscores.
		'''
		pass
	def class_names(self):
		''' Class names should use capitalized words, or CapWords, like NamingConventions.
		
		As Exception objects are also classes, they should also follow this convention,
		but they should have the suffix "Error" added to their name'''
		pass
	def variable_function_method_name(self):
		'''Public interface names should not have leading underscores.
		
		Private interface names should generally have a single leading underscores.
		Names that have two leading underscores will be "mangled" (see PEP 8).
		To Avoid clashes with builtin names, use a single trailing underscore.
		'''
		pass