new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # These values are not stored in memory
'''
Instead of value are stored elsewhere in the memory and array stores the references each of these object Array 
memory is contiguous for this reason, access is a constant time operation on array or python list arrays are really
fast in accessing values (Reading values in constant time) and pretty bad in searching, insertion, deletion values. 
'''
List = []
# List has allocated space of n+1.
print(len(List))
# Still its length is 0

# Append: Constant time Big O(1): Ammortized constant space complexity
List.append(20)
# Still its length is the same: 0
List.append(500)

'''
Before appending 500 to the list,
python will increase the memory allocation,
python does this by calling resize operation,
resize operation will increase the memory allocation by 4 blocks,
the growth pattern of the list type in python is: 0 4 8 16 25 35 46.
'''

List.extend(new_list)
# Extend: runtime operation Big O (n)
'''Extend makes a series of append calls on each of the elements in the new list until all of them have been appended 
into original list.'''
print(List)
# Searching
if 9 in new_list: print("Found it")

# Delete: Linear Runtime O(n) : This operation shift every element to the left.
# Insert: Linear Runtime O(n) : This operation shift every element to the right.
