import unittest
from shopping_cart_model import TheCart
from item import Item


class ShoppingCartTest(unittest.TestCase):
    def test_empty_total(self):
        cart = TheCart([])
        self.assertEqual(cart.total(), 0)

    def test_single_item_quantity_one(self):
        cart = TheCart([Item(100.0, 1)])
        self.assertEqual(cart.total(), 100.0)

    def test_two_item_quantity_one(self):
        cart = TheCart([Item(100.0, 1), Item(100.0, 1)])
        self.assertEqual(cart.total(), 200.0)

    def test_single_item_quantity_two(self):
        cart = TheCart([Item(100.0, 2)])
        self.assertEqual(cart.total(), 200.0)
