"""
Create a function called middle_element that has one parameter named lst.

If there are an odd number of elements in lst, the function should return the middle element. If there are an even number of elements, the function should return the average of the middle two elements.
"""


# Write your function here
def middle_element(lst):
    lst_len = len(lst)
    if (lst_len % 2) != 0:
        odd_index = int((lst_len - 1) / 2)
        print(odd_index)
        return lst[odd_index]
    else:
        even_index = int(lst_len / 2)
        return int((lst[even_index - 1] + lst[even_index]) / 2)


# Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
