class Book:
    def _init_(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def describe(self):
        print(f"{self.title} by {self.author}, {self.year}")


# Create at least 2 books
book1 = Book("Things Fall Apart", "Chinua Achebe", 1958)
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald",2000)