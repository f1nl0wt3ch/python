"""Create a function named double_index that has two parameters named lst and index.
The function should return a new list where all elements are the same as in lst except for the element at index, which should be double the value of the element at index of lst.
If index is not a valid index, the function should return the original list.

For example, the following code should return [1,2,6,4] because the element at index 2 has been doubled:

double_index([1, 2, 3, 4], 2)
After writing your function, un-comment the call to the function that we’ve provided for you to test your results.
"""


def double_index(lst, index):
    lst_len = len(lst)
    if index >= lst_len:
        return lst
    else:
        new = lst[index] * 2
        lst[index] = new
        return lst


# Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))
