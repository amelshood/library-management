import unittest
from library import Book, User, Library

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("Book1", "Author1", "1234567")

    def test_book_creation(self):
        self.assertEqual(self.book.title, "Book1")
        self.assertEqual(self.book.author, "Author1")
        self.assertEqual(self.book.isbn, "1234567")
        self.assertTrue(self.book.available)

    def test_book_string_representation(self):
        expected_str = "Book1 by Author1 (ISBN: 1234567)"
        self.assertEqual(str(self.book), expected_str)

    def test_borrow_book(self):
        self.assertTrue(self.book.borrow_book())
        self.assertFalse(self.book.available)

    def test_return_book(self):
        self.book.borrow_book()
        self.book.return_book()
        self.assertTrue(self.book.available)

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("User1", "001")
        self.book = Book("Book1", "Author1", "1234567")

    def test_borrow_book(self):
        self.assertTrue(self.user.borrow_book(self.book))
        self.assertIn(self.book, self.user.borrowed_books)
        self.assertFalse(self.book.available)

    def test_return_book(self):
        self.user.borrow_book(self.book)
        self.assertTrue(self.user.return_book(self.book))
        self.assertNotIn(self.book, self.user.borrowed_books)
        self.assertTrue(self.book.available)

    def test_view_borrowed_books(self):
        self.assertEqual(self.user.view_borrowed_books(), "No books borrowed.")
        self.user.borrow_book(self.book)
        self.assertEqual(self.user.view_borrowed_books(), ["Book1 by Author1 (ISBN: 1234567)"])

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.user = User("User1", "001")
        self.book = Book("Book1", "Author1", "1234567")

    def test_add_book(self):
        self.assertTrue(self.library.add_book(self.book))
        self.assertEqual(len(self.library.books), 1)
        duplicate_book = Book("Book1", "Author1", "1234567")
        self.assertFalse(self.library.add_book(duplicate_book))
        self.assertEqual(len(self.library.books), 1)

    def test_remove_book(self):
        self.library.add_book(self.book)
        self.assertTrue(self.library.remove_book(self.book))
        self.assertEqual(len(self.library.books), 0)

    def test_add_user(self):
        self.assertTrue(self.library.add_user(self.user))
        self.assertEqual(len(self.library.users), 1)

    def test_remove_user(self):
        self.library.add_user(self.user)
        self.assertTrue(self.library.remove_user(self.user))
        self.assertEqual(len(self.library.users), 0)

    def test_borrow_book(self):
        self.library.add_user(self.user)
        self.library.add_book(self.book)
        self.assertTrue(self.library.borrow_book(self.user, self.book))
        self.assertFalse(self.book.available)

    def test_return_book(self):
        self.library.add_user(self.user)
        self.library.add_book(self.book)
        self.library.borrow_book(self.user, self.book)
        self.assertTrue(self.library.return_book(self.user, self.book))
        self.assertTrue(self.book.available)

    def test_list_available_books(self):
        self.library.add_book(self.book)
        available_books = self.library.list_available_books()
        self.assertEqual(len(available_books), 1)

        self.library.add_user(self.user)
        self.library.borrow_book(self.user, self.book)

        available_books = self.library.list_available_books()
        self.assertEqual(len(available_books), 0)

if __name__ == "__main__":
    unittest.main()


