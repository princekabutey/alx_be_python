class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return f"'{self.title}' checked out successfully."
        return f"'{self.title}' is already checked out."

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return f"'{self.title}' returned successfully."
        return f"'{self.title}' is already available."

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                return book.check_out()
        return f"No book found with title '{title}'."

    def return_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                return book.return_book()
        return f"No book found with title '{title}'."

    def list_available_books(self):
        available_books = [f"{book.title} by {book.author}" for book in self._books if not book._is_checked_out]
        if available_books:
            print("\n".join(available_books))
        else:
            print("No books available.")
