class Book:
    def _init_(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def describe(self):
        print(f"{self.title} by {self.author}, {self.year}")


# Create at least 2 books
book1 = Book("After", "Ann Todd", 1958)
book2 = Book("Nothing more", "Ann Todd",2000)