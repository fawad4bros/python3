# def addition(x,y):
#     return x + y
# print(addition(10, 5))

"""  Lambda Function """ 

# addition = lambda x,y : x + y
# print(addition(10,5))

# def difference(x,y):
#     if x > y:
#         return x - y
#     return y - x
# print(difference(10, 5))

"""  Lambda Function """ 

# difference = lambda x,y: x - y if x > y else y - x
# print(difference(10,5))

"""  Syntax """ 
## Anonymous function
## Declaration with lambda keyword rather than def
## Any no. of arguments but only one expression
"""  Disadvantages """ 
## Lambda function can not be documented

"""  Map with Lambda """ 

## Map function takes a function and a Iterable 
## Map function always returns a Iterable object
# oddNo = [1,3,5,7,9]
# totalSum = map((lambda x: x - 1), oddNo)
# print(next(totalSum))
# print(next(totalSum))
# print(next(totalSum))
# print(next(totalSum))
# print(next(totalSum))
# print(next(totalSum))
# for i in totalSum:
#     print(i)

"""  Filter with Lambda """ 

## Filter function returns an iterable Object
## element will be returned if the condition is true

# numbers = [1,2,3,4,5,6,7,8,9]
# evenNo = filter((lambda x: x%2==0), numbers)
# for i in evenNo:
#     print(i)
# print(next(evenNo))
# print(next(evenNo))
# print(next(evenNo))
# print(next(evenNo))

"""  Reduce with Lambda """ 

## Reduce function returns an element
## function takes to arguments
## Reduce function belongs to the functools module.

# from functools import reduce
# numbers = [1,2,0,0,2]
# total = reduce((lambda x , y: x + y),numbers)
# print(total)

"""  Quiz """ 
## 1
# Which of the following is false?
# Lambda functions can have multiple expressions

## 2
# output of the following piece of code
# x = lambda a,b: a*b
# print(x(2,3))

## 3 
# Would the below lambda function below return two values?
# y = lambda x: x*2,4

## 4
# How many values does ‘z’ take in the following piece of code?
# z = map(lambda x,y:(x,y), range(3), range(2))
# z = list(z)
# print(z)

## 5
# Which of the following will return the given output? [‘orange’, ‘mango’]
# fruits = ['apple','orange','mango']
# x = filter(lambda fruit: 'o' in fruit,fruits)
# x = list(x)
# print(x)