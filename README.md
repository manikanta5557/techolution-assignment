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
## Design Pattern usage:
In the code design for the library management system described above, a few design patterns from the realm of software engineering are used. These patterns help structure the application in a way that promotes maintainability, scalability, and robustness. Here are the primary design patterns identified in the code:

### 1. Singleton Pattern
The Storage class in our code could be considered an example of the Singleton pattern, we ensure that only one instance of this class handles the file storage throughout the application.
### 2. Facade Pattern
The LibraryInterface class functions as a Facade, providing a simplified interface to the complex underlying system involving book and user management as well as checkout processes. It hides the complexities of the system and provides a single simple interface to the client, making the subsystems easier to use.
### 3. Command Pattern
While not fully fleshed out as typical command pattern implementations, the run method in LibraryInterface somewhat mirrors the command pattern. Each action (like adding a book, listing books, etc.) could be encapsulated as a command object, but currently, they're implemented as methods within the interface. To more closely align with the command pattern, these actions could be refactored into separate command classes that execute these specific actions.


