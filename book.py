class Book:
    def __init__(self, title, author, copies_available):
        self.title = title
        self.author = author
        self.copies_available = copies_available

class Library:
    total_books = 0

    def __init__(self):
        self.books = []

    # b) Add, Borrow, Return
    def add_book(self, title, author, copies):
        self.books.append(Book(title, author, copies))
        Library.total_books += copies

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.copies_available > 0:
                    book.copies_available -= 1
                    print(f"You borrowed {title}")
                else:
                    print(f"{title} not available")
                return
        print("Book not found")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.copies_available += 1
                print(f"You returned {title}")
                return
        print("Book not found")

    # d) Display
    def display_library_info(self):
        for b in self.books:
            print(f"{b.title} by {b.author}, Copies: {b.copies_available}")
        print(f"Total books in library: {Library.total_books}")


# c) Demonstration
lib = Library()
lib.add_book("Python", "John", 3)
lib.add_book("Database", "Mary", 2)
lib.add_book("Networking", "James", 1)

lib.display_library_info()

lib.borrow_book("Python")
lib.borrow_book("Networking")
lib.return_book("Python")

lib.display_library_info()
