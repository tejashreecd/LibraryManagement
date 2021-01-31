import enum

class Status(enum.Enum):
    unassigned = 1
    assigned = 2
    

class Book:
    def __init__(self, isbn, name, author):
        self.isbn = isbn
        self.name = name
        self.author = author
        self.status = Status.unassigned
    
