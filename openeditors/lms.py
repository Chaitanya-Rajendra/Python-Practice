# Library Management system (LMS) 
# Basic book Class
# class Book:
#     def __init__(self, book_id, title, author):
#         self.book_id = book_id
#         self.title = title
#         self.author = author
#         self.is_available = True

#     def display(self):
#         print("Book ID:", self.book_id)
#         print("Title:", self.title)
#         print("Author:", self.author)
#         print("Available: ", self.is_available)

# book1 = Book(101, "Python", "John Doe")
# book1.display()


#Encapsulation of class book
# Encapsulation use is  about we don't want anyone to modify important information.

# class Book:
#     def __init__(self, book_id, title, author):
#         self.__book_id = book_id
#         self.__title = title
#         self.__author = author
#         self.__is_available = True

#     # Issue the book
#     def issue_book(self):
#         if self.__is_available:
#             self.__is_available = False
#             print("Book has been issued.")
#         else:
#             print("Book is not available for issue.")

#     # Return the book
#     def return_book(self):
#         self.__is_available = True
#         print("Book has been returned.")

#     # Check availability
#     def get_availability(self):
#         return self.__is_available

#     # Display book details
#     def display(self):
#         print("Book ID:", self.__book_id)
#         print("Title:", self.__title)
#         print("Author:", self.__author)
#         print("Available:", self.__is_available)

# Abstaction 

from abc import ABC, abstractmethod

class LibraryItem(ABC):# Grandparent
  @abstractmethod
  def display(self):
    pass
  @abstractmethod
  def get_type(self):
    pass


class Book(LibraryItem):# Parent
  total_books = 0
  def __init__(self, book_id, title, author):
    self.__book_id = book_id
    self.__title = title
    self.__author = author
    self.__is_available = True
    Book.total_books += 1

  @property
  def book_id(self):
    return self.__book_id

  @property
  def title(self):
    return self.__title

  @property
  def author(self):
    return self.__author

  # Issue the book
  def issue_book(self):
    if self.__is_available:
      self.__is_available = False
      print("Book has been issued.")
    else:
      print("Book is not available for issue.")

  # Return the book
  def return_book(self):
    self.__is_available = True
    print("Book has been returned.")

  # Check availability
  def is_available(self):
    return self.__is_available

  # Display book details
  def display(self):
    print("Book ID:", self.book_id)
    print("Title:", self.title)
    print("Author:", self.author)
    print("Available:", self.is_available())

  def get_type(self):
    return "Book"

  # Operator Overloading
  def __eq__(self, other):
    if isinstance(other, Book):
      return self.book_id == other.book_id
    return False

  def __str__(self):
    return f"{self.title} by {self.author}"


class EBook(Book):# Child class
  def __init__(self, book_id, title, author, file_format):
    super().__init__(book_id, title, author)
    self.file_format = file_format

  #Method overriding
  def issue_book(self):
    print(f"'{self.title}' is an EBook access granted.")

  def get_type(self):
    return "EBook"

  def display(self):
    print(
      f"ID: {self.book_id} | "
      f"Title: {self.title} | "
      f"Author: {self.author} | "
      f"File Format: {self.file_format}"
    )

# Printed Book
class PrintedBook(Book):
  def __init__(self, book_id, title, author, pages):
    super().__init__(book_id, title, author)
    self.pages = pages

  def issue_book(self):
    if self.is_available():
      print(f"'{self.title}' is a Printed Book. Please collect it from the library.")
      super().issue_book()
    else:
      print(f"'{self.title}' is not available for issue.")

  def get_type(self):
    return "PrintedBook"

  def display(self):
    super().display()
    print("Pages:", self.pages)

# Member class

class Member:
  def __init__(self, member_id, name):
    self.member_id = member_id
    self.name = name
    self.borrowed_books = []

  def borrow_book(self, book):
    if book.is_available():
      book.issue_book()
      self.borrowed_books.append(book)
      print(f"{self.name} has borrowed '{book.title}'.")
    else:
      print(f"'{book.title}' is not available for borrowing.")

  def return_book(self, book):
    if book in self.borrowed_books:
      book.return_book()
      self.borrowed_books.remove(book)
      print(f"{self.name} has returned '{book.title}'.")
    else:
      print(f"{self.name} did not borrow '{book.title}'.")

  def display_member(self):
    print("Member ID:", self.member_id)
    print("Name:", self.name)
    print("Borrowed Books: ")
    if not self.borrowed_books:
      print("No borrowed books.")
    else:
      for book in self.borrowed_books:
        print(f"- {book.title} by {book.author}")

# Student Member
class studentMember(Member):
  def __init__(self, member_id, name, college):
    super().__init__(member_id, name)
    self.college = college

  def display_member(self):
    super().display_member()
    print("College:", self.college)

# Faculty Member
class facultyMember(Member):
  def __init__(self, member_id, name, department):
    super().__init__(member_id, name)
    self.department = department

  def display_member(self):
    super().display_member()
    print("Department: ", self.department)

class Library:
  def __init__(self, name):
    self.name = name
    self.books = []
    self.members = []

  #ADD BOOK
  def add_book(self, book):
    self.books.append(book)
    print(f"Book {book.title} added successfully.")

  #REMOVE BOOK
  def remove_book(self, book_id):
    for book in self.books:
      if book.book_id == book_id:
        self.books.remove(book)
        print("Book removed successfully.")
        return
    print("Book not found")

  #REGISTER MEMBER
  def register_member(self, member):
    self.members.append(member)
    print(f"Member {member.name} added successfully.")

  #SEARCH BOOK
  def search_book(self, title=None, author=None):
    found = False
    for book in self.books:
      if title and title.lower() in book.title.lower():
        book.display()
        found = True
      elif author and author.lower() in book.author.lower():
        book.display()
        found = True
    if not found:
      print("No book found.")

  #DISPLAY BOOKS
  def display_book(self):
    print("\nLibrary Books: ")
    if not self.books:
      print("No books available.")
      return
    for book in self.books:
      book.display()

  #DISPLAY MEMBERS
  def display_members(self):
    print("\n ----Members---- ")
    for member in self.members:
      member.display_member()

  #FIND MEMBER
  def find_member(self, member_id):
    for member in self.members:
      if member.member_id == member_id:
        return member
    return None

  #FIND BOOK
  def find_book(self, book_id):
    for book in self.books:
      if book.book_id == book_id:
        return book
    return None

library = Library("ABC Central Library")

book1 = Book(101, "Python Programming", "John Doe")
book2 = PrintedBook(103, "Machine Learning", "Alice Johnson", 300)
book3 = EBook(102, "Data Science with Python", "Jane Smith", "PDF")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
student1 = studentMember(1, "Alice", "XYZ College")
faculty1 = facultyMember(2, "Dr. Smith", "Computer Science")
library.register_member(student1)
library.register_member(faculty1)
library.display_book()
student1.borrow_book(book1)
student1.display_member()
student1.return_book(book1)
library.search_book(author="Jane Smith")

