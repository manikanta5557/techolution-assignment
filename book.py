# # Global list to store books
# books = []

# def add_book(title, author, isbn):
#     books.append({"title": title, "author": author, "isbn": isbn})

# def list_books():
#     for book in books:
#         print(book)
import logging
logging.basicConfig(filename='library_management.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"
class BookManager:
    def __init__(self, storage):
        self.storage = storage

    def add_book(self, book):
        """
        Adds a new book to the storage only if it does not already exist by ISBN.

        Args:
            self: The instance of the class.
            book (Book): The book object to be added to the storage.

        """
        books = self.storage.list_books()
        if book.isbn in books:
            # Log attempt to add a duplicate book
            logging.error(f"Attempted to add duplicate book with ISBN: {book.isbn}")
            print(f"Book with ISBN {book.isbn} already exists.")
            return
        self.storage.add_book(book)
        logging.info(f"Added book: {book}")
    def update_book(self, isbn, new_book):
        """Update an existing book's details.

        Args:
            self: The instance of the class.
            isbn : The ISBN of the book to be checked in.
            new_book (Book): The book object to be added to the storage.

        """
        data = self.storage.read_data()
        if isbn in data['books']:
            data['books'][isbn] = new_book.__dict__
            self.storage.write_data(data)
            logging.info(f"Updated book: {new_book}")
        else:
            print("Book with the given ISBN does not exist.")
            logging.error(f"Book with the given ISBN does not exist , isbn : {isbn}")
    def remove_book(self, isbn):
        """Remove a book from storage."""
        data = self.storage.read_data()
        if isbn in data['books']:
            del data['books'][isbn]
            self.storage.write_data(data)
            logging.info(f"Removed book with ISBN: {isbn}")
        else:
            print("Book with the given ISBN does not exist.")
            logging.error(f"Book with the given ISBN does not exist. isbn : {isbn}")
    def list_books(self):
        """List all books."""
        logging.info("Listed all books")
        return self.storage.list_books()

    def search_books(self, search_term, search_by='title'):
        """Search books by a given attribute (title, author, isbn)."""
        valid_search_terms = ['title', 'author', 'isbn']
        if search_by not in valid_search_terms:
            print("Invalid search type provided. Valid options are: title, author, isbn.")
        result = {}
        books = self.storage.list_books()
        for isbn, book in books.items():
            if search_term.lower() in book.get(search_by, '').lower():
                result[isbn] = book
        if len(result)== 0:
            print("No search items found with the given search item.")
        return result
