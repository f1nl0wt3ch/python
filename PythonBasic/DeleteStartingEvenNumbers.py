"""
Write a function called delete_starting_evens() that has a parameter named lst.

The function should remove elements from the front of lst until the front of the list is not even. The function should then return lst.

For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].

Make sure your function works even if every element in the list is even!
"""


# Write your function here
def delete_starting_evens(lst):
    for index in range(0, len(lst)):
        if lst[index] % 2 == 0:
            continue
        else:
            break
    if (index == len(lst) - 1):
        return []
    else:
        return lst[index:len(lst)]


# Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
