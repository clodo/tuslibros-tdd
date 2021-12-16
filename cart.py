class Cart:
    INVALID_QUANTITY_MSG = "You can't add books that doesn't belongs to catalog"
    INVALID_BOOK_MSG = "You can't add less than zero books"

    def __init__(self, catalog=[]):
        self.books = []
        self.catalog = catalog

    def empty(self):
        self.books = []

    def is_empty(self):
        return len(self.books) == 0

    def add_book(self, book, quantity = 1):
        self.assert_invalid_quantity(quantity)
        self.assert_invalid_book(book)

        for index in range(0, quantity):
            self.books.append(book)

    def assert_invalid_book(self, book):
        if book not in self.catalog:
            raise Exception(self.INVALID_BOOK_MSG)

    def assert_invalid_quantity(self, quantity):
        if quantity < 0:
            raise Exception(self.INVALID_QUANTITY_MSG)
        

    def count_book(self, book):
        return self.books.count(book)