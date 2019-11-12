"""
Notice that when we want to invoke the randint() function we call random.randint(). This is default behavior where Python offers a namespace for the module. A namespace isolates the functions, classes, and variables defined in the module from the code in the file doing the importing. Your local namespace, meanwhile, is where your code is run.

Python defaults to naming the namespace after the module being imported, but sometimes this name could be ambiguous or lengthy. Sometimes, the module’s name could also conflict with an object you have defined within your local namespace.

Fortunately, this name can be altered by aliasing using the as keyword:

import module_name as name_you_pick_for_the_module
Aliasing is most often done if the name of the library is long and typing the full name every time you want to use one of its functions is laborious.

You might also occasionally encounter import *. The * is known as a “wildcard” and matches anything and everything. This syntax is considered dangerous because it could pollute our local namespace. Pollution occurs when the same name could apply to two possible things. For example, if you happen to have a function floor() focused on floor tiles, using from math import * would also import a function floor() that rounds down floats.

Let’s combine your knowledge of the random library with another fun library called matplotlib, which allows you to plot your Python code in 2D.

You’ll use a new random function random.sample() that takes a range and a number as its arguments. It will return the specified number of random numbers from that range.
"""
import codecademylib3_seaborn
from matplotlib import pyplot as plt
import random

# Add your code below:
numbers_a = range(1,13)
print(numbers_a)
numbers_b = [ random.randint(0, 1000) for i in range(12) ]
print(numbers_b)
plt.plot(numbers_a, numbers_b)
plt.show()