numbers = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,10]
### Example

# even = []
# def findEven(numbers):
#     for each in numbers:
#         if each % 2 == 0:
#             even.append(each)
# findEven(numbers)
# print(even)

### Applying list comprehension

# evenList = [each for each in numbers if each % 2 == 0]
# print(sorted(evenList))

### Example

# evenSet = set()
# def getEvenSet(numbers):
#     for each in numbers:
#         if each % 2 == 0:
#             evenSet.add(each)
# getEvenSet(numbers)
# print(evenSet)

### Applying set comprehension

# evenSet = {each for each in numbers if each % 2 == 0}
# print(sorted(evenSet))

### Example
dic = {'fawad':1,'hammad':2,'saad':3,'jawad':4}
# evenIds = {}
# def getEvenId(dic):
#     for key, value in dic.items():
#         if value % 2 == 0:
#             evenIds.update({key:value})
# getEvenId(dic)
# print(evenIds)

### Applying dictionary comprehension

# evenIds = {key:value for key,value in dic.items() if value % 2 == 0}
# print(evenIds)

nList = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# evenNlist = []
# def getEven(nList):
#     for otrEach in nList:
#         for inrEach in otrEach:
#             if inrEach % 2 == 0:
#                 evenNlist.append(inrEach)
# getEven(nList)
# print(evenNlist)

### Applying nasted comprehension

# nEven = [[x for x in y if x % 2 == 0] for y in nList]
# print(nEven)