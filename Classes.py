name = 'fawad'
age = 21
num = [1,5,8,9]
typeof = type(name) #Properties
print(typeof)
typeof = type(age) #Properties
print(typeof)
typeof = type(num) #Properties
print(typeof)
NAME = name.upper() #Method
print(NAME)


class Car: #Class name starts with Capital Letter
    def __init__(self): #It runs when we create a new instance of this class or new object based on this class
        self.Name = 'Divo'
        self.Engine = 8.0
        self.Kerb_weight = 1961
        self.Power_output = 1103
    def Carinfo(self): #Method
        return f'Bugatti Car Name is {Bugatti.Name} Engine is {Bugatti.Engine} L quad-turbocharged W16 Kerb Weight is {Bugatti.Kerb_weight} Output Power is {Bugatti.Power_output} kW'

Bugatti = Car() #Bugatti is instance of Car
print(f'Name: {Bugatti.Name}')
print(f'Engine: {Bugatti.Engine}')
print(f'Kerb Weight: {Bugatti.Kerb_weight}')
print(f'Power: {Bugatti.Power_output}')
print(Bugatti.Carinfo())