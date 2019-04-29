# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 13:52:55 2018

@author: nbg4kdv
"""

''' Demonstrate map function'''
Vehicles = [ 'sedan','coupe','hatchback','wagon']
cars = map(str.capitalize, Vehicles)
print('Map object cars:',cars)
cars = list(map(str.capitalize,Vehicles))
print('List object cars:',cars)
cars = [car.capitalize() for car in Vehicles]
print('List object cars:',cars)
def quad(val):
    return val ** 4

nums = range(4)
print('List of nums:',list(nums))
quads = list(map(quad,nums))