'''Demonstrate basic list comprehensions '''
# Without list comprehensions :
odds = []
for num in range(10):
	if num % 2:
		odds.append(num)
print('add numbers :',odds)

even = []

for evenum in range(10):
	if not evenum % 2:
		even.append(evenum)
print('even numbers:' , even)

# with a list comprehensions
odds = [num for num in range(10) if num % 2]
print('odd numbers:', odds)

# More examples
nums = [str(num) for num in range(10)]
print('Number strings:', nums)

alphabet = [chr(ordinal) for ordinal in range(ord('A'),ord('z')+1) if chr(ordinal).isalpha()]
print('Alphabet:',alphabet)
printord = ord('A')
print('ordinal',printord)

			
alphabet =[]
for ordinal in range(ord('z')+1):
	if chr(ordinal).isalpha():
		alphabet.append(chr(ordinal))
print('Alphabet:',alphabet)		



