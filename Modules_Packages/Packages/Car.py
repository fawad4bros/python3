class Car: #Class name starts with Capital Letter

    Doors = 2 #class_Attributes Availability: CLASS and INSTANCE
    
    def __init__(self,Name,Engine,Kerb_weight,Power_output): #It runs when we create a new instance of this class or new object based on this class
        self.Name = Name #instance_Attributes Availability: INSTANCE Only
        self.Engine = Engine #instance_Attributes Availability: INSTANCE Only
        self.Kerb_weight = Kerb_weight #instance_Attributes Availability: INSTANCE Only
        self.Power_output = Power_output #instance_Attributes Availability: INSTANCE Only
    
    def Carinfo(self): #instance_Method Availability: INSTANCE Only
        return f'Bugatti Car Name is {self.Name} Engine is {self.Engine} L quad-turbocharged W16 Kerb Weight is {self.Kerb_weight} Output Power is {self.Power_output} kW'

    @classmethod #class_Method Availability: METHOD Only
    def common(cls):
        return f'All Bugattis have {cls.Doors} doors'

    @staticmethod # Availability: CLASS and INSTANCE
    def speed(speed='fast'):
        return f'The Bugatti goes {speed}'