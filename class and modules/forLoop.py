#friends =['Joseph','Glenn','Sally']
#for friend in friends:
#  print("Happy new year.", friend)
#print("Done")

largest = None

for itervar in[3,4,5,2,6,3,12,11]:
    if largest is None or itervar>largest:
        largest = itervar
    print('Loop',itervar,largest)
print('Largest',largest)
