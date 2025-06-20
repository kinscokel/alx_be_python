# library_system.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_details(self):
        return f"Title: {self.title}, Author: {self.author}"

    def __str__(self):
        return self.get_details()


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def get_details(self):
        return f"{super().get_details()}, File Size: {self.file_size}MB"

    def __str__(self):
        return self.get_details()


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self):
        return f"{super().get_details()}, Page Count: {self.page_count}"

    def __str__(self):
        return self.get_details()


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only instances of Book or its subclasses can be added.")

    def list_books(self):
        if not self.books:
            print("The library has no books.")
        else:
            for idx, book in enumerate(self.books, 1):
                print(f"{idx}. {book}")  # __str__ is called here
