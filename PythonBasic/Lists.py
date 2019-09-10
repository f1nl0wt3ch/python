# In python we couldn't use "plus" mark to combine string and number. Number should be converted to string.
thislist = ["orange", "apple", "banana"]
# Check an item is exist in list or not
if "apples" in thislist:
    print("Yes, apple is in the list")
elif "orange" and "apple" in thislist:
    print("Yes, orange is also in the list")
else:
    print("No one is in the list")

if len(thislist) > 0:
   print("There is "+str(len(thislist))+" items in the list")
else:
   print("The list is empty")
# Add more item to the list
thislist.append("cherry")
print(thislist)
# Add a new item to the first of list
thislist.insert(0, "cherry")
print("List after insert an item  to the first position of list:"+str(thislist))
# Remove an item from a list
thislist.remove("cherry")
print("List after remove: "+ str(thislist))
# Remove all item, that matched to keyword
list(filter(lambda x: x != "cherry"), thislist)
print(thislist)
# Create an object with 2 lists
list_object = zip(list1, list2)
# Length of a List
my_list = [1, 2, 3, 4, 5]
print(len(my_list)) // 5
# Generate a list using range
list = range(2, 20, 2) //will generate a list of numbers from 2 to 19 and it skips 2 item
# Selecting List Elements I
thislist[2] // will print banana
# Get the last item of list 
thislist[-1] // will print banana
# Slicing Lists
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
sublist = letters[1:6]
print(sublist) // ['b', 'c', 'd', 'e', 'f']
# Counting elements in a list
letters = ['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
num_i = letters.count('i')
print(num_i) // 4
# Sorting Lists I
names = ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
names_sort = names.sort()
print(names) // ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
print(names_sorted) // None
# Sorting Lists II
names = ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
sorted_names = sorted(names)
print(sorted_names) // ['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
print(names) // ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
# Review
inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']
inventory_len = len(inventory) // How many items are in the warehouse?
first = inventory[0] // Select the first element in inventory
last = inventory[-1] // Select the last element in inventory
three_lasts = inventory[-3:] // Select the last 3 elements in inventory
inventory_2_6 = inventory[2:6] // Select items from the inventory starting at index 2 and up to, but not including, index 6
first_3 = inventory[0:3] // Select the first 3 items of inventory
twin_beds = inventory.count('twin bed') // How many 'twin bed's are in inventory
inventory.sort() // Sort inventory using .sort()

# Len's Slice
toppings = ['pepperoni','pineapple','cheese','sausage','olives','anchovies','mushrooms']
prices = [2, 6, 1, 3, 2, 7, 2]
num_pizzas = len(toppings)
print("We sell "+str(num_pizzas)+" different kinds of pizza!")
pizzas = list(zip(prices, toppings))
pizzas.sort()
print(pizzas)
cheapest_pizza = pizzas[0]
print(cheapest_pizza)
priciest_pizza = pizzas[-1]
print(priciest_pizza)
print(pizzas[0:3])
num_two_dollar_slices = pizzas.count(2)
num_two_dollar_slices = []
for i in pizzas:
    if i[0] == 2:
      num_two_dollar_slices.append(i)

print(num_two_dollar_slices)

# Double Index
