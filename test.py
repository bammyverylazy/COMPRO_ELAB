from dataclasses import dataclass
class LibraryError(Exception):
    pass
class BookNotFoundError(Exception):
    pass
class BookUnavailableError(Exception):
    pass

@dataclass
class Book:
    isbn :str
    title :str
    author :str
    availability :bool = True
    
    def to_dict(self):
        return {
            "isbn" :self.isbn,
            "title" :self.title,
            "author":self.author,
            "availability": self.availability
        }
    @classmethod
    def from_dict(cls,data):
        return cls(
            isbn = data["isbn"],
            title = data["title"],
            author = data["author"],
            availability = data["availability"]
        )
        
    def book_borrow(self):
        if self.availability == False:
            raise BookUnavailableError("This book is unavailable.")
        self.availability = False
    def book_return(self):
        self.availability = True
        
@dataclass
class Member:
    member_id :str
    borrowed_books :dict = {}
    def to_dict(self):
        return {
            "member_id": self.member_id,
            "borrowed_books" :self.borrowed_books
        }
    @classmethod
    def from_dict(cls,data):
        return cls(
            member_id = data["member_id"],
            borrowed_books = data["borrowed_books"]
        )

class Library(Book,Member):
    def __init__(self,):
        
    def add_book(self,data):
        
    def search_book(self, isbn):
        if isbn not in Book:
            raise BookNotFoundError("There's no book searched.")
        return True
    def book_borrow(self,isbn):
        if self.search_book(isbn):
            