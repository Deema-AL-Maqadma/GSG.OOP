from Book import Book
from Library import Library

book1 = Book("CIMESTRY","JAK")
book2 = Book("DARK","TOM")
book3 = Book("JX","SAM")

my_books=[book1,book2,book3]

def printBooks(my_books):
    my_library=Library()
    for book in my_books:
        my_library.addBook(book)
    my_library.printBooks()

printBooks(my_books)
