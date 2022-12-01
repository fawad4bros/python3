""" What are Classes """

# class Person:
#     # class attribute are same for all instance of class
#     species = "Human"
#     # instance attribute are confined to the instance itself and my differ for each instance
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

""" Class Methods vs Instance Methods """

### Class Methods ###
## Used to access or modify class state
## Defination Syntax: @classmethod decorator OR the classmethod() function for a class method
## "cls" as the first parameter
## Can be called using classname or using class object
## Can access only class level attributes
## Bound to class

### Instance Methods ###
## Used to access or modify object/instance state
## Defination Syntax: Any method we create in a class will be created as an instance method 
## "self" as the first parameter
## Only be called using the object of the class
## The instance method can access both class level and object/instance attributes
## Bound to object/instance

## Example
# class Person:
#     state = 'Zinda'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     @classmethod
#     def check_state(cls):
#         # print(f'{cls.name} is {cls.state}') # AttributeError: type object 'Person' has no attribute 'name'
#         print(f'is {cls.state}')
#     def info(self):
#         print(f'{self.name} age of {self.age} is {self.state}')

### object/instance method and attribute can be accessed using the object/instance of class (Person)
# fawad = Person('Fawad', 24)
# fawad.state = 'died'
# print(fawad.state)
# fawad.info()
# fawad.check_state()

### @classmethod decorator, classmethod() function and class attribute can be accessed using class name (Person)
# print(Person.state)
# print(Person.check_state())

""" Key-Point @classmethod can only access Class Attribute and Object/Instance method can access Both"""

""" Static Methods """

## Performs tasks in isolation
## Static methods, marked with the @staticmethod decorator, do not have access to cls or self
## Cannot access class or object attributes so cannot change state
## Work like regular functions but belong to the class's namespace (Bound to class)
## Usecase: Utility functions, consume less memory

## Example changing the previous code

# class Person:
#     state = 'Zinda'
#     def __init__(self, name = '', age = 0):
#         self.name = name
#         self.age = age
#     @staticmethod
#     def info(name, age, state):
#         print(f'{name} age of {age} is {state}')
# Person.info('Fawad',24,'alive')
# jawad = Person()
# jawad.info('jawad',34,'Alive')

""" Dunder Methods """

## Often refferred to as Magic Methods
## Method that have two prefix and suffix underscores in the method name
## Dunder = Double Under (Underscores)
## Used for operator overloading
## Example: __init__ , __add__ , __len__ , __repr__

## Example
# num = 3
# # total = num + 2 # Internally a dunder method is being called __add__()
# total = num.__add__(2)
# print(total)

## Every operator is using a dunder method internally lets override the + operator in a class
## Example
# class coolingDown():
#     def __init__(self, val):
#         self.value = val
#     def __add__(self, val):
#         return self.value - val
# num = coolingDown(5)
# print(num + 2)

""" Example OOP"""
## _num is a protected variable
## __num is a private variable
## polymorphism is used for overriding and overloading
## In python overloading is not supported but can be achived by using libraries