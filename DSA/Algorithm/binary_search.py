'''
algo time: Constant, linear, logarithmic, quadratic.
Recursion: Recursion involves calling the same function again, and hence, has
 a very small length of code. However, as we saw in the analysis, the time
 complexity of recursion can get to be exponential when there are a
 considerable number of recursive calls. Hence, usage of recursion is
 advantageous in shorter code, but higher time complexity.

Iteration: Iteration is repetition of a block of code. This involves a larger
size of code, but the time complexity is generally lesser than it is for
recursion.

'''


# Iterative solution means, a solution is implemented using a loop structure of some kind.
# Iterative binary search
def binary_search(list, target):
    # In functional languages we try to avoid changing data (Variables: first, last ) that is given to a function.
    # functional languages do not like to modify data given to function, prefer a solution using recursion.
    # Python does not like recursion, python has maximum recursion depth, after that which are function hold execution.
    # Python's default recursion limit is 1000.
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


# Time complexity:
# Space complexity: Big O (1) constant space

# Recursive solution is a set of stopping condition and a function that call itself.
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
                # Returning a new list with the range [midpoint + 1: n-1]
                # New list is the sub-list of the previous list
                # Imp_Note: How many time a recursive function is called is known as recursive depth.
                return recursive_binary_search(list[midpoint + 1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)
            # python does not implement tail optimization


def verify(index):
    if index is not None:
        print(f"Recursive_binary_search: target has been found at {index} index ")
    else:
        print("Target has been not found")


result = recursive_binary_search(numbers, 6)
verify(result)

# Time complexity: logarithmic time Big O (log n)
# Space complexity: logarithmic space Big O (log n)
