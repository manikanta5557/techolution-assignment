from book import *
from user import *
from storage import *
from check import *
import logging
# for logging we will use logging module and storage module in library_management.log
logging.basicConfig(filename='library_management.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
#Main class for total library interface:
# The LibraryInterface class functions as a Facade,
# providing a simplified interface to the complex underlying system involving book and user management as well as checkout processes. 
class LibraryInterface:
    def __init__(self):
        self.storage = Storage('library_data.json')
        self.book_manager = BookManager(self.storage)
        self.user_manager = UserManager(self.storage)
        self.checkout_manager = CheckoutManager(self.storage)

    def run(self):
        while True:
            # list out all the choices to the user:
            print("\n1. Add Book")
            print("2. Update Book")
            print("3. Delete Book")
            print("4. List Books")
            print("5. Search Books")
            print("6. Add User")
            print("7. Update User")
            print("8. Delete User")
            print("9. List Users")
            print("10. Search Users")
            print("11. Checkout Book")
            print("12. Checkin Book")
            print("13. Track Book")
            print("14. List Checked Out Books")
            print("15. Exit")
            
            choice = input("Choose an option: ")
            # based on the selected choice we use the conditions:
            if choice == '1':
                title = input("Enter book title: ")
                while True:
                    author = input("Enter author name: ")
                    if any(char.isdigit() for char in author):
                        print("Author Name should contain characters only:")
                    else:
                        break
                while True:
                    isbn = input("Enter ISBN of the book: ")
                    if any(char.isalpha() for char in isbn):
                        print("ISBN number should contain integers only:")
                    else:
                        break
                self.book_manager.add_book(Book(title, author, isbn))
                print("Book successfully added!")
            elif choice == '2':
                while True:
                    isbn = input("Enter ISBN of the book to update: ")
                    if any(char.isalpha() for char in isbn):
                        print("ISBN number should contain integers only:")
                    else:
                        break
                title = input("Enter new book title: ")
                while True:
                    author = input("Enter new author name: ")
                    if any(char.isdigit() for char in author):
                        print("Author Name should contain characters only:")
                    else:
                        break
                new_book = Book(title, author, isbn)
                self.book_manager.update_book(isbn, new_book)
                print("Book successfully updated!")
            elif choice == '3':
                while True:
                    isbn = input("Enter ISBN of the book to delete: ")
                    if any(char.isalpha() for char in isbn):
                        print("ISBN number should contain integers only:")
                    else:
                        break
                self.book_manager.remove_book(isbn)
                print("Book successfully deleted!")
            elif choice == '4':
                books = self.book_manager.list_books()
                for isbn, details in books.items():
                    print(Book(**details))
            elif choice == '5':
                search_by = input("Search by (title, author, isbn): ")
                search_term = input("Enter search term: ")
                results = self.book_manager.search_books(search_term, search_by)
                for isbn, book in results.items():
                    print(f"{isbn}: {Book(**book)}")
            elif choice == '6':
                user_id = input("Enter user ID: ")
                while True:
                    name = input("Enter user name: ")
                    if any(char.isdigit() for char in name):
                        print("User Name should contain characters only:")
                    else:
                        break
                self.user_manager.add_user(User(user_id, name))
                print("User added to database!")
            elif choice == '7':
                user_id = input("Enter user ID of the user to update: ")
                while True:
                    name = input("Enter new user name: ")
                    if any(char.isdigit() for char in name):
                        print("User Name should contain characters only:")
                    else:
                        break
                new_user = User(user_id, name)
                self.user_manager.update_user(user_id, new_user)
                print("User info updated!")
            elif choice == '8':
                user_id = input("Enter user ID of the user to delete: ")
                self.user_manager.remove_user(user_id)
                print("User successfully deleted!")
            elif choice == '9':
                users = self.user_manager.list_users()
                for user_id, details in users.items():
                    print(User(**details))
            elif choice == '10':
                search_by = input("Search by (name, user_id): ")
                search_term = input("Enter search term: ")
                results = self.user_manager.search_users(search_term, search_by)
                for user_id, user in results.items():
                    print(f"{user_id}: {User(**user)}")
            elif choice == '11':
                user_id = input("Enter User ID: ")
                while True:
                    isbn = input("Enter ISBN of the book to checkout: ")
                    if any(char.isalpha() for char in isbn):
                        print("ISBN number should contain integers only:")
                    else:
                        break
                print(self.checkout_manager.checkout_book(isbn, user_id))
                print(f"Book successfully checked out to user {isbn}")
            elif choice == '12':
                while True:
                    isbn = input("Enter ISBN of the book to checkin: ")
                    if any(char.isalpha() for char in isbn):
                        print("ISBN number should contain integers only:")
                    else:
                        break
                print(self.checkout_manager.checkin_book(isbn))
                print(f"Book with {isbn} number is checked in")
            elif choice == '13':
                while True:
                    isbn = input("Enter ISBN of the book to track:")
                    if any(char.isalpha() for char in isbn):
                        print("ISBN number should contain integers only:")
                    else:
                        break
                print(self.checkout_manager.track_book(isbn))
            elif choice == '14':
                print(self.checkout_manager.list_checked_out_books())
            elif choice == '15':
                print("Exiting...")
                break

if __name__ == "__main__":
    interface = LibraryInterface()
    interface.run()
