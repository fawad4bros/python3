""" Def: A decorator is a design pattern in Python that allows a user 
to add new functionality to an existing object  without modifying its structure. 
Decorators are usually called before the definition of a function you want to decorate"""

"""While applying Multiple Decorators to a Single Object. The decorators will be applied in the bottom up order """

## Creating Decorator

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper

# def say_hi():
#     return 'hello there'

# decorate = uppercase_decorator(say_hi)
# decorate()

## Appying Decorator

@uppercase_decorator
def say_hi():
    return 'hello there'

say_hi()
