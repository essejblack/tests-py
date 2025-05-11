class BookSoldError(Exception):
    pass

class BookStore(object):
    def __init__(self,available_books=[]):
        self.available_books = available_books
        self.to_order=[]
    def add_book(self,name):
        self.available_books.append(name)
    def find_book(self,name:str,case_sens=False):
        books = self.available_books + self.to_order
        books.sort()

        if name == "":
            return books

        if case_sens:
            return [book for book in books if book.find(name) != -1]
        else:
            return [book for book in books if book.lower().find(name.lower()) != -1]

    def buy(self,name):
        if name in self.available_books:
            return self.available_books.pop(self.available_books.index(name))
        else:
            raise BookSoldError("Sorry")

