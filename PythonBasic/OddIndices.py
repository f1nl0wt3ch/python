"""
Create a function named odd_indices() that has one parameter named lst.

The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.

For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].
"""
#Write your function here
def odd_indices(lst):
    new_list = []
    for index in range(0, len(lst)):
        if index % 2 != 0:
           new_list.append(lst[index])
        else:
           continue
    return new_list

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))