from dataclasses import dataclass,field
class LibraryError(Exception):
    pass
class BookNotFoundError(LibraryError):
    pass
class BookUnavailableError(LibraryError):
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
        
    def borrow(self):
        if not self.availability :
            raise BookUnavailableError("This book is unavailable.")
        self.availability = False
    def book_return(self):
        self.availability = True
        
@dataclass
class Member:
    member_id :str
    borrowed_books : list[str] = field(default_factory=list) ## what
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

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
    def add_book(self, book: Book):
        self.books[book.isbn] = book
    def add_member(self, member:Member):
        self.members[member.member_id] = member
    def search_book(self, isbn):
        if isbn not in self.books:
            raise BookNotFoundError("There's no book searched.")
        return self.books[isbn]
    def  borrow_book(self, isbn: str, member_id: str):
        book = self.search_book(isbn)
        if member_id not in self.members:
            raise LibraryError("Member not found.")
        member = self.members[member_id]
        book.borrow()
        member.borrowed_books.append(isbn)
        
  ###########      
library = Library()

book1 = Book("001", "Python Basics", "Alice")
member1 = Member("M001")

library.add_book(book1)
library.add_member(member1)

library.borrow_book("001", "M001")

print(book1)
print(member1)