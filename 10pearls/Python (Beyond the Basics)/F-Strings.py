first = "fawad"
last = "naeem"
todo = "Code Test Code"
task = {"name":"Code Test Code","by":"Fawad"}

### %-formatting: oldest technique (before Python 3.6)

# print("%s Code Test Code" % first) 
# print("%s %s" % (first, todo)) 

### str.format(): (before Python 3.6)

# print("{0} {1}".format(first, todo))
# # indexing
# print("{what} {who}".format(what=task['name'], who=task['by']))
# print("{name} {by}".format(**task))
# # passing the dictionary

### F-String: (since Python 3.6)

# print(f"{todo} {first} {last}")
# # f"Display{variable}"

# print(f"{todo.lower()} {first.upper()} {last.upper()}")
## f"Call{function}"

# import datetime
# time_today = datetime.datetime.today()
# print(f'Result:{"Friday" if time_today.weekday() == 4 else "notFriday" }')
# # f"Evaluate{expression}"

# class Vehicle():
#     def __init__(self,company,color,vehicleNumber):
#         self.company = company
#         self.color = color
#         self.vehicleNumber = vehicleNumber
#     def alert(self):
#         return f"A vehicle of {self.company}, {self.color} color {self.vehicleNumber} number just violated a traffic light"

# vehicle = Vehicle("BMW","Blue","2531MNA")
# print(vehicle.alert())
# # F-String uses in class

### Quiz

##1
# print(f'{{5*3}}')
# print(f'{{{5*3}}}')
# print(f'5*3')
# print(f'{5*3}')

##2
# print(f""" fawad \
# naeem
# raza """)

##3
# print(f"{'fawad'}")
# print(f'{"fawad"}')
# print(f"""fawad""")

##4
## Fstring expressions can also include comments using the # symbol.
## True

##5
# f'{\"Fawad naeem\"}'

##6
## Which of the following are not advantages of f-strings?
## F-strings allow inline commenting
## F-strings allow all characters of the ascii table to be used within

##7
## Apart from f-strings, there are r-strings, u-strings and b-strings as well
## True

# learn more
# https://peps.python.org/pep-0498/