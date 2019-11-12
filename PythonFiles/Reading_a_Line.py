"""
Reading a Line
Sometimes you don’t want to iterate through a whole file. For that, there’s a different file method, .readline(), which will only read a single line at a time. If the entire document is read line by line in this way subsequent calls to .readline() will not throw an error but will start returning an empty string (""). Suppose we had this file:

millay_sonnet.txt

with open('millay_sonnet.txt') as sonnet_doc:
  first_line = sonnet_doc.readline()
  second_line = sonnet_doc.readline()
  print(second_line)
This script also creates a file object called sonnet_doc that points to the file millay_sonnet.txt. It then reads in the first line using sonnet_doc.readline() and saves that to the variable first_line. It then saves the second line (So make the most of this, your little day,) into the variable second_line and then prints it out.

"""
with open('welcome.txt') as first_line_doc:
     first_line = first_line_doc.readline()
     print(first_line)