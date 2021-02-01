"""
You may remember the concept of scope from when you were learning about functions in Python. If a variable is defined inside of a function, it will not be accessible outside of the function.

Scope also applies to classes and to the files you are working within.

Files have scope? You may be wondering.

Yes. Even files inside the same directory do not have access to each other’s variables, functions, classes, or any other code. So if I have a file sandwiches.py and another file hungry_people.py, how do I give my hungry people access to all the sandwiches I defined?

Well, files are actually modules, so you can give a file access to another file’s content using that glorious import statement.

With a single line of from sandwiches import sandwiches at the top of hungry_people.py, the hungry people will have all the sandwiches they could ever want.

"""
# Import library below:
from library import always_three

# Call your function below:
always_three()
