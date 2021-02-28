class Car: #Class name starts with Capital Letter
    def __init__(self,Name,Engine,Kerb_weight,Power_output): #It runs when we create a new instance of this class or new object based on this class
        self.Name = Name #Attributes
        self.Engine = Engine #Attributes
        self.Kerb_weight = Kerb_weight #Attributes
        self.Power_output = Power_output #Attributes
    def Carinfo(self): #Method
        return f'Bugatti Car Name is {Bugatti.Name} Engine is {Bugatti.Engine} L quad-turbocharged W16 Kerb Weight is {Bugatti.Kerb_weight} Output Power is {Bugatti.Power_output} kW'

Bugatti = Car('Divo',8.0 ,1961 ,1103) #Bugatti is instance of Car
print(f'Name: {Bugatti.Name}')
print(f'Engine: {Bugatti.Engine}')
print(f'Kerb Weight: {Bugatti.Kerb_weight}')
print(f'Power: {Bugatti.Power_output}')
print(Bugatti.Carinfo())

Bugatti = Car('Chiron',8.0 ,1996,1103) #Bugatti is instance of Car
print(f'Name: {Bugatti.Name}')
print(f'Engine: {Bugatti.Engine}')
print(f'Kerb Weight: {Bugatti.Kerb_weight}')
print(f'Power: {Bugatti.Power_output}')
print(Bugatti.Carinfo())