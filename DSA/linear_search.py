def linear_search(lists, target):
    # Taking a list and a number from the user.
    for i in range(0, len(lists)):
        # Taking the length of the lists and setting it as the range.
        if lists[i] == target:
            # If the the value at lists[i] is equal to the target (number provided by the user)
            return i
            # Return the index of the Target value.
    return None
    # Return None if there is no match found.


def verify(index):
    # Taking the index parameter
    if index is not None:
        # If index parameter is not null (must be holding some value)
        print("Target found at", index)
        # Printing the index of the value
    else:
        print("target not found in list")


number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = linear_search(number, 11)
verify(result)
result = linear_search(number, 9)
verify(result)