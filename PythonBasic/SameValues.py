"""
Write a function named same_values() that takes two lists of numbers of equal size as parameters.

The function should return a list of the indices where the values were equal in lst1 and lst2.

For example, the following code should return [0, 2, 3]

same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])
"""


# Write your function here
def same_values(lst1, lst2):
    new_list = []
    for i in range(0, len(lst1)):
        if lst1[i] == lst2[i]:
            new_list.append(i)
    return new_list


# Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
