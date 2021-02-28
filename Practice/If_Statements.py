age = int(input('Enter your age:'))

if age < 10:
    print('Child')

elif age < 21:
    print('Young')

else:
    print('You are wise')

meal = input('Do you eat meat? (y/n)')

if meal == 'y':
    print('Meat here')

else:
    print('Here veggie')