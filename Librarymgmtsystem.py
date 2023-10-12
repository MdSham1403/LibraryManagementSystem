library = {}  # Dictionary to store library books

# Function to add a book to the library
def add_book():
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    copies = int(input("Enter the number of copies: "))
    
    if title in library:
        library[title]['copies'] += copies
    else:
        library[title] = {'author': author, 'copies': copies}

# Function to display available books
def display_books():
    print("\nAvailable Books:")
    for title, info in library.items():
        print(f"Title: {title}, Author: {info['author']}, Copies available: {info['copies']}")

# Function to borrow a book
def borrow_book():
    title = input("Enter the title of the book you want to borrow: ")
    
    if title in library and library[title]['copies'] > 0:
        library[title]['copies'] -= 1
        print(f"You have borrowed '{title}'. Enjoy your reading!")
    elif title in library and library[title]['copies'] == 0:
        print("Sorry, this book is currently out of stock.")
    else:
        print("Book not found in the library.")

# Function to return a book
def return_book():
    title = input("Enter the title of the book you are returning: ")
    
    if title in library:
        library[title]['copies'] += 1
        print(f"Thank you for returning '{title}'.")
    else:
        print("Book not found in the library.")

# Main menu
while True:
    print("\nLibrary Management System Menu:")
    print("1. Add a book")
    print("2. Display available books")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_book()
    elif choice == '2':
        display_books()
    elif choice == '3':
        borrow_book()
    elif choice == '4':
        return_book()
    elif choice == '5':
        print("Thank you for using the Library Management System.")
        break
    else:
        print("Invalid choice. Please try again.")
