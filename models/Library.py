from exceptions.BookNotFound import BookNotFound
from exceptions.BookNotFound import BookAlreadyAssigned
from models.Book import Status

class Library:
    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)
        

    def view(self):
        return self.books

    def delete(self, isbn):
        for book in self.books:
            if isbn == book.isbn:
                self.books.remove(book)
                return
        raise BookNotFound(isbn)

    def borrow(self, isbn):
        for book in self.books:
            if isbn == book.isbn and book.status == Status.unassigned:
                book.status = Status.assigned
                return
            elif isbn == book.isbn and book.status == Status.assigned:
                raise BookAlreadyAssigned(isbn)
        raise BookNotFound(isbn)
