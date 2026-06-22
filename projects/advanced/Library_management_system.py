class Book:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available

    def borrow(self):
        if self.available:
            self.available = False
            print(f"You have borrowed '{self.title}' by {self.author}.")
        else:
            print(f"Sorry, '{self.title}' by {self.author} is currently unavailable.")
    
    def return_book(self):
        if not self.available:
            self.available = True
            print(f"You have returned '{self.title}' by {self.author}.")
        else:
            print(f"'{self.title}' by {self.author} was not borrowed.")
    
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", True)
book2 = Book("To Kill a Mockingbird", "Harper Lee", True)
book3 = Book("1984", "George Orwell", True)

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' by {book.author} has been added to the library.")

    def display_books(self):
        print("Books in the library:")
        for book in self.books:
            status = "Available" if book.available else "Unavailable"
            print(f"'{book.title}' by {book.author} - {status}")
    
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                book.borrow()
                return
        print(f"Sorry, '{title}' is not in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                return
        print(f"Sorry, '{title}' is not in the library.")

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_books()

library.borrow_book("1984")
library.display_books()

library.return_book("1984")
library.display_books()