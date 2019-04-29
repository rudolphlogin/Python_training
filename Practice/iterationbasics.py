odds =[num for num in range(1,10) if num %2]
print('Odd numbers' , odds)

odds= []
for num in range(1,10):
    if num %2:
        odds.append(num)
print ('Odd numbers',odds)

odds =[str(num) for num in range(1,10) if num %2]
print('Number Strings' , odds)

alphabet = [chr(ordinal) for ordinal in range(ord('A'),ord('z')+1) if chr(ordinal).isalpha()]
print('Alphabet',alphabet)
