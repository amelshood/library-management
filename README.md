# Library Management System

A Python-based library management system that enables managing books, users, and borrowing operations in a library setting.

## Features

- **Book Management**: Add, remove, and track books in the library
- **User Management**: Register, remove, and manage library users
- **Borrowing System**: Allow users to borrow and return books
- **Availability Tracking**: Monitor which books are available or borrowed
- **User History**: Track which books are borrowed by each user

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/amelshood/library-management.git
cd library-management
```

No additional dependencies are required as this project uses only Python's standard library.

## Project Structure

```
library-management/
├── library.py                 # Main implementation
├── test_library.py            # Test suite
├── README.md                  # This file
└── .gitignore                 # Git ignore file
```

## Usage

### Basic Usage

```python
from library import Book, User, Library

# Create a library
library = Library()

# Add books to the library
book = Book("Book1", "Author1", "1234567")
library.add_book(book)

# Register a user
user = User("User1", "001")
library.add_user(user)

# Borrow a book
library.borrow_book(user, book)

# View borrowed books
borrowed_books = user.view_borrowed_books()
print(borrowed_books)

# Return a book
library.return_book(user, book)

# List available books
available_books = library.list_available_books()
print(available_books)
```

### Running the Example

To see a full demonstration of the library system in action, run:

```bash
python example.py
```

This will show various operations including:
- Adding books and users
- Borrowing and returning books
- Listing available books
- Viewing user borrowed books

## Classes and Methods

### Book Class

Represents a book in the library.

- `__init__(title, author, isbn)` - Create a new book
- `borrow_book()` - Mark the book as borrowed
- `return_book()` - Mark the book as returned/available

### User Class

Represents a library user.

- `__init__(name, user_id)` - Create a new user
- `borrow_book(book)` - Borrow a book
- `return_book(book)` - Return a borrowed book
- `view_borrowed_books()` - View all books borrowed by the user

### Library Class

Manages the overall library system.

- `add_book(book)` - Add a book to the library
- `remove_book(book)` - Remove a book from the library
- `add_user(user)` - Register a user
- `remove_user(user)` - Remove a user
- `borrow_book(user, book)` - Process a book borrowing
- `return_book(user, book)` - Process a book return
- `list_available_books()` - List all available books

## Testing

Run the test suite to verify all functionality:

```bash
python test_library.py
```

The tests cover all major components and functions of the library system.

## Acknowledgments

- This project was created as a learning exercise for object-oriented programming in Python.