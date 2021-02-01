"""
Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.

The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.
"""


# Write your function here
def larger_sum(lst1, lst2):
    lst1_sum = 0
    lst2_sum = 0
    for i in lst1:
        lst1_sum += i
    for j in lst2:
        lst2_sum += j
    if lst1_sum >= lst2_sum:
        return lst1
    else:
        return lst2


# Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))
