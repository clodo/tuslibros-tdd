import unittest

from cart import Cart
from cashier import Cashier


class TestEcommerce(unittest.TestCase):

    # Iteration 1
    def test_can_create_an_empty_cart(self):
        cart = self.__empty_cart()

        self.assertTrue(cart.is_empty())

    def test_add_a_book_to_an_empty_cart(self):
        cart = self.__empty_cart()
        book = "book 1"
        cart.add_book(book)

        self.assertFalse(cart.is_empty())
        self.assertEqual(cart.count_book(book), 1)

    def test_be_able_to_add_more_than_one_book(self):
        cart = self.__empty_cart()
        cart.add_book("book 1")
        cart.add_book("book 2")
        cart.add_book("book 3")

        self.assertFalse(cart.is_empty())
        self.assertEqual(cart.count_book("book 1"), 1)
        self.assertEqual(cart.count_book("book 2"), 1)
        self.assertEqual(cart.count_book("book 3"), 1)

    def test_can_add_more_than_one_of_the_same_book(self):
        cart = self.__empty_cart()
        book = "book 1"
        cart.add_book(book, 2)

        self.assertEqual(cart.count_book(book), 2)

    def test_not_be_able_to_add_negative_quantity_of_books(self):
        cart = self.__empty_cart()
        book = "book 1"
        
        with self.assertRaises(Exception) as context: 
            cart.add_book(book, -1)
            
        self.assertEqual(str(context.exception), Cart.INVALID_QUANTITY_MSG)
        self.assertEqual(cart.count_book(book), 0)

    def test_can_only_add_books_from_tus_libros(self):
        cart = self.__empty_cart()
        book = "external book"

        with self.assertRaises(Exception) as context: 
            cart.add_book(book)

        self.assertEqual(str(context.exception), Cart.INVALID_BOOK_MSG)
        self.assertEqual(cart.count_book(book), 0)
    
    # Iteration 2  
    def test_can_not_checkout_empty_cart(self):
        cart = self.__empty_cart()
        
        cashier = Cashier()

        with self.assertRaises(Exception) as context:
            cashier.checkout(cart)

        self.assertEqual(str(context.exception), Cashier.EMPTY_CART_MSG)

    def test_can_checkout_a_cart_with_one_book_of_10_pesos(self):
        cart = self.__empty_cart()
        book = "book 1"
        cart.add_book(book)

        cashier = Cashier()

        ticket_total = cashier.checkout(cart)

        self.assertEqual(ticket_total, 10)
        self.assertTrue(cart.is_empty())

    def __empty_cart(self):
        catalog = ['book 1', 'book 2', 'book 3'] 
        return Cart(catalog)

if __name__ == '__main__':
    unittest.main()