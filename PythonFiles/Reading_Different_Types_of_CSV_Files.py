"""
Reading Different Types of CSV Files
I need to level with you, I’ve been lying to you for the past two exercises. Well, kind of. We’ve been acting like CSV files are Comma-Separated Values files. It’s true that CSV stands for that, but it’s also true that other ways of separating values are valid CSV files these days.

People used to call Tab-Separated Values files TSV files, but as other separators grew in popularity everyone realized that creating a new .[a-z]sv file format for every value-separating character used is not sustainable.

So we call all files with a list of different values a CSV file and then use different delimiters (like a comma or tab) to indicate where the different values start and stop.

Let’s say we had an address book. Since addresses usually use commas in them, we’ll need to use a different delimiter for our information. Since none of our data has semicolons (;) in them, we can use those.

addresses.csv

Name;Address;Telephone
Donna Smith;126 Orr Corner Suite 857\nEast Michael, LA 54411;906-918-6560
Aaron Osborn;6965 Miller Station Suite 485\nNorth Michelle, KS 64364;815.039.3661x42816
Jennifer Barnett;8749 Alicia Vista Apt. 288\nLake Victoriaberg, TN 51094;397-796-4842x451
Joshua Bryan;20116 Stephanie Stravenue\nWhitneytown, IA 87358;(380)074-6173
Andrea Jones;558 Melissa Keys Apt. 588\nNorth Teresahaven, WA 63411;+57(8)7795396386
Victor Williams;725 Gloria Views Suite 628\nEast Scott, IN 38095;768.708.3411x954
Notice the \n character, this is the escape sequence for a new line. The possibility of a new line escaped by a \n character in our data is why we pass the newline='' keyword argument to the open() function.

Also notice that many of these addresses have commas in them! This is okay, we’ll still be able to read it. If we wanted to, say, print out all the addresses in this CSV file we could do the following:

import csv

with open('addresses.csv', newline='') as addresses_csv:
  address_reader = csv.DictReader(addresses_csv, delimiter=';')
  for row in address_reader:
    print(row['Address'])
Notice that when we call csv.DictReader we pass in the delimiter parameter, which is the string that’s used to delineate separate fields in the CSV. We then iterate through the CSV and print out each of the addresses.
"""
import csv

isbn_list = []
with open('books.csv') as books_csv:
    books_reader = csv.DictReader(books_csv, delimiter='@')
    for row in books_reader:
        print(row)
        isbn_list.append(row.get('ISBN'))
