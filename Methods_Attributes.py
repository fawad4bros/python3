class Car: #Class name starts with Capital Letter

    Doors = 2 #class_Attributes Availability: CLASS and INSTANCE
    
    def __init__(self,Name,Engine,Kerb_weight,Power_output): #It runs when we create a new instance of this class or new object based on this class
        self.Name = Name #instance_Attributes Availability: INSTANCE Only
        self.Engine = Engine #instance_Attributes Availability: INSTANCE Only
        self.Kerb_weight = Kerb_weight #instance_Attributes Availability: INSTANCE Only
        self.Power_output = Power_output #instance_Attributes Availability: INSTANCE Only
    
    def Carinfo(self): #instance_Method Availability: INSTANCE Only
        return f'Bugatti Car Name is {Bugatti.Name} Engine is {Bugatti.Engine} L quad-turbocharged W16 Kerb Weight is {Bugatti.Kerb_weight} Output Power is {Bugatti.Power_output} kW'

    @classmethod #class_Method Availability: METHOD Only
    def common(cls):
        return f'All Bugattis have {cls.Doors} doors'

    @staticmethod # Availability: CLASS and INSTANCE
    def speed(speed='fast'):
        return f'The Bugatti goes {speed}'

Bugatti = Car('Divo',8.0 ,1961 ,1103) #Bugatti is instance of Car
print(f'Name: {Bugatti.Name}')
print(f'Engine: {Bugatti.Engine}')
print(f'Kerb Weight: {Bugatti.Kerb_weight}')
print(f'Power: {Bugatti.Power_output}')
print(Bugatti.Carinfo())

print(Bugatti.speed('Very Fast')) #staticmethod
print(Car.speed('Very Fast')) #staticmethod

print(Bugatti.Doors) #class_Attributes
print(Car.Doors) #class_Attributes

print(Car.common()) #class_Method
print(Bugatti.common()) #class_Method

#print(Car.Carinfo()) #instance_Method #Dont have access through Class to Instance method
print(Bugatti.Carinfo()) #instance_Method 