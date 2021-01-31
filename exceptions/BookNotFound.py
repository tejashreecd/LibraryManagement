class BookNotFound(Exception):
    def __init__(self, isbn, message="Book Not Found"):
        self.isbn = isbn
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.isbn} -> {self.message}'

class BookAlreadyAssigned(Exception):
    def __init__(self, isbn, message="Book Already Assigned"):
        self.isbn = isbn
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.isbn} -> {self.message}'