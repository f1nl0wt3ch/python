"""
Writing a File
Reading a file is all well and good, but what if we want to create a file of our own? With Python we can do just that. It turns out that our open() function that we’re using to open a file to read needs another argument to open a file to write to.

with open('generated_file.txt', 'w') as gen_file:
  gen_file.write("What an incredible file!")
Here we pass the argument 'w' to open() in order to indicate to open the file in write-mode. The default argument is 'r' and passing 'r' to open() opens the file in read-mode as we’ve been doing.

This code creates a new file in the same folder as script.py and gives it the text What an incredible file!. It’s important to note that if there is already a file called generated_file.txt it will completely overwrite that file, erasing whatever its contents were before.
"""

with open('bad_bands.txt', 'w') as bad_bands_doc:
    bad_bands_doc.write("Hello Python")
