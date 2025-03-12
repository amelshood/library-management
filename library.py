class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def __str__(self):  
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

    def borrow_book(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        if not self.available:
            self.available = True
            return True
        return False

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow_book():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book)
            return True
        return False

    def view_borrowed_books(self):
        if not self.borrowed_books:
            return 'No books borrowed.'
        return [str(book) for book in self.borrowed_books]

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        for existing_book in self.books:
            if existing_book.isbn == book.isbn:
                return False
        self.books.append(book)
        return True

    def remove_book(self, book):
        for book in self.books:
            self.books.remove(book)
            return True
        return False

    def add_user(self, user):
        for existing_user in self.users:
            if existing_user.user_id == user.user_id:
                return False
        self.users.append(user)
        return True

    def remove_user(self, user):
        for user in self.users:
            self.users.remove(user)
            return True
        return False

    def borrow_book(self, user, book):
        if book in self.books and user in self.users and book.available:
            return user.borrow_book(book)
        return False

    def return_book(self, user, book):
        if book in self.books and user in self.users:
            return user.return_book(book)
        return False

    def list_available_books(self):
        available_books = [book for book in self.books if book.available]
        return [str(book) for book in available_books]