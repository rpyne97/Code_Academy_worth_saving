# Use "with block" to open 'document.txt' and save in a temporary file_object cool_doc
# The with syntax replaces older ways to access files where you need to call .close() on the file object manually.
with open('document.txt') as cool_doc:
  # Read the contents of cool_doc
  cool_contents = cool_doc.read()
print(cool_contents)

# Add the 'w' argument to write text into file
# This will overwrite anything in the text file
# You must now read this text file again if you would like to access it in python namespace
with open('document.txt', 'w') as cool_doc:
    cool_doc.write('next cool thing')
print(cool_contents)

# Add the 'a' argument to append text into file
# You must now read this text file again if you would like to access it in python namespace
with open('document.txt', 'a') as cool_doc:
    cool_doc.write('next cool thing')
print(cool_contents)

# Reading csv files---------------------------------------------

# csv library
import csv
# pass the additional keyword argument newline='' to the file opening open() function so that we don’t accidentally mistake a line break in one of our data fields as a new row in our CSV
with open('cool_csv.csv', newline = '') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file) # create a DictReader object which uses the header row as keys
  for row in cool_csv_dict: # iterate through the dictionary rows
    print(row['Cool Fact']) # print each value for key 'Cool Fact'

# can add a delimit argument if it is not comma separated
# in this case, add the rows from the library key to a new list
with open('books.csv') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter = '@')
  for row in books_reader:
    isbn_list.append(row['ISBN'])

# Writing csv files---------------------------------------------

# Write the list of dictionaries to a csv file
access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
# There are shared keys across libraries. They can be used as the header row in the output file
fields = ['time', 'address', 'limit']

# Create a writeable file called 'logger.csv' and store in temp variable
with open('logger.csv', 'w') as logger_csv:
  log_writer = csv.DictWriter(logger_csv, fieldnames=fields) # create a csv.Dictwriter instance and use second argument to let it know the field names
  log_writer.writeheader() # write the header to the instance
  for item in access_log: # iterate through the list of dictionaries
    log_writer.writerow(item)
# Check to see what it looks like
with open('logger.csv') as logger_read:
    logger_view = logger_read.read()
# This file could now be easily imported into excel
print(logger_view)

# You will can also check to see this file was created in the cwd
import os
for file_name in os.listdir('.'):
    print(file_name)

# With pandas

