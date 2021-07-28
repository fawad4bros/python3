'''
Recursion: Recursion involves calling the same function again, and hence, has
 a very small length of code. However, as we saw in the analysis, the time
 complexity of recursion can get to be exponential when there are a
 considerable number of recursive calls. Hence, usage of recursion is
 advantageous in shorter code, but higher time complexity.

Iteration: Iteration is repetition of a block of code. This involves a larger
size of code, but the time complexity is generally lesser than it is for
recursion.

'''


# Iterative binary search
def binary_search(list, target):
    first = 0
    # Every List starts at 0 index that's why we are storing 0 in first variable.
    last = len(list) - 1
    # Storing the last index of list in last variable.
    while first <= last:
        midpoint = (first + last) // 2
        # Finding the midpoint index of the list.
        if list[midpoint] == target:
            # if the midpoint index value is equal to target value.
            return midpoint
        elif list[midpoint] < target:
            # if midpoint index value is less then target value.
            first = midpoint + 1
            # increase the index value by 1: Go on the right side of the list.
        else:
            last = midpoint - 1
            # decrease the index value by 1: Go left side of the list.
    return None


def verify(index):
    if index is not None:
        print(f"Target value found in the list at {index} index")
    else:
        print("Target value not found in the list")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = binary_search(numbers, 10)
verify(result)


# Recursive binary search

def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2
        if list[midpoint] == target:
            return midpoint
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint + 1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)


def verify(index):
    if index is not None:
        print(f"Recursive_binary_search: target has been found at {index} index ")
    else:
        print("Target has been not found")


result = recursive_binary_search(numbers, 6)
verify(result)
