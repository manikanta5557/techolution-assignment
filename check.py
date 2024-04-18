import logging
#  we use logging module to log all the actions in the library_management.log
logging.basicConfig(filename='library_management.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
class CheckoutManager:
    def __init__(self, storage):
        self.storage = storage

    def checkout_book(self, isbn, user_id):
        """
        Check out a book for a user.

        Args:
            self: The instance of the class.
            isbn : The ISBN of the book to be checked out.
            user_id (str): The ID of the user checking out the book.

        Returns:
            str: A message indicating the result of the checkout process."""
        data = self.storage.read_data()
        if isbn in data['books']:
            if isbn in data['checkout']:
                return "This book is already checked out."
            if user_id in data['users']:
                data['checkout'][isbn] = user_id
                self.storage.write_data(data)
                logging.info(f"Book {isbn} checked out to user {user_id}.")
                return f"Book {isbn} checked out to user {user_id}."
            logging.error(f"User does not exist to checkout with used_id: {user_id}")
            return "User does not exist."
        logging.error(f"Non-existing book tried to checkout")
        return "Book does not exist."

    def checkin_book(self, isbn):
        """
        Check in a book.

        Args:
            self: The instance of the class.
            isbn : The ISBN of the book to be checked in.

        Returns:
            str: A message indicating the result of the check-in process.

        """
        data = self.storage.read_data()
        if isbn in data['checkout']:
            del data['checkout'][isbn]
            self.storage.write_data(data)
            logging.info(f"Book {isbn} checked in.")
            return f"Book {isbn} checked in."
        logging.error(f"Book tried to checkin without checking out")
        return "This book is not checked out."
    
    def track_book(self, isbn):
        """
        track a book.

        Args:
            self: The instance of the class.
            isbn : The ISBN of the book to be checked in.

        Returns:
            str: A message indicating the result of the tracking of a book.

        """
        data = self.storage.read_data()
        if isbn in data['checkout']:
            logging.info(f"Book {isbn} is checked out to user {data['checkout'][isbn]}.")
            return f"Book {isbn} is checked out to user {data['checkout'][isbn]}."
        elif isbn in data['books']:
            logging.error(f"Book {isbn} is available in the library.")
            return f"Book {isbn} is available in the library."
        logging.error(f"Book tried to track with isbn {isbn} doesnt exist.")
        return "Book does not exist."

    def list_checked_out_books(self):
        """
        For listing checked out books.

        Args:
            self: The instance of the class.

        Returns:
            list: A list of books checked out to users.

        """
        data = self.storage.read_data()
        checked_out_books = {isbn: data['users'][data['checkout'][isbn]]['name'] for isbn in data['checkout']}
        return checked_out_books if checked_out_books else "No books are currently checked out."
