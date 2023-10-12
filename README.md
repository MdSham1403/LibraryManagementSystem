# LibraryManagementSystem

Project Title: Library Management System in Python

Description:
This Python script demonstrates a simple Library Management System, which allows users to perform essential operations related to managing library books. The script uses a dictionary to store book information and provides a command-line interface for users to interact with the library.

Code Description:

1.Initialization: The code starts with the initialization of an empty dictionary named library, which is used to store book records.

2.Add a Book:

The add_book function prompts the user to input details of a new book, including the title, author, and the number of copies.
If the book already exists in the library, the code increments the number of copies. If not, a new entry is added to the library.
3.Display Available Books:

The display_books function lists all the available books in the library, including their titles, authors, and the number of copies.
4.Borrow a Book:

The borrow_book function allows users to borrow a book by entering the book's title.
It checks if the book is available and reduces the number of copies if it is. If the book is out of stock or not in the library, appropriate messages are displayed.
5.Return a Book:

The return_book function enables users to return a borrowed book by entering the book's title.
It increments the number of copies if the book exists in the library; otherwise, it informs the user that the book is not found.
6.Main Menu:

The script displays a main menu that provides options for various actions, including adding, displaying, borrowing, and returning books. Users can also choose to quit the system.
7.User Interaction:

The code uses input to gather user input and responds accordingly based on the selected menu option.
Usage:

Users run the script, and it presents them with a menu to perform library management tasks.
Users can add books, view available books, borrow books, return books, or exit the system.
Enhancements:

This code serves as a basic demonstration of a library management system. To make it more practical, you can consider implementing features like a persistent database, user authentication, and more complex user interactions.
You may also want to add error handling to make the code more robust.
