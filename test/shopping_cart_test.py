import unittest
from shopping_cart_model import the_cart
from item import item


class shopping_cart_test(unittest.TestCase):
    def test_empty_total(self):
        cart = the_cart([])
        self.assertEqual(cart.total(), 0)

    def test_single_item_quantity_one(self):
        cart = the_cart([item(100.0, 1)])
        self.assertEqual(cart.total(), 100.0)

    def test_two_item_quantity_one(self):
        cart = the_cart([item(100.0, 1), item(100.0, 1)])
        self.assertEqual(cart.total(), 200.0)

    def test_single_item_quantity_two(self):
        cart = the_cart([item(100.0, 2)])
        self.assertEqual(cart.total(), 200.0)
