for n in range(5):
    print(n)

for n in range(3,10): #3 to 9
    print(n)

for n in range(0,20,4): # 4 indicate the jumps
    print(n)

Burgers = ['Beef','Chicken','Veg','Supreme','double'] 

for burger in range(len(Burgers)): #len(Burgers) to find the length of range
    print(burger, Burgers[burger])

for Burger in range(len(Burgers)-1,-1,-1):
    print(Burger,Burgers[Burger]) 