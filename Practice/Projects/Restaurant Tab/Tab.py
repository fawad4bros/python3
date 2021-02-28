class Tab:
    menu = { #Dictionary #class_Attributes
        'beef': 1000,
        'chicken': 700,
        'veggie': 400,
        'soft_drink': 60,
        'desert': 200,
        'coffee': 200        
    }

    def __init__(self): #instance_Attributes
        self.total = 0 
        self.items = []

    def add(self,item): #instance_Method
        self.items.append(item)
        self.total += self.menu[item] #self.menu[item] Will return the key:beef value i.e 1000 

    def print_bill(self,tax,service):
        tax = (tax/100)*self.total
        service = (service/100)*self.total
        total = self.total+tax+service

        for item in self.items:
            print(f'{item:20} PKR {self.menu[item]}') #item:20 will add 20 characters space 
        print(f'{"Total":20} PKR {total:.2f}') #"Total":20 will add 20 characters space 