# techolution-assignment
## Library Management System
LMS allows libraries to maintain a comprehensive database of their books, including details such as title, author, publisher, and ISBN. This helps in easy tracking and locating of books within the library.
## Installation
It make usage of logging module in python.
```bash
pip install logging
```
## Usage
```bash
python main.py
```
# Documentation:
Here is the clear description of all the classes that i have used for LMS.
### 1. Book Class
#### Purpose:
Represents a book in the library.
#### Responsibilities:
Holds details about a book, including its title, author, and ISBN.
Provides a method to return a formatted string representation of the book for easy display.
### 2. User Class
#### Purpose:
Represents a library user or member.
#### Responsibilities:
Stores information about a user, such as their unique user ID and name.
Offers a method to return a string representation of the user's information.
### 3. BookManager Class
#### Purpose:
Manages all book-related operations in the library system.
#### Responsibilities:
Handles CRUD (Create, Read, Update, Delete) operations for books.
Facilitates searching for books based on various attributes like title, author, or ISBN.
Interfaces with the Storage class to persist book data.
### 4. UserManager Class
#### Purpose:
Manages all user-related operations within the library.
#### Responsibilities:
Manages CRUD operations for users.
Enables searching for users by attributes such as name or user ID.
Works with the Storage class to manage user data storage and retrieval.
### 5. CheckoutManager Class
#### Purpose:
Handles the checkout and check-in processes of books.
#### Responsibilities:
Manages the checkout process, ensuring a book can only be checked out if it is not currently with another user.
Handles the check-in process, making books available again in the library.
Tracks the status of books, whether they are checked out or available, and identifies which user has any checked-out book.
### 6. Storage Class
#### Purpose:
Manages data storage and retrieval for the library system.
#### Responsibilities:
Provides methods to read and write data to a JSON file, acting as the persistence layer for the application.
Ensures that data for books, users, and checkout records is accurately maintained and synchronized.
### 7. LibraryInterface Class
#### Purpose:
Provides a command-line interface (CLI) for interacting with the library management system.
#### Responsibilities:
Offers a menu-driven interface for library operations such as adding or removing books and users, checking books in and out, and tracking books.
Delegates user commands to the appropriate managers (BookManager, UserManager, CheckoutManager) for processing.
Serves as the primary point of interaction for users with the library system, ensuring a seamless and user-friendly experience.
