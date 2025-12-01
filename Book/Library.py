class Library:

    def __init__(self):
        self.books=[]

    def addBook(self,book):
        self.books.append(book)

    def printBooks(self):
        for book in self.books:
            print(book.getInfo())