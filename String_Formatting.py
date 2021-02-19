num1 = 3.142000
num2 = 10.142000
#Previous
print('num1 is',num1,'and num2 is',num2)

#Format method
print('Num1 is {0} and num2 is {1} with Format method'.format(num1,num2))

#Format method with precision
print('Num1 is {0:.4} and num2 is {1:.4} with precision'.format(num1,num2))

#Format method with floating precision 
print('Num1 is {0:.4f} and num2 is {1:.4f} with floating precision'.format(num1,num2))

#Using F-Strings
print(f'Num1 is {num1:.4f} and num2 is {num2:.4f} with F-String')