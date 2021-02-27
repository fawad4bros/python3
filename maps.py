#Apply a function on data and return new list of data
from random import shuffle
def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)
words = ['fawad','hammad','saad','jawad']
anagrams = []

for word in words:
    anagrams.append(jumble(word))
print(anagrams)
# or
#map(function,data)

print(list(map(jumble,words)))

#Comprehensions Method
print([jumble(word) for word in words])