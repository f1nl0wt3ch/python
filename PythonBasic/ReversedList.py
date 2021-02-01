"""
Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.

The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.

For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.
"""


# Write your function here
def reversed_list(lst1, lst2):
    sorted_lst2 = sorted(lst2)
    for index in range(0, len(lst1)):
        if lst1[index] != sorted_lst2[index]:
            return False
    return True


# Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
