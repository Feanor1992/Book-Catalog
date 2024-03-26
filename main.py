import os
import re
import tkinter
from tkinter import messagebox

# Determining the directory with books
library_dir = 'I:\Artem\Library'

# Creating a dictionary to store a catalog of books
books = {}


# function recursively scans the directory of books and adds all found books to the books dictionary
def scan_directory(directory):
    for item in os.listdir(directory):
        # create the full path by joining the directory path with the item name
        item_path = os.path.join(directory, item)

        # check if the item is a directory using
        if os.path.isdir(item_path):
            scan_directory(item_path)
        else:
            # getting the book title from the file name
            book_name = re.split('\.', item)[0]

            # add book to a dictionary
            books[book_name] = {
                "author": directory.split('\\')[-1],
                'read': False,
                'path': item_path
            }


















































