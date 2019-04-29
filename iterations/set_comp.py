''' Demonstrate set comprehensions'''
from math import pi
pi_limits ={val*pi*0.1 for val in range(-10,11)}
print('pi limts:',pi_limits)
print('pi in pi_limits:', pi in pi_limits)

from calendar import isleap
leapyears = { year for year in range(2016,2066) if isleap(year)}
print('leapyears:',leapyears)
print('2016 in leapyears:', 2017 in leapyears)

leaparray =[]
leaparray =[year for year in range(2016,2066) if isleap(year)]
print('leapyears:',leaparray)


basket_a = {'apple','orange','pear'}
basket_b = {'lemon','pear','peach'}

basket = {fruit_a +'-'+ fruit_b for fruit_a,fruit_b in zip(basket_a,basket_b) if fruit_a != fruit_b}
print('basket:',basket)

basket = {fruits for fruits in zip(basket_a,basket_b) }
print('basket:',basket)


#change the set 
basket_ac = ('apple','orange','pear')
basket_bc = ('lemon','pear','peach')

baskets = {fruitsset for fruitsset in zip(basket_ac,basket_bc)}
print('fruitsset:', baskets)