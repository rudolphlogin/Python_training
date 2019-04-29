# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:34:27 2018

@author: NBG4KDV
"""

'''Demonstrate basic iteration'''

print('For Loop:')
seq = 'abcde'
for chars in seq:
    print(chars, end='*')

numb = [1,2,3,4,5,6,7,8,9]
for num in numb:
    print(num,end='')
    print(num)
    
    
index =0
while index < len(seq):
    print(seq[index])
    index +=1
    
    
seq_upper = [c.upper() for c in seq]
tup_pairs = zip(seq,seq_upper)
print('\nIs tup_pairs iterable?',hasattr(tup_pairs,'__iter__'))
print('For loop:')
for pair in tup_pairs:
    print(pair,end='')
    break

print('\nIs tup_pairs an iterator?',hasattr(tup_pairs,'__next__'))
print('Iteration #2',tup_pairs.__next__()) #next() in python2


print('\nIs a seq in iterable?',hasattr(seq,'__iter__'))
print('\nIs a seq in iterator?',hasattr(seq,'__next__'))

#create an iterator object

it = iter(seq)
print('\nIs it iterable?',hasattr(it,'__iter__'))
print('\nIs it iterable?',hasattr(it,'__next__'))

print('\niteration #1',it.__next__())
print('\niteration #2',it.__next__())
print('\niteration #3',it.__next__())
print('\niteration #4',it.__next__())
print('\niteration #5',it.__next__())
print('\niteration #6',it.__next__())