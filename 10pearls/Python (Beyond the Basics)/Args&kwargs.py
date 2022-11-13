gift = ['F','A','W','A','D']
a,s,d,f,g = gift

# a,s,d,f,g,h = gift
# # ValueError: not enough values to unpack (expected 6, got 5)

# a,s,d,f = gift
## ValueError: too many values to unpack (expected 4)

# *present, = 'F','A','W','A','D'
# print(*present)
## packing using asterisk operator and trailing comma

# x,*y = present
# print(x)
# print(*y)
## un-packing using asterisk operator

### Example
# grades = sorted([98,85,13,54,11,15])
# low,*mid,high=grades
# print(low)
# print(*mid)
# print(high)
## Find High and low

### Example
# l = [1,2,3,4,5]
# t = (1,2,3,4,5)
# def multi(*args):
#     result = 1
#     for each in args:
#         result = result * each
#     return result
# print(multi(1,2,3,4,5))
# print(multi(*[1,2,3,4,5]))
# print(multi(*(1,2,3,4,5)))
# print(multi(*l))
# print(multi(*t))

### Example
# def intro(**kwargs):
#     for key, value in kwargs.items():
#         print(f"Hi my name is {key} and I'm a {value}") 
# dic = {'fawad':'Developer','hammad':'Doctor','saad':'ML Engr','jawad':'AI Engr'}
# intro(**dic)

### Quiz

##1
# Which of the following is not a difference between a keyword argument and a non-keyword argument?
# Keyword arguments need to be greater in number than non-keyword arguments

##2
## How many keyword arguments can be passed to a function with default parameters, in a single function call?
# def intro(kwargs):
#     for key, value in kwargs.items():
#         print(f"Hi my name is {key} and I'm a {value}") 
# intro(fawad='Developer')

##3
# what is the result of the following piece of code?
# myQuiz = "this is a Quiz"
# a, b, *c = myQuiz
# print(a)
# print(b)
# print(c)

##4
# When to use *args and **kwargs?
# When we don’t know how many arguments need to be passed to a python function, we can use packing

##5
# x,y,*z,*t = (12,20,30,40)
# print(z)