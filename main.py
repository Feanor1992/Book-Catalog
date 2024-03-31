import os
import re
import tkinter as tk
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


# function for displaying a book catalog
def show_catalog():
    # iterate over each book in the books list
    for book_name in books:
        book_frame = tk.Frame(main_window)
        book_frame.pack()

        # label for book name
        book_name_label = tk.Label(book_frame, text=book_name)
        book_name_label.pack(side=tk.LEFT)

        # label for author
        author_label = tk.Label(book_frame, text=books[book_name]['author'])
        author_label.pack(side=tk.LEFT)

        # checkbox for read status
        read_checkbox = tk.Checkbutton(book_frame, variable=books[book_name]['read'])
        read_checkbox.pack(side=tk.RIGHT)


# function for searching books
def search_book(query):
    results = []
    for book_name in books:
        if query in book_name or query in books[book_name]['author']:
            results.append(book_name)
    return results


# Function to display search results
def show_search_results(results):
    search_results_frame.pack()
    for book_name in results:
        book_frame = tk.Frame(search_results_frame)
        book_frame.pack()

        # label for book name
        book_name_label = tk.Label(book_frame, text=book_name)
        book_name_label.pack(side=tk.LEFT)

        # label for author
        author_label = tk.Label(book_frame, text=books[book_name]['author'])
        author_label.pack(side=tk.LEFT)


# function for marking a book as read
def mark_as_read(book_name):
    books[book_name]['read'] = True


# main window
main_window = tk.Tk()
main_window.geometry('600x400')

# search bar
search_bar = tk.Entry(main_window)
search_bar.pack()

# search button
search_button = tk.Button(main_window, text="Search",
                          command=lambda: show_search_results(search_book(search_bar.get())))
search_button.pack()

# catalog frame
catalog_frame = tk.Frame(main_window)
catalog_frame.pack()

# search results frame
search_results_frame = tk.Frame(main_window)

# scanning a directory with books
scan_directory(library_dir)

# displaying the book catalog
#show_catalog()

# start the main loop
main_window.mainloop()








































