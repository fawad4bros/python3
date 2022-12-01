"""  Pre-Requisites: Understanding Iterators """ 

## What is an iterator?
## An iterator is an object that has a countable number of things
## Objects that can be Traversed over
## Has the methods: __iter__() and __next__()

""" Iterators VS Iterable """ 

"""  Iterable """ 
## How to know if a object is Iterable?
## If we can iterate over an object by using a loop, it is called Iterable Object
## Iterable do not have methods: __iter__() and __next__()

## Expamle
# listA = [1,2,3,4,5]
# print(type(listA))
# for i in listA:
#     print(i)
# next(listA) # TypeError: 'list' object is not an iterator

"""  Iterators """ 
## Iterators object have the methods of  __iter__() and __next__()
## Convert an Iterable into Iterator by using iter()

## Example
# listA = [1,2,3,4,5]
# iterator = iter(listA)
# print(next(iterator))

"""  Custom Iterators """ 

# class Count:
##    Custom Iterator that counts upwards
#     def __init__(self,start=0):
#         self.num = start
#     def __iter__(self):
#         return self
#     def __next__ (self):
#         if self.num == 10:
#             raise StopIteration()
#         num = self.num
#         self.num = num + 1
#         return num
# fire = Count()
# print(next(fire))
# print(next(fire))
# print(next(fire))
# for i in Count():
#     print(i)

"""  What are Generators """ 

## Generator Function always have a Yield Keyword 
## Generator Function always returns a Iterator Object
## The returned Iterator Object by the Generator Function is called Generator Object
## Generator Objects are Lazy iterators as they do not store their content in memory

## Key_point All Generators are Iterators but All Iterators are not Generators

## Example
# def get_sequence_upto(x):
#     for i in range(x):
#         yield i
# seq = get_sequence_upto(3)
# print(next(seq))
# print(next(seq))
# print(next(seq))

"""  Using Generators """ 

"""  Generator Expression/Generator Comprehension? """ 
## my_set = (<Expression> for <Item> in <Iterable> if <Condition>)
# def Count():
#     for i in range(10):
#         yield i+1
## Example of Generator Expression/Generator Comprehension
# Count = (i+1 for i in range(10))
# print(next(Count))
# print(next(Count))
# print(next(Count))
# print(next(Count))
# print(next(Count))

"""  Advantages of using Generators? """ 

## 1 Easy to implement?
## Generator Expression/Generator Comprehension is the easy way of creating Iterators rather than creating OPP way of Iterators or Generator Function way of Iterators

## 2 Memory Efficient (& Time Efficient compared to List Comprehensions)?
## A function first create a sequence and store it the the memory and than return that sequence on the other hand Generators create a sequence on the go. Create a single element of sequence and return it.

## 3 Represent infinite Stream
## In python function can not create a infinite Stream but Generators can !

## 4 Pipelining Generators
## Exmple of Pipelining Generators
# def fibonacci_numbers(nums):
#     x, y = 0, 1
#     for _ in range(nums):
#         x, y = y, x + y
#         yield x
# def cube(numbers):
#     for num in numbers:
#         yield num**3
# print(sum(cube(fibonacci_numbers(5))))

""" Key-Point way of creating Iterators (OPP way of Iterators < Generator Function way of Iterators < Generator Expression/Generator Comprehension ) """ 

"""  Understanding Generators """ 

""" Everytime a generator reaches the Yield Keyword, the program suspends function execution and returns the Yielded value to the caller. 
The state of the function is saved, allowing it to resume whenever generator methods called, from the point it was suspended at earlier """

## Key-Point Generator objects can make use of the following methods:
## .send() 
## .throw()
## .close()

""" Quiz """
# 1
# Which of the following are false?
# Generator function can only have one yield: True
# Generator functions can only have one return keyword: False
# Generator functions cannot have yield and return together: True

# 2
# Generator functions can generate infinite values?
# True

# 3
# Which of the following is an advantage of a generator?
# Generators consume less memory

# 4
# “A map function returns a generator”?
# True

# 5
# “Generator expressions create anonymous generator functions”?
# True

# 6
# squares = (x*x for x in range(5))
# print(next(squares))
# print(next(squares))
# print(next(squares))
# print(next(squares))
# print(next(squares))