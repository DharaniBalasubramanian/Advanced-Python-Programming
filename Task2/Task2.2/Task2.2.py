#  Design a Library Management System
# - Objective: Demonstrate mastery of OOP by designing a complex system with multiple interacting classes.
# - Instructions:
#   - Step 1: Create classes such as `Book`, `Member`, `Librarian`, and `Library`.
#   - Step 2: Implement methods for borrowing and returning books, searching for books, and managing library inventory.
#   - Step 3: Implement a `LibraryCard` class that tracks the borrowing history of members.
#   - Step 4: Implement fine calculation for overdue books and notifications for book availability.
# - Expected Output: A fully functional library management system with rich OOP features, including inheritance, encapsulation, and polymorphism.


from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, isbn, copies=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        self.borrowed = 0

    def borrow_book(self):
        if self.copies > self.borrowed:
            self.borrowed += 1
        else:
            print(f"All copies of '{self.title}' are currently borrowed.")

    def return_book(self):
        if self.borrowed > 0:
            self.borrowed -= 1
        else:
            print(f"No copies of '{self.title}' are currently borrowed.")

    def is_available(self):
        return self.copies > self.borrowed

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.library_card = LibraryCard(self)

    def borrow_book(self, book, library, borrow_date=None):
        if book in library.books and book.is_available():
            book.borrow_book()
            if borrow_date is None:
                borrow_date = datetime.now()
            due_date = borrow_date + timedelta(days=14)  # Due date is 14 days from the borrow date
            self.library_card.add_borrowed_book(book, borrow_date, due_date)
        else:
            print(f"'{book.title}' is not available.")

    def return_book(self, book, library, return_date=None):
        if book in self.library_card.borrowed_books:
            book.return_book()
            if return_date is None:
                return_date = datetime.now()
            self.library_card.return_book(book, return_date)
        else:
            print(f"{self.name} does not have '{book.title}' to return.")

class Librarian:
    def __init__(self, name, librarian_id):
        self.name = name
        self.librarian_id = librarian_id

    def add_book(self, library, book):
        library.add_book(book)
        print(f"Library Update: '{book.title}' added to the Library by Librarian {self.name}")

    def remove_book(self, library, book):
        library.remove_book(book)
        print(f"Library Update: '{book.title}' removed from the Library by Librarian {self.name}")

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print(f"'{book.title}' is not found in the library.")

    def show_books(self):
        print(f"Books in {self.name}:")
        if self.books:
            for book in self.books:
                print(f"'{book.title}' by {book.author} (ISBN: {book.isbn}) - Available: {book.copies - book.borrowed}/{book.copies}")
        else:
            print("No books available in the library.")

class LibraryCard:
    def __init__(self, member):
        self.member = member
        self.borrowed_books = {}  # Store books and due dates
        self.fines = 0

    def add_borrowed_book(self, book, borrow_date, due_date):
        self.borrowed_books[book] = (borrow_date, due_date)
        print(f"Borrowers Details:\nBook '{book.title}' borrowed by {self.member.name}. Borrow date: {borrow_date.strftime('%Y-%m-%d')}, Due date: {due_date.strftime('%Y-%m-%d')}.")

    def return_book(self, book, return_date):
        if book in self.borrowed_books:
            borrow_date, due_date = self.borrowed_books.pop(book)
            if return_date > due_date:
                overdue_days = (return_date - due_date).days
                fine = overdue_days * 10  # Fine of $10 per overdue day
                self.fines += fine
                print(f"Return Details:\n'{book.title}' was returned late. Fine: ${fine}")
            else:
                print(f"Return Details:\n'{book.title}' returned on time.")
            print(f"{self.member.name} has {self.fines} Rupees in fines.")
        else:
            print(f"{self.member.name} does not have '{book.title}' to return.")

    def show_borrowing_history(self):
        print(f"{self.member.name}'s Borrowing History:")
        if self.borrowed_books:
            for book, (borrow_date, due_date) in self.borrowed_books.items():
                print(f"Book: '{book.title}', Borrow Date: {borrow_date.strftime('%Y-%m-%d')}, Due Date: {due_date.strftime('%Y-%m-%d')}")
        else:
            print(f"{self.member.name} has no borrowed books.")

# Example usage:

# Create a Library
library = Library("City Library")

# Create Books
book1 = Book("Agni Siragugal", "A.P.J. Abdul Kalam", "33440", copies=1)
book2 = Book("The Atomic Habits", "James Clear", "66644", copies=20)

# Create Members
member1 = Member("Monisha", 101)
member2 = Member("Vinisha", 102)

# Create a Librarian
librarian = Librarian("Prasanth", 20001)

# Librarian adds books to the library
librarian.add_book(library, book1)
librarian.add_book(library, book2)

# Show available books
print("-----------------------------------------------------")
library.show_books()
print("-----------------------------------------------------")

# 1. Monisha borrows 'Agni Siragugal' on 1st October 2024
borrow_date_monisha = datetime(2024, 10, 1)
member1.borrow_book(book1, library, borrow_date_monisha)
print("-----------------------------------------------------")

# 2. Monisha returns 'Agni Siragugal' on 15th October 2024
return_date_monisha = datetime(2024, 10, 15)
member1.return_book(book1, library, return_date_monisha)
print("-----------------------------------------------------")

# 3. Vinisha borrows 'Agni Siragugal' on 21st October 2024
borrow_date_vinisha = datetime(2024, 10, 21)
member2.borrow_book(book1, library, borrow_date_vinisha)
print("-----------------------------------------------------")

# 4. Librarian removes 'The Atomic Habits' from the library
librarian.remove_book(library, book2)
print("-----------------------------------------------------")

# Show available books after removal
library.show_books()

