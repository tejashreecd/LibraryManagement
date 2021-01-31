from models.Library import Library
import click
from click_shell import shell
from models.Book import Book
from exceptions.BookNotFound import BookNotFound
library = Library()

@shell(prompt='Library> ', intro='Starting my app...')
def library_mgmt():
    pass

@click.command()
def view_books():
    books = library.view()
    for book in books:
        print("Book title: {} & Book author: {} & Book status: {}".format(book.name, book.author, book.status))

@click.command()
@click.option("--isbn", prompt="ISBN of book", help="Please enter ISBN of book")
@click.option("--name", prompt="name of book", help="Please enter name of book")
@click.option("--author", prompt="author of book", help="Please enter author of book")
def add_book(isbn, name, author):
    book = Book(isbn, name, author)
    library.add(book)

@click.command()
@click.option("--isbn", prompt="ISBN of book", help="Please enter ISBN of book")
def delete_book(isbn):
    try:
        library.delete(isbn)
    except BookNotFound as e:
        print(str(e))

@click.command()
@click.option("--isbn", prompt="ISBN of book", help="Please enter ISBN of book")
def borrow_book(isbn):
    library.borrow(isbn)

library_mgmt.add_command(add_book)
library_mgmt.add_command(delete_book)
library_mgmt.add_command(view_books)
library_mgmt.add_command(borrow_book)
if __name__ == "__main__":
    library_mgmt()



