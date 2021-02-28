num = [2,5,7,8,6,4,2,5]
sorting = sorted(num)
print(sorting)
names = ['saad','hammad','fawad','jawad','fawad','jawad']
sorting = sorted(names) #First Capital letters then small letters
print(sorting)
uniqe = set(num) #Removes the duplicates
print(uniqe)
uniqe = set(names) # order will be disturbed
print(uniqe) 

dictionry = {'Fawad':'BSCS','Hammad':'MBBS','Saad':'MS','Jawad':'MS'}
#Values = set(dictionry.values())
#print(Values)
dictionry_valuse = dictionry.values()
dictionry_set = set(dictionry_valuse)
print(dictionry_set)




def DegreeCount(dictionary):
    degrees = list(dictionry.values())
    for degree in set(degrees): # Remove set () and see what happens
        num = degrees.count(degree)
        print(f'There are {num} {degree} Degrees')
person = {}
while True:
    name = input('Name: ')
    degree = input('Degree: ')
    person[name] = degree
    another = input('Another ? (y/n) ')
    if another == 'y':
        continue
    else:
        break
DegreeCount(person)