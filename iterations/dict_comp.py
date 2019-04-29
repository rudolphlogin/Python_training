# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 13:23:00 2018

@author: nbg4kdv
"""

'''Demonstrate dictionary comprehensions'''
keys=[1,'a',2,'b',3,'c']
print('List Keys :\n',keys)
values=[100,'apple',200,'berry',300,'cherry']
print('List of values :\n',values)

# new dictionary using zip
bundle= dict(zip(keys,values))
print('dictionary bundle :\n',bundle)

# zip value cannot display directly but using loop unlike dict
zipvalue = zip(keys,values)
print('zip value:',[pair for pair in zipvalue])

#new dectionary using comprehension
box = {k:v for (k,v) in zip(keys,values)}
print('Dictionary box :\n',box)

# new dictionaries uisng conditional comprehension and key/value expressions
alpha = {k.upper():v for (k,v) in zip(keys,values) if isinstance(k,str)}
print('dictionary alpha:\n',alpha)

numer = {k:v for (k,v) in zip(keys,values) if isinstance(k,int)}
print('dictionary alpha:\n',numer)

#using a conditional list
cond = [True if isinstance(test,str) else False for test in keys]
print('Conditional list:\n',cond)

zipvaluescond = zip(keys, values,cond)
print('zipvaluescond:\n',[zipdet for zipdet in zipvaluescond])

fruit = {key:value.upper() for (value,key,test) in zip(keys, values,cond) if test}
print('Dictionary fruit:\n',fruit)