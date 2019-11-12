"""
datetime is just the beginning. There are hundreds of Python modules that you can use. Another one of the most commonly used is random which allows you to generate numbers or select items at random.

With random, we’ll be using more than one piece of the module’s functionality, so the import syntax will look like:

import random
We’ll work with two common random functions:

random.choice() which takes a list as an argument and returns a number from the list
random.randint() which takes two numbers as arguments and generates a random number between the two numbers you passed in
Let’s take randomness to a whole new level by picking a random number from a list of randomly generated numbers between 1 and 100.
"""

# Import random below:
import random

# Create random_list below:
random_list = []

# Create randomer_number below:
random_list = [random.randint(1, 101) for i in range(101)]
print(random_list)
#for i in range(0,101):
    #print(random.randint(1, 100))
#    random_list.append(random.randint(1, 100))

# Print randomer_number below:
randomer_number = random.choice(random_list)
print(randomer_number)